"""Vergleicht übersetzte Kapitel mit dem deutschen Original.

python3 werkzeuge/uebersetzung_pruefen.py <sprache> [dateiname ...]
Ohne Dateinamen werden alle deutschen Kapitel geprüft.
Prüft: Datei vorhanden, gleiche PMIDs/NCTs, gleiche Zahl an Überschriften je Ebene, Tabellenzeilen, Listenpunkte;
Längenverhältnis (Hinweis auf Kürzungen). Exit-Code 1 bei Fehlern.
"""
import collections
import pathlib
import re
import sys

BASIS = pathlib.Path(__file__).resolve().parent.parent


def kennzahlen(text):
    zeilen = text.splitlines()
    return {
        "pmid": collections.Counter(re.findall(r"PMID\s*(\d{6,9})", text)),
        "nct": collections.Counter(re.findall(r"NCT\d{8}", text)),
        "ueberschriften": collections.Counter(len(m) for m in re.findall(r"^(#{1,4}) ", text, re.M)),
        "tabellenzeilen": sum(1 for z in zeilen if z.lstrip().startswith("|")),
        "listenpunkte": sum(1 for z in zeilen if re.match(r"\s*([-*]|\d+\.) ", z)),
        "zeichen": len(text),
    }


def main(sprache, namen):
    quelle = BASIS / "buch/kapitel"
    ziel = BASIS / f"buch/{sprache}/kapitel"
    dateien = [quelle / n for n in namen] if namen else sorted(quelle.glob("*.md"))
    fehler = 0
    for q in dateien:
        z = ziel / q.name
        meldungen = []
        if not z.exists():
            print(f"FEHLT   {z}")
            fehler += 1
            continue
        a, b = kennzahlen(q.read_text(encoding="utf-8")), kennzahlen(z.read_text(encoding="utf-8"))
        for feld in ("pmid", "nct"):
            if a[feld] != b[feld]:
                fehlend = set(a[feld]) - set(b[feld])
                extra = set(b[feld]) - set(a[feld])
                if fehlend or extra:
                    meldungen.append(f"FEHLER  {feld}: fehlend {sorted(fehlend)} zusätzlich {sorted(extra)}")
        if a["ueberschriften"] != b["ueberschriften"] and not q.name.startswith("90-glossar"):
            meldungen.append(f"FEHLER  Überschriften {dict(a['ueberschriften'])} vs. {dict(b['ueberschriften'])}")
        if a["tabellenzeilen"] != b["tabellenzeilen"]:
            meldungen.append(f"FEHLER  Tabellenzeilen {a['tabellenzeilen']} vs. {b['tabellenzeilen']}")
        if abs(a["listenpunkte"] - b["listenpunkte"]) > 1:
            meldungen.append(f"FEHLER  Listenpunkte {a['listenpunkte']} vs. {b['listenpunkte']}")
        verh = b["zeichen"] / max(1, a["zeichen"])
        if verh < 0.75 or verh > 1.35:
            meldungen.append(f"FEHLER  Längenverhältnis {verh:.2f} – gekürzt oder ergänzt?")
        fehler += sum(m.startswith("FEHLER") for m in meldungen)
        print(f"{'OK     ' if not meldungen else 'PRÜFEN '} {q.name} (Länge {verh:.2f})")
        for m in meldungen:
            print("   " + m)
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
