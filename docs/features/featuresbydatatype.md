# Text-Fabric features Nestle 1904LFT (sorted by data type)
###### *(or browse by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme), or [feature type](featuresbyfeaturetype.md#readme))*

This is the key to the meaning of the features in this TextFabric dataset. The available features can be taken together in the following groups: 

* [String datatype features](#string-datatype)
* [Integer datatype features](#integer-datatype)
* [Link datatype features](#link-datatype)
* [Configuration data`](featuresbydatatype.md#configuration-data)

## String datatype

Name | Feature type | Available on node | Description | Examples
--- | --- | --- | --- | ---
[after](after.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Space or punctuation after word | ` ` `.`
[book](book.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`book`](featuresbynodetype.md#book-notes) | Full book name | `Matthew` ... `Revelation`
[bookshort](bookshort.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`book`](featuresbynodetype.md#book-notes) | Short book name | `MAT` `MAR` ... `REV`
[case](case.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical case | `nominative` `genitive` `dative`
[degree](degree.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Degree of an comparative or superlative adjective | `superlative` `comparative`
[gloss](gloss.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | English gloss | `faith`
[gn](gn.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical gender | `masculine` `feminine` `neuter`
[nodeID](nodeID.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Node ID  | `n56001015007`
[lemma](lemma.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Lexical lemma (cf. BDAG) |
[lex_dom](lex_dom.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Lexical domain according to SDBG | `092004`
[ln](ln.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Louw-Nida lexical classification | `93.169a`
[markafter](markafter.md) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Text critical marker after word | `-`, `)`, `]` , `]]`
[markbefore](markbefore.md) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes)| Text critical marker before word| `-`, `(`, `[`, `[[`
[markorder](markorder.md) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes)| Order of punctuation and text critical marker | `0`, `2`
[mood](mood.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical mood of a verb | `indicative` `optative `
[morph](morph.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Morphological tag | `V-AAI-3S` `N-GSF`
[normalized](normalized.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Surface word stripped of punctations |
[number](number.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical number | `singular` `plural`
[person](person.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical person | `first` `second` `third`
[junction](junction.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) |Junction information | `coordinate` `subordinate`
[roleclausedistance](roleclausedistance.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | distance to wg describing word function | `1` `3`
[sp](sp.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Part of Speech | `det` `adv` `prep`
[sp_full](sp_full.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Part of Speech (full) | `conjunction` `pronoun`
[strongs](strongs.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Strongs number | `5547`
[tense](tense.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical tense of the verb | `present` `aorist`
[type](type.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) |Gramatical type of noun or pronoun | `common` `personal`
[unicode](unicode.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Word as it appears in the text (in unicode) | `λόγος`
[voice](voice.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Gramatical voice of the verb | `active` `passive`
[wgrolelong](wgrolelong.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup role (full)| 
[wgrule](wgrule.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup rule | 
[wgtype](wgtype.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup type | `Verbless` `VerbElided`
[word](word.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Word as it appears in the text | `λόγος`
[wordrole](wordrole.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Synctactic role of word | `s` `o` `adv` `aux` 
[wordtranslit](wordtranslit.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Word transliterated to Latin characters| `logos`
[wordunacc](wordunacc.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Word without accents| `λογος`
[wgclass](wgclass.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup class | 
[wgrole](wgrole.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup role | `ClCl` `DetNP` `Conj-CL` `S-V-O`

## Integer datatype

Name | Feature type | Available on node | Description | Examples
--- | --- | --- | --- | ---
[booknumber](booknumber.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`book`](featuresbynodetype.md#book-notes) | NT book number (Matthew=1, ... , Revelation=27) | `3` `8`
[chapter](chapter.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) | Chapter number inside book | `1` `2` ...
[headverse](headverse.md#readme) | [`node`](featuresbyfeaturetype.md#node-features) | [`sentence`](featuresbynodetype.md#sentence-nodes) | Verse number of start of sentence | `1` `2`
[monad](monad.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Monad (word order in corpus) | `1` .. `137779`
[orig_order](orig_order.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Orig Order (word order in XML file)  | `1` .. `137779`
[verse](verse.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`verse`](featuresbynodetype.md#verse-nodes)| Verse number inside chapter | `1` `2`
[wgnum](wgnum.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`wg`](featuresbynodetype.md#wordgroup-nodes) | Wordgroup number | `1` `2`

## Link datatype

Name | Feature type | Available on node | Description | Examples
--- | --- | --- | --- | ---
[subj_ref](subj_ref.md#readme) | [`Edge`](featuresbyfeaturetype.md#edge-features) | [`word`](featuresbynodetype.md#word-nodes) | Subject reference |


## Configuration data

Name | Feature type | Available on node | Description | Examples
--- | --- | --- | --- | ---
[oslots](oslots.md) | [`Config`](featuresbyfeaturetype.md#config-features) | - | slot containment | `1` `1-11` `2010-2015,2020-2030`
[otext](otext.md) | [`Config`](featuresbyfeaturetype.md#config-features) |  - |  configuration for sections, structure, and text formats (textapi) | *no data, only specifications*  
[otype](otype.md) | [`Node`](featuresbyfeaturetype.md#node-features) |  | node type | `book` `verse` `clause` `phrase` `word`
