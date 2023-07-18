# The \<p\> tag in Low Fat Trees XML

Examining the data the most logical conclusion is that the \<p\> tag contains the full surface text of a single sentence.
This can also be seen in the following image, the \<p\>..\</p\>  pair is at the same level (i.e. parallel) to the top \<wg\> ..\</wg\>
of that same sentence. 

Hence, the \<p\> tag provides a kind of redundant information, so it was not incorporate it into this LFT Text-Fabric implementation. 
The content of the string can be recreated using Text-Fabric by using the following method:
>T.text(node, fmt=..., ...)
