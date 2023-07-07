# Feature: gn

Feature group |Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String`  | [`word`](featuresbynodetype.md#word-nodes)

## Feature description

Gramatical gender for wordtypes nouns, adjectives, pronouns, participles, and definite articles.

## Feature values

Value | Description | Frequency
 --- | --- | ---
`feminine` | grammatical gender is feminine | 18736
`masculine` | grammatical gender is masculine | 41486
`neuter` | grammatical gender is neuter | 13753
` ` | empty for any other wordtype | 63804

## Source description

Taken from XML attribute `gender` of tag `w` (word).

---
###### [Click here for list of all features](home.md#readme)
