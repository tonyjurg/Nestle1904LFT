# Text-Fabric features Nestle 1904LFT (sorted per node type)
###### *(or browse by [feature type](featuresbyfeaturetype.md#readme) or [feature group](featuresbygroup.md#readme))*

This Text-Fabric dataset contains the following node types:
* [27 `book` nodes](#book-nodes)
* [260 `chapter`nodes](#chapter-nodes)
* [7943 `verse` nodes](#verse-nodes)
* [8011 `sentence` nodes](#sentence-nodes)
* [114879 `wg` (wordgroup) nodes](#wordgroup-nodes)
* [137779	`word` nodes](#word-nodes)

Below are all node features listed: 

## Book nodes 

Feature | Feature group | Data type | Description | Examples
--- | --- | --- | --- | ---
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Book name (fully spelled out) | `Luke` `Jude`
[bookshort](bookshort.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Book name (abbreviated) | `MAT` `MAR` ... `REV`
[booknumber](booknumber.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer`  |  NT book number (Matthew=1, ... , Revelation=27) | `3` `8`

## Chapter nodes 

Feature | Feature group | Data type | Description  | Examples
--- | --- | --- | --- | ---
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Chapter | `1` `28`

## Verse nodes 

Feature | Feature group | Data type | Short description | Examples
--- | --- | --- | --- | ---
[verse](verse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Verse | `2` `26`

## Sentence nodes 

Feature | Feature group | Data type | Short description | Examples
--- | --- | --- | --- | ---
[sentence](sentence.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Sentence number (counted per chapter) | `9`

## Wordgroup nodes 

Feature | Feature group |  Data type | Description | Examples
--- | --- | --- | --- | ---
[appos](appos.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |  appositioncontainer information | `conjuncted-wg` `modifier-scope`
[junction](junction.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Junction information | `coordinate` `subordinate` 
[wgclass](wgclass.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Wordgroup class |  `np` `cl`
[wglevel](wglevel.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Wordgroup level |
[wgnum](wgnum.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` |Wordgroup number |
[wgrole](wgrole.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |Wordgroup role | `s` `o` `apposition`
[wgrule](wgrule.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |Wordgroup rule | 
[wgtype](wgtype.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |Wordgroup type | `Verbless` `VerbElided`

## Word nodes 

Feature | Feature group |Data type | Description | Examples
--- | --- | --- | --- | ---
[after](after.md#readme) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | `String` | space or punctuation after word | 
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Short book abbreviation | 
[bookshort](bookshort.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Book name (abbreviated) | 
[booknumber](booknumber.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` |  NT book number (Matthew=1, ...,  Revelation=27) | 
[case](case.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical case | `nominative` `accusative`
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Chapter number inside book |
[degree](degree.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Degree of an comparative or superlative adjective | 
[morph](morph.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Morphological tag (Sandborg-Petersen morphology) | 
[gloss](gloss.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | English gloss |
[gn](gn.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical gender | `masculine` `feminine` `neuter`
[lemma](lemma.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Lexeme (lemma) |
[lex_dom](lex_dom.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Lexical domain according to Semantic Dictionary of Biblical Greek, SDBG | `092004`
[ln](ln.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Louw-Nida lexical classification | `93.169a`
[markafter](markafter.md) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | `String` | Text critical marker after word | `-`, `)`, `]` , `]]`
[markbefore](markbefore.md) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | `String` | Text critical marker before word| `-`, `(`, `[`, `[[`
[markorder](markorder.md) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | `String` | Order of punctuation and text critical marker | 
[monad](monad.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Monad (word order in corpus) | `1` .. `137779`
[mood](mood.md#readme) |  [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical mood of a verb | `indicative` `optative`
[nodeID](nodeID.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Node ID (as in the XML source data) |
[normalized](normalized.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Surface word stripped of punctations |
[nu](nu.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical number | `singular` `plural`
[number](number.md#readme) |  [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical number of the verb | `plural`
[orig_order](orig_order.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Orig Order (word order in XML file) | `1` .. `137779`
[person](person.md#readme) |  [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical person of the verb | `first` `second` `third`
[sentence](sentence.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Sentence number (counted per chapter) | 
[sp](sp.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Part of Speech (abbreviated) | 
[sp_full](sp_full.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Part of Speech (long description) | 
[strongs](strongs.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String`  | Strongs number | 
[subj_ref](subj_ref.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | `String`  | Subject reference (to nodeID in XML source data) |
[tense](tense.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical tense of the verb | `present` `aorist`
[type](type.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical type of noun or pronoun | `common` `personal`
[unicode](unicode.md#readme) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | `String` |  Word as it appears in the text (in unicode)| `λόγος`
[verse](verse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Verse number inside chapter | 
[voice](voice.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical voice of the verb |
[word](word.md#readme) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | `String` |  Word as it appears in the text | `λόγος`
[wordrole](wordrole.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |  Word role in the text (abbriviated)|
[wordrolelong](wordrolelong.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |  Word role in the text |
[word](word.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Word as it appears in the text | `λόγος`
[wordtranslit](wordtranslit.md#readme) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | `String` | Word transliterated to Latin characters| `logos`
[wordunacc](wordunacc.md#readme) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | `String` | Word without accents| `λογος`


 
