# Text-Fabric features Nestle1904LFT (sorted by feature type)
###### *(or browse by [node type](featuresbynodetype.md#readme) or [feature group](featuresbygroup.md#readme))*

The features of this Text-Fabric dataset:

* [Node features](#node-features):
* [Edge features](#edge-features):
* [Config features](#config-features):

## Node features

Name | Feature group | Node type | Description | Examples
--- | --- | --- | --- | ---
[after](after.md#readme) | [`Orthographic`](featuresbygroup.md#orthographic-features) | [`word`](featuresbynodetype.md#word-nodes) | Space or punctuation after word | ` ` `.`
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`book`](featuresbynodetype.md#book-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) [`sentence`](featuresbynodetype.md#sentence-nodes) [`verse`](featuresbynodetype.md#verse-nodes) [`word`](featuresbynodetype.md#word-nodes)| Book name | `Matthew` `Mark`
[booknumber](booknumber.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`book`](featuresbynodetype.md#book-nodes) [`word`](featuresbynodetype.md#word-nodes)| Sequence number of book | `1` `2` ... `27`
[bookshort](bookshort.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`book`](featuresbynodetype.md#book-nodes) [`word`](featuresbynodetype.md#word-nodes)| Short book name | `MAT` `MAR` ... `REV`
[case](case.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical case | `nominative` `genitive` `dative`
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`word`](featuresbynodetype.md#word-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) [`verse`](featuresbynodetype.md#verse-nodes) |  Chapter number inside book | `1` `2` ...
[clausetype](clausetype.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Clause type information | `VerbElided` `Verbless`
[degree](degree.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`word`](featuresbynodetype.md#word-nodes) | Degree of an comparative or superlative adjective | `superlative` `comparative`
[gn](gn.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical gender | `masculine` `feminine` `neuter`
[gloss](gloss.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`word`](featuresbynodetype.md#word-nodes)  | English gloss | 
[headverse](headverse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`sentence`](featuresbynodetype.md#sentence-nodes) | Verse of first word of sentence |
[junction](junction.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Junction information | `coordinate` `subordinate` 
[lemma](lemma.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`word`](featuresbynodetype.md#word-nodes) | Lexical lemma (cf. BDAG) |
[lex_dom](lex_dom.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`word`](featuresbynodetype.md#word-nodes) | Lexical domain according to SDBG | `092004`
[ln](ln.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`word`](featuresbynodetype.md#word-nodes) | Louw-Nida lexical classification | `93.169a`
[markafter](markafter.md#readme) | [`Orthographic`](featuresbygroup.md#orthographic-features) | [`word`](featuresbynodetype.md#word-nodes) | Text critical marker after word | `-` `)`
[markbefore](markbefore.md#readme) | [`Orthographic`](featuresbygroup.md#orthographic-features) | [`word`](featuresbynodetype.md#word-nodes) | Text critical marker before word| `-` `(`
[markorder](markorder.md#readme) | [`Orthographic`](featuresbygroup.md#orthographic-features) | [`word`](featuresbynodetype.md#word-nodes) | Order of punctuation and text critical marker | ` ` `0` 
[monad](monad.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`word`](featuresbynodetype.md#word-nodes)  | Monad (word order in corpus)| `1` .. `137779`
[mood](mood.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical mood of a verb | `indicative` `optative `
[morhp](morph.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`word`](featuresbynodetype.md#word-nodes) |  Morphological tag | `V-AAI-3S` `N-GSF`
[nodeID](nodeID.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`word`](featuresbynodetype.md#word-nodes) | Node ID | `n56001015007`
[normalized](normalized.md#readme) | [`Orthographic`](featuresbygroup.md#orthographic-features) | [`word`](featuresbynodetype.md#word-nodes) | Surface word stripped of punctations |
[nu](nu.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`word`](featuresbynodetype.md#word-nodes)  | Gramatical number| `singular` `plural`
[orig_order](orig_order.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`word`](featuresbynodetype.md#word-nodes) | Orig Order (word order in XML file)  | `1` .. `137779`
[otype](otype.md) | [`Grid`](featuresbygroup.md#grid-features) | | node type data | 
[person](person.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical person | `first` `second` `third`
[ref](ref.md#readme) | [`Relational`](featuresbygroup.md#relational-features)  | [`word`](featuresbynodetype.md#word-nodes) | Referent | `n40001011005`
[roleclausedistance](roleclausedistance.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`word`](featuresbynodetype.md#word-nodes) | distance to wg describing word function|
[strongs](strongs.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | [`word`](featuresbynodetype.md#word-nodes) | Strongs number | `5547`
[subj_ref](subj_ref.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | [`word`](featuresbynodetype.md#word-nodes) | Subject reference |
[tense](tense.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`word`](featuresbynodetype.md#word-nodes) |  Gramatical tense of the verb | `present` `aorist`
[type](type.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) [`Syntactic`](featuresbygroup.md#syntactic-features) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical type of noun or pronoun | `common` `personal`
[unicode](unicode.md#readme) | [`Orthographic`](featuresbygroup.md#orthographic-features)  | [`word`](featuresbynodetype.md#word-nodes) | Word as it appears in the text (in unicode)| `λόγος`
[verse](verse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | | Sequence number  | `1` `2` ...   Verse number inside chapter | `1` `2`
[voice](voice.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical voice of the verb | `active` `passive`
[wgclass](wgclass.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup class |  `np` `cl`
[wglevel](wglevel.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup level |
[wgnum](wgnum.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup number | `34`
[wgrole](wgrole.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup role  | `s` `o` `apposition`
[wgrule](wgrule.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup rule | `ClCl` `ClCl2`
[wgtype](wgtype.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | WordGroup type | `Verbless` `VerbElided`
[word](word.md#readme) | [`Orthographic`](featuresbygroup.md#orthographic-features) | [`word`](featuresbynodetype.md#word-nodes) | Word as it appears in the text | `λόγος`
[wordlevel](wordlevel.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`word`](featuresbynodetype.md#word-nodes) | Number of parent wordgroups for a word | 
[wordrole](wordrole.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`word`](featuresbynodetype.md#word-nodes) | Role of the word (abbreviated) | 
[wordrolelong](wordrolelong.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | [`word`](featuresbynodetype.md#word-nodes) | Role of the word (full) | 
[wordtranslit](wordtranslit.md#readme) | [`Orthographic`](featuresbygroup.md#orthographic-features) | [`word`](featuresbynodetype.md#word-nodes) | Word transliterated to Latin characters| `logos`
[wordunacc](wordunacc.md#readme) | [`Orthographic`](featuresbygroup.md#orthographic-features) | [`word`](featuresbynodetype.md#word-nodes) | Word without accents| `λογος`

## Edge features

Name | Feature group | Node type | Description | Example
--- | --- | --- | --- | ---
[subj_ref](subj_ref.md#readme) | [`Relational`](featuresbygroup.md#relational-features)  | [`word`](featuresbynodetype.md#word-nodes) | Subject reference |

## Config features

Name | Feature group | Node type | Description| Examples
---| --- | --- | --- | ---
[oslots](oslots.md) | [`Grid`](featuresbygroup.md#grid-features) | | slot containment | `1` `1-11` `2010-2015,2020-2030`
[otext](otext.md) | [`Grid`](featuresbygroup.md#grid-features) | | configuration for sections, structure, and text formats (textapi) | *no data, only specifications*  


