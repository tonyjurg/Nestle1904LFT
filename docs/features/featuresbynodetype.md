# Text-Fabric features Nestle 1904LFT (sorted per node type)
###### *(or browse by [feature type](featuresbyfeaturetype.md#readme), [data type](featuresbydatatype.md#readme), or [feature group](featuresbygroup.md#readme))*

This Text-Fabric dataset contains the following node types:
* [27 `book` nodes](#book-nodes)
* [260 `chapter`nodes](#chapter-nodes)
* [7944 `verse` nodes](#verse-nodes)
* [18609 `sentence` nodes](#sentence-nodes)
* [30479 `clause` nodes](#clause-nodes)
* [106868 `wg` (wordgroup) nodes](#wordgroup-nodes)
* [137779	`word` nodes](#word-nodes)

Below are all node features listed: 

## Book nodes 

Feature | Feature group | Data type | Description | Examples
--- | --- | --- | --- | ---
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Book name (fully spelled out) | `Luke` `Jude`
[bookshort](bookshort.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Book name (abbreviated) | `MAT` `MAR` ... `REV`
[booknumber](booknumber.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) |  NT book number (Matthew=1, ... , Revelation=27) | `3` `8`

## Chapter nodes 

Feature | Feature group | Data type | Description  | Examples
--- | --- | --- | --- | ---
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Book name (fully spelled out) | `Luke` `Jude`
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Chapter | `1` `28`

## Verse nodes 

Feature | Feature group | Data type | Short description | Examples
--- | --- | --- | --- | ---
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Book name (fully spelled out) | `Luke` `Jude`
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Chapter | `1` `28`
[verse](verse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Verse | `2` `26`

## Sentence nodes 

Feature | Feature group | Data type | Short description | Examples
--- | --- | --- | --- | ---
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Book name (fully spelled out) | `Luke` `Jude`
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Chapter | `1` `28`
[headverse](headverse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Verse where the sentence starts | `2` `26`
[sentence](sentence.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Sentence number (counted per chapter) | `9`

## Wordgroup nodes 

Feature | Feature group |  Data type | Description | Examples
--- | --- | --- | --- | ---
[junction](junction.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Junction information | `apposition` ` ` 
[wgclass](wgclass.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Wordgroup class |  `np` `cl`
[wglevel](wglevel.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Wordgroup level |
[wgnum](wgnum.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) |Wordgroup number |
[wgrole](wgrole.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) |Wordgroup role | `s` `o` `apposition`
[wgrule](wgrule.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) |Wordgroup rule | `PrepNp` `Conj-CL`
[wgtype](wgtype.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) |Wordgroup type | `group` `apposition`

## Word nodes 

Feature | Feature group |Data type | Description | Examples
--- | --- | --- | --- | ---
[after](after.md#readme) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | [`string`](featuresbydatatype.md#string-datatype) | space or punctuation after word | 
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Short book abbreviation | 
[bookshort](bookshort.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | Book name (abbreviated) | 
[booknumber](booknumber.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [[`integer`](featuresbydatatype.md#integer-datatype)](featuresbydatatype.md#integer-datatype)|  NT book number (Matthew=1, ...,  Revelation=27) | 
[case](case.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical case | `nominative` `accusative`
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Chapter number inside book |
[degree](degree.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Degree of an  adjective | ` ` `comparative` `superlative`
[morph](morph.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Morphological tag (Sandborg-Petersen morphology) | 
[gloss](gloss.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | English gloss |
[gn](gn.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical gender | `masculine` `feminine` `neuter`
[lemma](lemma.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | Lexeme (lemma) |
[lex_dom](lex_dom.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | Lexical domain according to Semantic Dictionary of Biblical Greek, SDBG | `092004`
[ln](ln.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | Louw-Nida lexical classification | `93.169a`
[markafter](markafter.md) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | [`string`](featuresbydatatype.md#string-datatype) | Text critical marker after word | `-`, `)`, `]` , `]]`
[markbefore](markbefore.md) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | [`string`](featuresbydatatype.md#string-datatype) | Text critical marker before word| `-`, `(`, `[`, `[[`
[markorder](markorder.md) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | [`string`](featuresbydatatype.md#string-datatype) | Order of punctuation and text critical marker | 
[monad](monad.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Monad (word order in corpus) | `1` .. `137779`
[mood](mood.md#readme) |  [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical mood of a verb | `indicative` `optative`
[nodeID](nodeID.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Node ID (as in the XML source data) |
[normalized](normalized.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | Surface word stripped of punctations |
[nu](nu.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical number | `singular` `plural`
[number](number.md#readme) |  [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical number of the verb | `plural`
[orig_order](orig_order.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Orig Order (word order in XML file) | `1` .. `137779`
[person](person.md#readme) |  [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical person of the verb | `first` `second` `third`
[sentence](sentence.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Sentence number (counted per chapter) | 
[sp](sp.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Part of Speech (abbreviated) | 
[sp_full](sp_full.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | Part of Speech (long description) | 
[strongs](strongs.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype)  | Strongs number | 
[subj_ref](subj_ref.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | [`string`](featuresbydatatype.md#string-datatype)  | Subject reference (to nodeID in XML source data) |
[tense](tense.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical tense of the verb | `present` `aorist`
[type](type.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical type of noun or pronoun | `common` `personal`
[unicode](unicode.md#readme) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | [`string`](featuresbydatatype.md#string-datatype) |  Word as it appears in the text (in unicode)| `λόγος`
[verse](verse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) | Verse number inside chapter | 
[voice](voice.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | Gramatical voice of the verb | `active` `passive`
[word](word.md#readme) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | [`string`](featuresbydatatype.md#string-datatype) |  Word as it appears in the text | `λόγος`
[wordrole](wordrole.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) |  Word role in the text (abbriviated)|
[wordrolelong](wordrolelong.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) |  Word role in the text | `Adverbial` `Subject` `Verbal`
[word](word.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Word as it appears in the text | `λόγος`
[wordtranslit](wordtranslit.md#readme) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | [`string`](featuresbydatatype.md#string-datatype) | Word transliterated to Latin characters| `logos`
[wordunacc](wordunacc.md#readme) | [`Orthographic`](featuresbygroup.md#Orthographic-features) | [`string`](featuresbydatatype.md#string-datatype) | Word without accents| `λογος`


 
