# Auftrag: Peptid-Kapitel schreiben

Du schreibst Kapitel für das E-Book „Das Peptid-Handbuch – Alle Humanstudien im Vergleich“ von Josef Gallab
(Deutsch, Stand November 2026, erscheint bei Amazon KDP). Arbeitsverzeichnis: /home/user/ebooks

1. Lies zuerst `buch/STIL.md` vollständig und halte dich exakt daran (Aufbau, Zitierweise, absolute Regeln).
2. Lies `buch/gliederung.md`, damit du weißt, was in anderen Teilen steht (Grundlagen, Vergleich, Risiken,
   Zukunft werden von anderen geschrieben – wiederhole dort Behandeltes nicht ausführlich).
3. Für jedes deiner Peptide:
   - Studiendaten: `recherche/studien/<kuerzel>.json`. Sie ist groß – lies sie gezielt, z. B.
     `python3 -c "import json;d=json.load(open('recherche/studien/X.json'));[print(s['pmid'],s['jahr'],s['erstautor'],s['titel']) for s in d['humanstudien_alle']]"`
     und Abstracts einzeln. Die automatische Auswahl ist unvollständig: Suche zusätzlich gezielt mit
     `python3 werkzeuge/pubmed.py suche ...` nach den wichtigsten Zulassungs-/Endpunktstudien, großen Meta-Analysen,
     Fallserien und Sicherheitsdaten (z. B. Namen der Studienprogramme). Bei Peptiden ohne Humanstudien
     auch nach Fallberichten, Pilotstudien, Vergiftungs-/Nebenwirkungsberichten und Analysen von Graumarkt-Produkten suchen.
   - Jede Studie, die du nennst, hast du mit `python3 werkzeuge/pubmed.py zeige <PMID>` gelesen.
     Zahlen nur aus dem gelesenen Abstract/Registereintrag. Erstautor + Jahr müssen zum PubMed-Eintrag passen.
   - Laufende Studien über `python3 werkzeuge/pubmed.py ctsuche "<begriff>" 100` bzw. die `ctgov`-Liste in der JSON.
   - Nenne im Abschnitt „Studien am Menschen“ zu Beginn die Größenordnung der Studienlage
     (Anzahl der Humanstudien laut `humanstudien_alle`, Anzahl Registereinträge laut `ctgov`), Abfragedatum Oktober 2026.
   - Schreibe das Kapitel nach `buch/kapitel/<Dateiname>` (Dateinamen siehe unten).
   - Schreibe zusätzlich `recherche/vergleich/<kuerzel>.yaml` mit genau diesen Feldern (kurz, deutsch):
     ```
     name: ...
     gruppe: A|B|C|D|E|F
     evidenz: A|B|C|D
     zulassung_eu: ...      # z. B. "ja (Wegovy, Ozempic)" / "nein"
     zulassung_usa: ...
     wada: ...              # z. B. "verboten (S0)" / "nicht gelistet"
     humanstudien: <Zahl>   # aus humanstudien_alle
     registerstudien: <Zahl>
     kernergebnis: ...      # ein Satz, mit PMID
     hauptrisiko: ...       # ein Satz
     ausblick: ...          # ein Satz
     ```
   - Prüfe: `python3 werkzeuge/pruefen.py buch/kapitel/<Dateiname>` – alle FEHLER beheben, jeden HINWEIS ansehen
     (Autor-Hinweise: korrigiere den Autornamen auf den echten Erstautor).
4. Schreibe außerdem die Gruppeneinleitung `buch/kapitel/2<X>00-einleitung.md`, falls sie dir zugeteilt ist:
   beginnt mit `# Teil II · <Buchstabe> – <Gruppentitel>`, 400–800 Wörter: was die Gruppe verbindet,
   Überblickstabelle (Peptid | Evidenz | Zulassung | Kurz), Lesehinweis.
5. Kein git commit, keine Änderungen an Dateien anderer Gruppen, an werkzeuge/ oder recherche/studien/.
6. Gib am Ende eine kurze Liste zurück: Dateien, Wortzahl je Kapitel, Ergebnis von pruefen.py, offene Unsicherheiten.

Qualität vor Tempo – aber schreibe alle dir zugeteilten Kapitel vollständig fertig.
