# Metodologia

Questa appendice descrive come sono stati cercati, selezionati e verificati gli studi per questo libro. Dovrebbe permetterLe di ricostruire la ricerca e, se necessario, di ripeterla o aggiornarla in prima persona.

### Banche dati

La ricerca si basa su due banche dati liberamente accessibili:

- **PubMed** (pubmed.ncbi.nlm.nih.gov), la banca dati bibliografica della National Library of Medicine statunitense. Registra pubblicazioni di riviste biomediche con titolo, autori, riassunto (abstract) e parole chiave. Ogni voce ha un numero univoco, il PMID.
- **ClinicalTrials.gov** (clinicaltrials.gov), il registro degli studi dei National Institutes of Health statunitensi. Qui vengono registrati prima del loro inizio studi clinici da tutto il mondo, con disegno, numero previsto di partecipanti, endpoint e stato. Ogni studio ha un numero NCT.

Entrambe le banche dati sono state interrogate tramite le loro interfacce di programmazione ufficiali e pubblicamente accessibili: PubMed tramite le E-Utilities del National Center for Biotechnology Information, ClinicalTrials.gov tramite l'interfaccia di programmazione nella versione 2. Altre banche dati come Embase, Cochrane Library, Web of Science, il registro UE degli studi o registri nazionali non sono state consultate in modo sistematico.

### Periodo delle interrogazioni

Le interrogazioni sistematiche sono state effettuate nell'**ottobre 2026**; il conteggio dei risultati per tutti i peptidi risale al 28 ottobre 2026. Ricerche mirate integrative su singoli studi, casi clinici e revisioni sono state svolte nello stesso periodo. Gli studi pubblicati successivamente non sono considerati. Il libro è aggiornato a novembre 2026.

### Strategia di ricerca

Per ciascuno dei 58 peptidi e sostanze di confronto è stato definito un proprio termine di ricerca PubMed. Comprende il nome internazionale del principio attivo e le abbreviazioni, i nomi in codice e i nomi commerciali di uso comune, e cerca nel titolo e nel riassunto (contrassegno `[tiab]`) o solo nel titolo (`[ti]`). Per termini ambigui il termine di ricerca è stato ristretto, per esempio per i peptidi di collagene ai lavori sull'assunzione o per la kisspeptina ai lavori sulla somministrazione del peptide.

A questo termine di ricerca sono stati applicati tre filtri:

**Studi sull'uomo.** Per trovare studi clinici sull'uomo, il termine di ricerca è stato combinato con il seguente filtro:

`(clinical trial[pt] OR randomized controlled trial[pt]) AND humans[mh]`

La parte `[pt]` cerca il tipo di pubblicazione che PubMed assegna a ogni articolo; `humans[mh]` sta per la parola chiave «esseri umani» nel sistema di parole chiave MeSH. Si trovano così articoli contrassegnati come studio clinico o come studio randomizzato controllato e che riguardano esseri umani.

**Meta-analisi e revisioni.** Per i lavori di sintesi il termine di ricerca è stato combinato con questo filtro:

`(meta-analysis[pt] OR systematic review[pt])`

**Ricerca preclinica.** Per i peptidi con meno di 25 studi sull'uomo trovati sono stati inoltre analizzati i lavori restanti più rilevanti senza il filtro per gli studi sull'uomo, per includere studi sugli animali e di laboratorio, casi clinici e analisi di prodotti del mercato grigio.

**Studi di registro.** Su ClinicalTrials.gov per ogni peptide è stato usato un proprio termine di ricerca, per lo più semplice, con il nome del principio attivo. Sono state registrate tutte le voci, indipendentemente da stato e fase dello studio.

Oltre a queste ricerche automatizzate, per ogni capitolo sono stati cercati in modo mirato i principali studi registrativi e di esito, grandi meta-analisi, programmi di studio (per esempio STEP, SURMOUNT o SELECT), dati di sicurezza, casi clinici e analisi di laboratorio di prodotti del mercato grigio. Per la Parte I sono stati inoltre ricercati lavori sulla storia della medicina dei peptidi, sulle forme farmaceutiche, sulla metodologia degli studi e sul mercato grigio.

### Termini di ricerca per peptide

