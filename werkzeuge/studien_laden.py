"""Lädt pro Peptid die Studiendaten in recherche/studien/<kuerzel>.json.

Inhalt je Datei:
- humanstudien_alle: alle PubMed-Humanstudien (Kurzinfo) -> fürs Studienverzeichnis
- humanstudien_detail: die relevantesten Humanstudien mit Abstract
- metaanalysen: die relevantesten Übersichtsarbeiten mit Abstract
- praeklinik: bei schwacher Humanevidenz die relevantesten übrigen Arbeiten mit Abstract
- ctgov: alle registrierten Studien (gekürzt)

Aufruf: python3 werkzeuge/studien_laden.py [kuerzel ...]
"""
import json
import pathlib
import re
import sys

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pubmed  # noqa: E402

BASIS = pathlib.Path(__file__).resolve().parent.parent
ZIEL = BASIS / "recherche/studien"
HUMAN = " AND (clinical trial[pt] OR randomized controlled trial[pt]) AND humans[mh]"
META = " AND (meta-analysis[pt] OR systematic review[pt])"


def kuerzel(name):
    k = name.split("(")[0].split("/")[0].strip().lower()
    k = k.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    return re.sub(r"[^a-z0-9]+", "-", k).strip("-")


def mit_abstract(ids):
    info, abs_ = pubmed.kurz(ids), pubmed.abstracts(ids)
    return [dict(info[i], abstract=abs_.get(i, "")) for i in ids if i in info]


def laden(p):
    q = f"({p['pubmed']})"
    _, alle = pubmed.suche(q + HUMAN, 10000, sort="pub_date")
    _, top = pubmed.suche(q + HUMAN, 60)
    _, meta = pubmed.suche(q + META, 15)
    daten = {
        "name": p["name"],
        "status": p["status"],
        "suchbegriff_pubmed": p["pubmed"],
        "suchbegriff_ctgov": p["ctgov"],
        "humanstudien_alle": list(pubmed.kurz(alle).values()),
        "humanstudien_detail": mit_abstract(top),
        "metaanalysen": mit_abstract(meta),
        "praeklinik": [],
    }
    if len(alle) < 25:
        _, rest = pubmed.suche(f"{q} NOT ({q}{HUMAN})", 40)
        daten["praeklinik"] = mit_abstract(rest)
    ct = pubmed.ct_studien(p["ctgov"], 1000)
    daten["ctgov"] = ct
    return daten


def main():
    auswahl = set(sys.argv[1:])
    ZIEL.mkdir(parents=True, exist_ok=True)
    liste = yaml.safe_load((BASIS / "recherche/peptide.yaml").read_text())
    for gruppe_id, gruppe in liste.items():
        for p in gruppe["peptide"]:
            k = kuerzel(p["name"])
            if auswahl and k not in auswahl:
                continue
            datei = ZIEL / f"{k}.json"
            d = laden(p)
            d["gruppe"] = gruppe_id
            datei.write_text(json.dumps(d, ensure_ascii=False, indent=1))
            print(f"{k:<35} human={len(d['humanstudien_alle']):>4} detail={len(d['humanstudien_detail']):>3} "
                  f"meta={len(d['metaanalysen']):>3} praekl={len(d['praeklinik']):>3} ctgov={len(d['ctgov']):>4}",
                  flush=True)


if __name__ == "__main__":
    main()
