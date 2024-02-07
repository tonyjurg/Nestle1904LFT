# Formats

>   A.showFormats()
> 
 format|	level |	template
---|---|---
text-critical |	word |	{unicode}
text-normalized |	word |	{normalized}{after}
text-orig-full |	word |	{word}{after}
text-transliterated	| word |	{wordtranslit}{after}
text-unaccented |	word |	{wordunacc}{after}

## Example
```
for formats in T.formats:
    print(f'fmt={formats}\t: {T.text(139200,formats)}')
fmt=text-critical	: Ἀρχὴ τοῦ εὐαγγελίου Ἰησοῦ Χριστοῦ (Υἱοῦ Θεοῦ). 
fmt=text-normalized	: Ἀρχή τοῦ εὐαγγελίου Ἰησοῦ Χριστοῦ Υἱοῦ Θεοῦ. 
fmt=text-orig-full	: Ἀρχὴ τοῦ εὐαγγελίου Ἰησοῦ Χριστοῦ Υἱοῦ Θεοῦ. 
fmt=text-transliterated	: Arkhe tou euaggeliou Iesou Khristou Uiou Theou. 
fmt=text-unaccented	: Αρχη του ευαγγελιου Ιησου Χριστου Υιου Θεου.
```
