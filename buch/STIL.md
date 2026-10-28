# Stil- und Arbeitsregeln für „Das Peptid-Handbuch“

Autor: Josef Gallab · Sprache: Deutsch (österreichischer Autor, aber neutrales Hochdeutsch) · Stand: November 2026

## Ton
- Sachlich, verständlich, für interessierte Laien. Fachbegriffe beim ersten Auftreten kurz erklären.
- Anrede der Leser mit „Sie“. Neutrale Formen bevorzugen („Teilnehmende“, „Fachleute“).
- Kurze Absätze, klare Sätze. Keine Werbesprache, keine Ausrufezeichen, kein Hype.
- Ehrlich über Unsicherheit: „Die Daten reichen nicht aus, um … zu sagen.“

## Absolute Regeln
1. **Keine erfundenen Quellen oder Zahlen.** Jede genannte Studie trägt PMID oder NCT-Nummer.
   Jede Zahl (Teilnehmende, Prozent, Kilogramm, p-Werte …) stammt aus dem Abstract bzw. dem Registereintrag,
   den du selbst mit `python3 werkzeuge/pubmed.py zeige <PMID>` bzw. `... nct <NCT>` gelesen hast.
   Wenn du eine Zahl nicht belegen kannst, lass sie weg.
2. **Keine Dosierungen, Einnahme-/Injektionsanleitungen, Zyklen, „Stacks“ oder Bezugsquellen** für nicht
   zugelassene Stoffe. Du darfst berichten, welche Dosis *in einer Studie* untersucht wurde, wenn das für das
   Verständnis nötig ist („in der Studie erhielten die Teilnehmenden 2,4 mg pro Woche“) – nie als Empfehlung.
   Bei zugelassenen Arzneimitteln: Verweis auf Fachinformation und ärztliche Begleitung.
3. **Keine Heil- oder Gesundheitsversprechen.** Nie „heilt“, „hilft gegen“, sondern „in Studie X verringerte sich …“.
4. Tier- und Laborergebnisse immer ausdrücklich als solche kennzeichnen („bei Ratten“, „in Zellkulturen“).
5. Rechtslage und WADA-Status nach bestem Wissen mit Hinweis „Stand 2026, bitte aktuell prüfen“.
6. Bei Zukunftsaussagen klar trennen: *gesichert* (laufende registrierte Studien, angekündigte Zulassungsanträge)
   vs. *Einschätzung* (eigene Prognose, als solche formuliert).

## Formatierung (Pandoc-Markdown, wird zu EPUB)
- Datei beginnt mit `## <Peptidname>` (Peptid-Kapitel) – keine `#`-Überschrift in Peptid-Kapiteln.
- Unterabschnitte mit `###`, nicht tiefer als `####`.
- Zitierweise im Text: `(Wilding 2021, PMID 33567185)` bzw. `(NCT05929066)`. Immer genau so: „PMID“ + Leerzeichen + Zahl.
- Tabellen: höchstens 4 Spalten (Kindle-Bildschirme sind schmal), kurze Zellen. Vorlage Studientabelle:

  | Studie | Teilnehmende und Design | Dauer | Ergebnis |
  |---|---|---|---|
  | STEP 1 (Wilding 2021), PMID 33567185 | 1.961 Erwachsene mit Adipositas, RCT gegen Placebo | 68 Wochen | −14,9 % Körpergewicht vs. −2,4 % |

- Zahlen im deutschen Format: 1.961 · 14,9 % · −2,4 kg.
- Keine Bilder, keine HTML-Tags, keine Fußnoten.

## Aufbau eines Peptid-Kapitels
```
## Name

### Steckbrief
(kurze Liste: Art/Struktur · Herkunft · Wirkprinzip · Zulassung EU/USA · WADA · Evidenzstufe A–D)

### Wie es wirken soll
### Studien am Menschen
(Fließtext + Studientabelle; bei großen Wirkstoffen die wichtigsten Zulassungs- und Endpunktstudien,
 Meta-Analysen; Rest zusammenfassend)
### Tier- und Laborstudien
### Risiken und Nebenwirkungen
### Rechtslage
### Laufende Studien und Ausblick
### Fazit
(drei bis fünf Sätze)
```
Evidenzstufen: **A** mehrere große RCTs am Menschen/Zulassung · **B** einzelne RCTs am Menschen ·
**C** nur kleine oder unkontrollierte Humanstudien · **D** nur Tier- und Laborstudien.

## Umfang (Richtwert)
- Große Wirkstoffe (Semaglutid, Tirzepatid, Liraglutid, Exenatid, Dulaglutid, Oxytocin, Kollagen …): 3.000–5.000 Wörter
- Mittlere: 1.800–3.000 Wörter
- Kleine mit dünner Datenlage: 1.000–1.800 Wörter

## Werkzeuge
- Studiendaten je Peptid: `recherche/studien/<kuerzel>.json` (Humanstudien mit Abstract, Meta-Analysen,
  Präklinik, ClinicalTrials.gov-Liste). Nicht alles auf einmal lesen – mit `python3 -c` / `jq` gezielt filtern.
- Gezielt suchen: `python3 werkzeuge/pubmed.py suche "semaglutide[ti] AND SELECT[tiab]" 10`
- Abstract lesen: `python3 werkzeuge/pubmed.py zeige 37952131`
- Registerstudien: `python3 werkzeuge/pubmed.py ctsuche "retatrutide" 50` und `... nct NCT05929066`
- Prüfen: `python3 werkzeuge/pruefen.py buch/kapitel/<datei>.md` – muss ohne FEHLER durchlaufen.
