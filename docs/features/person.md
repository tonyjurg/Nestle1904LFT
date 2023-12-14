# Feature: person

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features)  | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes)

## Feature description

Gramatical person of a verb.

## Feature values

Value | Description | Frequency
--- | --- | ---
`first`| First person (either singular or plural) | 2943
`second` | Second person (either singular or plural) | 3729
`third` | Third person (either singular or plural) | 12747
`''` | Empty for any wordtypes other than verb | 118360


## Source description

Taken from XML attribute `person` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
