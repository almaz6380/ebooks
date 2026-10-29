"""Erzeugt das vollständige Studienverzeichnis (Anhang) aus recherche/studien/*.json.

python3 werkzeuge/verzeichnis.py <sprache> <zieldatei>
"""
import json
import pathlib
import sys

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from studien_laden import kuerzel  # noqa: E402

BASIS = pathlib.Path(__file__).resolve().parent.parent

TEXTE = yaml.safe_load((BASIS / "werkzeuge/verzeichnis_texte.yaml").read_text())


def esc(s):
    for z in "*_[]`<>|#":
        s = s.replace(z, "\\" + z)
    return s


def main(sprache, ziel):
    t = TEXTE[sprache]
    liste = yaml.safe_load((BASIS / "recherche/peptide.yaml").read_text())
    kap = BASIS / ("buch/kapitel" if sprache == "de" else f"buch/{sprache}/kapitel")
    namen = {}
    for f in kap.glob("2[A-F][0-9][0-9]-*.md"):
        erste = f.read_text(encoding="utf-8").lstrip().splitlines()[0]
        if erste.startswith("## "):
            namen[f.stem[5:]] = {sprache: erste[3:].strip()}
    teile = [f"# {t['titel']}\n", t["einleitung"], ""]
    gesamt = 0
    for gruppe in liste.values():
        for p in gruppe["peptide"]:
            k = kuerzel(p["name"])
            d = json.loads((BASIS / f"recherche/studien/{k}.json").read_text())
            studien = sorted(d["humanstudien_alle"], key=lambda s: (s["jahr"], s["pmid"]), reverse=True)
            gesamt += len(studien)
            name = namen.get(k, {}).get(sprache, p["name"])
            teile.append(f"## {name} ({len(studien)})\n")
            if not studien:
                teile.append(t["keine"] + "\n")
                continue
            for s in studien:
                teile.append(f"- {s['jahr']} · {esc(s['erstautor'])} · *{esc(s['journal'])}* · "
                             f"{esc(s['titel'])}. PMID {s['pmid']}")
            teile.append("")
    teile.insert(2, t["summe"].format(gesamt=f"{gesamt:,}".replace(",", t["tausender"])) + "\n")
    pathlib.Path(ziel).write_text("\n".join(teile), encoding="utf-8")
    print(f"{ziel}: {gesamt} Einträge")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
