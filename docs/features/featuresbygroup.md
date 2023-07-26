# Text-Fabric features Nestle 1904LFT (sorted by feature group)
###### *(or browse by [node type](featuresbynodetype.md#readme) or [feature type](featuresbyfeaturetype.md#readme))*

This is the key to the meaning of the features in this TextFabric dataset. The available features can be taken together in the following groups: 

* [Grid features](#grid-features)
* [Sectional features](#sectional-features)
* [Lexical features](#lexical-features)
* [Orthograpic features](#orthograpic-features)
* [Morphological features](#morphological-features)
* [Syntactic features](#syntactic-features)
* [Relational features](#relational-features)

## Grid features

Name|Feature type|Available on node|Description|Examples
---|---|---|---|---
[oslots](oslots.md) | [`Config`](featuresbyfeaturetype.md#config-features) | - | slot containment | `1` `1-11` `2010-2015,2020-2030`
[otext](otext.md) | [`Config`](featuresbyfeaturetype.md#config-features) |  - |  configuration for sections, structure, and text formats (textapi) | *no data, only specifications*  
[otype](otype.md) | [`Node`](featuresbyfeaturetype.md#node-features) |  | node type | `book` `verse` `clause` `phrase` `word`

## Sectional features

Name|Feature type|Available on node|Description|Examples
---|---|---|---|---
[book](book.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`book`](featuresbynodetype.md#book-notes) | Short book name | `MAT` `MAR` ... `REV`
[chapter](chapter.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`chapter`](featuresbynodetype.md#chapter-nodes) | Chapter number inside book | `1` `2` ...
[monad](monad.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Monad (word order in corpus) | `1` .. `137779`
[nodeID](nodeID.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Node ID  | `n56001015007`
[orig_order](orig_order.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) | Orig Order (word order in XML file)  | `1` .. `137779`
[verse](verse.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | [`word`](featuresbynodetype.md#word-nodes) [`verse`](featuresbynodetype.md#verse-nodes)| Verse number inside chapter | `1` `2`

## Lexical features

Name| Feature type | Description | Examples
---|---|---|---
[gloss](gloss.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | English gloss | `faith`
[lemma](lemma.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Lexical lemma (cf. BDAG) |
[lex_dom](lex_dom.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Lexical domain according to SDBG | `092004`
[ln](ln.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Louw-Nida lexical classification | `93.169a`
[strongs](strongs.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Strongs number | `5547`

## Orthograpic features

Name | Feature type | Description | Examples
--- | --- | --- | ---
[after](after.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Space or punctuation after word | ` ` `.`
[normalized](normalized.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Surface word stripped of punctations |
[unicode](unicode.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Word as it appears in the text (in unicode) |
[word](word.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Word as it appears in the text | 

## Morphological features

Name | Feature type |Description | Examples
--- | --- | --- | ---
[case](case.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical case | `nominative` `genitive` `dative`
[degree](degree.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Degree of an comparative or superlative adjective | `superlative` `comparative`
[gn](gn.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical gender | `masculine` `feminine` `neuter`
[mood](mood.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical mood of a verb | `indicative` `optative `
[morph](morph.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Morphological tag | `V-AAI-3S` `N-GSF`
[number](number.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical number | `singular` `plural`
[person](person.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical person | `first` `second` `third`
[tense](tense.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical tense of the verb | `present` `aorist`
[type](type.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical type of noun or pronoun | `common` `personal`
[voice](voice.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Gramatical voice of the verb | `active` `passive`

## Syntactic features

Name | Feature type | Description | Examples
--- | --- | --- | ---
[appos](appos.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Appostioncontainer information | `conjuncted-wg` `modifier-scope` 
[clausetype](clausetype.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Clause type information | `Verbless` `VerbElided`
[junction](junction.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Junction information | `coordinate` `subordinate`
[wordrole](wordrole.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Synctactic role of word | `s` `o` `adv` `aux` 
[roleclausedistance](roleclausedistance.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | distance to wg describing word function |
[wgrole](wgrole.md#readme) | [`Node`](featuresbyfeaturetype.md#node-features) | Word Group role | `ClCl` `DetNP` `Conj-CL` `S-V-O`


## Relational features

Name | Feature type |Description | Example
--- | --- | --- | ---
[ref](ref.md#readme) | [`Edge`](featuresbyfeaturetype.md#edge-features) | Referent | `n40001011005`
[subj_ref](subj_ref.md#readme) | [`Edge`](featuresbyfeaturetype.md#edge-features) | Subject reference |

