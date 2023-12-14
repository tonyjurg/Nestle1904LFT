# Feature: markbefore

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Textcritical`](featuresbygroup.md#textcritical-features) | [`Node`](featuresbyfeaturetype.md#node-features)  | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes)

## Feature description 

Text critical marker before word.

## Feature values 

markbefore | Description | Frequency
---  | --- | ---
`` | no mark | 137745
`—` | Dash | 16
`(` | Opening round bracket| 10
`[[` |Double opening square brackets | 7
`[` |Single opening square bracket | 1

## Note

Use the option `fmt='text-critical'` to print the text including text critical marks, see following example from Mark 1:1.

<pre>
T.text(139200,fmt='text-critical')
Ἀρχὴ τοῦ εὐαγγελίου Ἰησοῦ Χριστοῦ (Υἱοῦ Θεοῦ). 
</pre>

See also the following [Jupyter Notebook](https://nbviewer.org/github/tonyjurg/Nestle1904LFT/blob/main/docs/usecases/various_text_formats.ipynb).

## Source description

Computed based upon from XML attribute `unicode` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
