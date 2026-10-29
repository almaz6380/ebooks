"""Baut das E-Book (EPUB für KDP, zusätzlich DOCX) für eine Sprache.

python3 werkzeuge/bauen.py de        -> ausgabe/das-peptid-handbuch_de.epub (+ .docx)

Kapitel: Deutsch in buch/kapitel/, andere Sprachen in buch/<sprache>/kapitel/.
Metadaten: buch/metadaten.yaml (je Sprache).
"""
import pathlib
import re
import subprocess
import sys

import yaml

BASIS = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASIS / "werkzeuge"))
import satz  # noqa: E402
import verzeichnis  # noqa: E402


def main(sprache):
    meta_alle = yaml.safe_load((BASIS / "buch/metadaten.yaml").read_text())
    meta = meta_alle[sprache]
    kap_dir = BASIS / ("buch/kapitel" if sprache == "de" else f"buch/{sprache}/kapitel")
    bau = BASIS / f"bau/{sprache}"
    bau.mkdir(parents=True, exist_ok=True)

    verzeichnis.main(sprache, bau / "92-studienverzeichnis.md")
    # „0-“ sortiert vor „00-titelei“: Impressum steht ganz vorne
    (bau / "0-impressum.md").write_text(meta["impressum"], encoding="utf-8")

    # Kapitel in den Bauordner kopieren: Quellen als Fußnoten, Vorsichtshinweise gebündelt (satz.py),
    # geschützte Leerzeichen, damit Zahl und Einheit nicht getrennt werden
    teile = [bau / "0-impressum.md", bau / "92-studienverzeichnis.md"]
    for d in kap_dir.glob("*.md"):
        text = satz.vorbereiten(d.read_text(encoding="utf-8"), sprache, d.name)
        text = re.sub(r"(\d) (%|kg|mg|µg|mmol|Wochen|Monate|Jahre|Tage|Stunden)\b", "\\1\u00a0\\2", text)
        text = re.sub(r"(\d) %", "\\1\u00a0%", text)
        text = re.sub(r"(PMID|NCT|Phase) (\d)", "\\1\u00a0\\2", text)
        (bau / d.name).write_text(text, encoding="utf-8")
        teile.append(bau / d.name)
    teile.sort(key=lambda p: p.name)

    m = {
        "title": [{"type": "main", "text": meta["titel"]}, {"type": "subtitle", "text": meta["untertitel"]}],
        "creator": [{"role": "author", "text": meta["autor"]}],
        "lang": meta["lang"],
        "date": "2026-11",
        "rights": meta["rechte"],
        "description": meta["beschreibung_kurz"],
        "subject": meta.get("schlagworte", []),
        "toc-title": meta["inhalt"],
    }
    (bau / "meta.yaml").write_text(yaml.safe_dump(m, allow_unicode=True), encoding="utf-8")

    ausgabe = BASIS / "ausgabe"
    ausgabe.mkdir(exist_ok=True)
    name = f"das-peptid-handbuch_{sprache}"
    gemeinsam = ["pandoc", *map(str, teile), "--from", "markdown+pipe_tables-implicit_figures",
                 "--metadata-file", str(bau / "meta.yaml"), "--toc", "--toc-depth=2"]
    subprocess.run(gemeinsam + ["-o", str(ausgabe / f"{name}.epub"), "--split-level=2",
                                "--css", str(BASIS / "buch/stil.css"),
                                "--epub-cover-image", str(BASIS / f"cover/cover_{sprache}.jpg")], check=True)
    subprocess.run(gemeinsam + ["-o", str(ausgabe / f"{name}.docx")], check=True)
    for endung in ("epub", "docx"):
        f = ausgabe / f"{name}.{endung}"
        print(f"{f} ({f.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "de")
