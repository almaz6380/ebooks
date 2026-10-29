# Methodik

Dieser Anhang beschreibt, wie die Studien für dieses Buch gesucht, ausgewählt und geprüft wurden. Er soll es Ihnen ermöglichen, die Recherche nachzuvollziehen und bei Bedarf selbst zu wiederholen oder zu aktualisieren.

### Datenbanken

Grundlage der Recherche sind zwei frei zugängliche Datenbanken:

- **PubMed** (pubmed.ncbi.nlm.nih.gov), die Literaturdatenbank der US-amerikanischen National Library of Medicine. Sie verzeichnet Veröffentlichungen aus biomedizinischen Fachzeitschriften mit Titel, Autorinnen und Autoren, Zusammenfassung (Abstract) und Schlagwörtern. Jeder Eintrag hat eine eindeutige Nummer, die PMID.
- **ClinicalTrials.gov** (clinicaltrials.gov), das Studienregister der US-amerikanischen National Institutes of Health. Hier werden klinische Studien aus aller Welt vor ihrem Beginn registriert, mit Design, geplanter Teilnehmerzahl, Endpunkten und Status. Jede Studie hat eine NCT-Nummer.

Beide Datenbanken wurden über ihre offiziellen, öffentlich zugänglichen Programmierschnittstellen abgefragt: PubMed über die E-Utilities des National Center for Biotechnology Information, ClinicalTrials.gov über die Programmierschnittstelle in Version 2. Andere Datenbanken wie Embase, Cochrane Library, Web of Science, das EU-Studienregister oder nationale Register wurden nicht systematisch durchsucht.

### Abfragezeitraum

Die systematischen Abfragen erfolgten im **Oktober 2026**; die Zählung der Treffer für alle Peptide stammt vom 28. Oktober 2026. Ergänzende gezielte Suchen zu einzelnen Studien, Fallberichten und Übersichtsarbeiten wurden im selben Zeitraum durchgeführt. Später erschienene Studien sind nicht berücksichtigt. Der Stand des Buches ist November 2026.

### Suchstrategie

Für jedes der 58 Peptide und Vergleichsstoffe wurde ein eigener PubMed-Suchbegriff festgelegt. Er umfasst den internationalen Wirkstoffnamen sowie gebräuchliche Kurz-, Code- und Handelsbezeichnungen und sucht in Titel und Zusammenfassung (Kennzeichnung `[tiab]`) oder nur im Titel (`[ti]`). Bei mehrdeutigen Begriffen wurde der Suchbegriff eingeschränkt, etwa bei Kollagenpeptiden auf Arbeiten zur Einnahme oder bei Kisspeptin auf Arbeiten zur Verabreichung des Peptids.

Auf diesen Suchbegriff wurden drei Filter angewendet:

**Humanstudien.** Um klinische Studien am Menschen zu finden, wurde der Suchbegriff mit folgendem Filter kombiniert:

`(clinical trial[pt] OR randomized controlled trial[pt]) AND humans[mh]`

Der Teil `[pt]` sucht nach dem Publikationstyp, den PubMed jedem Artikel zuordnet; `humans[mh]` steht für das Schlagwort „Menschen“ im Schlagwortsystem MeSH. Gefunden werden damit Artikel, die als klinische Studie oder als randomisierte kontrollierte Studie gekennzeichnet sind und Menschen betreffen.

**Meta-Analysen und Übersichtsarbeiten.** Für zusammenfassende Arbeiten wurde der Suchbegriff mit diesem Filter kombiniert:

`(meta-analysis[pt] OR systematic review[pt])`

**Präklinik.** Bei Peptiden mit weniger als 25 gefundenen Humanstudien wurden zusätzlich die relevantesten übrigen Arbeiten ohne den Humanstudien-Filter ausgewertet, um Tier- und Laborstudien, Fallberichte und Analysen von Graumarkt-Produkten zu erfassen.

**Registerstudien.** In ClinicalTrials.gov wurde für jedes Peptid ein eigener, meist einfacher Suchbegriff mit dem Wirkstoffnamen verwendet. Erfasst wurden alle Einträge unabhängig von Status und Studienphase.

Über diese automatisierten Suchen hinaus wurde für jedes Kapitel gezielt nach den wichtigsten Zulassungs- und Endpunktstudien, großen Meta-Analysen, Studienprogrammen (zum Beispiel STEP, SURMOUNT oder SELECT), Sicherheitsdaten, Fallberichten und Laboranalysen von Graumarkt-Produkten gesucht. Für Teil I wurden außerdem Arbeiten zur Geschichte der Peptidmedizin, zu Darreichungsformen, zur Studienmethodik und zum Graumarkt recherchiert.

### Suchbegriffe je Peptid

