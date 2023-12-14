# Feature: tense <a name="start"></a>

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) | ✅ 

## Feature description
Gramatical tense of a verb.

## Feature values

tense (this feature) | Explanation | Frequency
--- | --- | ---
aorist | Describing a simple action in the past | 11803
imperfect | Describing an ongoing action in the past | 1689
perfect | Describing a completed action in the present time | 1572
pluperfect | Describing a completed action in the past | 88
present | Describing an ongoing action in the present time | 11579
future | Describing a simple or ongoing action in the future | 1626
'' | Empty for any wordtype other than a verb | 109422

## Note
The 'future perfect' tense (describing a completed action in the future) is not found in the text.

## Source description

Taken from (optional) XML attribute `tense` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme), [Datatype](featuresbydatatype.md#readme)  or [feature type](featuresbyfeaturetype.md#readme).*
