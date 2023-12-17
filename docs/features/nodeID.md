# Feature: nodeID <a name="start"></a>

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Sectional`](featuresbygroup.md#sectional-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) | [✅](featuresbystatus.md#Trustworthy "Trustworthy")

## Feature description 
Node ID in the format like `n56001015007`.

```
The letter 'n' followe by a 11-digit unique id in the format

    BBCCCVVVWWW
    BB          => zero-padded book, NT starts at 40
      CCC       => zero-padded chapter
         VVV    => zero-padded verse
            WWW => zero-padded word index (instance within the verse)
```

## Source description

Taken from XML attribute `xml:id` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [feature group](featuresbygroup.md#start), [data type](featuresbydatatype.md#start)  or [feature type](featuresbyfeaturetype.md#start).*