Die folgenden Tabellen geben die PubMed-Suchbegriffe wieder, die für die systematische Abfrage verwendet wurden. An jeden Begriff wurden die oben beschriebenen Filter angehängt. Ein Sternchen am Wortende steht für beliebige Wortendungen, `OR` verknüpft alternative Bezeichnungen, `AND` schränkt die Suche ein.

#### A. Stoffwechsel und Gewicht

| Peptid | PubMed-Suchbegriff |
|---|---|
| Exenatid | `exenatide[tiab]` |
| Liraglutid | `liraglutide[tiab]` |
| Dulaglutid | `dulaglutide[tiab]` |
| Semaglutid | `semaglutide[tiab]` |
| Tirzepatid | `tirzepatide[tiab]` |
| Retatrutid | `retatrutide[tiab]` |
| Survodutid | `survodutide[tiab]` |
| Mazdutid | `mazdutide[tiab]` |
| Cagrilintid bzw. CagriSema | `cagrilintide[tiab]` |
| Amycretin | `amycretin[tiab]` |
| Maridebart Cafraglutid (MariTide) | `maridebart[tiab] OR AMG 133[tiab]` |
| Pramlintid | `pramlintide[tiab]` |
| Setmelanotid | `setmelanotide[tiab]` |
| AOD-9604 | `AOD9604[tiab] OR AOD-9604[tiab]` |
| Orforglipron (Vergleich) | `orforglipron[tiab]` |

#### B. Heilung, Regeneration und Immunsystem

| Peptid | PubMed-Suchbegriff |
|---|---|
| BPC-157 | `BPC 157[tiab] OR BPC-157[tiab] OR pentadecapeptide BPC[tiab]` |
| TB-500 bzw. Thymosin Beta-4 | `thymosin beta-4[tiab] OR thymosin beta4[tiab] OR TB-500[tiab] OR TB500[tiab]` |
| Thymosin Alpha-1 (Thymalfasin) | `thymosin alpha 1[tiab] OR thymalfasin[tiab] OR thymosin alpha1[tiab]` |
| KPV | `KPV[tiab] AND (peptide[tiab] OR tripeptide[tiab])` |
| LL-37 | `LL-37[tiab] OR cathelicidin[tiab]` |
| ARA-290 (Cibinetid) | `ARA 290[tiab] OR ARA290[tiab] OR cibinetide[tiab]` |
| Larazotid | `larazotide[tiab]` |
| Thymalin bzw. Thymogen | `thymalin[tiab] OR thymogen[tiab]` |

#### C. Wachstumshormon-Achse

| Peptid | PubMed-Suchbegriff |
|---|---|
| Sermorelin | `sermorelin[tiab]` |
| Tesamorelin | `tesamorelin[tiab]` |
| CJC-1295 | `CJC-1295[tiab] OR CJC 1295[tiab]` |
| Ipamorelin | `ipamorelin[tiab]` |
| GHRP-2 (Pralmorelin) | `GHRP-2[tiab] OR pralmorelin[tiab]` |
| GHRP-6 | `GHRP-6[tiab]` |
| Hexarelin | `hexarelin[tiab]` |
| Macimorelin | `macimorelin[tiab]` |
| Mecasermin (IGF-1) | `mecasermin[tiab] OR rhIGF-1[tiab]` |
| IGF-1 LR3 | `LR3-IGF-1[tiab] OR IGF-1 LR3[tiab] OR "Long R3"[tiab]` |
| Ibutamoren (MK-677) (Vergleich) | `ibutamoren[tiab] OR MK-677[tiab] OR MK-0677[tiab]` |

#### D. Gehirn, Schlaf und Langlebigkeit

| Peptid | PubMed-Suchbegriff |
|---|---|
| Semax | `semax[tiab]` |
| Selank | `selank[tiab]` |
| Cerebrolysin | `cerebrolysin[tiab]` |
| Dihexa | `dihexa[tiab]` |
| DSIP | `delta sleep-inducing peptide[tiab] OR DSIP[tiab]` |
| Epitalon (Epithalon) | `epitalon[tiab] OR epithalon[tiab] OR epithalone[tiab]` |
| Pinealon | `pinealon[tiab]` |
| MOTS-c | `MOTS-c[tiab]` |
| Humanin | `humanin[tiab]` |
| SS-31 (Elamipretid) | `elamipretide[tiab] OR SS-31[tiab]` |
| FOXO4-DRI | `FOXO4-DRI[tiab]` |
| Glutathion | `glutathione[ti] AND (supplementation[tiab] OR oral[tiab] OR intravenous[tiab])` |

#### E. Hormone, Sexualität und Pigmentierung

