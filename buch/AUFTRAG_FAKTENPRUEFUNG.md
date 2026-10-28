# Auftrag: Faktenprüfung und Korrektur

Buch: „Das Peptid-Handbuch“ (Deutsch), Kapitel in /home/user/ebooks/buch/kapitel/. Arbeitsverzeichnis /home/user/ebooks.
Dir sind bestimmte Dateien zugeteilt (siehe Nachricht). Bearbeite NUR diese Dateien.

## Was zu prüfen ist
Jede Zeile (Fließtext oder Tabellenzeile), die eine PMID und eine Zahl enthält (außer Jahreszahlen).
Liste dir die Zeilen z. B. so auf:
`grep -n "PMID" buch/kapitel/<datei> | grep -E "[0-9]"`

Für jede Zeile: Abstract jeder genannten PMID lesen (`python3 werkzeuge/pubmed.py zeige <PMID> [<PMID> ...]` –
mehrere PMIDs pro Aufruf spart Zeit; Abstracts derselben PMID nur einmal lesen). Prüfe streng:
- Teilnehmerzahlen, Prozente, Prozentpunkte vs. Prozent, kg, Hazard/Odds Ratios, Konfidenzintervalle, Dauer
- Zuordnung zu Studienarm/Dosis/Vergleichsgruppe, relative vs. absolute Angaben
- Erstautor und Jahr, Studientyp (RCT, Meta-Analyse, Fallbericht, Übersicht)
- Kernaussage (z. B. „verbesserte sich“ vs. „blieb stabil“, „signifikant“ vs. „nicht signifikant“)
- Angaben wie Land, Hersteller, Studienname: nur behalten, wenn im Abstract belegt oder allgemein gesichert
  (z. B. Studienname aus dem Titel, Hersteller eines zugelassenen Medikaments).

## Was zu tun ist
- **Korrekt:** nichts ändern.
- **Ungenau oder falsch:** direkt in der Datei korrigieren (Edit-Werkzeug, minimal, Stil und Satzbau beibehalten).
  Die Korrektur muss durch den Abstract-Wortlaut gedeckt sein.
- **Zahl nicht im Abstract:** Wenn die Zahl plausibel aus dem Volltext stammen könnte, prüfe, ob sie für die Aussage nötig ist.
  Wenn nicht nötig → Zahl entfernen und Satz so umformulieren, dass er durch den Abstract gedeckt ist.
  Wenn sie für eine Tabelle zentral ist → durch die Abstract-Angabe ersetzen oder „k. A.“ eintragen.
- Keine neuen Inhalte, keine neuen Quellen, keine stilistischen Überarbeitungen ohne sachlichen Grund.
- Achte darauf, dass Tabellen intakt bleiben (gleiche Spaltenzahl).
- Nach Abschluss jeder Datei: `python3 werkzeuge/pruefen.py buch/kapitel/<datei>` muss ohne FEHLER laufen.

## Bericht
Schreibe ein Protokoll nach /tmp/claude-0/-home-user-ebooks/29fe1b24-a774-5c4a-92e4-dd1d1dc503f0/scratchpad/faktenpruefung_<gruppe>.md:
je Datei Anzahl geprüfter Zeilen, Anzahl Korrekturen, und jede Korrektur als „Datei:Zeile – alt → neu – Grund (Abstract-Zitat)“.
Gib am Ende eine Zusammenfassung zurück: geprüfte Zeilen, Korrekturen gesamt, auffällige Muster. Kein git commit.
