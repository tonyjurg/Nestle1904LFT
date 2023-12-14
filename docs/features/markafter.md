# Feature: markafter <a name="start"></a>

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | --- 
[`Textcritical`](featuresbygroup.md#textcritical-features) | [`Node`](featuresbyfeaturetype.md#node-features)  | [`string`](featuresbydatatype.md#string-datatype) | [`word`](featuresbynodetype.md#word-nodes) | 🆗

## Feature description 

Text critical marker after word.

## Feature values 

markafter | Description | Unicode codepoint | Frequency
---  | --- | --- | ---
`` | no mark | - | 137728
`—` | Em dash |  [`&#8212`](https://www.codetable.net/decimal/8212) | 31
`)` | Right Parenthesis [`&#41`](https://www.codetable.net/decimal/41) | 11
`]]` | Right Square Bracket (2x) | [`&#93`](https://www.codetable.net/decimal/91) (2x) | 7
`(` | Left Parenthesis  | [`&#40`](https://www.codetable.net/decimal/40) | 1 
`]` | Right Square Bracket | [`&#93`](https://www.codetable.net/decimal/93) | 1

## Notes

See also the following related features:
   * [markbefore](markbefore.md#start): Text critical marker before word.
   * [markorder](markorder.md#start): Order of punctuation and text critical marker.
    
Use the option `fmt='text-critical'` to print the text including text critical marks, see following example from Mark 1:1.

<pre>
T.text(139200,fmt='text-critical')
Ἀρχὴ τοῦ εὐαγγελίου Ἰησοῦ Χριστοῦ (Υἱοῦ Θεοῦ). 
</pre>

See also the following [Jupyter Notebook](https://nbviewer.org/github/tonyjurg/Nestle1904LFT/blob/main/docs/usecases/various_text_formats.ipynb#bullet3x6).

## Source description

Computed based upon from XML attribute `unicode` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [feature group](featuresbygroup.md#start), [Datatype](featuresbydatatype.md#start)  or [feature type](featuresbyfeaturetype.md#start).*
