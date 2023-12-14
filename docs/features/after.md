# Feature: after

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Orthographic`](featuresbygroup.md#orthographic-features) | [`Node`](featuresbyfeaturetype.md#node-features)  | `string` | [`word`](featuresbynodetype.md#word-nodes) | ✅ 

## Feature description 

This feature includes either a regular space character or a punctuation mark followed by a regular space character, occurring after a word. 

## Feature values 

after | symbol name | Unicode codepoint | Frequency
---  | --- | --- | ---
` ` | Space | [`&#32`](https://www.codetable.net/decimal/32)  |  119272
`, ` | Comma  | [`&#44`](https://www.codetable.net/decimal/44)   | 9441
`. ` | Full Stop | [`&#46`](https://www.codetable.net/decimal/46) | 5712
`· ` | Midle Dot | [`&#183`](https://www.codetable.net/decimal/183) | 2355
`; ` | Semicolon | [`&#59`](https://www.codetable.net/decimal/59) | 969
`— ` | Em Dash | [`&#8212`](https://www.codetable.net/decimal/8212) | 30

## Note

This feature does not include  textcritical markers. These details can be found in the following features:
Name | Data type | Availble for node types | Description | Examples
--- | --- | --- | --- | --- 
[markafter](markafter.md#readme) | `string` | [`word`](featuresbynodetype.md#word-nodes) | Text critical marker after word | `-` `)`
[markbefore](markbefore.md#readme) | `string` | [`word`](featuresbynodetype.md#word-nodes) | Text critical marker before word| `-` `(`
[markorder](markorder.md#readme) | `string` | [`word`](featuresbynodetype.md#word-nodes) | Order of punctuation and text critical marker | ` ` `0` 


## Source description

Taken from XML attribute `after` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
