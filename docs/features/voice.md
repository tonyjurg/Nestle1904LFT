# Feature: voice

Feature group |Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) | ✅

## Feature description
Gramatical voice of the verb.

## Feature values

voice (this feature) | explanation | Frequency
--- | --- | ---
active | Sentences subject is agent of the verb's action | 20742
middle | Sentences subject is both agent and affected by the verb's action | 2408
middlePassive | | 1714
passive | The subject of the verb is being acted upon | 3493
'' | Empty for wordtypes other than verbs | 109422

## Notes

The Bible Online Learner dataset contains additional details.

## Source description

Taken from XML attribute `voice` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
