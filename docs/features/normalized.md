# Feature: normalized <a name="start"></a>

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Orthographic`](featuresbygroup.md#orthographic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) | ✅

## Feature description

Normalized Greek text (changed accents and diacritics to their standard forms). Also trailing punctuations are removed.

## Notes

See also the following related features:
   * [unicode](unicode.md#start): Word as it appears in the text (in unicode)
   * [word](word.md#start): Word as it appears in the text
   * [wordtranslit](wordtranslit.md#start): Word transliterated to Latin characters	
   * [wordunacc](wordunacc.md#start): Word without accents


Use the option `fmt='text-normalized'` to print results in transliterated format. Following example will print Mark 1:1 in normalized format:

<pre>
T.text(139200,fmt='text-normalized')
Ἀρχή τοῦ εὐαγγελίου Ἰησοῦ Χριστοῦ Υἱοῦ Θεοῦ. 
</pre>

See also the following [Jupyter Notebook](https://nbviewer.org/github/tonyjurg/Nestle1904LFT/blob/main/docs/usecases/various_text_formats.ipynb#bullet3x3).

## Source description

Taken from XML attribute `normalized` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [feature group](featuresbygroup.md#start), [Datatype](featuresbydatatype.md#start)  or [feature type](featuresbyfeaturetype.md#start).*
