# Feature: wordunacc

Feature group | Feature type | Data type | Available for node types
---  | --- | --- | ---
[`Orthograpic`](featuresbygroup.md#orthograpic-features) | [`Node`](featuresbyfeaturetype.md#node-features) | `String`  | [`word`](featuresbynodetype.md#word-nodes)

## Feature description

Unaccented Greek text (diacritics removed).

## Note

Use the option `fmt='text-unaccented'` to print results in unaccented format, Following example will print Mark 1:1 in uaccented format:

<pre>
T.text(139200,fmt='text-unaccented')
Αρχη του ευαγγελιου Ιησου Χριστου Υιου Θεου. 
</pre>

See also the following [Jupyter Notebook](https://nbviewer.org/github/tonyjurg/Nestle1904LFT/blob/main/docs/usecases/various_text_formats.ipynb).

## Source description

Calculated from XML attribute `unicode` of tag `w` (word).

---
###### *Browse all features by [node type](featuresbynodetype.md#readme), [feature group](featuresbygroup.md#readme) or [feature type](featuresbyfeaturetype.md#readme).*
