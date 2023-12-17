# Feature: roleclausedistance <a name="start"></a>

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) | [⚠️](featuresbystatus.md#Caution "Caution")

## Feature description

Distance to wordgroup defining the role of this word

## Notes

See also the following related features:
   * [wgrule](wgrule.md#start): Class of the wordgroup.
   * [wgclass](wgclass.md#start): All material found before a word.
   * [wordrole](wordrole.md#start): Syntactical role of the word (abbreviated).
   * [wgrole](wgrole.md#start): Syntactical role of the word (abbreviated).
   * [wglevel](wglevel.md#start): Number of the parent wordgroups for a wordgroup.
   * [roleclausedistance](roleclausedistance.md#start): Distance to wordgroup defining the role of this word.

The following image (part of the syntax tree of John 1 verse 1) demonstrates their relationship:

<img src="images/clause_wg_wordrole.png" width="550">

See also this [Jupyter notebook](https://nbviewer.org/github/tonyjurg/Nestle1904LFT/blob/main/docs/usecases/relation_clause_wg_word.ipynb) for more details.

## Source description

Calculated.

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [feature group](featuresbygroup.md#start), [data type](featuresbydatatype.md#start)  or [feature type](featuresbyfeaturetype.md#start).*
