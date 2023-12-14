# Feature: nu

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | ✅ 

## Feature description
Gramatical number of a noun.

## Feature values

Value | Description | Frequency
--- | --- | ---
plural | Plural gramatical number | 29091
singular | Singular gramatical number | 69846
'' | Empty for any wordtype other than noun | 38842

## Note

See also related feature [person](person.md#readme).

For gramatical number of a verb see feature [number](number.md#readme).

## Source description

Taken from XML attribute `number` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme), [Datatype](featuresbydatatype.md#readme)  or [feature type](featuresbyfeaturetype.md#readme).*
