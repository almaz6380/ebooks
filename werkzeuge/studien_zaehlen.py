"""Zählt pro Peptid die Studien in PubMed und ClinicalTrials.gov.

Aufruf: python3 werkzeuge/studien_zaehlen.py
Ergebnis: recherche/studienzahlen.csv (+ Übersicht in der Konsole)
"""
import csv
import datetime
import pathlib
import time

import requests
import yaml

BASIS = pathlib.Path(__file__).resolve().parent.parent
PUBMED = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
CTGOV = "https://clinicaltrials.gov/api/v2/studies"

FILTER = {
    "pubmed_gesamt": "",
    "pubmed_humanstudien": " AND (clinical trial[pt] OR randomized controlled trial[pt]) AND humans[mh]",
    "pubmed_rct": " AND randomized controlled trial[pt]",
    "pubmed_metaanalysen": " AND (meta-analysis[pt] OR systematic review[pt])",
}


def pubmed_anzahl(begriff):
    for versuch in range(4):
        try:
            r = requests.get(PUBMED, params={"db": "pubmed", "term": begriff, "retmode": "json", "retmax": 0}, timeout=30)
            r.raise_for_status()
            return int(r.json()["esearchresult"]["count"])
        except Exception:
            time.sleep(2 ** (versuch + 1))
        finally:
            time.sleep(0.4)  # NCBI: max. 3 Anfragen/s ohne API-Schlüssel
    return None


def ctgov_anzahl(begriff):
    for versuch in range(4):
        try:
            r = requests.get(CTGOV, params={"query.intr": begriff, "countTotal": "true", "pageSize": 1}, timeout=30)
            r.raise_for_status()
            return r.json().get("totalCount", 0)
        except Exception:
            time.sleep(2 ** (versuch + 1))
    return None


def main():
    daten = yaml.safe_load((BASIS / "recherche/peptide.yaml").read_text())
    zeilen = []
    for gruppe_id, gruppe in daten.items():
        for p in gruppe["peptide"]:
            zeile = {"gruppe": gruppe_id, "peptid": p["name"], "status": p["status"],
                     "vergleich": p.get("vergleich", False)}
            for spalte, zusatz in FILTER.items():
                zeile[spalte] = pubmed_anzahl(f"({p['pubmed']}){zusatz}")
            zeile["ctgov_registriert"] = ctgov_anzahl(p["ctgov"])
            zeilen.append(zeile)
            print(f"{p['name']:<45} {zeile['pubmed_gesamt']!s:>7} {zeile['pubmed_humanstudien']!s:>6} "
                  f"{zeile['pubmed_rct']!s:>6} {zeile['pubmed_metaanalysen']!s:>6} {zeile['ctgov_registriert']!s:>6}")

    ziel = BASIS / "recherche/studienzahlen.csv"
    with ziel.open("w", newline="", encoding="utf-8") as f:
        f.write(f"# Abfrage vom {datetime.date.today().isoformat()}\n")
        w = csv.DictWriter(f, fieldnames=list(zeilen[0]))
        w.writeheader()
        w.writerows(zeilen)
    print(f"\nGespeichert: {ziel}")


if __name__ == "__main__":
    main()
