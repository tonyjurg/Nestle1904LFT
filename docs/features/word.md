# Feature: word <a name="start"></a>

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Orthographic`](featuresbygroup.md#orthographic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) | [✅](featuresbystatus.md#Trustworthy "Trustworthy")

## Feature description 

The word as it appears in the text excluding [punctuations](after.md#start) and [critical markers](featuresbygroup.md#textcritical-features)). In terms of the synatax tree this is considered the terminal node.

## Notes

See also the following related features:
   * [normalized](normalized.md#start): Surface word stripped of punctations	
   * [unicode](unicode.md#start): Word as it appears in the text (in unicode)
   * [wordtranslit](wordtranslit.md#start): Word transliterated to Latin characters	
   * [wordunacc](wordunacc.md#start): Word without accents
   
The following table will show the difference between these features using Mark 1:1 as example:

<img src="images/textfeatures.png" width="600">

## Source description

Taken from the data of XML tag `w`.

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [feature group](featuresbygroup.md#start), [data type](featuresbydatatype.md#start)  or [feature type](featuresbyfeaturetype.md#start).*
