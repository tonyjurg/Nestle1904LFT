# Feature: markorder

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | --- 
[`Orthographic`](featuresbygroup.md#orthographic-features) | [`Node`](featuresbyfeaturetype.md#node-features)  | `String` | [`word`](featuresbynodetype.md#word-nodes)

## Feature description 

This feature includes either a regular space character or a punctuation mark followed by a regular space character, occurring after a word.

## Feature values 

markorder | Description | Frequency
---  | --- | ---
` ` | No critical marks | 137694
`0` | Mark is before word | 34
`1` | Mark is after word, no punctuations after word | 9
`2` | Mark is after word, punctuations is after mark | 10
`3` | Mark is after word, punctuations is before mark | 32

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
