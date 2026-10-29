# Méthodologie

Cette annexe décrit comment les études de ce livre ont été recherchées, sélectionnées et vérifiées. Elle doit vous permettre de retracer la recherche documentaire et, si nécessaire, de la refaire vous-même ou de la mettre à jour.

### Bases de données

La recherche repose sur deux bases de données en libre accès :

- **PubMed** (pubmed.ncbi.nlm.nih.gov), la base de données bibliographique de la National Library of Medicine américaine. Elle répertorie les publications de revues biomédicales avec leur titre, leurs autrices et auteurs, leur résumé (abstract) et leurs mots-clés. Chaque entrée possède un numéro unique, le PMID.
- **ClinicalTrials.gov** (clinicaltrials.gov), le registre d'études des National Institutes of Health américains. Des études cliniques du monde entier y sont enregistrées avant leur début, avec leur plan, le nombre de participants prévu, les critères d'évaluation et leur statut. Chaque étude possède un numéro NCT.

Les deux bases de données ont été interrogées via leurs interfaces de programmation officielles et accessibles au public : PubMed via les E-Utilities du National Center for Biotechnology Information, ClinicalTrials.gov via l'interface de programmation en version 2. D'autres bases de données comme Embase, la Cochrane Library, Web of Science, le registre des essais cliniques de l'UE ou des registres nationaux n'ont pas été explorées de manière systématique.

### Période d'interrogation

Les interrogations systématiques ont eu lieu en **octobre 2026** ; le décompte des résultats pour tous les peptides date du 28 octobre 2026. Des recherches ciblées complémentaires sur certaines études, certains rapports de cas et certaines revues ont été effectuées au cours de la même période. Les études parues ultérieurement ne sont pas prises en compte. Le livre reflète la situation de novembre 2026.

### Stratégie de recherche

Pour chacun des 58 peptides et substances de comparaison, un terme de recherche PubMed spécifique a été défini. Il comprend la dénomination commune internationale ainsi que les abréviations, noms de code et noms commerciaux usuels, et cherche dans le titre et le résumé (balise `[tiab]`) ou uniquement dans le titre (`[ti]`). Pour les termes ambigus, la recherche a été restreinte, par exemple aux travaux portant sur la prise orale pour les peptides de collagène ou aux travaux portant sur l'administration du peptide pour la kisspeptine.

Trois filtres ont été appliqués à ce terme de recherche :

**Études chez l'humain.** Pour trouver des études cliniques chez l'humain, le terme de recherche a été combiné avec le filtre suivant :

`(clinical trial[pt] OR randomized controlled trial[pt]) AND humans[mh]`

La partie `[pt]` recherche le type de publication que PubMed attribue à chaque article ; `humans[mh]` correspond au mot-clé « humains » du système de mots-clés MeSH. On trouve ainsi les articles signalés comme étude clinique ou comme étude contrôlée randomisée et portant sur des humains.

**Méta-analyses et revues.** Pour les travaux de synthèse, le terme de recherche a été combiné avec ce filtre :

`(meta-analysis[pt] OR systematic review[pt])`

**Études précliniques.** Pour les peptides comptant moins de 25 études chez l'humain, les autres travaux les plus pertinents ont en outre été analysés sans le filtre « études chez l'humain », afin de recenser les études animales et de laboratoire, les rapports de cas et les analyses de produits du marché gris.

**Études enregistrées.** Dans ClinicalTrials.gov, un terme de recherche spécifique, le plus souvent simple, reprenant le nom de la substance a été utilisé pour chaque peptide. Toutes les inscriptions ont été recensées, quels que soient leur statut et la phase de l'étude.

Au-delà de ces recherches automatisées, une recherche ciblée a été menée pour chaque chapitre afin de trouver les principales études d'autorisation et de critères cliniques, les grandes méta-analyses, les programmes d'études (par exemple STEP, SURMOUNT ou SELECT), les données de sécurité, les rapports de cas et les analyses de laboratoire de produits du marché gris. Pour la partie I, des travaux sur l'histoire de la médecine peptidique, les formes galéniques, la méthodologie des études et le marché gris ont en outre été recherchés.

### Termes de recherche par peptide

Les tableaux suivants reproduisent les termes de recherche PubMed utilisés pour l'interrogation systématique. Les filtres décrits plus haut ont été ajoutés à chaque terme. Un astérisque en fin de mot remplace n'importe quelle terminaison, `OR` relie des dénominations alternatives, `AND` restreint la recherche.

