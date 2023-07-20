# Feature: case

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Morphological`](featuresbygroup.md#morphological-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String` | [`word`](featuresbynodetype.md#word-nodes)

## Feature description

Gramatical case for wordtypes noun, pronoun, adjective, article, or participle.

## Feature values

case 'short' (TBA?) | case (this feature) | explanation | Frequency
--- | --- | --- | ---
acc | accusative | Generaly indicating the direct object of a verb | 23031
dat | dative | Generaly indicating indirect object of a verb | 12126
gen | genitive | Generaly indicating possesion | 19515
nom | nominative | Generaly indicating the subject | 24197
voc | vocative | Adressee of speech | 649
'' | '' | Empty for any other word type | 58261

## Source description

Taken from XML attribute `case` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
