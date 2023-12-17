# Features by feature group <a name="start"></a>

###### *(or browse by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), or [feature type](featuresbyfeaturetype.md#start))*

This is the key to the meaning of the features in this TextFabric dataset. The available features can be taken together in the following groups: 

* [Grid features](#grid-features)
* [Sectional features](#sectional-features)
* [Lexical features](#lexical-features)
* [Orthographic features](#orthographic-features)
* [Textcritical_features](#textcritical-features)
* [Morphological features](#morphological-features)
* [Syntactic features](#syntactic-features)
* [Relational features](#relational-features)

## Grid features

Name | Feature type | Data type |  Available on node | Description | Examples
--- | --- | --- | --- | --- | ---
[oslots](oslots.md#start) | [`Config`](featuresbyfeaturetype.md#config-features) | - | - | slot containment | `1` `1-11` `2010-2015,2020-2030`
[otext](otext.md#start) | [`Config`](featuresbyfeaturetype.md#config-features) |  - |  - | configuration for sections, structure, and text formats (textapi) | *no data, only specifications*  
[otype](otype.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | - | - | node type | `book` `verse` `clause` `phrase` `word`

## Sectional features

Name | Feature type | Data type | Available on node | Description | Examples
--- | --- | --- | --- | --- | ---
[book](book.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) |  [`word`](featuresbynodetype.md#word-nodes) [`book`](featuresbynodetype.md#book-notes) | Full book name | `Matthew` ... `Revelation`
[booknumber](booknumber.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) |  [`word`](featuresbynodetype.md#word-nodes) [`book`](featuresbynodetype.md#book-notes) | NT book number (Matthew=1, ... , Revelation=27) | `3` `8`
[bookshort](bookshort.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`book`](featuresbynodetype.md#book-notes) | Short book name | `MAT` `MAR` ... `REV`
[chapter](chapter.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) | Chapter number inside book | `1` `2` ...
[headverse](headverse.md#start) | [`node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | [`sentence`](featuresbynodetype.md#sentence-nodes) | Verse number of start of sentence | `1` `2`
[monad](monad.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Monad (word order in corpus) | `1` .. `137779`
[nodeID](nodeID.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Node ID  | `n56001015007`
[orig_order](orig_order.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Orig Order (word order in XML file)  | `1` .. `137779`
[verse](verse.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`verse`](featuresbynodetype.md#verse-nodes)| Verse number inside chapter | `1` `2`
[wgnum](wgnum.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`integer`](featuresbydatatype.md#integer-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup number | `1` `2`

## Lexical features

Name | Feature type | Data type | Available on node | Description | Examples
--- | --- | --- | --- | --- | ---
[gloss](gloss.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | English gloss | `faith`
[lemma](lemma.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Lexical lemma (cf. BDAG) |
[lex_dom](lex_dom.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Lexical domain according to SDBG | `092004`
[ln](ln.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Louw-Nida lexical classification | `93.169a`
[strongs](strongs.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Strongs number | `5547`

## Orthographic features

Name | Feature type | Data type | Available on node | Description | Examples
--- | --- | --- | --- | --- | ---
[after](after.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Space or punctuation after word | ` ` `.`
[normalized](normalized.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Surface word stripped of punctations |
[unicode](unicode.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Word as it appears in the text (in unicode) | `λόγος`
[word](word.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Word as it appears in the text | `λόγος`
[wordtranslit](wordtranslit.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Word transliterated to Latin characters| `logos`
[wordunacc](wordunacc.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Word without accents| `λογος`

## Textcritical features

Name | Feature type | Data type  | Available on node | Description | Examples
--- | --- | --- | --- | --- | ---
[markafter](markafter.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Text critical marker after word | `-`, `)`, `]` , `]]`
[markbefore](markbefore.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes)| Text critical marker before word| `-`, `(`, `[`, `[[`
[markorder](markorder.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes)| Order of punctuation and text critical marker | `0`, `2`

## Morphological features

Name | Feature type | Data type | Available on node | Description | Examples
--- | --- | --- | --- | --- | ---
[case](case.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical case | `nominative` `genitive` `dative`
[degree](degree.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) |Degree of an comparative or superlative adjective | `superlative` `comparative`
[gn](gn.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical gender | `masculine` `feminine` `neuter`
[mood](mood.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical mood of a verb | `indicative` `optative `
[morph](morph.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) |Morphological tag | `V-AAI-3S` `N-GSF`
[number](number.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical number | `singular` `plural`
[person](person.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical person | `first` `second` `third`
[sp](sp.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) |Part of Speech | `det` `adv` `prep`
[sp_full](sp_full.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) |Part of Speech (full) | `conjunction` `pronoun`
[tense](tense.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical tense of the verb | `present` `aorist`
[type](type.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical type of noun or pronoun | `common` `personal`
[voice](voice.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical voice of the verb | `active` `passive`

## Syntactic features

Name | Feature type | Data type | Available on node | Description | Examples
--- | --- | --- | --- | --- | ---
[junction](junction.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) |Junction information | `coordinate` `subordinate`
[wordrole](wordrole.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Synctactic role of word | `s` `o` `adv` `aux` 
[roleclausedistance](roleclausedistance.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | distance to wg describing word function | `1` `3`
[wgclass](wgclass.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup class | 
[wgrole](wgrole.md#start) | [`Node`](featuresbyfeaturetype.md#node-features)  | [`string`](featuresbydatatype.md#string-datatype) |Wordgroup role | `s` `o` `apposition`
[wgrole](wgrole.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup role | `ClCl` `DetNP` `Conj-CL` `S-V-O`
[wgrolelong](wgrolelong.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup role (full)| 
[wgrule](wgrule.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup rule | 
[wgtype](wgtype.md#start) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup type | `Verbless` `VerbElided`

## Relational features

Name | Feature type | Data type | Available on node | Description | Examples
--- | --- | --- | --- | --- | ---
[subj_ref](subj_ref.md#start) | [`Edge`](featuresbyfeaturetype.md#edge-features) | | [`word`](featuresbynodetype.md#word-nodes) | Subject reference |