#### A. Métabolisme et poids

| Peptide | Terme de recherche PubMed |
|---|---|
| Exénatide | `exenatide[tiab]` |
| Liraglutide | `liraglutide[tiab]` |
| Dulaglutide | `dulaglutide[tiab]` |
| Sémaglutide | `semaglutide[tiab]` |
| Tirzépatide | `tirzepatide[tiab]` |
| Rétatrutide | `retatrutide[tiab]` |
| Survodutide | `survodutide[tiab]` |
| Mazdutide | `mazdutide[tiab]` |
| Cagrilintide ou CagriSema | `cagrilintide[tiab]` |
| Amycrétine | `amycretin[tiab]` |
| Maridebart cafraglutide (MariTide) | `maridebart[tiab] OR AMG 133[tiab]` |
| Pramlintide | `pramlintide[tiab]` |
| Setmélanotide | `setmelanotide[tiab]` |
| AOD-9604 | `AOD9604[tiab] OR AOD-9604[tiab]` |
| Orforglipron (comparaison) | `orforglipron[tiab]` |

#### B. Guérison, régénération et système immunitaire

| Peptide | Terme de recherche PubMed |
|---|---|
| BPC-157 | `BPC 157[tiab] OR BPC-157[tiab] OR pentadecapeptide BPC[tiab]` |
| TB-500 ou thymosine bêta 4 | `thymosin beta-4[tiab] OR thymosin beta4[tiab] OR TB-500[tiab] OR TB500[tiab]` |
| Thymosine alpha 1 (thymalfasine) | `thymosin alpha 1[tiab] OR thymalfasin[tiab] OR thymosin alpha1[tiab]` |
| KPV | `KPV[tiab] AND (peptide[tiab] OR tripeptide[tiab])` |
| LL-37 | `LL-37[tiab] OR cathelicidin[tiab]` |
| ARA-290 (cibinétide) | `ARA 290[tiab] OR ARA290[tiab] OR cibinetide[tiab]` |
| Larazotide | `larazotide[tiab]` |
| Thymaline ou thymogène | `thymalin[tiab] OR thymogen[tiab]` |

#### C. Axe de l'hormone de croissance

| Peptide | Terme de recherche PubMed |
|---|---|
| Sermoréline | `sermorelin[tiab]` |
| Tésamoréline | `tesamorelin[tiab]` |
| CJC-1295 | `CJC-1295[tiab] OR CJC 1295[tiab]` |
| Ipamoréline | `ipamorelin[tiab]` |
| GHRP-2 (pralmoréline) | `GHRP-2[tiab] OR pralmorelin[tiab]` |
| GHRP-6 | `GHRP-6[tiab]` |
| Hexaréline | `hexarelin[tiab]` |
| Macimoréline | `macimorelin[tiab]` |
| Mécasermine (IGF-1) | `mecasermin[tiab] OR rhIGF-1[tiab]` |
| IGF-1 LR3 | `LR3-IGF-1[tiab] OR IGF-1 LR3[tiab] OR "Long R3"[tiab]` |
| Ibutamorène (MK-677) (comparaison) | `ibutamoren[tiab] OR MK-677[tiab] OR MK-0677[tiab]` |

#### D. Cerveau, sommeil et longévité

| Peptide | Terme de recherche PubMed |
|---|---|
| Semax | `semax[tiab]` |
| Selank | `selank[tiab]` |
| Cerebrolysin | `cerebrolysin[tiab]` |
| Dihexa | `dihexa[tiab]` |
| DSIP | `delta sleep-inducing peptide[tiab] OR DSIP[tiab]` |
| Epitalon (Epithalon) | `epitalon[tiab] OR epithalon[tiab] OR epithalone[tiab]` |
| Pinealon | `pinealon[tiab]` |
| MOTS-c | `MOTS-c[tiab]` |
| Humanine | `humanin[tiab]` |
| SS-31 (élamipretide) | `elamipretide[tiab] OR SS-31[tiab]` |
| FOXO4-DRI | `FOXO4-DRI[tiab]` |
| Glutathion | `glutathione[ti] AND (supplementation[tiab] OR oral[tiab] OR intravenous[tiab])` |

#### E. Hormones, sexualité et pigmentation

