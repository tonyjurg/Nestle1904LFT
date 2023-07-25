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
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Book name (fully spelled out) | `Luke`
[bookshort](bookshort.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Book name (abbreviated) | `MAT`
[booknumber](booknumber.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer`  |  NT book number (Matthew=1, ... , Revelation=27) | `3` `8`

## Chapter nodes 

Feature | Feature group | Data type | Description  | Examples
--- | --- | --- | --- | ---
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Chapter | `1` `28`
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Chapter number inside book |

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
[appos](appos.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |  appositioncontainer |
[clausetype](clausetype.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Clause type information | `VerbElided`
[cltype](cltype.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |Clause type | `Verbless` `VerbElided`
[rule](rule.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Clause rule | `ClCl` `ClCl2`
[role](role.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |Role wordgroup | `s` `o` `apposition`
[wgclass](wgclass.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | WordGroup class |  `np` `cl`

## Word nodes 

Feature | Feature group |Data type | Description | Examples
--- | --- | --- | --- | ---
[after](after.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | `String` | space or punctuation after word | 
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Short book abbreviation | 
[book_long](book_long.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` |  Book name (fully spelled out) |
[bookshort](bookshort.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Book name (abbreviated) | 
[booknumber](booknumber.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` |  NT book number (Matthew=1, ...,  Revelation=27) | 
[case](case.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical case | `nominative` `accusative`
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Chapter number inside book |
[degree](degree.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Degree of an comparative or superlative adjective | 
[morph](morph.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Morphological tag (Sandborg-Petersen morphology) | 
[gloss](gloss.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | English gloss |
[gn](gn.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical gender | `masculine` `feminine` `neuter`
[lemma](lemma.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Lexeme (lemma) |
[lex_dom](lex_dom.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Lexical domain according to Semantic Dictionary of Biblical Greek, SDBG |
[ln](ln.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Louw-Nida lexical classification (not present everywhere) |
[monad](monad.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Monad | **WARNING (see feature description)**
[mood](mood.md#readme) |  [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical mood of a verb | `indicative` `optative`
[nodeID](nodeID.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Node ID (as in the XML source data) |
[normalized](normalized.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Surface word stripped of punctations |
[nu](nu.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical number | `singular` `plural`
[number](number.md#readme) |  [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical number of the verb | `plural`
[orig_order](orig_order.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Word order within corpus | 
[person](person.md#readme) |  [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical person of the verb | `first` `second` `third`
[sentence](sentence.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Sentence number (counted per chapter) | 
[sp](sp.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Part of Speech (abbreviated) | 
[sp_full](sp_full.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Part of Speech (long description) | 
[strongs](strongs.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String`  | Strongs number | 
[subj_ref](subj_ref.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | `String`  | Subject reference (to nodeID in XML source data) |
[tense](tense.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical tense of the verb | `present` `aorist`
[type](type.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical type of noun or pronoun | `common` `personal`
[verse](verse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Verse number inside chapter | 
[voice](voice.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical voice of the verb |
[word](word.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | `String` |  Word as it appears in the text |



 
