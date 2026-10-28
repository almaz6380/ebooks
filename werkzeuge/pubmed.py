"""Kleine Helfer für PubMed und ClinicalTrials.gov.

Kommandozeile:
  python3 werkzeuge/pubmed.py suche "semaglutide AND SELECT[ti]" [anzahl]
  python3 werkzeuge/pubmed.py zeige 37952131 [weitere PMIDs ...]     (mit Abstract)
  python3 werkzeuge/pubmed.py kurz 37952131 [weitere PMIDs ...]      (nur Titel/Jahr/Journal)
  python3 werkzeuge/pubmed.py nct NCT03548935 [weitere NCT ...]
  python3 werkzeuge/pubmed.py ctsuche "retatrutide" [anzahl]
"""
import sys
import time
import xml.etree.ElementTree as ET

import requests

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
CTGOV = "https://clinicaltrials.gov/api/v2/studies"
_letzte = [0.0]


def _get(url, params, json=True):
    for versuch in range(5):
        warte = 0.4 - (time.time() - _letzte[0])
        if warte > 0:
            time.sleep(warte)
        _letzte[0] = time.time()
        try:
            r = requests.get(url, params=params, timeout=60)
            if r.status_code == 404:
                return None
            if r.status_code == 429:
                raise RuntimeError("429")
            r.raise_for_status()
            return r.json() if json else r.text
        except Exception:
            time.sleep(2 ** (versuch + 1))
    raise RuntimeError(f"Abfrage fehlgeschlagen: {url} {params}")


def suche(begriff, anzahl=20, sort="relevance"):
    d = _get(EUTILS + "esearch.fcgi", {"db": "pubmed", "term": begriff, "retmode": "json",
                                       "retmax": anzahl, "sort": sort})
    return int(d["esearchresult"]["count"]), d["esearchresult"]["idlist"]


def kurz(pmids):
    """Titel, Jahr, Journal, Erstautor, DOI, Publikationstyp je PMID."""
    ergebnis = {}
    pmids = list(pmids)
    for i in range(0, len(pmids), 200):
        teil = pmids[i:i + 200]
        d = _get(EUTILS + "esummary.fcgi", {"db": "pubmed", "id": ",".join(teil), "retmode": "json"})
        for pmid in d.get("result", {}).get("uids", []):
            e = d["result"][pmid]
            if e.get("error") or not e.get("title"):
                continue
            doi = next((a["value"] for a in e.get("articleids", []) if a["idtype"] == "doi"), "")
            ergebnis[pmid] = {
                "pmid": pmid,
                "titel": e.get("title", "").rstrip("."),
                "jahr": (e.get("pubdate", "") or "")[:4],
                "journal": e.get("source", ""),
                "erstautor": (e.get("authors") or [{}])[0].get("name", ""),
                "doi": doi,
                "typ": e.get("pubtype", []),
            }
    return ergebnis


def abstracts(pmids):
    """Abstract-Text je PMID."""
    ergebnis = {}
    pmids = list(pmids)
    for i in range(0, len(pmids), 100):
        teil = pmids[i:i + 100]
        xml = _get(EUTILS + "efetch.fcgi", {"db": "pubmed", "id": ",".join(teil), "retmode": "xml"}, json=False)
        for art in ET.fromstring(xml).iter("PubmedArticle"):
            pmid = art.findtext(".//MedlineCitation/PMID")
            teile = []
            for a in art.iter("AbstractText"):
                label = a.get("Label")
                text = "".join(a.itertext()).strip()
                teile.append(f"{label}: {text}" if label else text)
            ergebnis[pmid] = " ".join(teile)
    return ergebnis


def ct_studien(begriff, anzahl=1000):
    felder = ("NCTId,BriefTitle,Phase,OverallStatus,EnrollmentCount,StartDate,CompletionDate,"
              "Condition,LeadSponsorName,HasResults,StudyType")
    studien, token = [], None
    while len(studien) < anzahl:
        p = {"query.intr": begriff, "pageSize": min(200, anzahl - len(studien)), "fields": felder}
        if token:
            p["pageToken"] = token
        d = _get(CTGOV, p)
        for s in d.get("studies", []):
            ps = s.get("protocolSection", {})
            ident, status = ps.get("identificationModule", {}), ps.get("statusModule", {})
            design = ps.get("designModule", {})
            studien.append({
                "nct": ident.get("nctId"),
                "titel": ident.get("briefTitle"),
                "phase": ",".join(design.get("phases", []) or []),
                "typ": design.get("studyType"),
                "status": status.get("overallStatus"),
                "teilnehmende": (design.get("enrollmentInfo") or {}).get("count"),
                "start": (status.get("startDateStruct") or {}).get("date"),
                "ende": (status.get("completionDateStruct") or {}).get("date"),
                "erkrankungen": (ps.get("conditionsModule") or {}).get("conditions", []),
                "sponsor": ((ps.get("sponsorCollaboratorsModule") or {}).get("leadSponsor") or {}).get("name"),
                "ergebnisse": s.get("hasResults", False),
            })
        token = d.get("nextPageToken")
        if not token:
            break
    return studien


def nct(ids):
    ergebnis = {}
    for i in ids:
        try:
            d = _get(f"{CTGOV}/{i}", {"fields": "NCTId,BriefTitle,Phase,OverallStatus,EnrollmentCount,StartDate,CompletionDate"})
        except RuntimeError:
            d = None
        if not d:
            ergebnis[i] = None
            continue
        ps = d.get("protocolSection", {})
        ergebnis[i] = {
            "titel": ps.get("identificationModule", {}).get("briefTitle"),
            "phase": ",".join(ps.get("designModule", {}).get("phases", []) or []),
            "status": ps.get("statusModule", {}).get("overallStatus"),
            "teilnehmende": (ps.get("designModule", {}).get("enrollmentInfo") or {}).get("count"),
            "start": (ps.get("statusModule", {}).get("startDateStruct") or {}).get("date"),
        }
    return ergebnis


if __name__ == "__main__":
    befehl, args = sys.argv[1], sys.argv[2:]
    if befehl == "suche":
        n = int(args[1]) if len(args) > 1 else 20
        gesamt, ids = suche(args[0], n)
        print(f"Treffer gesamt: {gesamt}")
        for e in kurz(ids).values():
            print(f"PMID {e['pmid']} | {e['jahr']} | {e['erstautor']} | {e['journal']} | {e['titel']}")
    elif befehl in ("zeige", "kurz"):
        info = kurz(args)
        abs_ = abstracts(args) if befehl == "zeige" else {}
        for p in args:
            e = info.get(p)
            if not e:
                print(f"PMID {p}: NICHT GEFUNDEN\n")
                continue
            print(f"PMID {p} | {e['jahr']} | {e['erstautor']} | {e['journal']} | DOI {e['doi']}\n{e['titel']}")
            if befehl == "zeige":
                print(abs_.get(p, "(kein Abstract)"))
            print()
    elif befehl == "nct":
        for k, v in nct(args).items():
            print(k, v if v else "NICHT GEFUNDEN")
    elif befehl == "ctsuche":
        n = int(args[1]) if len(args) > 1 else 50
        for s in ct_studien(args[0], n):
            print(f"{s['nct']} | {s['phase']} | {s['status']} | n={s['teilnehmende']} | {s['start']} | {s['titel']}")
