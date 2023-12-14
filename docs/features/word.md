# Feature: word <a name="start"></a>

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Orthographic`](featuresbygroup.md#orthographic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) | ✅

## Feature description 

The word as it appears in the text (excl. [punctuations](after.md#readme) and [critical markers](featuresbygroup.md#textcritical-features)). 

## Notes

See also the following related features:
   * [normalized](normalized.md#readme): Surface word stripped of punctations	
   * [unicode](unicode.md#readme): Word as it appears in the text (in unicode)
   * [wordtranslit](wordtranslit.md#readme): Word transliterated to Latin characters	
   * [wordunacc](wordunacc.md#readme): Word without accents

In terms of the synatax tree this is considered the terminal node.

## Source description

Taken from the data of XML tag `w`.

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme), [Datatype](featuresbydatatype.md#readme)  or [feature type](featuresbyfeaturetype.md#readme).*
