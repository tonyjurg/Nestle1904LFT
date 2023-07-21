# Feature: appos

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features)  | `String` | [`word`](featuresbynodetype.md#word-nodes)

## Feature description 

This feature indicates if a wordgroup is the containing wordgroup of an apposition.

## Feature values 

value | description | Frequency
---  | --- | --- 
` ` | no apposition | 46169
`modifier-scope` | TBD | 29645
`wrapper-clause-scope` | TBD | 12166
`wrapper-scope` | TBD | 11264
`conjuncted-wg` | TBD | 8075
`group` | TBD | 4957
`modifier-clause-scope` | TBD |	1712
`apposition-group` | TBD | 891

## Note

This use and meaning of this feature is not stable (yet) in the source data.

## Source description

Taken from (optional) XML attribute `appositioncontainer` of tag `wg` (wordgroup).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
