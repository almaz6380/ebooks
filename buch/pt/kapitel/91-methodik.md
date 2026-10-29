# Metodologia

Este apêndice descreve como os estudos para este livro foram buscados, selecionados e verificados. Ele deve permitir que você acompanhe a pesquisa e, se necessário, a repita ou atualize por conta própria.

### Bancos de dados

A base da pesquisa são dois bancos de dados de acesso livre:

- **PubMed** (pubmed.ncbi.nlm.nih.gov), o banco de dados bibliográfico da National Library of Medicine dos EUA. Ele registra publicações de revistas biomédicas com título, autores, resumo (abstract) e palavras-chave. Cada registro tem um número único, o PMID.
- **ClinicalTrials.gov** (clinicaltrials.gov), o registro de estudos dos National Institutes of Health dos EUA. Aqui, estudos clínicos de todo o mundo são registrados antes de seu início, com desenho, número planejado de participantes, desfechos e status. Cada estudo tem um número NCT.

Os dois bancos de dados foram consultados por meio de suas interfaces de programação oficiais e de acesso público: o PubMed pelos E-Utilities do National Center for Biotechnology Information, o ClinicalTrials.gov pela interface de programação na versão 2. Outros bancos de dados, como Embase, Cochrane Library, Web of Science, o registro de estudos da UE ou registros nacionais, não foram pesquisados sistematicamente.

### Período de consulta

As consultas sistemáticas foram feitas em **outubro de 2026**; a contagem dos resultados para todos os peptídeos é de 28 de outubro de 2026. Buscas complementares direcionadas sobre estudos, relatos de caso e revisões específicos foram realizadas no mesmo período. Estudos publicados posteriormente não foram considerados. A situação do livro é de novembro de 2026.

### Estratégia de busca

Para cada um dos 58 peptídeos e substâncias de comparação, foi definido um termo de busca próprio no PubMed. Ele abrange o nome internacional da substância, bem como designações abreviadas, de código e comerciais usuais, e busca no título e no resumo (marcação `[tiab]`) ou apenas no título (`[ti]`). No caso de termos ambíguos, o termo de busca foi restringido, por exemplo, nos peptídeos de colágeno, a trabalhos sobre ingestão ou, na kisspeptina, a trabalhos sobre administração do peptídeo.

A esse termo de busca foram aplicados três filtros:

**Estudos em humanos.** Para encontrar estudos clínicos em humanos, o termo de busca foi combinado com o seguinte filtro:

`(clinical trial[pt] OR randomized controlled trial[pt]) AND humans[mh]`

A parte `[pt]` busca pelo tipo de publicação que o PubMed atribui a cada artigo; `humans[mh]` representa o descritor “seres humanos” no sistema de descritores MeSH. Com isso, são encontrados artigos marcados como estudo clínico ou como ensaio clínico randomizado e que se referem a seres humanos.

**Metanálises e revisões.** Para trabalhos de síntese, o termo de busca foi combinado com este filtro:

`(meta-analysis[pt] OR systematic review[pt])`

**Pré-clínica.** Para peptídeos com menos de 25 estudos em humanos encontrados, foram avaliados adicionalmente os demais trabalhos mais relevantes sem o filtro de estudos em humanos, para captar estudos em animais e de laboratório, relatos de caso e análises de produtos do mercado cinza.

**Estudos de registro.** No ClinicalTrials.gov, foi usado para cada peptídeo um termo de busca próprio, em geral simples, com o nome da substância. Foram incluídos todos os registros, independentemente de status e fase do estudo.

Além dessas buscas automatizadas, para cada capítulo buscaram-se de forma direcionada os mais importantes estudos de aprovação e de desfechos, grandes metanálises, programas de estudos (por exemplo STEP, SURMOUNT ou SELECT), dados de segurança, relatos de caso e análises laboratoriais de produtos do mercado cinza. Para a Parte I, foram pesquisados ainda trabalhos sobre a história da medicina com peptídeos, as formas farmacêuticas, a metodologia de estudos e o mercado cinza.

### Termos de busca por peptídeo