Le tabelle seguenti riportano i termini di ricerca PubMed usati per l'interrogazione sistematica. A ogni termine sono stati aggiunti i filtri descritti sopra. Un asterisco alla fine di una parola sta per qualsiasi desinenza, `OR` collega denominazioni alternative, `AND` restringe la ricerca.

#### A. Metabolismo e peso

| Peptide | Termine di ricerca PubMed |
|---|---|
| Exenatide | `exenatide[tiab]` |
| Liraglutide | `liraglutide[tiab]` |
| Dulaglutide | `dulaglutide[tiab]` |
| Semaglutide | `semaglutide[tiab]` |
| Tirzepatide | `tirzepatide[tiab]` |
| Retatrutide | `retatrutide[tiab]` |
| Survodutide | `survodutide[tiab]` |
| Mazdutide | `mazdutide[tiab]` |
| Cagrilintide o CagriSema | `cagrilintide[tiab]` |
| Amicretina | `amycretin[tiab]` |
| Maridebart cafraglutide (MariTide) | `maridebart[tiab] OR AMG 133[tiab]` |
| Pramlintide | `pramlintide[tiab]` |
| Setmelanotide | `setmelanotide[tiab]` |
| AOD-9604 | `AOD9604[tiab] OR AOD-9604[tiab]` |
| Orforglipron (confronto) | `orforglipron[tiab]` |

#### B. Guarigione, rigenerazione e sistema immunitario

| Peptide | Termine di ricerca PubMed |
|---|---|
| BPC-157 | `BPC 157[tiab] OR BPC-157[tiab] OR pentadecapeptide BPC[tiab]` |
| TB-500 o timosina beta-4 | `thymosin beta-4[tiab] OR thymosin beta4[tiab] OR TB-500[tiab] OR TB500[tiab]` |
| Timosina alfa-1 (timalfasina) | `thymosin alpha 1[tiab] OR thymalfasin[tiab] OR thymosin alpha1[tiab]` |
| KPV | `KPV[tiab] AND (peptide[tiab] OR tripeptide[tiab])` |
| LL-37 | `LL-37[tiab] OR cathelicidin[tiab]` |
| ARA-290 (cibinetide) | `ARA 290[tiab] OR ARA290[tiab] OR cibinetide[tiab]` |
| Larazotide | `larazotide[tiab]` |
| Thymalin o Thymogen | `thymalin[tiab] OR thymogen[tiab]` |

#### C. Asse dell'ormone della crescita

| Peptide | Termine di ricerca PubMed |
|---|---|
| Sermorelina | `sermorelin[tiab]` |
| Tesamorelina | `tesamorelin[tiab]` |
| CJC-1295 | `CJC-1295[tiab] OR CJC 1295[tiab]` |
| Ipamorelina | `ipamorelin[tiab]` |
| GHRP-2 (pralmorelina) | `GHRP-2[tiab] OR pralmorelin[tiab]` |
| GHRP-6 | `GHRP-6[tiab]` |
| Hexarelin | `hexarelin[tiab]` |
| Macimorelina | `macimorelin[tiab]` |
| Mecasermina (IGF-1) | `mecasermin[tiab] OR rhIGF-1[tiab]` |
| IGF-1 LR3 | `LR3-IGF-1[tiab] OR IGF-1 LR3[tiab] OR "Long R3"[tiab]` |
| Ibutamoren (MK-677) (confronto) | `ibutamoren[tiab] OR MK-677[tiab] OR MK-0677[tiab]` |

#### D. Cervello, sonno e longevità

| Peptide | Termine di ricerca PubMed |
|---|---|
| Semax | `semax[tiab]` |
| Selank | `selank[tiab]` |
| Cerebrolysin | `cerebrolysin[tiab]` |
| Dihexa | `dihexa[tiab]` |
| DSIP | `delta sleep-inducing peptide[tiab] OR DSIP[tiab]` |
| Epitalon (Epithalon) | `epitalon[tiab] OR epithalon[tiab] OR epithalone[tiab]` |
| Pinealon | `pinealon[tiab]` |
| MOTS-c | `MOTS-c[tiab]` |
| Umanina | `humanin[tiab]` |
| SS-31 (elamipretide) | `elamipretide[tiab] OR SS-31[tiab]` |
| FOXO4-DRI | `FOXO4-DRI[tiab]` |
| Glutatione | `glutathione[ti] AND (supplementation[tiab] OR oral[tiab] OR intravenous[tiab])` |

