# Feature: sp

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String` | [`word`](featuresbynodetype.md#word-nodes)

## Feature description
abbreviated Part of Speech description for each wordtype.

## Feature values 

Label (this feature) | Part of Speech Full ([feature: sp_full](sp_full.md#readme)) | frequency | Example
--- | --- | --- | ---
adj | Adjective | 8452 | 
adv | adverb (currently missing!) | 6147 |
conj | Conjunction | 18227 |
det | Determiner (article) | 19786 |
intj | Interjection | 15 |
noun | Noun | 28455 |
num | Numeral | 476 |
prep | Preposition | 10914 | `περὶ` `εἰς`
ptcl | Particle | 773 |
pron | Pronoun | 16177 |
verb | Verb | 28357 | 


## Source description

Taken from XML attribute `class` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
