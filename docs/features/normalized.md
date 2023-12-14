# Feature: normalized

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Orthographic`](featuresbygroup.md#orthographic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | [`string`](featuresbydatatype.md#string-datatype)  | [`word`](featuresbynodetype.md#word-nodes)

## Feature description

Normalized Greek text (changed accents and diacritics to their standard forms). Also trailing punctuations are removed.

## Note

Use the option `fmt='text-normalized'` to print results in transliterated format. Following example will print Mark 1:1 in normalized format:

<pre>
T.text(139200,fmt='text-normalized')
Ἀρχή τοῦ εὐαγγελίου Ἰησοῦ Χριστοῦ Υἱοῦ Θεοῦ. 
</pre>

See also the following [Jupyter Notebook](https://nbviewer.org/github/tonyjurg/Nestle1904LFT/blob/main/docs/usecases/various_text_formats.ipynb).

## Source description

Taken from XML attribute `normalized` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