#### E. Ormoni, sessualità e pigmentazione

| Peptide | Termine di ricerca PubMed |
|---|---|
| Bremelanotide (PT-141) | `bremelanotide[tiab] OR PT-141[tiab]` |
| Melanotan II | `melanotan[tiab]` |
| Afamelanotide | `afamelanotide[tiab]` |
| Kisspeptina | `kisspeptin[tiab] AND (administration[tiab] OR infusion[tiab] OR injection[tiab])` |
| Ossitocina (intranasale) | `intranasal oxytocin[tiab]` |
| Gonadorelina | `gonadorelin[tiab]` |

#### F. Collagene, alimentazione e cosmetica

| Peptide | Termine di ricerca PubMed |
|---|---|
| Collagene idrolizzato o peptidi di collagene | `(collagen hydrolysate[tiab] OR collagen peptide*[tiab]) AND (supplement*[tiab] OR oral[tiab] OR ingestion[tiab])` |
| Lattotripeptidi (VPP/IPP) | `lactotripeptide*[tiab] OR (valyl-prolyl-proline[tiab])` |
| Carnosina | `carnosine[ti] AND (supplementation[tiab] OR oral[tiab])` |
| GHK-Cu (peptide di rame) | `GHK-Cu[tiab] OR copper tripeptide[tiab] OR copper peptide GHK[tiab]` |
| Palmitoil pentapeptide-4 (Matrixyl) | `palmitoyl pentapeptide[tiab] OR matrixyl[tiab]` |
| Acetil esapeptide-8 (Argireline) | `acetyl hexapeptide[tiab] OR argireline[tiab]` |

### Entità dei risultati

Complessivamente le 58 interrogazioni hanno dato 3.216 risultati con il filtro per gli studi sull'uomo e 1.739 risultati con il filtro per meta-analisi e revisioni. Su ClinicalTrials.gov sono state trovate 4.879 voci di registro. Questi totali contengono conteggi multipli, perché alcuni studi riguardano più peptidi – per esempio gli studi di confronto tra semaglutide e tirzepatide. I numeri per peptide sono indicati all'inizio della sezione «Studi sull'uomo» del rispettivo capitolo.

La distribuzione è molto diseguale: ai farmaci GLP-1 autorizzati corrispondono centinaia di studi sull'uomo, per molti peptidi del mercato grigio invece nessuno o solo una manciata.

### Selezione e analisi

Per ogni peptide tutti i risultati con il filtro per gli studi sull'uomo sono stati registrati come elenco sintetico (titolo, anno, rivista, primo autore o prima autrice); costituiscono la base dell'elenco degli studi in appendice. Gli studi sull'uomo e le revisioni più importanti secondo la rilevanza di PubMed sono stati letti e analizzati con i loro riassunti, integrati dai lavori cercati in modo mirato.

Per la presentazione nel testo vale:

- Ogni studio citato è stato letto sulla base della sua voce in PubMed o della voce di registro.
- I numeri – per esempio numeri di partecipanti, percentuali, variazioni di peso o valori p – provengono esclusivamente dal riassunto della pubblicazione o dalla voce di registro. Ciò che non è documentato lì non viene citato come numero.
- I testi completi non sono stati analizzati in modo sistematico. Dettagli che si trovano solo nel testo completo, per esempio singoli tassi di effetti collaterali o sottogruppi, mancano quindi in parte.
- I risultati sugli animali e di laboratorio sono indicati espressamente come tali.
- Per gli studi in corso viene riportato solo ciò che è nel registro. Sono contrassegnati come *accertati* (registrati, in corso), le previsioni proprie come *valutazione*.

### Livelli di evidenza

Ogni peptide ha ricevuto un livello di evidenza secondo i seguenti criteri:

| Livello | Criterio |
|---|---|
| A | più grandi studi randomizzati sull'uomo, autorizzazione come farmaco |
| B | singoli studi randomizzati sull'uomo |
| C | solo studi piccoli o non controllati sull'uomo |
| D | solo studi sugli animali e di laboratorio |

