# Feature: ln <a name="start"></a>

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Lexical`](featuresbygroup.md#lexical-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) | [✅](featuresbystatus.md#Trustworthy "Trustworthy") 

## Feature description

Louw-Nida lexical classification.

## Feature values:

Value | Desription | Frequency
--- | --- | ---
xx.yy  | one or more entries for the Louw-Nida references | 126756
'' | Empty | 11023

## Interpreting the data

The Louw-Nida Lexical Classification, by Johannes P. Louw and Eugene A. Nida, is a system for organizing New Testament Greek vocabulary. It categorizes words into 93 semantic domains based on meaning and context, emphasizing the importance of context in understanding word nuances. Lookup of values for feature ln can be performed in [Louw-Nida Lexicon](https://www.laparola.net/greco/louwnida.php).

## Notes

See also the related feature [lex_dom](lex_dom.md#start).

## Source description

Taken from XML attribute `domain` of tag `w` (word). The word sense data for this feature was compiled by the United Bible Societies MARBLE project. See [Macula-Greek Licence](https://github.com/Clear-Bible/macula-greek/blob/main/LICENSE.md).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [feature group](featuresbygroup.md#start), [data type](featuresbydatatype.md#start)  or [feature type](featuresbyfeaturetype.md#start).*