As tabelas a seguir reproduzem os termos de busca do PubMed usados na consulta sistemática. A cada termo foram acrescentados os filtros descritos acima. Um asterisco no fim da palavra representa quaisquer terminações, `OR` une designações alternativas, `AND` restringe a busca.

#### A. Metabolismo e peso

| Peptídeo | Termo de busca no PubMed |
|---|---|
| Exenatida | `exenatide[tiab]` |
| Liraglutida | `liraglutide[tiab]` |
| Dulaglutida | `dulaglutide[tiab]` |
| Semaglutida | `semaglutide[tiab]` |
| Tirzepatida | `tirzepatide[tiab]` |
| Retatrutida | `retatrutide[tiab]` |
| Survodutida | `survodutide[tiab]` |
| Mazdutida | `mazdutide[tiab]` |
| Cagrilintida ou CagriSema | `cagrilintide[tiab]` |
| Amicretina | `amycretin[tiab]` |
| Maridebarte cafraglutida (MariTide) | `maridebart[tiab] OR AMG 133[tiab]` |
| Pranlintida | `pramlintide[tiab]` |
| Setmelanotida | `setmelanotide[tiab]` |
| AOD-9604 | `AOD9604[tiab] OR AOD-9604[tiab]` |
| Orforglipron (comparação) | `orforglipron[tiab]` |

#### B. Cura, regeneração e sistema imunológico

| Peptídeo | Termo de busca no PubMed |
|---|---|
| BPC-157 | `BPC 157[tiab] OR BPC-157[tiab] OR pentadecapeptide BPC[tiab]` |
| TB-500 ou timosina beta-4 | `thymosin beta-4[tiab] OR thymosin beta4[tiab] OR TB-500[tiab] OR TB500[tiab]` |
| Timosina alfa-1 (timalfasina) | `thymosin alpha 1[tiab] OR thymalfasin[tiab] OR thymosin alpha1[tiab]` |
| KPV | `KPV[tiab] AND (peptide[tiab] OR tripeptide[tiab])` |
| LL-37 | `LL-37[tiab] OR cathelicidin[tiab]` |
| ARA-290 (cibinetida) | `ARA 290[tiab] OR ARA290[tiab] OR cibinetide[tiab]` |
| Larazotida | `larazotide[tiab]` |
| Timalina ou timogen | `thymalin[tiab] OR thymogen[tiab]` |

#### C. Eixo do hormônio do crescimento

| Peptídeo | Termo de busca no PubMed |
|---|---|
| Sermorelina | `sermorelin[tiab]` |
| Tesamorelina | `tesamorelin[tiab]` |
| CJC-1295 | `CJC-1295[tiab] OR CJC 1295[tiab]` |
| Ipamorelina | `ipamorelin[tiab]` |
| GHRP-2 (pralmorelina) | `GHRP-2[tiab] OR pralmorelin[tiab]` |
| GHRP-6 | `GHRP-6[tiab]` |
| Hexarelina | `hexarelin[tiab]` |
| Macimorelina | `macimorelin[tiab]` |
| Mecasermina (IGF-1) | `mecasermin[tiab] OR rhIGF-1[tiab]` |
| IGF-1 LR3 | `LR3-IGF-1[tiab] OR IGF-1 LR3[tiab] OR "Long R3"[tiab]` |
| Ibutamoreno (MK-677) (comparação) | `ibutamoren[tiab] OR MK-677[tiab] OR MK-0677[tiab]` |

#### D. Cérebro, sono e longevidade

| Peptídeo | Termo de busca no PubMed |
|---|---|
| Semax | `semax[tiab]` |
| Selank | `selank[tiab]` |
| Cerebrolysin | `cerebrolysin[tiab]` |
| Dihexa | `dihexa[tiab]` |
| DSIP | `delta sleep-inducing peptide[tiab] OR DSIP[tiab]` |
| Epitalon (Epithalon) | `epitalon[tiab] OR epithalon[tiab] OR epithalone[tiab]` |
| Pinealon | `pinealon[tiab]` |
| MOTS-c | `MOTS-c[tiab]` |
| Humanina | `humanin[tiab]` |
| SS-31 (elamipretida) | `elamipretide[tiab] OR SS-31[tiab]` |
| FOXO4-DRI | `FOXO4-DRI[tiab]` |
| Glutationa | `glutathione[ti] AND (supplementation[tiab] OR oral[tiab] OR intravenous[tiab])` |