La classificazione si riferisce ai dati complessivi sull'uomo e al principale ambito d'uso studiato. È una valutazione dell'autore basata sugli studi analizzati e non una classificazione ufficiale.

### Limiti della metodologia

Come ogni ricerca bibliografica, anche questa ha dei limiti, di cui dovrebbe tenere conto durante la lettura:

**I risultati non equivalgono a studi indipendenti.** Un grande studio viene spesso pubblicato in più articoli – risultato principale, sottogruppi, follow-up, qualità della vita. Ciascuno di questi articoli è un risultato a sé. Al contrario, più studi possono essere riassunti in un unico articolo. I numeri dei risultati riflettono quindi l'ordine di grandezza della ricerca, non il numero esatto di studi indipendenti.

**I tipi di pubblicazione non sono sempre corretti.** Il filtro per gli studi sull'uomo si basa sull'indicizzazione di PubMed. Alcuni studi non sono contrassegnati come studio clinico e quindi mancano; alcuni lavori contrassegnati come studio clinico sono, a un esame più attento, studi osservazionali o lavori di laboratorio con materiale umano. Gli articoli molto recenti spesso non sono ancora completamente indicizzati.

**I termini di ricerca possono avere lacune.** Un termine di ricerca trova solo ciò che è descritto nel titolo o nel riassunto con le parole scelte. Gli studi che indicano una sostanza solo con un nome in codice o con un'altra grafia possono mancare. Al contrario, sigle ambigue come «KPV» o «SS-31» possono includere anche lavori su temi del tutto diversi. Per i capitoli i risultati sono stati quindi esaminati e non ripresi senza verifica.

**Lingue.** PubMed registra prevalentemente riviste in lingua inglese. I lavori pubblicati solo in altre lingue e in riviste non registrate mancano in gran parte. Ciò riguarda in particolare alcuni peptidi studiati e usati soprattutto in Russia o in altri paesi dell'Europa orientale, come Semax, Selank, Epitalon o Thymalin. Per questi la situazione effettiva degli studi è forse più ampia, ma difficilmente verificabile per i lettori internazionali.

**Studi non pubblicati.** Gli studi mai pubblicati non sono contenuti in PubMed. Il registro ClinicalTrials.gov aiuta a riconoscere queste lacune, ma non comprende tutti gli studi del mondo.

**Solo riassunti.** L'analisi si basa sui riassunti. Questi riportano i risultati principali, ma possono presentare in modo abbreviato limiti, effetti collaterali o debolezze metodologiche.

**Istantanea.** La ricerca riflette la situazione a ottobre 2026. In ambiti in rapida crescita come i farmaci GLP-1 escono nuovi studi ogni settimana.

### Controllo di qualità

Le interrogazioni delle banche dati sono state eseguite tramite le interfacce citate, con programmi di supporto scritti appositamente. Per l'analisi valevano regole vincolanti: ogni studio nel testo è citato con PMID o numero NCT; ogni numero deve provenire da un riassunto o da una voce di registro effettivamente consultati; gli studi possono essere citati solo se la loro voce è stata prima consultata e letta.

Inoltre ogni capitolo è stato controllato con un programma di verifica. Per ogni PMID e numero NCT citato nel testo, il programma richiama la voce in PubMed o in ClinicalTrials.gov e segnala come errore un numero inesistente. Confronta inoltre il primo autore o la prima autrice e l'anno di pubblicazione, riportati nel testo prima del PMID, con la voce della banca dati e segnala le discrepanze. Infine cerca formulazioni non ammesse come promesse di guarigione, raccomandazioni di dosaggio o indicazioni su fonti di approvvigionamento. Un capitolo era considerato finito solo quando questa verifica si concludeva senza errori. Il programma controlla inoltre se un lavoro citato è stato nel frattempo ritirato; tali lavori sono espressamente segnalati nel testo. Per concludere, circa 1.450 passaggi contenenti cifre sono stati confrontati uno per uno con i riassunti e, dove necessario, corretti.

Questa verifica garantisce che ogni fonte citata esista e sia attribuita correttamente. Non può escludere del tutto che un risultato sia riportato nel testo in modo abbreviato o fuorviante. Per questo tutte le fonti sono indicate in modo che possa consultarle personalmente – come fare è spiegato nella sezione «Su questo libro» all'inizio.
