"""Prüft Kapitel-Dateien: Existieren alle zitierten PMIDs und NCT-Nummern?
Passen Jahr und Autor, die direkt vor der PMID stehen, zum PubMed-Eintrag?
Enthält der Text verbotene Formulierungen?

Aufruf: python3 werkzeuge/pruefen.py buch/kapitel/*.md
Ausgabe: FEHLER (muss behoben werden) und HINWEIS (bitte ansehen). Exit-Code 1 bei FEHLER.
"""
import json
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pubmed  # noqa: E402

CACHE = pathlib.Path(__file__).resolve().parent.parent / "recherche/pruef_cache.json"
PMID_RE = re.compile(r"PMID[:\s]*(\d{6,9})")
NCT_RE = re.compile(r"\bNCT\d{8}\b")
# "(Wilding 2021, PMID 33567185)" oder "Wilding et al. 2021; PMID ..."
ZITAT_RE = re.compile(r"([A-ZÄÖÜ][\w'\-ÄÖÜäöüéèáàñçøå]+)(?: et al\.| und Kollegen| u\. a\.)?,? \(?(\d{4})\)?[,;]? PMID[:\s]*(\d{6,9})")
VERBOTEN = [
    (r"\bheilt\b", "Heilversprechen"),
    (r"\b(empfohlene|empfehlen wir|wir empfehlen) (Dosis|Dosierung)", "Dosierungsempfehlung"),
    (r"\b(bestellen|kaufen Sie|Bezugsquelle|erhältlich bei)\b", "Bezugsquelle"),
    (r"\bStack(s)?\b", "Stack-Empfehlung"),
    (r"<[a-zA-Z/][^>]*>", "HTML-Tag"),
]


def norm(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def main(dateien):
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {"pmid": {}, "nct": {}}
    texte = {d: pathlib.Path(d).read_text(encoding="utf-8") for d in dateien}
    alle_pmid = {p for t in texte.values() for p in PMID_RE.findall(t)}
    alle_nct = {n for t in texte.values() for n in NCT_RE.findall(t)}
    neu = [p for p in alle_pmid if p not in cache["pmid"]]
    if neu:
        info = pubmed.kurz(neu)
        for p in neu:
            cache["pmid"][p] = info.get(p)
    neu = [n for n in alle_nct if n not in cache["nct"]]
    if neu:
        cache["nct"].update(pubmed.nct(neu))
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=0))

    fehler = 0
    for d, t in texte.items():
        meldungen = []
        for p in sorted(set(PMID_RE.findall(t))):
            if not cache["pmid"].get(p):
                meldungen.append(f"FEHLER  PMID {p} existiert nicht")
        for n in sorted(set(NCT_RE.findall(t))):
            if not cache["nct"].get(n):
                meldungen.append(f"FEHLER  {n} existiert nicht")
        for autor, jahr, p in ZITAT_RE.findall(t):
            e = cache["pmid"].get(p)
            if not e:
                continue
            if e["jahr"] and abs(int(e["jahr"]) - int(jahr)) > 1:
                meldungen.append(f"FEHLER  PMID {p}: Jahr {jahr} im Text, PubMed sagt {e['jahr']} ({e['titel'][:70]})")
            if norm(autor) not in norm(e["erstautor"]) and autor[0].isupper() and len(autor) > 2:
                meldungen.append(f"HINWEIS PMID {p}: '{autor}' im Text, Erstautor laut PubMed '{e['erstautor']}' ({e['titel'][:70]})")
        for muster, art in VERBOTEN:
            for m in re.finditer(muster, t):
                zeile = t[:m.start()].count("\n") + 1
                meldungen.append(f"HINWEIS Zeile {zeile}: {art}: „{t[max(0, m.start()-40):m.end()+40].strip()}“")
        if not t.lstrip().startswith("#"):
            meldungen.append("FEHLER  Datei beginnt nicht mit einer Überschrift")
        woerter = len(t.split())
        n_fehler = sum(m.startswith("FEHLER") for m in meldungen)
        fehler += n_fehler
        print(f"== {d}: {woerter} Wörter, {len(set(PMID_RE.findall(t)))} PMIDs, "
              f"{len(set(NCT_RE.findall(t)))} NCTs, {n_fehler} Fehler")
        for m in meldungen:
            print("  " + m)
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
