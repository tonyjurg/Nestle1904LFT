# Feature: markafter <a name="start"></a>

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | --- 
[`Textcritical`](featuresbygroup.md#textcritical-features) | [`Node`](featuresbyfeaturetype.md#node-features)  | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | 🆗

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

## Notes

See also the following related features:
   * [markbefore](markbefore.md#readme): Text critical marker before word.
   * [markorder](markorder.md#readme): Order of punctuation and text critical marker.
    
Use the option `fmt='text-critical'` to print the text including text critical marks, see following example from Mark 1:1.

<pre>
T.text(139200,fmt='text-critical')
Ἀρχὴ τοῦ εὐαγγελίου Ἰησοῦ Χριστοῦ (Υἱοῦ Θεοῦ). 
</pre>

See also the following [Jupyter Notebook](https://nbviewer.org/github/tonyjurg/Nestle1904LFT/blob/main/docs/usecases/various_text_formats.ipynb#bullet3x6).

## Source description

Computed based upon from XML attribute `unicode` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme), [Datatype](featuresbydatatype.md#readme)  or [feature type](featuresbyfeaturetype.md#readme).*