| Peptid | PubMed-Suchbegriff |
|---|---|
| Bremelanotid (PT-141) | `bremelanotide[tiab] OR PT-141[tiab]` |
| Melanotan II | `melanotan[tiab]` |
| Afamelanotid | `afamelanotide[tiab]` |
| Kisspeptin | `kisspeptin[tiab] AND (administration[tiab] OR infusion[tiab] OR injection[tiab])` |
| Oxytocin (intranasal) | `intranasal oxytocin[tiab]` |
| Gonadorelin | `gonadorelin[tiab]` |

#### F. Kollagen, Ernährung und Kosmetik

| Peptid | PubMed-Suchbegriff |
|---|---|
| Kollagenhydrolysat bzw. Kollagenpeptide | `(collagen hydrolysate[tiab] OR collagen peptide*[tiab]) AND (supplement*[tiab] OR oral[tiab] OR ingestion[tiab])` |
| Lactotripeptide (VPP/IPP) | `lactotripeptide*[tiab] OR (valyl-prolyl-proline[tiab])` |
| Carnosin | `carnosine[ti] AND (supplementation[tiab] OR oral[tiab])` |
| GHK-Cu (Kupferpeptid) | `GHK-Cu[tiab] OR copper tripeptide[tiab] OR copper peptide GHK[tiab]` |
| Palmitoyl-Pentapeptid-4 (Matrixyl) | `palmitoyl pentapeptide[tiab] OR matrixyl[tiab]` |
| Acetyl-Hexapeptid-8 (Argireline) | `acetyl hexapeptide[tiab] OR argireline[tiab]` |

### Umfang der Treffer

Insgesamt ergaben die 58 Abfragen mit dem Humanstudien-Filter 3.216 Treffer, mit dem Filter für Meta-Analysen und Übersichtsarbeiten 1.739 Treffer. In ClinicalTrials.gov wurden 4.879 Registereinträge gefunden. Diese Summen enthalten Mehrfachzählungen, weil manche Studien mehrere Peptide betreffen – etwa Vergleichsstudien zwischen Semaglutid und Tirzepatid. Die Zahlen je Peptid werden zu Beginn des Abschnitts „Studien am Menschen“ im jeweiligen Kapitel genannt.

Die Verteilung ist sehr ungleich: Auf die zugelassenen GLP-1-Medikamente entfallen Hunderte von Humanstudien, für viele Graumarkt-Peptide dagegen keine oder nur eine Handvoll.

### Auswahl und Auswertung

Für jedes Peptid wurden alle Treffer mit dem Humanstudien-Filter als Kurzliste (Titel, Jahr, Fachzeitschrift, Erstautorin oder Erstautor) erfasst; sie bilden die Grundlage des Studienverzeichnisses im Anhang. Die nach PubMed-Relevanz wichtigsten Humanstudien und Übersichtsarbeiten wurden mit ihren Zusammenfassungen gelesen und ausgewertet, ergänzt um die gezielt gesuchten Arbeiten.

Für die Darstellung im Text gilt:

- Jede genannte Studie wurde anhand ihres PubMed-Eintrags beziehungsweise Registereintrags gelesen.
- Zahlen – etwa Teilnehmerzahlen, Prozentwerte, Gewichtsveränderungen oder p-Werte – stammen ausschließlich aus der Zusammenfassung der Veröffentlichung oder aus dem Registereintrag. Was dort nicht belegt ist, wird nicht als Zahl genannt.
- Volltexte wurden nicht systematisch ausgewertet. Details, die nur im Volltext stehen, etwa einzelne Nebenwirkungsraten oder Untergruppen, fehlen daher teilweise.
- Tier- und Laborergebnisse werden ausdrücklich als solche gekennzeichnet.
- Bei laufenden Studien wird nur berichtet, was im Register steht. Sie werden als *gesichert* (registriert, laufend) gekennzeichnet, eigene Prognosen als *Einschätzung*.

### Evidenzstufen

Jedes Peptid erhielt eine Evidenzstufe nach folgenden Kriterien:

| Stufe | Kriterium |
|---|---|
| A | mehrere große randomisierte Studien am Menschen, Zulassung als Arzneimittel |
| B | einzelne randomisierte Studien am Menschen |
| C | nur kleine oder unkontrollierte Studien am Menschen |
| D | nur Tier- und Laborstudien |

Die Einstufung bezieht sich auf die Datenlage am Menschen insgesamt und auf das wichtigste untersuchte Anwendungsgebiet. Sie ist eine Bewertung des Autors auf Grundlage der ausgewerteten Studien und keine offizielle Klassifikation.

### Grenzen der Methodik

Wie jede Literaturrecherche hat auch diese Grenzen, die Sie bei der Lektüre berücksichtigen sollten:

