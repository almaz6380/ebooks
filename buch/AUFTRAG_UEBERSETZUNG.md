# Auftrag: Kapitel übersetzen

Buch: „Das Peptid-Handbuch – Alle Humanstudien im Vergleich“ von Josef Gallab (E-Book, Amazon KDP, Stand November 2026).
Arbeitsverzeichnis: /home/user/ebooks. Quelle: `buch/kapitel/<datei>.md` (Deutsch).
Ziel: `buch/<sprache>/kapitel/<gleicher Dateiname>.md`.

## Regeln
1. **Vollständig und treu übersetzen.** Nichts kürzen, nichts hinzufügen, keine Inhalte „verbessern“.
   Jede Tabellenzeile, jede Liste, jeder Absatz bleibt erhalten. Struktur (Überschriftenebenen `#`, `##`, `###`, `####`),
   Tabellen, Fettdruck und Listen bleiben identisch.
2. **Zitate unverändert:** „PMID 12345678“ und „NCT01234567“ exakt so übernehmen (auch das Wort PMID).
   Autorennamen und Jahre unverändert. Studiennamen (STEP 1, SURMOUNT-5 …) unverändert.
   Beispiel EN: `(Wilding 2021, PMID 33567185)`.
3. **Zahlenformat der Zielsprache:** EN: 1,961 · 14.9% · −2.4 kg. FR: 1 961 · 14,9 % · −2,4 kg.
   ES/IT/PT/NL: 1.961 · 14,9 % · −2,4 kg (ES: 1961 bzw. 14,9 %; NL: 14,9% ohne Leerzeichen ist auch üblich – einheitlich bleiben).
4. **Fachbegriffe** in der in der Zielsprache üblichen medizinischen Form (Wirkstoffnamen nach INN der Zielsprache:
   EN semaglutide, FR sémaglutide, ES semaglutida, IT semaglutide, PT semaglutida, NL semaglutide).
   Handelsnamen unverändert. Abkürzungen wie HbA1c, GLP-1, RCT, WADA unverändert; deutsche Abkürzungen
   (z. B. „vs.“, „u. a.“) in die Zielsprache übertragen.
5. **Ton:** sachlich, verständlich, für interessierte Laien; Leseranrede in der höflichen/üblichen Sachbuchform der Zielsprache
   (EN: you; FR: vous; ES: usted bzw. neutral; IT: Lei bzw. neutral; PT-BR: você; NL: u).
6. **Inhaltliche Treue bei Recht/Medizin:** Rechtsangaben (EU, Österreich, Deutschland, USA, WADA) unverändert inhaltlich
   übernehmen – keine eigenen Länderergänzungen. Vorsichtsformulierungen („Stand 2026, bitte aktuell prüfen“,
   „nach Kenntnis des Autors“, „Einschätzung“) immer mitübersetzen. Keine Heilversprechen, keine Dosierempfehlungen
   hinzufügen. Verweise auf Kapitel („siehe Kapitel Semaglutid“) mit dem übersetzten Kapitelnamen.
7. Englische Originaltitel von Studien, falls im Text zitiert, bleiben englisch.
8. Keine HTML-Tags, keine Fußnoten.

## Ablauf
- Lies vor dem Start `buch/STIL.md` (Hintergrund) und eine bereits übersetzte Datei derselben Sprache, falls vorhanden,
  damit Begriffe einheitlich sind. Für Glossar-Begriffe: halte dich an `buch/<sprache>/glossar_begriffe.md`, falls vorhanden.
- Übersetze Datei für Datei. Große Dateien in mehreren Schritten schreiben (z. B. Abschnitt für Abschnitt anhängen),
  aber am Ende muss jede Zieldatei vollständig sein.
- Prüfe danach jede Datei: `python3 werkzeuge/uebersetzung_pruefen.py <sprache> <datei>` – meldet fehlende/zusätzliche PMIDs/NCTs,
  abweichende Überschriften- und Tabellenzeilenzahl. Alle Abweichungen beheben.
- Kein git commit. Gib am Ende die Liste der Dateien und das Prüfergebnis zurück.