| Peptide | Terme de recherche PubMed |
|---|---|
| Brémélanotide (PT-141) | `bremelanotide[tiab] OR PT-141[tiab]` |
| Melanotan II | `melanotan[tiab]` |
| Afamélanotide | `afamelanotide[tiab]` |
| Kisspeptine | `kisspeptin[tiab] AND (administration[tiab] OR infusion[tiab] OR injection[tiab])` |
| Ocytocine (intranasale) | `intranasal oxytocin[tiab]` |
| Gonadoréline | `gonadorelin[tiab]` |

#### F. Collagène, nutrition et cosmétique

| Peptide | Terme de recherche PubMed |
|---|---|
| Hydrolysat de collagène ou peptides de collagène | `(collagen hydrolysate[tiab] OR collagen peptide*[tiab]) AND (supplement*[tiab] OR oral[tiab] OR ingestion[tiab])` |
| Lactotripeptides (VPP/IPP) | `lactotripeptide*[tiab] OR (valyl-prolyl-proline[tiab])` |
| Carnosine | `carnosine[ti] AND (supplementation[tiab] OR oral[tiab])` |
| GHK-Cu (peptide de cuivre) | `GHK-Cu[tiab] OR copper tripeptide[tiab] OR copper peptide GHK[tiab]` |
| Palmitoyl pentapeptide-4 (Matrixyl) | `palmitoyl pentapeptide[tiab] OR matrixyl[tiab]` |
| Acétyl hexapeptide-8 (Argireline) | `acetyl hexapeptide[tiab] OR argireline[tiab]` |

### Volume des résultats

Au total, les 58 interrogations ont donné 3 216 résultats avec le filtre « études chez l'humain » et 1 739 résultats avec le filtre « méta-analyses et revues ». Dans ClinicalTrials.gov, 4 879 inscriptions au registre ont été trouvées. Ces totaux comportent des doubles comptages, car certaines études concernent plusieurs peptides – par exemple les études comparant le sémaglutide et le tirzépatide. Les chiffres par peptide sont indiqués au début de la section « Études chez l'humain » de chaque chapitre.

La répartition est très inégale : les médicaments GLP-1 autorisés totalisent des centaines d'études chez l'humain, tandis que de nombreux peptides du marché gris n'en comptent aucune ou seulement une poignée.

### Sélection et analyse

Pour chaque peptide, tous les résultats obtenus avec le filtre « études chez l'humain » ont été consignés sous forme de liste abrégée (titre, année, revue, première autrice ou premier auteur) ; ils constituent la base du répertoire des études en annexe. Les études chez l'humain et les revues les plus importantes selon la pertinence PubMed ont été lues et analysées à partir de leurs résumés, complétées par les travaux recherchés de manière ciblée.

Pour la présentation dans le texte, les règles suivantes s'appliquent :

- Chaque étude citée a été lue à partir de son entrée PubMed ou de son inscription au registre.
- Les chiffres – par exemple le nombre de participants, les pourcentages, les variations de poids ou les valeurs p – proviennent exclusivement du résumé de la publication ou de l'inscription au registre. Ce qui n'y est pas étayé n'est pas indiqué sous forme de chiffre.
- Les textes intégraux n'ont pas été analysés de manière systématique. Les détails qui ne figurent que dans le texte intégral, par exemple certains taux d'effets indésirables ou certains sous-groupes, manquent donc en partie.
- Les résultats animaux et de laboratoire sont expressément signalés comme tels.
- Pour les études en cours, seul ce qui figure dans le registre est rapporté. Elles sont désignées comme *établies* (enregistrées, en cours), les prévisions personnelles comme *appréciation*.

### Niveaux de preuve

Chaque peptide a reçu un niveau de preuve selon les critères suivants :

| Niveau | Critère |
|---|---|
| A | plusieurs grandes études randomisées chez l'humain, autorisation comme médicament |
| B | études randomisées isolées chez l'humain |
| C | uniquement de petites études ou des études non contrôlées chez l'humain |
| D | uniquement des études animales et de laboratoire |

Le classement se rapporte à l'ensemble des données chez l'humain et au principal domaine d'utilisation étudié. Il s'agit d'une évaluation de l'auteur fondée sur les études analysées, et non d'une classification officielle.

### Limites de la méthodologie

Comme toute recherche bibliographique, celle-ci a des limites dont vous devriez tenir compte à la lecture :

