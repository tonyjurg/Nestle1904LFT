# Feature: sp_full <a name="start"></a>

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | ✅

## Feature description
Full Part of Speech description for each wordtype.

## Feature values 

Part of Speech Full (this feature) | Label ([feature: sp](sp.md#start)) | Frequency | Examples
--- | --- | --- | ---
adjective | adj | 8452 | `ἕκαστον` `ἰδίου`
adverb | adv | 6147 | `οὐκ`
conjunction | conj | 18227 | `καὶ` `δὲ` `ὅτι`
determiner | det | 19786 | `τὸν` `ταῖς` `ὁ`
interjection | intj | 15 | `Ὦ` `ναί`
noun | noun | 28455 | `βίβλῳ` `Θεὸς`
numeral | num | 476 | `Ἑπτά` `πέντε`
preposition | prep | 10914 | `περὶ` `εἰς`
particle | ptcl | 773 | `λέγων`
pronoun | pron | 16177 | `Ἐγὼ`
verb | verb | 28357 | `εἶπεν` `ἀνέγνωτε`

## Source description

Taken from XML attribute `class` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [feature group](featuresbygroup.md#start), [data type](featuresbydatatype.md#start)  or [feature type](featuresbyfeaturetype.md#start).*
