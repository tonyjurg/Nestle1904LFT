# Feature: tense

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String`  | [`word`](featuresbynodetype.md#word-nodes)

## Feature description
Gramatical tense of a verb.

## Feature values

tense (this feature) | Explanation | Frequency
--- | --- | ---
Aorist | Describing a simple action in the past | 11803
Imperfect | Describing an ongoing action in the past | 1689
Perfect | Describing a completed action in the present time | 1572
Pluperfect | Describing a completed action in the past | 88
Present | Describing an ongoing action in the present time | 11579
Future | Describing a simple or ongoing action in the future | 1626
'' | Empty for any wordtype other than a verb | 109422

## Note
The 'future perfect' tense (Describing a completed action in the future) is not found in the text.

## Source description

Taken from (optional) XML attribute `tense` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
