# Feature: sp

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | ✅

## Feature description
abbreviated Part of Speech description for each wordtype.

## Feature values 

Label (this feature) | Part of Speech Full ([feature: sp_full](sp_full.md#readme)) | Frequency | Examples
--- | --- | --- | ---
adj | Adjective | 8452 | `ἕκαστον` `ἰδίου`
adv | adverb | 6147 | `οὐκ` 
conj | Conjunction | 18227 | `καὶ` `δὲ` `ὅτι`
det | Determiner (article) | 19786 | `τὸν` `ταῖς` `ὁ`
intj | Interjection | 15 | `Ὦ` `ναί`
noun | Noun | 28455 | `βίβλῳ` `Θεὸς`
num | Numeral | 476 | `Ἑπτά` `πέντε`
prep | Preposition | 10914 | `περὶ` `εἰς`
ptcl | Particle | 773 | `λέγων`
pron | Pronoun | 16177 | `Ἐγὼ`
verb | Verb | 28357 | `εἶπεν` `ἀνέγνωτε`


## Source description

Taken from XML attribute `class` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme), [Datatype](featuresbydatatype.md#readme)  or [feature type](featuresbyfeaturetype.md#readme).*