**Treffer sind nicht gleich eigenständige Studien.** Eine große Studie wird oft in mehreren Artikeln veröffentlicht – Hauptergebnis, Untergruppen, Nachbeobachtung, Lebensqualität. Jeder dieser Artikel ist ein eigener Treffer. Umgekehrt können Studien in einem Artikel zusammengefasst sein. Die Trefferzahlen geben deshalb die Größenordnung der Forschung wieder, nicht die exakte Zahl unabhängiger Studien.

**Publikationstypen sind nicht immer korrekt.** Der Humanstudien-Filter beruht auf der Verschlagwortung durch PubMed. Manche Studien sind nicht als klinische Studie gekennzeichnet und fehlen deshalb; manche als klinische Studie gekennzeichnete Arbeiten sind bei näherem Hinsehen Beobachtungsstudien oder Laborarbeiten mit menschlichem Material. Sehr neue Artikel sind oft noch nicht vollständig verschlagwortet.

**Suchbegriffe können Lücken haben.** Ein Suchbegriff findet nur, was im Titel oder in der Zusammenfassung mit den gewählten Wörtern beschrieben ist. Studien, die einen Stoff nur unter einem Code-Namen oder in einer anderen Schreibweise führen, können fehlen. Umgekehrt können mehrdeutige Kürzel wie „KPV“ oder „SS-31“ auch Arbeiten zu ganz anderen Themen erfassen. Für die Kapitel wurden die Treffer deshalb gesichtet und nicht ungeprüft übernommen.

**Sprachen.** PubMed verzeichnet überwiegend englischsprachige Fachzeitschriften. Arbeiten, die nur in anderen Sprachen und in nicht verzeichneten Zeitschriften erschienen sind, fehlen weitgehend. Das betrifft besonders einige Peptide, die vor allem in Russland oder anderen Ländern Osteuropas erforscht und eingesetzt werden, etwa Semax, Selank, Epitalon oder Thymalin. Für sie ist die tatsächliche Studienlage möglicherweise umfangreicher, aber für internationale Leserinnen und Leser schwer überprüfbar.

**Nicht veröffentlichte Studien.** Studien, die nie veröffentlicht wurden, sind in PubMed nicht enthalten. Das Register ClinicalTrials.gov hilft, solche Lücken zu erkennen, erfasst aber nicht alle Studien weltweit.

**Nur Zusammenfassungen.** Die Auswertung beruht auf den Zusammenfassungen. Sie geben die Hauptergebnisse wieder, können aber Einschränkungen, Nebenwirkungen oder methodische Schwächen verkürzt darstellen.

**Momentaufnahme.** Die Recherche gibt den Stand vom Oktober 2026 wieder. In schnell wachsenden Feldern wie den GLP-1-Medikamenten erscheinen jede Woche neue Studien.

### Qualitätsprüfung

Die Datenbankabfragen liefen über die genannten Schnittstellen mit eigens dafür geschriebenen Hilfsprogrammen. Für die Auswertung galten verbindliche Regeln: Jede Studie im Text wird mit PMID oder NCT-Nummer zitiert; jede Zahl muss aus einer tatsächlich abgerufenen Zusammenfassung oder einem Registereintrag stammen; Studien dürfen nur genannt werden, wenn ihr Eintrag zuvor abgerufen und gelesen wurde.

Zusätzlich wurde jedes Kapitel mit einem Prüfprogramm kontrolliert. Es ruft für jede im Text genannte PMID und NCT-Nummer den Eintrag in PubMed beziehungsweise ClinicalTrials.gov ab und meldet als Fehler, wenn eine Nummer nicht existiert. Es vergleicht außerdem Erstautorin oder Erstautor und Erscheinungsjahr, die im Text vor der PMID stehen, mit dem Datenbankeintrag und weist auf Abweichungen hin. Schließlich sucht es nach unzulässigen Formulierungen wie Heilversprechen, Dosierungsempfehlungen oder Hinweisen auf Bezugsquellen. Ein Kapitel galt erst als fertig, wenn diese Prüfung ohne Fehler durchlief. Außerdem prüft das Programm, ob eine zitierte Arbeit inzwischen zurückgezogen wurde; solche Arbeiten sind im Text ausdrücklich gekennzeichnet. Zum Abschluss wurden rund 1.450 Textstellen mit Zahlen einzeln mit den Zusammenfassungen verglichen und, wo nötig, korrigiert.

Diese Prüfung stellt sicher, dass jede zitierte Quelle existiert und richtig zugeordnet ist. Sie kann nicht vollständig ausschließen, dass ein Ergebnis im Text verkürzt oder missverständlich wiedergegeben ist. Deshalb sind alle Quellen so angegeben, dass Sie sie selbst nachschlagen können – wie das geht, steht im Abschnitt „Über dieses Buch“ am Anfang.
