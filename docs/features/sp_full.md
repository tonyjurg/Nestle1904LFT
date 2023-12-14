# Feature: sp_full

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | ✅

## Feature description
Full Part of Speech description for each wordtype.

## Feature values 

Part of Speech Full (this feature) | Label ([feature: sp](sp.md#readme)) | Frequency | Examples
--- | --- | --- | ---
adjective | adj | 8452 | 
adverb | adv | 6147 | 
conjunction | conj | 18227 | `καὶ` `δὲ` `ὅτι`
determiner | det | 19786 | `τὸν` `ταῖς` `ὁ`
interjection | intj | 15 | `Ὦ` `ναί`
noun | noun | 28455 |
numeral | num | 476 | `Ἑπτά` `πέντε`
preposition | prep | 10914 | `περὶ` `εἰς`
particle | ptcl | 773 | 
pronoun | pron | 16177 | 
verb | verb | 28357 | 

## Source description

Taken from XML attribute `class` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
