# About this dataset

This repository is part of a set of repositories dedicated to storing the code and data generated for the 'Nestle 1904 Text-Fabric conversion project'. One of the objectives of this project is to create a high-quality Text-Fabric presentation of the Treebank Nestle 1904 Greek New Testament, resembling the Text-Fabric implementation of the Hebrew Old Testament ([BHSA](https://github.com/ETCBC/bhsa)). The project is a collaboration between [ETCBC](https://github.com/ETCBC) (Vrije Universiteit Amsterdam) and [CBLC](https://github.com/CenterBLC) (Andrews University). 

The project project various TextFabric presentations of the Nestle 1904 Greek New Testament, including:
* Nestle1904GBI: [`Webpage`](https://tonyjurg.github.io/Nestle1904GBI/) [`Github`](https://github.com/tonyjurg/Nestle1904GBI)
* Nestle1904LFT: [`Webpage`](https://tonyjurg.github.io/Nestle1904LFT/) [`Github`](https://github.com/tonyjurg/Nestle1904LFT)
* tfgreek2 (test version for final product): [`Github`](https://github.com/saulocantanhede/tfgreek2)
* Nestle1904 (ETCBC version; planned): [`Github`](https://github.com/ETCBC/nestle1904)

Each version utilizes a different conversion method and/or employs different sourcedata, resulting in a distinct set of features that have been tailored to its specific intended use.

## Differences between datasets

Each of these Text-Fabric implementations has distinct features and was created differently. The fundamental differences are in the following areas:

1. Starting data (XML input data):
* [‘GBI nodes’](https://github.com/tonyjurg/Nestle1904GBI/tree/main/resources/sourcedata)
*	[‘Low Fat Tree’](https://github.com/tonyjurg/Nestle1904LFT/tree/main/resources/xml)

2. Production tools used to perform the conversion to Text-Fabric:
*	Module [tf.convert.walker](https://annotation.github.io/text-fabric/tf/convert/walker.html#tf.convert.walker) with dedicated director function).
*	Module [tf.convert.xml](https://annotation.github.io/text-fabric/tf/convert/xml.html#tf.convert.xml)].

3. Level of syntactical information:
*	‘Basic implementation’: limited syntactical information (e.g., ‘subject’, ‘object’).
*	'Full implementation': includes all available syntactical information.

4. Method of handling syntactic information (as present in the LowFatTree data):
*	an almost ‘as found’ presentation of wordgroups (lacks ‘clause’ and ‘phrase’ nodes).
*	a significant amount of 'interpretation' by adding clauses and phrases.
*	'hybrid': offering option to present data either 'as found' or 'interpreted'. 

The following table shows how each of the previous mentioned Text-Fabric implementations relate to these areas:

Text-Fabric implementation | Starting data | Production tool | Syntactic information | handling syntactic info
--- | --- | --- | --- | ---
[Nestle1904GBI](https://tonyjurg.github.io/Nestle1904GBI/) | [‘GBI nodes’](https://github.com/tonyjurg/Nestle1904GBI/tree/main/resources/sourcedata) | [tf.convert.walker](https://annotation.github.io/text-fabric/tf/convert/walker.html#tf.convert.walker) | ‘Basic’ | 'interpretation' 
[Nestle1904LFT](https://tonyjurg.github.io/Nestle1904LFT/) | [‘Low Fat Tree’](https://github.com/tonyjurg/Nestle1904LFT/tree/main/resources/xml) | [tf.convert.walker](https://annotation.github.io/text-fabric/tf/convert/walker.html#tf.convert.walker) | 'Full' | ‘as found’ 
[tfgreek2](https://github.com/saulocantanhede/tfgreek2) | [‘Low Fat Tree’](https://github.com/tonyjurg/Nestle1904LFT/tree/main/resources/xml) | [tf.convert.xml](https://annotation.github.io/text-fabric/tf/convert/xml.html#tf.convert.xml)] | 'Full' | 'hybrid'
[Nestle1904](https://github.com/ETCBC/nestle1904) | [‘Low Fat Tree’](https://github.com/tonyjurg/Nestle1904LFT/tree/main/resources/xml) | [tf.convert.xml](https://annotation.github.io/text-fabric/tf/convert/xml.html#tf.convert.xml)] | 'Full' | 'hybrid'

## Example showing the difference betwen GBI and LFT

One of main differences between the GBI and LFT Text-Fabric implementation is the handling and presenation of syntactical information. The effects can be demonstrated by the two images depicting the graphical representation of John 1:1.

**The Nestle1904GBI implementation**

<img src="assets/images/john1v1GBI.jpg" alt="John 1v1 in Nestle1904GBI Text-Fabric">

**The Nestle1904LFT implementation**

<img src="assets/images/john1v1LFT.jpg" alt="John 1v1 in Nestle1904LFT Text-Fabric">





