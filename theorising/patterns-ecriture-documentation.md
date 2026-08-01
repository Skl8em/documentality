---
title: "Patterns d'écriture pour documentation lisible (humain + LLM)"
diataxis: reference
view: synchronic
audience: [developer, AI]
status: draft
---

Cette référence consolide les pratiques d'écriture qui réduisent la charge cognitive et améliorent la lisibilité, en distinguant ce qui bénéficie aux lecteurs humains, aux LLMs, ou aux deux. Chaque entrée précise le domaine de recherche d'origine et une référence d'entrée vérifiée.

**Légende bénéfice** : `H` = humain · `M` = modèle LLM · `H+M` = les deux · `M>H` = utile aux deux, déterminant pour le modèle

**Marqueur de vérification** : les références marquées ✓ ont été vérifiées via recherche web (URL stable). Les autres relèvent de connaissances générales solides mais non re-vérifiées au moment de la rédaction.

---

## 1. Organisation et navigation

### 1.1 Titres sémantiques porteurs d'intention

**Bénéfice** : H+M
**Domaine** : sciences de l'information, UX writing
**Référence** : Morville, P. & Rosenfeld, L. (2006), *Information Architecture for the World Wide Web*, 3e éd., O'Reilly.

Le titre doit transmettre l'information même hors contexte de lecture.

- ✗ `Configuration avancée`
- ✓ `Configurer le timeout de connexion SQL`

### 1.2 Modularité auto-suffisante (topic-based authoring)

