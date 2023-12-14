# Features by feature type  <a name="start"></a>
###### *(or browse by [node type](featuresbynodetype.md#start), [data type](featuresbydatatype.md#start), or [feature group](featuresbygroup.md#start))*

The features of this Text-Fabric dataset:

* [Node features](#node-features):
* [Edge features](#edge-features):
* [Config features](#config-features):

## Node features

Name | Feature group | Data type | Availble for node types | Description | Examples
--- | --- | --- | --- | --- | ---
[after](after.md#start) | [`Orthographic`](featuresbygroup.md#orthographic-features) | [`string`](featuresbydatatype.md#string-datatype) |  [`word`](featuresbynodetype.md#word-nodes) | Space or punctuation after word | ` ` `.`
[book](book.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | [`book`](featuresbynodetype.md#book-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) [`verse`](featuresbynodetype.md#verse-nodes) [`word`](featuresbynodetype.md#word-nodes)| Book name | `Matthew` `Mark`
[booknumber](booknumber.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) | [`book`](featuresbynodetype.md#book-nodes) [`word`](featuresbynodetype.md#word-nodes)| Sequence number of book | `1` `2` ... `27`
[bookshort](bookshort.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) |[`book`](featuresbynodetype.md#book-nodes) [`word`](featuresbynodetype.md#word-nodes)| Short book name | `MAT` `MAR` ... `REV`
[case](case.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical case | `nominative` `genitive` `dative`
[chapter](chapter.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) | [`word`](featuresbynodetype.md#word-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) [`verse`](featuresbynodetype.md#verse-nodes) |  Chapter number inside book | `1` `2` ...
[clausetype](clausetype.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Clause type information | `VerbElided` `Verbless`
[degree](degree.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Degree of an comparative or superlative adjective | `superlative` `comparative`
[gn](gn.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical gender | `masculine` `feminine` `neuter`
[gloss](gloss.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes)  | English gloss | 
[headverse](headverse.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | [`sentence`](featuresbynodetype.md#sentence-nodes) | Verse of first word of sentence |
[junction](junction.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Junction information | `coordinate` `subordinate` 
[lemma](lemma.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Lexical lemma (cf. BDAG) |
[lex_dom](lex_dom.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Lexical domain according to SDBG | `092004`
[ln](ln.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Louw-Nida lexical classification | `93.169a`
[markafter](markafter.md#start) | [`Textcritical`](featuresbygroup.md#textcritical-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Text critical marker after word | `-` `)`
[markbefore](markbefore.md#start) | [`Textcritical`](featuresbygroup.md#textcritical-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Text critical marker before word| `-` `(`
[markorder](markorder.md#start) | [`Textcritical`](featuresbygroup.md#textcritical-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Order of punctuation and text critical marker | ` ` `0` 
[monad](monad.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) | [`word`](featuresbynodetype.md#word-nodes)  | Monad (word order in corpus)| `1` .. `137779`
[mood](mood.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical mood of a verb | `indicative` `optative `
[morhp](morph.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) |  Morphological tag | `V-AAI-3S` `N-GSF`
[nodeID](nodeID.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Node ID | `n56001015007`
[normalized](normalized.md#start) | [`Orthographic`](featuresbygroup.md#orthographic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Surface word stripped of punctations |
[nu](nu.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes)  | Gramatical number| `singular` `plural`
[orig_order](orig_order.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Orig Order (word order in XML file)  | `1` .. `137779`
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) |[`string`](featuresbydatatype.md#string-datatype) | | node type data | 
[person](person.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical person | `first` `second` `third`
[ref](ref.md#start) | [`Relational`](featuresbygroup.md#relational-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Referent | `n40001011005`
[roleclausedistance](roleclausedistance.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | distance to wg describing word function|
[strongs](strongs.md#start) | [`Lexical`](featuresbygroup.md#lexical-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Strongs number | `5547`
[subj_ref](subj_ref.md#start) | [`Relational`](featuresbygroup.md#relational-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Subject reference |
[tense](tense.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) |  Gramatical tense of the verb | `present` `aorist`
[type](type.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical type of noun or pronoun | `common` `personal`
[unicode](unicode.md#start) | [`Orthographic`](featuresbygroup.md#orthographic-features)  | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Word as it appears in the text (in unicode)| `λόγος`
[verse](verse.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`integer`](featuresbydatatype.md#integer-datatype) |  [`word`](featuresbynodetype.md#word-nodes)  [`verse`](featuresbynodetype.md#verse-nodes) | Verse number inside chapter | `1` `2`
[voice](voice.md#start) | [`Morphological`](featuresbygroup.md#morphological-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical voice of the verb | `active` `passive`
[wgclass](wgclass.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup class |  `np` `cl`
[wglevel](wglevel.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup level |
[wgnum](wgnum.md#start) | [`Sectional`](featuresbygroup.md#sectional-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup number | `34`
[wgrole](wgrole.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup role  | `s` `o` `apposition`
[wgrule](wgrule.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup rule | `ClCl` `ClCl2`
[wgtype](wgtype.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | WordGroup type | `Verbless` `VerbElided`
[word](word.md#start) | [`Orthographic`](featuresbygroup.md#orthographic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Word as it appears in the text | `λόγος`
[wordlevel](wordlevel.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Number of parent wordgroups for a word | 
[wordrole](wordrole.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Role of the word (abbreviated) | 
[wordrolelong](wordrolelong.md#start) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Role of the word (full) | 
[wordtranslit](wordtranslit.md#start) | [`Orthographic`](featuresbygroup.md#orthographic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Word transliterated to Latin characters| `logos`
[wordunacc](wordunacc.md#start) | [`Orthographic`](featuresbygroup.md#orthographic-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | Word without accents| `λογος`

## Edge features

Name | Feature group | Data type | Node type | Description | Example
--- | --- | --- | --- | --- | ---
[subj_ref](subj_ref.md#start) | [`Relational`](featuresbygroup.md#relational-features)  | | [`word`](featuresbynodetype.md#word-nodes) | Subject reference |

## Config features

Name | Feature group | Data type | Node type | Description| Examples
---| --- | --- | --- | --- | ----
[oslots](oslots.md) | [`Grid`](featuresbygroup.md#grid-features) | | | slot containment | `1` `1-11` `2010-2015,2020-2030`
[otext](otext.md) | [`Grid`](featuresbygroup.md#grid-features) | | | configuration for sections, structure, and text formats (textapi) |  *no data, only specifications*  