**Un résultat n'est pas forcément une étude indépendante.** Une grande étude est souvent publiée dans plusieurs articles – résultat principal, sous-groupes, suivi, qualité de vie. Chacun de ces articles constitue un résultat distinct. À l'inverse, plusieurs études peuvent être regroupées dans un même article. Le nombre de résultats reflète donc l'ordre de grandeur de la recherche, et non le nombre exact d'études indépendantes.

**Les types de publication ne sont pas toujours corrects.** Le filtre « études chez l'humain » repose sur l'indexation effectuée par PubMed. Certaines études ne sont pas signalées comme études cliniques et manquent donc ; certains travaux signalés comme études cliniques se révèlent, à y regarder de plus près, être des études observationnelles ou des travaux de laboratoire sur du matériel humain. Les articles très récents ne sont souvent pas encore entièrement indexés.

**Les termes de recherche peuvent présenter des lacunes.** Un terme de recherche ne trouve que ce qui est décrit avec les mots choisis dans le titre ou le résumé. Les études qui ne désignent une substance que par un nom de code ou une autre orthographe peuvent manquer. À l'inverse, des abréviations ambiguës comme « KPV » ou « SS-31 » peuvent aussi faire apparaître des travaux portant sur des sujets tout à fait différents. Pour les chapitres, les résultats ont donc été examinés et non repris sans vérification.

**Langues.** PubMed répertorie principalement des revues anglophones. Les travaux parus uniquement dans d'autres langues et dans des revues non répertoriées manquent en grande partie. Cela concerne en particulier certains peptides étudiés et utilisés surtout en Russie ou dans d'autres pays d'Europe de l'Est, comme le Semax, le Selank, l'Epitalon ou la thymaline. Pour eux, les données réelles sont peut-être plus abondantes, mais difficilement vérifiables pour des lectrices et lecteurs internationaux.

**Études non publiées.** Les études qui n'ont jamais été publiées ne figurent pas dans PubMed. Le registre ClinicalTrials.gov aide à repérer ces lacunes, mais ne recense pas toutes les études du monde entier.

**Uniquement des résumés.** L'analyse repose sur les résumés. Ceux-ci rendent compte des principaux résultats, mais peuvent présenter de manière abrégée les limites, les effets indésirables ou les faiblesses méthodologiques.

**Instantané.** La recherche reflète la situation d'octobre 2026. Dans des domaines en croissance rapide comme celui des médicaments GLP-1, de nouvelles études paraissent chaque semaine.

### Assistance par l'IA et contrôle de la qualité

Ce livre a été documenté et rédigé avec l'assistance de l'intelligence artificielle, puis revu par l'auteur. L'IA a été utilisée pour les tâches suivantes :

- réalisation des interrogations des bases de données via les interfaces citées, à l'aide de programmes auxiliaires écrits spécialement à cet effet,
- lecture et analyse des résumés et des inscriptions aux registres,
- rédaction de projets de texte selon des règles de style et de travail fixes.

Pour éviter le risque connu que des systèmes d'IA inventent des sources ou des chiffres, des règles contraignantes s'appliquaient : chaque étude mentionnée dans le texte est citée avec son PMID ou son numéro NCT ; chaque chiffre doit provenir d'un résumé ou d'une inscription au registre effectivement consultés ; les études ne peuvent être citées que si leur entrée a été préalablement consultée et lue.

En outre, chaque chapitre a été contrôlé à l'aide d'un programme de vérification. Pour chaque PMID et chaque numéro NCT mentionné dans le texte, celui-ci consulte l'entrée dans PubMed ou ClinicalTrials.gov et signale une erreur si un numéro n'existe pas. Il compare aussi la première autrice ou le premier auteur et l'année de publication indiqués dans le texte avant le PMID avec l'entrée de la base de données et signale les divergences. Enfin, il recherche des formulations inadmissibles comme des promesses de guérison, des recommandations de dosage ou des indications de sources d'approvisionnement. Un chapitre n'était considéré comme terminé que lorsque ce contrôle se déroulait sans erreur.

Ce contrôle garantit que chaque source citée existe et est correctement attribuée. Il ne peut pas exclure entièrement qu'un résultat soit rendu de manière abrégée ou ambiguë dans le texte. C'est pourquoi toutes les sources sont indiquées de manière à ce que vous puissiez les consulter vous-même – la marche à suivre est expliquée dans la section « À propos de ce livre », au début.
