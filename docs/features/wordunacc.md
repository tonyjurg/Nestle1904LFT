# Feature: wordunacc <a name="start"></a>

Feature group | Feature type | Data type | Available for node types | Feature status
---  | --- | --- | --- | ---
[`Orthographic`](featuresbygroup.md#orthographic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes) | [✅](featuresbystatus.md#Trustworthy "Trustworthy")

## Feature description

Unaccented Greek text (diacritics removed).

## Note

See also the following related features:
   * [normalized](normalized.md#start): Surface word stripped of punctations	
   * [unicode](unicode.md#start): Word as it appears in the text (in unicode)
   * [word](word.md#start): Word as it appears in the text
   * [wordtranslit](wordtranslit.md#start): Word transliterated to Latin characters	

The following table will show the difference between these features using Mark 1:1 as example:

<img src="images/textfeatures.png" width="600">

Use the option `fmt='text-unaccented'` to print results in unaccented format, Following example will print Mark 1:1 in uaccented format:

<pre>
T.text(139200,fmt='text-unaccented')
Αρχη του ευαγγελιου Ιησου Χριστου Υιου Θεου. 
</pre>

See this [jupyter notebook](https://nbviewer.org/github/tonyjurg/Nestle1904LFT/blob/main/docs/usecases/various_text_formats.ipynb#bullet3x2) for usage examples.

## Source description

Calculated from XML attribute `unicode` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#start), [feature group](featuresbygroup.md#start), [data type](featuresbydatatype.md#start)  or [feature type](featuresbyfeaturetype.md#start).*
