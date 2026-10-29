# Das Peptid-Handbuch – Josef Gallab

E-Book für Amazon KDP in 7 Sprachen. Stand der Recherche: Oktober/November 2026.

## Fertige Dateien zum Hochladen

| Sprache | Titel | Manuskript | Cover |
|---|---|---|---|
| Deutsch | Das Peptid-Handbuch | `ausgabe/das-peptid-handbuch_de.epub` | `cover/cover_de.jpg` |
| Englisch | The Peptide Handbook | `ausgabe/das-peptid-handbuch_en.epub` | `cover/cover_en.jpg` |
| Spanisch | El manual de los péptidos | `ausgabe/das-peptid-handbuch_es.epub` | `cover/cover_es.jpg` |
| Französisch | Le guide des peptides | `ausgabe/das-peptid-handbuch_fr.epub` | `cover/cover_fr.jpg` |
| Italienisch | Il manuale dei peptidi | `ausgabe/das-peptid-handbuch_it.epub` | `cover/cover_it.jpg` |
| Niederländisch | Het peptidenhandboek | `ausgabe/das-peptid-handbuch_nl.epub` | `cover/cover_nl.jpg` |
| Portugiesisch (BR) | O manual dos peptídeos | `ausgabe/das-peptid-handbuch_pt.epub` | `cover/cover_pt.jpg` |

Zusätzlich je Sprache eine `.docx`-Fassung (zum Lesen/Bearbeiten in Word oder Kindle Create).
Alle EPUB-Dateien bestehen EPUBCheck 5.1 ohne Fehler und Warnungen.

## Vor dem Hochladen

1. **`kdp/vor-veroeffentlichung-pruefen.md`** – 209 Angaben ohne Studienbeleg (Zulassungen, Rechtslage,
   WADA, Patente) gegenprüfen. Änderungen im deutschen Kapitel machen; Übersetzungen anpassen.
2. **Übersetzungen** von Muttersprachler:innen stichprobenartig gegenlesen lassen.
3. **KDP-Angaben:** `kdp/de.md` (Deutsch, Schritt für Schritt) und `kdp/uebersetzungen.md` (alle anderen Sprachen:
   Klappentext, Schlüsselwörter, Kategorien).
4. KI-Frage bei KDP ehrlich beantworten: Text KI-generiert; Übersetzungen KI-generiert; Cover ohne Bild-KI.

## Inhalt

58 Peptide in 6 Gruppen, Grundlagen, großer Vergleich, Risiken, Zukunft, Glossar, Methodik und ein
Studienverzeichnis mit 3.216 Humanstudien-Veröffentlichungen. Rund 1.240 PubMed-Quellen und 260 Registerstudien
im Text, jede per Skript gegen PubMed bzw. ClinicalTrials.gov geprüft (Existenz, Jahr, Erstautor, Rückzug);
rund 1.450 Textstellen mit Zahlen wurden zusätzlich einzeln gegen die Abstracts geprüft.

## Ordner

- `buch/kapitel/` – deutsches Manuskript (Markdown) · `buch/<sprache>/kapitel/` – Übersetzungen
- `buch/STIL.md`, `buch/AUFTRAG_*.md` – Regeln für Schreiben, Faktenprüfung und Übersetzung
- `recherche/` – Peptidliste, Studiendaten (PubMed/ClinicalTrials.gov), Vergleichsdaten
- `werkzeuge/` – Skripte: `bauen.py <sprache>` (EPUB/DOCX), `pruefen.py` (Quellenprüfung),
  `uebersetzung_pruefen.py`, `cover.py`, `pubmed.py`, `studien_laden.py`
- `cover/` – Cover je Sprache; `cover/texte.yaml` für die Cover-Texte

## Neu bauen

```
python3 werkzeuge/bauen.py de        # bzw. en, es, fr, it, nl, pt
python3 werkzeuge/cover.py --sprache de [--hintergrund bild.png]   # mit KI-Hintergrund, sobald fal.ai/kie.ai Guthaben haben
```
