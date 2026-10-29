# Auftrag: Duzen, KI-Hinweise entfernen, Vorwort/Autorenseite übersetzen

Buch: „Das Peptid-Handbuch“ von Josef Gallab. Arbeitsverzeichnis /home/user/ebooks.
Deutsch liegt in `buch/kapitel/`, deine Sprache in `buch/<sprache>/kapitel/`. Kein git commit.

## Aufgabe A – Leser duzen (nur wenn in der Nachricht verlangt)
Der Autor hat entschieden: Das ganze Buch duzt die Leserin/den Leser (informelle Anrede).
- Deutsch: Sie → du, Ihnen → dir, Ihr/Ihre … → dein/deine …, Verbformen anpassen („finden Sie“ → „findest du“,
  „Prüfen Sie“ → „Prüfe“). Achtung: „Sie“ als 3. Person Plural („sie“, z. B. „Die Studien … Sie zeigen“ am Satzanfang)
  NICHT ändern – nur die Leseranrede.
- ES: usted → tú (Verbformen, Pronomen, Possessiva: „su médico“ → „tu médico“ nur wenn der Leser gemeint ist).
- FR: vous → tu (toi, ton/ta/tes, Verbformen). Nur Leseranrede, nicht „vous“ in Zitaten/anderen Bedeutungen.
- IT: Lei/La/Le/Sua/Suo → tu/ti/te/tuo/tua (Verbformen, Imperativ). Unpersönliche Formulierungen dürfen bleiben.
- NL: u/uw → je/jij/jouw (Verbformen).
Vorgehen: Finde alle Stellen mit Leseranrede (grep), ändere nur diese, minimal und grammatisch korrekt.
Keine anderen inhaltlichen Änderungen. Danach `python3 werkzeuge/uebersetzung_pruefen.py <sprache>` (bei Nicht-Deutsch)
bzw. `python3 werkzeuge/pruefen.py buch/kapitel/*.md` (Deutsch) – keine neuen Fehler.

## Aufgabe B – KI-Hinweise entfernen (alle Nicht-Deutsch-Sprachen)
Das Buch darf nicht erwähnen, dass es mit KI erstellt wurde. Die deutsche Fassung ist bereits angepasst – übernimm
die Änderungen sinngemäß und vollständig in deine Sprache:
1. `00-titelei.md`: Überschrift „Transparenz: Wie dieses Buch entstanden ist“ heißt jetzt „Wie dieses Buch entstanden ist“;
   der erste Absatz darunter lautet jetzt: „Für dieses Buch wurden die Datenbanken PubMed und ClinicalTrials.gov systematisch
   durchsucht und die Zusammenfassungen der gefundenen Studien ausgewertet.“ (Der zweite Absatz bleibt.)
2. `91-methodik.md`: Der Abschnitt „KI-Unterstützung und Qualitätsprüfung“ heißt jetzt „Qualitätsprüfung“; Einleitung und
   Aufzählung zur KI wurden ersetzt durch: „Die Datenbankabfragen liefen über die genannten Schnittstellen mit eigens dafür
   geschriebenen Hilfsprogrammen. Für die Auswertung galten verbindliche Regeln:“ (danach geht es mit „Jede Studie im Text
   wird mit PMID oder NCT-Nummer zitiert; …“ weiter). Am Ende des Absatzes „Ein Kapitel galt erst als fertig, …“ wurden zwei
   Sätze ergänzt (Rückzugsprüfung und rund 1.450 einzeln geprüfte Textstellen) – siehe deutsche Datei.
Vergleiche mit `buch/kapitel/00-titelei.md` und `buch/kapitel/91-methodik.md` und mache deine Fassung inhaltlich identisch.
Suche danach in ALLEN deinen Dateien nach weiteren Erwähnungen, dass das Buch mit KI/AI erstellt wurde, und entferne sie.
NICHT entfernen: inhaltliche Themen wie „KI im Peptiddesign“ in 53-prognosen.md (das ist ein Forschungsthema, kein Hinweis
auf die Entstehung des Buches). „KI“ als Konfidenzintervall ist ebenfalls kein KI-Hinweis.

## Aufgabe C – Vorwort und Autorenseite übersetzen (alle Nicht-Deutsch-Sprachen)
Übersetze `buch/kapitel/0-vorwort.md` → `buch/<sprache>/kapitel/0-vorwort.md` und
`buch/kapitel/93-autor.md` → `buch/<sprache>/kapitel/93-autor.md`. Persönlicher, warmer Ton, informelle Anrede (du/tu/tú/je/você;
Englisch: you). Überschriften: „# Vorwort“ / „# Über den Autor“ in deiner Sprache. Unterschrift *Josef Gallab* bleibt.
Treu übersetzen, nichts ergänzen.

## Abschluss
`python3 werkzeuge/uebersetzung_pruefen.py <sprache>` muss für alle Dateien OK melden. Gib eine kurze Liste der geänderten Dateien
und der Zahl geänderter Anrede-Stellen zurück.
