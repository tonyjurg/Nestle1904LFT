# All Features <a name="start"></a>

In Text-Fabric, a "feature" refers to attributes associated with nodes, which represent linguistic elements in the text, including words, word groups, sentences, and verses. These features contain additional information specific to these nodes, facilitating diverse linguistic analyses and data extraction.

The full featureset of this Text-Fabric dataset can be viewed by different grouping methods:
* [Grouped by feature type](featuresbyfeaturetype.md#start)
     * [`Node`](featuresbyfeaturetype.md#node-features): the fundamental units or entities in the data model.
     * [`Edge`](featuresbyfeaturetype.md#edge-features): relationships or links, establishing connections between nodes in the data model.
     * [`Config`](featuresbyfeaturetype.md#config-features): contains the configuration or settings that define the behavior and parameters of the data processing or analysis.
* [Grouped by feature group](featuresbygroup.md#start):
     * [`Grid`](featuresbygroup.md#grid-features): pertains to the arrangement and organization of the data.
     * [`Sectional`](featuresbygroup.md#sectional-features): encompasses attributes or elements related to divisions within the text.
     * [`Lexical`](featuresbygroup.md#lexical-features): focuses on aspects related to individual words, their meanings, and lexical properties.
     * [`Orthograpic`](featuresbygroup.md#Orthograpic-features): deals with features related to the visual representation of the text.
     * [`Textcritical`](featuresbygroup.md#textcritical-features): deals with features related to textual critical issue.
     * [`Morphological`](featuresbygroup.md#morphological-features):  involves attributes that describe the internal structure and form of words.
     * [`Syntactic`](featuresbygroup.md#syntactic-features): covers properties related to the arrangement of words and phrases to form meaningful sentences and phrases. 
     * [`Relational`](featuresbygroup.md#relational-features): encompasses attributes that describe relationships or connections between nodes.
* [Grouped by node type](featuresbynodetype.md#start):
     * [`word`](featuresbynodetype.md#word-nodes): represents individual words in the text.
     * [`wg`](featuresbynodetype.md#wordgroup-nodes) (wordgroup): refers to a collection or grouping of words that form a cohesive unit.
     * [`sentence`](featuresbynodetype.md#sentence-nodes): represents individual sentences in the text.
     * [`verse`](featuresbynodetype.md#verse-nodes): pertains to divisions within a larger textual unit, specificaly the biblical verse.
     * [`chapter`](featuresbynodetype.md#chapter-nodes): divisions within the text that group related content together, specificaly the biblical chapter.
     * [`book`](featuresbynodetype.md#book-nodes): the highest-level division within the text, corresponding to a bible book.
* [Grouped by datatype](featuresbydatatype.md#start):
     * [`string`](featuresbydatatype.md#string-datatype): Datatype of feature is string.
     * [`integer`](featuresbydatatype.md#integer-datatype): Datatype of feature is integer.
     * [`link`](featuresbydatatype.md#link-datatype): Datatype of feature is link.
     * [`configuration`](featuresbydatatype.md#configuration-data): Configuration data.

## The concept 'features' in Text-Fabric

Text-Fabric, true to its name, implements the concepts of 'warp' and 'weft', inspired by textile weaving, to represent its data. The 'warp' denotes the foundational structured data, encompassing linguistic annotations like words, and phrases, while the 'weft' refers to the additional layers of information, known as features. These features encompass linguistic data, annotations, and metadata, seamlessly woven into the 'warp' data, resulting in a clear separation between structure and content. This approach enables Text-Fabric to efficiently handle complex linguistic datasets with versatility.
