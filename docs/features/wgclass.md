# Feature: wgclass <a name="start"></a>

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Syntactic`](featuresbygroup.md#syntactic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`wg`](featuresbynodetype.md#wordgroup-nodes) | ✅

## Feature description 

Class of the wordgroup.

## Feature values

Value | Description | Frequency
--- |  --- | ---
np | Normal phrase | 33710
cl | Clause |	30857
cl*	| Clause (not in XML source) | 16378
empty | No clause type defined |	12760
pp	|| 11169
vp	|| 207
adjp ||	168
advp ||	166
adv	|| 7
nump ||	7


## Source description

Taken from (optional) XML attribute `class` of tag `wg` (wordgroup).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme), [Datatype](featuresbydatatype.md#readme)  or [feature type](featuresbyfeaturetype.md#readme).*
