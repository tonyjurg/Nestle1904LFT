# Feature: markafter

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features)  | `String` | [`word`](featuresbynodetype.md#word-nodes)

## Feature description 

Text critical marker after word.

## Feature values 

markafter | Description | Frequency
---  | --- | ---
`` | no mark | 137728
`—` | Dash | 31
`)` | Closing round bracket| 11
`]]` |Double closing square brackets | 7
`(` | Opening round bracket|1 
`]` |Single closing square bracket | 1

## Note

Use the option `fmt='text-critical'` to print the text including text critical marks, see following example from Mark 1:1.

<pre>
T.text(139200,fmt='text-critical')
Ἀρχὴ τοῦ εὐαγγελίου Ἰησοῦ Χριστοῦ (Υἱοῦ Θεοῦ). 
</pre>

## Source description

Computed based upon from XML attribute `unicode` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
