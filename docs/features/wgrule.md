# Feature: wgrule <a name="start"></a>

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`wg`](featuresbynodetype.md#wordgroup-nodes) | [✅](featuresbystatus.md#Trustworthy "Trustworthy")

## Feature description 

Word Group rule

## Feature values

here are almost countless number of values possible. The list below will provide the top 25.

value | explanation | Frequency
--- | --- | ---
` ` | empty |	 21645
`DetNP` | | 15696
`PrepNp` | | 11044
`NPofNP` | | 6819
`Conj-CL`	| | 5576
`CLaCL` | | 3829
`sub-CL`  | | 	 3029
`V2CL`	 | |  	 2843
`V-O`	  | | 	 2725
`DetCL`	  | | 	 2011
`Np-Appos` | |	1908
`V-ADV`   | |	 1687
`ClCl`	  | subordinate clause follows the main clause | 1579
`NpAdjp`	 | | 1371
`AdjpNp`  | | 1368
`NpaNp`	 | |  1366
`DetAdj`  | | 1282
`ADV-V`	 | | 1137
`O-V`	 | | 1076
`that-VP`	 | | 894
`ClCl2` | subordinate clause precedes the main clause | 887
`NP-CL`	 | | 874
`All-NP`  | | 846
`Np2CL` | | 781
`NpPp` | | 676

## Note
See also the following related features:
   * [wgrule](wgrule.md#start): Class of the wordgroup.
   * [wgclass](wgclass.md#start): All material found before a word.
   * [wordrole](wordrole.md#start): Syntactical role of the word (abbreviated).
   * [wgrole](wgrole.md#start): Syntactical role of the word (abbreviated).
   * [wglevel](wglevel.md#start): Number of the parent wordgroups for a wordgroup.
   * [roleclausedistance](roleclausedistance.md#start): Distance to wordgroup defining the role of this word.

The following image (part of the syntax tree of John 1 verse 1) demonstrates their relationship:

<img src="images/clause_wg_wordrole.png" width="500">

See also this [Jupyter notebook](https://nbviewer.org/github/tonyjurg/Nestle1904LFT/blob/main/docs/usecases/relation_clause_wg_word.ipynb) for more details.

See also some other related features:
   * [junction](junction.md#start): 

## Source description

Taken from (optional) XML attribute `rule` of tag `wg` (wordgroup).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [feature group](featuresbygroup.md#start), [data type](featuresbydatatype.md#start)  or [feature type](featuresbyfeaturetype.md#start).*