#### E. Hormônios, sexualidade e pigmentação

| Peptídeo | Termo de busca no PubMed |
|---|---|
| Bremelanotida (PT-141) | `bremelanotide[tiab] OR PT-141[tiab]` |
| Melanotan II | `melanotan[tiab]` |
| Afamelanotida | `afamelanotide[tiab]` |
| Kisspeptina | `kisspeptin[tiab] AND (administration[tiab] OR infusion[tiab] OR injection[tiab])` |
| Ocitocina (intranasal) | `intranasal oxytocin[tiab]` |
| Gonadorelina | `gonadorelin[tiab]` |

#### F. Colágeno, nutrição e cosmética

| Peptídeo | Termo de busca no PubMed |
|---|---|
| Hidrolisado de colágeno ou peptídeos de colágeno | `(collagen hydrolysate[tiab] OR collagen peptide*[tiab]) AND (supplement*[tiab] OR oral[tiab] OR ingestion[tiab])` |
| Lactotripeptídeos (VPP/IPP) | `lactotripeptide*[tiab] OR (valyl-prolyl-proline[tiab])` |
| Carnosina | `carnosine[ti] AND (supplementation[tiab] OR oral[tiab])` |
| GHK-Cu (peptídeo de cobre) | `GHK-Cu[tiab] OR copper tripeptide[tiab] OR copper peptide GHK[tiab]` |
| Palmitoil pentapeptídeo-4 (Matrixyl) | `palmitoyl pentapeptide[tiab] OR matrixyl[tiab]` |
| Acetil hexapeptídeo-8 (Argireline) | `acetyl hexapeptide[tiab] OR argireline[tiab]` |

### Volume de resultados

No total, as 58 consultas resultaram em 3.216 resultados com o filtro de estudos em humanos e em 1.739 resultados com o filtro de metanálises e revisões. No ClinicalTrials.gov, foram encontrados 4.879 registros. Essas somas contêm contagens múltiplas, porque alguns estudos se referem a vários peptídeos – como estudos comparativos entre semaglutida e tirzepatida. Os números por peptídeo são citados no início da seção “Estudos em humanos” de cada capítulo.

A distribuição é muito desigual: aos medicamentos de GLP-1 aprovados correspondem centenas de estudos em humanos; para muitos peptídeos do mercado cinza, por outro lado, nenhum ou apenas um punhado.

### Seleção e avaliação

Para cada peptídeo, todos os resultados com o filtro de estudos em humanos foram registrados como lista resumida (título, ano, revista, primeiro autor ou primeira autora); eles formam a base do índice de estudos no apêndice. Os estudos em humanos e as revisões mais importantes segundo a relevância do PubMed foram lidos e avaliados com seus resumos, complementados pelos trabalhos buscados de forma direcionada.

Para a apresentação no texto, vale:

- Cada estudo citado foi lido com base em seu registro no PubMed ou em seu registro de estudo.
- Números – como número de participantes, percentuais, variações de peso ou valores p – vêm exclusivamente do resumo da publicação ou do registro do estudo. O que não está comprovado ali não é citado como número.
- Textos completos não foram avaliados sistematicamente. Detalhes que só constam do texto completo, como taxas individuais de efeitos colaterais ou subgrupos, faltam por isso em parte.
- Resultados em animais e de laboratório são expressamente identificados como tais.
- Para estudos em andamento, relata-se apenas o que consta do registro. Eles são identificados como *assegurados* (registrados, em andamento), e prognósticos próprios como *avaliação*.

### Níveis de evidência

Cada peptídeo recebeu um nível de evidência segundo os seguintes critérios:

| Nível | Critério |
|---|---|
| A | vários grandes estudos randomizados em humanos, aprovação como medicamento |
| B | estudos randomizados isolados em humanos |
| C | apenas estudos pequenos ou não controlados em humanos |
| D | apenas estudos em animais e de laboratório |