**Bénéfice** : H+M (déterminant pour RAG)
**Domaine** : sciences de l'information, architecture documentaire
**Référence vérifiée ✓** : [OASIS (2015), *Darwin Information Typing Architecture (DITA) Version 1.3*, OASIS Standard.](http://docs.oasis-open.org/dita/dita/v1.3/os/part0-overview/dita-v1.3-os-part0-overview.html)

Chaque section doit être compréhensible sans le document complet.

- ✗ "Comme expliqué dans la section précédente, le pipeline..."
- ✓ "Le pipeline (décrit en détail dans `pipeline.md`) reçoit..."

### 1.3 Séparation par type de document (Diátaxis)

**Bénéfice** : H+M
**Domaine** : architecture documentaire (origine pratique, fondement en psychologie de la mémoire procédurale vs déclarative)
**Référence vérifiée ✓** : [Procida, D., *Diátaxis documentation framework*.](https://diataxis.fr/)

Tutoriel, how-to, référence, explication ont des structures incompatibles ; les mélanger dégrade les quatre.

- ✗ Un seul document "Guide utilisateur" qui mélange premiers pas, tâches courantes et architecture
- ✓ Quatre sections distinctes avec rôle explicite dans le frontmatter

### 1.4 Progressive disclosure

**Bénéfice** : H+M
**Domaine** : UX / interaction design
**Référence** : [Nielsen, J. (2006), "Progressive Disclosure", Nielsen Norman Group.](https://www.nngroup.com/articles/progressive-disclosure/)

Montrer le minimum nécessaire pour avancer, rendre le détail accessible sans l'imposer.

- ✗ Tout le détail d'implémentation dans le tutoriel d'introduction
- ✓ Tutoriel court, liens explicites vers la référence pour aller plus loin

### 1.5 F-pattern et scan visuel

**Bénéfice** : H (peu pertinent pour M)
**Domaine** : recherche UX, eye-tracking
**Référence vérifiée ✓** : [Nielsen, J. (2006), "F-Shaped Pattern For Reading Web Content", Nielsen Norman Group. Étude originale sur 232 utilisateurs. Confirmée par réplication en 2017.](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered/)

Antérieur : [Morkes, J. & Nielsen, J. (1997), "Concise, SCANNABLE, and Objective: How to Write for the Web".](https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/)

Les lecteurs scannent en F. Ancrer l'information clé sur les premières lignes et les premiers mots des paragraphes.

- ✗ Information critique enterrée au milieu d'un paragraphe en bas de page
- ✓ Première phrase du paragraphe = idée principale

### 1.6 Information scent / information foraging

**Bénéfice** : H+M (M utilise les mêmes signaux pour la pertinence RAG)
**Domaine** : sciences cognitives appliquées à l'IHM
**Référence** : Pirolli, P. & Card, S. (1999), "Information Foraging", *Psychological Review*, 106(4), 643-675. DOI : 10.1037/0033-295X.106.4.643

Chaque lien, titre, ou première phrase doit donner un "scent" — un signal fiable de ce qu'on trouve si on suit. Les promesses non tenues détournent durablement la confiance.

- ✗ Lien "Plus d'infos" sans préciser sur quoi
- ✓ Lien "Voir le format détaillé des paramètres `Result`"

---

## 2. Charge cognitive et densité

### 2.1 Limite de mémoire de travail (chunking)

**Bénéfice** : H (peu pertinent pour M directement)
**Domaine** : psychologie cognitive
**Références** :

- Miller, G. A. (1956), "The Magical Number Seven, Plus or Minus Two", *Psychological Review*, 63(2), 81-97.
- **Vérifiée ✓** : Cowan, N. (2001), "The magical number 4 in short-term memory: A reconsideration of mental storage capacity", *Behavioral and Brain Sciences*, 24(1), 87-114. DOI : 10.1017/S0140525X01003922. Révision quantitative à ~4 chunks.

Une section qui force à maintenir plus de 4-5 éléments simultanément en mémoire de travail dépasse les capacités humaines.

- ✗ Liste de 12 paramètres traités au même niveau sans regroupement
- ✓ Regroupement par fonction (3-4 groupes de 3-4 éléments)

### 2.2 Théorie de la charge cognitive (intrinsèque / extrinsèque / germanique)

**Bénéfice** : H+M (le concept de charge extrinsèque s'applique aux LLMs comme bruit de contexte)
**Domaine** : psychologie de l'éducation
**Référence vérifiée ✓** : [Sweller, J. (1988), "Cognitive Load During Problem Solving: Effects on Learning", *Cognitive Science*, 12(2), 257-285. DOI : 10.1207/s15516709cog1202_4. Open access](https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1202_4)

Synthèse récente : Sweller, J., van Merriënboer, J. & Paas, F. (2019), "Cognitive Architecture and Instructional Design: 20 Years Later", *Educational Psychology Review*, 31, 261-292. DOI : 10.1007/s10648-019-09465-5

Tout effort cognitif qui ne contribue pas à la compréhension (charge extrinsèque) doit être éliminé.

- ✗ Jargon non défini au premier usage, navigation ambiguë
- ✓ Glossaire intégré au premier usage, structure prévisible

### 2.3 Split-attention effect

**Bénéfice** : H+M
**Domaine** : psychologie cognitive (sous-produit de Sweller)
**Référence** : Ayres, P. & Sweller, J. (2005), "The Split-Attention Principle in Multimedia Learning", in R. E. Mayer (éd.), *Cambridge Handbook of Multimedia Learning*, Cambridge University Press.

Forcer le lecteur (ou le LLM) à intégrer deux sources séparées dégrade la compréhension.

- ✗ Schéma en haut de page, légende des éléments en bas
- ✓ Annotations intégrées au schéma, ou texte directement à côté de l'élément concerné

### 2.4 Principe de cohérence (exclure le matériel non pertinent)

**Bénéfice** : H+M (M particulièrement sensible au bruit en contexte)
**Domaine** : recherche en apprentissage multimédia
**Référence** : Mayer, R. E. (2009), *Multimedia Learning*, 2e éd., Cambridge University Press, ISBN 978-0521735353. Chapitre sur le coherence principle.

Tout contenu décoratif, anecdotique ou tangentiel dégrade la compréhension du contenu principal.

- ✗ Anecdotes historiques dans une référence technique
- ✓ Information opérationnelle uniquement, les explications conceptuelles dans des documents séparés (type `explanation` au sens Diátaxis)

### 2.5 Principe de signaling (mise en évidence du structurel)

**Bénéfice** : H+M
**Domaine** : recherche en apprentissage multimédia
**Référence** : Mayer, R. E. & Fiorella, L. (2014), "Principles for Reducing Extraneous Processing in Multimedia Learning: Coherence, Signaling, Redundancy, Spatial Contiguity, and Temporal Contiguity Principles", in Mayer (éd.), *Cambridge Handbook of Multimedia Learning*, 2e éd.

Mettre en évidence la structure (titres, transitions, mots-clés en gras avec parcimonie) aide à la fois la mémoire humaine et la segmentation LLM.

- ✗ Texte plat sans relief structurel
- ✓ Hiérarchie typographique explicite, mots-clés terminologiques mis en évidence

---

## 3. Style et clarté linguistique

### 3.1 Plain language : voix active, mot courant, peu de nominalisations

**Bénéfice** : H+M
**Domaine** : linguistique appliquée, mouvement plain language
**Référence** : [Plain Language Action and Information Network (2011), *Federal Plain Language Guidelines*.](https://www.plainlanguage.gov/guidelines/)

Recherche académique : Schriver, K. (1997), *Dynamics in Document Design*, Wiley, ISBN 978-0471306368.

- ✗ "La mise en œuvre de la vérification de la conformité des données"
- ✓ "Pour vérifier que les données sont conformes"

### 3.2 Phrases à structure linéaire, imbrication minimale

**Bénéfice** : H+M (M particulièrement sensible aux ambiguïtés syntaxiques)
**Domaine** : psycholinguistique
**Référence** : Gibson, E. (1998), "Linguistic complexity: locality of syntactic dependencies", *Cognition*, 68(1), 1-76. DOI : 10.1016/S0010-0277(98)00034-1

La distance syntaxique entre éléments dépendants détermine la difficulté de traitement (dependency locality theory).

- ✗ "La valeur retournée, si le flag est actif et que la connexion n'a pas été fermée par le timeout, est un objet Result."
- ✓ "Si le flag est actif et la connexion ouverte, la fonction retourne un objet `Result`."

### 3.3 Cohérence terminologique stricte

**Bénéfice** : M>H (un humain expert tolère la variation, un LLM moins)
**Domaine** : terminologie, ingénierie de la connaissance
**Référence** : [ISO 704:2022, *Terminology work — Principles and methods*.](https://www.iso.org/standard/79077.html)

Choisir un terme par concept, s'y tenir, documenter explicitement les synonymes du domaine.

- ✗ `process`, `tâche`, `job` utilisés de façon interchangeable
- ✓ "Un *process* (aussi appelé *job* dans la documentation bancaire source) est..."

### 3.4 Lutte contre la malédiction du savoir

**Bénéfice** : H+M
**Domaine** : sciences cognitives, psycholinguistique
**Références** :

- Pinker, S. (2014), *The Sense of Style: The Thinking Person's Guide to Writing in the 21st Century*, Viking, ISBN 978-0670025855. Chapitre "The Curse of Knowledge".
- Fondement empirique : Camerer, C., Loewenstein, G. & Weber, M. (1989), "The Curse of Knowledge in Economic Settings: An Experimental Analysis", *Journal of Political Economy*, 97(5), 1232-1254.

L'auteur sait des choses que le lecteur ignore et oublie systématiquement ce qu'il a fallu apprendre pour comprendre.

- ✗ Acronymes non développés, présupposés implicites sur l'architecture
- ✓ Développement au premier usage, présupposés explicités en tête de section

---

## 4. Exemples et concrétisation

### 4.1 Worked examples (exemples résolus)

**Bénéfice** : H+M (effet particulièrement marqué pour M)
**Domaine** : psychologie de l'éducation
**Référence** : Sweller, J. & Cooper, G. A. (1985), "The Use of Worked Examples as a Substitute for Problem Solving in Learning Algebra", *Cognition and Instruction*, 2(1), 59-89. DOI : 10.1207/s1532690xci0201_3

Un exemple résolu pas-à-pas active des schémas plus robustes qu'une définition abstraite.

- ✗ "Un `ProcessResult` encapsule l'état de sortie et les métadonnées d'exécution."
- ✓ Idem + exemple complet montrant construction, accès aux champs, cas d'erreur

### 4.2 Exemples négatifs explicites (contre-exemples)

**Bénéfice** : H+M
**Domaine** : sciences cognitives de l'apprentissage de concepts
**Référence** : Tennyson, R. D. & Park, O. C. (1980), "The Teaching of Concepts: A Review of Instructional Design Research Literature", *Review of Educational Research*, 50(1), 55-70. DOI : 10.3102/00346543050001055

Un exemple positif seul crée un attracteur unipolaire. Un exemple positif + un négatif crée une frontière qui force l'inférence de la règle.

- ✗ Ne montrer que le happy path
- ✓ "Ne pas faire : `result.value` avant de vérifier `result.ok` — lève une `UnboundError`."

### 4.3 Pluralité et hétérogénéité des exemples

**Bénéfice** : M>H (mitige l'effet attracteur sur LLM)
**Domaine** : apprentissage de concepts, prompt engineering
**Références** :

- Pour les humains : Gick, M. L. & Holyoak, K. J. (1983), "Schema induction and analogical transfer", *Cognitive Psychology*, 15(1), 1-38. DOI : 10.1016/0010-0285(83)90002-6
- **Vérifiée ✓** pour les LLMs : [Anthropic, *Use examples (multishot prompting) to guide Claude's behavior*, documentation officielle. Recommande explicitement 3-5 exemples *diversifiés* couvrant les cas limites.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting)

Un exemple unique fixe implicitement toutes ses dimensions comme contraintes. Plusieurs exemples hétérogènes forcent l'identification de ce qui est libre vs contraint.

- ✗ Un seul exemple, mention "il y en a d'autres" — surpondéré par le LLM
- ✓ 3 exemples qui varient sur les dimensions non pertinentes (longueur, registre, contexte d'usage)

### 4.4 Encadrement principe → exemple → principe

**Bénéfice** : M>H
**Domaine** : prompt engineering, théorie de la spécification
**Référence** : Apparenté au principe d'expansion-illustration-récapitulation classique en rhétorique. Pas de référence académique unique pour le pattern dans le contexte LLM ; observation empirique convergente dans la littérature prompt engineering.

L'instruction abstraite est traitée avec moins de poids que la structure concrète. Répéter le principe après l'exemple ramène l'attention à l'abstraction.

- ✗ "Voici un exemple [exemple]. Il y en a d'autres."
- ✓ "Le critère est X. Par exemple : [exemple]. D'autres formes valides incluent [forme abstraite A], [forme abstraite B]."

### 4.5 Nommer explicitement les dimensions libres

**Bénéfice** : M>H
**Domaine** : prompt engineering, théorie de la spécification
**Référence** : Pas de référence académique canonique ; reformulation pratique du principe d'abstraction explicite. Apparenté aux travaux sur la spécification par contrat (voir 7.2).

Plutôt que "il y en a d'autres", énumérer ce qui peut varier.

- ✗ "Voici un exemple — il y a d'autres formes possibles."
- ✓ "Voici un exemple. Le format, le registre et la longueur sont libres ; seule la structure du retour est contrainte."

---

## 5. Clarté référentielle (spécifique LLM)

### 5.1 Élimination des références anaphoriques inter-sections

**Bénéfice** : M>H (les humains familiers du document compensent, les chunks RAG non)
**Domaine** : linguistique computationnelle, NLP
**Référence** : [Jurafsky, D. & Martin, J. H. (2025), *Speech and Language Processing*, 3e éd., version manuscrite en ligne. Chapitres sur coreference resolution.](https://web.stanford.edu/~jurafsky/slp3/)

"Cette valeur", "comme vu plus haut", "le module ci-dessus" tombent quand un chunk est extrait isolé.

- ✗ "Cette valeur doit correspondre à celle définie plus haut."
- ✓ "La valeur `timeout_ms` doit correspondre à `DB_TIMEOUT` dans `config.py`."

### 5.2 Récapitulatif explicite en début et fin de section

**Bénéfice** : M>H
**Domaine** : NLP, recherche sur les LLMs (lost-in-the-middle)
**Référence vérifiée ✓** : [Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F. & Liang, P. (2024), "Lost in the Middle: How Language Models Use Long Contexts", *Transactions of the Association for Computational Linguistics*, 12, 157-173.](https://aclanthology.org/2024.tacl-1.9/) — [preprint arXiv:2307.03172 (2023)](https://arxiv.org/abs/2307.03172)

Les LLMs utilisent mieux l'information placée en début et en fin de contexte. Redondance acceptable pour un humain qui scanne, déterminante pour un LLM.

- ✗ Section qui plonge directement dans le détail
- ✓ "Cette section explique X. Points clés : A, B, C." + "En résumé, X fonctionne via A et B."

### 5.3 Position de l'information critique

**Bénéfice** : M>H
**Domaine** : NLP
**Référence** : Liu et al. (2024), voir 5.2.

L'information critique ne doit pas être au milieu d'un long contexte.

- ✗ Configuration critique enterrée à mi-chemin d'un long README
- ✓ Configuration critique en début ou fin, ou dans un fichier dédié court

---

## 6. Méta-information et ancrage (frontmatter)

### 6.1 Phase d'écriture (`written-at`) et phase de validité (`valid-for`)

**Bénéfice** : H+M
**Domaine** : ingénierie documentaire, sciences de l'information
**Référence** : Pas de référence académique canonique pour le pattern phase-based versioning. Approche apparentée : [Semantic Versioning](https://semver.org/). Inspiration plus ancienne : pratiques de release management en génie logiciel.

Une phase nommée encode l'état d'esprit et le contexte de production, qu'une date ISO ne transmet pas.

- ✗ `date: 2023-03-11` (information morte sans contexte)
- ✓ `written-at: poc` + `valid-for: mvp` (information vivante, écart calculable)

### 6.2 Type Diátaxis explicite

**Bénéfice** : H+M
**Domaine** : architecture documentaire
**Référence** : Procida, voir 1.3.

Le frontmatter `diataxis: tutorial | how-to | reference | explanation` indique au lecteur (et au LLM) le mode de lecture attendu.

### 6.3 Audience explicite (incluant l'IA si pertinent)

**Bénéfice** : M (signal de priorité d'optimisation)
**Domaine** : design documentaire, prompt engineering

`audience: [developer, AI]` ou `primary-reader: AI` indique que les pratiques spécifiques LLM doivent être priorisées sur ce document.

### 6.4 Statut explicite (draft / stable / deprecated)

**Bénéfice** : H+M
**Domaine** : gestion de cycle de vie documentaire

Un LLM ne détecte pas la péremption implicite — il faut la rendre explicite.

- ✗ Ancien document sans marquage
- ✓ `status: deprecated` + `superseded-by: nouveau-fichier.md`

---

## 7. Spécifique au code (docstrings, commentaires)

### 7.1 Premier paragraphe du docstring auto-suffisant

**Bénéfice** : H+M
**Domaine** : ingénierie logicielle
**Référence vérifiée ✓** : [PEP 257 — *Docstring Conventions*, Python Software Foundation.](https://peps.python.org/pep-0257/)

Les outils d'autocomplétion, les LLMs, les générateurs de doc ne récupèrent souvent que le premier paragraphe.

- ✗ Docstring qui commence par le contexte historique
- ✓ Première phrase = ce que fait la fonction (entrée → sortie)

### 7.2 Documenter invariants et cas d'échec (Design by Contract)

**Bénéfice** : M>H
**Domaine** : ingénierie logicielle, programmation par contrat
**Référence** : Meyer, B. (1992), "Applying Design by Contract", *IEEE Computer*, 25(10), 40-51. DOI : 10.1109/2.161279

Les LLMs génèrent du code basé sur les patterns documentés ; documenter explicitement les cas d'erreur réduit leur réapparition.

- ✗ `Returns: Result object`
- ✓ `Returns: Result object. result.ok is False if [conditions]. Raises ValueError if [condition].`

---

## 8. Points complémentaires non développés ci-dessus

Ces points méritent mention mais ne nécessitent pas de section dédiée pour ton usage.

### 8.1 Expertise reversal effect

**Bénéfice** : H (à connaître pour calibrer)
**Référence** : Kalyuga, S., Ayres, P., Chandler, P. & Sweller, J. (2003), "The Expertise Reversal Effect", *Educational Psychologist*, 38(1), 23-31. DOI : 10.1207/S15326985EP3801_4

Ce qui aide un novice (worked examples détaillés, redondance) peut ralentir un expert. Implication : segmenter par audience, ou rendre la verbosité optionnelle (progressive disclosure).

### 8.2 Effet de génération / self-explanation

**Bénéfice** : H (peu transférable au LLM en lecture)
**Référence** : Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P. & Glaser, R. (1989), "Self-Explanations: How Students Study and Use Examples in Learning to Solve Problems", *Cognitive Science*, 13(2), 145-182. DOI : 10.1207/s15516709cog1302_1

On retient mieux ce qu'on a produit. Pertinent pour les tutoriels, moins pour les références.

### 8.3 Advance organizers

**Bénéfice** : H+M
**Référence** : Ausubel, D. P. (1960), "The use of advance organizers in the learning and retention of meaningful verbal material", *Journal of Educational Psychology*, 51(5), 267-272. DOI : 10.1037/h0046669

Une introduction qui pose le cadre conceptuel avant le détail améliore la rétention humaine. Pour le LLM, équivaut au récapitulatif initial de 5.2.

### 8.4 Communauté de pratique et glossaire intégré

**Bénéfice** : H+M
**Référence** : Lave, J. & Wenger, E. (1991), *Situated Learning: Legitimate Peripheral Participation*, Cambridge University Press, ISBN 978-0521423748.

Le vocabulaire technique présuppose une communauté. Quand la communauté change, le présupposé devient barrière. Documenter le vocabulaire au premier usage rend le document résistant au turnover.

---

## Notes sur la complétude

Cette liste est exhaustive sur les quatre axes demandés (organisation, style, structure, layout) au niveau des principes établis. Elle est non exhaustive sur :

- les techniques de rédaction génériques (relire à voix haute, faire relire par un naïf, etc.) — relèvent du métier d'écriture plus que de la recherche
- les questions de typographie fine et de design éditorial — domaine connexe mais distinct
- les outils et chaînes d'édition (linters, validators, générateurs de doc) — relèvent de l'outillage, pas du contenu

## Mode de vérification

Au moment de la rédaction (12 juin 2026), les références marquées ✓ ont été directement vérifiées via recherche web : Sweller 1988, Cowan 2001, Liu et al. 2024, Morkes & Nielsen 1997, Nielsen 2006 (F-pattern), OASIS DITA 1.3, Procida (Diátaxis), Anthropic multishot prompting, PEP 257.

Les autres références sont des classiques académiques bien établis cités de mémoire avec un niveau de confiance élevé sur l'auteur/titre/journal, mais sans re-vérification systématique des numéros de page ou DOI. Si une citation précise doit servir dans un livrable formel, une re-vérification ciblée est recommandée.
