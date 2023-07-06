# Text-Fabric features Nestle 1904LFT (sorted per node type)
###### *(or browse by [feature type](featuresbyfeaturetype.md#readme) or [feature group](featuresbygroup.md#readme))*

This Text-Fabric dataset contains the following node types:
* [`word` nodes](#word-nodes)
* [`wg` (wordgroup) nodes](#wordgroup-nodes)
* [`phrase` nodes](#phrase-nodes)
* [`clause` nodes](#clause-nodes)
* [`sentence` nodes](#sentence-nodes)
* [`verse` nodes](#verse-nodes)
* [`chapter`nodes](#chapter-nodes)
* [`book` nodes](#book-nodes)

Below are all node features listed: 

## Word nodes 

Feature | Feature group |Data type | Description
--- | --- | --- | ---
[after](after.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | `String` | space or punctuation after word
[book_code](book_code.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Short book abbreviation
[book_long](book_long.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` |  Book name (fully spelled out)
[book_short](book_short.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Book name (abbreviated)
[booknum](booknum.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` |  NT book number (Matthew=1, Mark=2, ..., Revelation=27)
[case](case.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical case (Nominative, Genitive, Dative, Accusative, Vocative)
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Chapter number inside book
[clause](clause.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Clause number (counted per chapter)
[degree](degree.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Degree of an comparative or superlative adjective
[morph](morph.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Morphological tag (Sandborg-Petersen morphology)
[gloss](gloss.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | English gloss
[gn](gn.md#readme) | str | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical gender (Masculine, Feminine, Neuter)
[lemma](lemma.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Lexeme (lemma)
[lex_dom](lex_dom.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Lexical domain according to Semantic Dictionary of Biblical Greek, SDBG
[ln](ln.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Louw-Nida lexical classification (not present everywhere)
[monad](monad.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Monad
[mood](mood.md#readme) |  [`Morphological`](featuresbygroup.md#morphological-features) | `String` | | Gramatical mood of a verb (Indicative, Optative, etc.)
[nodeID](nodeID.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Node ID (as in the XML source data)
[normalized](normalized.md#readme) | [`Lexical`](featuresbygroup.md#lexical-features) | `String` | Surface word stripped of punctations
[nu](nu.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | | Gramatical number (Singular, Plural)
[number](number.md#readme) |  [`Morphological`](featuresbygroup.md#morphological-features) | `String` | | Gramatical number of the verb
[orig_order](orig_order.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Word order within corpus
[person](person.md#readme) |  [`Morphological`](featuresbygroup.md#morphological-features) | `String` | | Gramatical person of the verb (first, second, third)
[phrase](phrase.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Phrase number (counted per chapter)
[sentence](sentence.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Sentence number (counted per chapter)
[sp](sp.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Part of Speech (abbreviated)
[sp_full](sp_full.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Part of Speech (long description)
[strongs](strongs.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String`  | Strongs number
[subj_ref](subj_ref.md#readme) | [`Relational`](featuresbygroup.md#relational-features) | `String`  | Subject reference (to nodeID in XML source data)
[tense](tense.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical tense of the verb (e.g. Present, Aorist)
[text](text.md#readme) | [`Orthograpic`](featuresbygroup.md#orthograpic-features) | `String` |  Word as it appears in the text
[type](type.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical type of noun or pronoun (e.g. Common, Personal)
[verse](verse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | Verse number inside chapter
[voice](voice.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical voice of the verb


## Wordgroup nodes 

Feature | Feature group |  Data type | Description
--- | --- | --- | --- 
[appos](appos.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |  appositioncontainer
[articular](articular.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `Integer` | Indicates if wordgroup contains an article
[clauseType](clauseType.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Clause type information (`normalized`)
[cls](cls.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | WordGroup class (e.g. `np` `cl`)
[cltype](cltype.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |Clause type (`Verbless` `VerbElided`)
[crule](crule.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Clause rule (`ClCl` `ClCl2`)
[role](role.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |Role wordgroup (`s` `o` `apposition`)
[type](type.md#readme) | [`Morphological`](featuresbygroup.md#morphological-features) | `String` | Gramatical type of noun or pronoun (e.g. common, personal)

## Phrase nodes
Feature | Feature group | Data type | Short description
--- | --- | --- | ---
[phrase](phrase.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer`  | Phrase number (counted per chapter)
[phrasefunction](phrasefunction.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Phrase function (abbreviated)
[phrasefunction_long](phrasefunction_long.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Phrase function (long description)
[phrasetype](phrasetype.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Phrase type information


## Clause nodes
Feature | Feature group | Data type | Short description
--- | --- | --- | ---
[clause](clause.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Clause number (counted per chapter)
[clauserule](clauserule.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Clause rule information
[clausetype](clausetype.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` | Clause type information (verb, verbless, elided, minor, etc.)

## Sentence nodes 
Feature | Feature group | Data type | Short description
--- | --- | --- | ---
[sentence](sentence.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Sentence number (counted per chapter)
[sentencetype](sentencetype.md#readme) | [`Syntactic`](featuresbygroup.md#syntactic-features) | `String` |  sentence type information

## Verse nodes 
Feature | Feature group | Data type | Short description
--- | --- | --- | ---
[verse](verse.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Verse

## Chapter nodes 

Feature | Feature group | Data type | Description
--- | --- | --- | --- 
[chapter](chapter.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Chapter
[num](num.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer` | Chapter number inside book

## Book nodes 

Feature | Feature group | Data type | Description
--- | --- | --- | --- 
[book](book.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Book name (fully spelled out)
[bookshort](bookshort.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `String` | Book name (abbreviated)
[booknum](booknum.md#readme) | [`Sectional`](featuresbygroup.md#sectional-features) | `Integer`  |  NT book number (Matthew=1, Mark=2, ..., Revelation=27)