A classificação refere-se aos dados em humanos como um todo e à aplicação estudada mais importante. É uma avaliação do autor com base nos estudos analisados, e não uma classificação oficial.

### Limites da metodologia

Como toda pesquisa bibliográfica, também esta tem limites, que você deve considerar na leitura:

**Resultados não equivalem a estudos independentes.** Um grande estudo é frequentemente publicado em vários artigos – resultado principal, subgrupos, acompanhamento, qualidade de vida. Cada um desses artigos é um resultado próprio. Inversamente, estudos podem estar reunidos em um único artigo. Os números de resultados refletem, por isso, a ordem de grandeza da pesquisa, não o número exato de estudos independentes.

**Os tipos de publicação nem sempre estão corretos.** O filtro de estudos em humanos baseia-se na indexação feita pelo PubMed. Alguns estudos não estão marcados como estudo clínico e por isso faltam; alguns trabalhos marcados como estudo clínico são, examinados mais de perto, estudos observacionais ou trabalhos de laboratório com material humano. Artigos muito recentes muitas vezes ainda não estão completamente indexados.

**Termos de busca podem ter lacunas.** Um termo de busca só encontra o que está descrito no título ou no resumo com as palavras escolhidas. Estudos que mencionam uma substância apenas sob um nome de código ou com outra grafia podem faltar. Inversamente, siglas ambíguas como “KPV” ou “SS-31” podem captar também trabalhos sobre temas completamente diferentes. Para os capítulos, os resultados foram, por isso, revisados e não adotados sem verificação.

**Idiomas.** O PubMed registra predominantemente revistas em língua inglesa. Trabalhos publicados apenas em outros idiomas e em revistas não indexadas estão em grande parte ausentes. Isso afeta especialmente alguns peptídeos pesquisados e usados sobretudo na Rússia ou em outros países do Leste Europeu, como Semax, Selank, Epitalon ou timalina. Para eles, a situação real dos estudos é possivelmente mais ampla, mas difícil de verificar para leitores internacionais.

**Estudos não publicados.** Estudos que nunca foram publicados não constam do PubMed. O registro ClinicalTrials.gov ajuda a reconhecer essas lacunas, mas não abrange todos os estudos do mundo.

**Apenas resumos.** A avaliação baseia-se nos resumos. Eles reproduzem os resultados principais, mas podem apresentar de forma abreviada limitações, efeitos colaterais ou fraquezas metodológicas.

**Retrato instantâneo.** A pesquisa reflete a situação de outubro de 2026. Em campos de crescimento rápido, como o dos medicamentos de GLP-1, novos estudos são publicados toda semana.

### Controle de qualidade

As consultas aos bancos de dados foram feitas pelas interfaces citadas, com programas auxiliares escritos especificamente para isso. Para a avaliação, valeram regras obrigatórias: cada estudo no texto é citado com PMID ou número NCT; cada número precisa vir de um resumo ou registro de estudo efetivamente consultado; estudos só podem ser citados se seu registro tiver sido consultado e lido antes.

Além disso, cada capítulo foi verificado com um programa de controle. Ele consulta, para cada PMID e número NCT citado no texto, o registro no PubMed ou no ClinicalTrials.gov e aponta como erro quando um número não existe. Compara também o primeiro autor ou a primeira autora e o ano de publicação, que constam do texto antes do PMID, com o registro do banco de dados e indica divergências. Por fim, procura formulações inadmissíveis, como promessas de cura, recomendações de dose ou indicações de onde comprar. Um capítulo só era considerado pronto quando essa verificação passava sem erros. Além disso, o programa verifica se um trabalho citado foi retratado nesse meio-tempo; esses trabalhos estão expressamente identificados no texto. Para concluir, cerca de 1.450 trechos com números foram comparados um a um com os resumos e, quando necessário, corrigidos.

Essa verificação garante que cada fonte citada existe e está corretamente atribuída. Ela não pode excluir completamente que um resultado esteja reproduzido no texto de forma abreviada ou ambígua. Por isso, todas as fontes estão indicadas de modo que você possa consultá-las por conta própria – como fazer isso está explicado na seção “Sobre este livro”, no início.
