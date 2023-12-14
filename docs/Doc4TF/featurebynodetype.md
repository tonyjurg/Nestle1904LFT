<p>N1904 Greek New Testament Text-Fabric dataset <a href="https://github.com/tonyjurg/Nestle1904LFT">tonyjurg/Nestle1904LFT - 0.6</a></p>

<h1>Features per node type</h1>

<h2>book</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td><code>string</code></td>
  <td>✅ Book name (in English language)</td>
  <td><code>Luke</code> <code>Matthew</code></td>
</tr>
<tr>
  <td><A HREF="booknumber.md#readme">booknumber</A></td>
  <td><code>integer</code></td>
  <td>✅ NT book number (Matthew=1, Mark=2, ..., Revelation=27)</td>
  <td><code>3</code> <code>5</code></td>
</tr>
<tr>
  <td><A HREF="bookshort.md#readme">bookshort</A></td>
  <td><code>string</code></td>
  <td>✅ Book name (abbreviated)</td>
  <td><code>Luke</code> <code>Acts</code></td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> ``</td>
</tr>
</tbody>
</table>

<h2>chapter</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td><code>string</code></td>
  <td>✅ Book name (in English language)</td>
  <td><code>Luke</code> <code>Matthew</code></td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td><code>integer</code></td>
  <td>✅ Chapter number inside book</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> ``</td>
</tr>
</tbody>
</table>

<h2>verse</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td><code>string</code></td>
  <td>✅ Book name (in English language)</td>
  <td><code>Luke</code> <code>Matthew</code></td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td><code>integer</code></td>
  <td>✅ Chapter number inside book</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> ``</td>
</tr>
<tr>
  <td><A HREF="verse.md#readme">verse</A></td>
  <td><code>integer</code></td>
  <td>✅ Verse number inside chapter</td>
  <td><code>10</code> <code>12</code></td>
</tr>
</tbody>
</table>

<h2>sentence</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td><code>string</code></td>
  <td>✅ Book name (in English language)</td>
  <td><code>Luke</code> <code>Matthew</code></td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td><code>integer</code></td>
  <td>✅ Chapter number inside book</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="headverse.md#readme">headverse</A></td>
  <td><code>string</code></td>
  <td>✅ Start verse number of a sentence</td>
  <td><code>1</code> <code>7</code></td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> ``</td>
</tr>
<tr>
  <td><A HREF="sentence.md#readme">sentence</A></td>
  <td><code>integer</code></td>
  <td>✅ Sentence number (counted per chapter)</td>
  <td><code>3</code> <code>4</code></td>
</tr>
</tbody>
</table>

<h2>wg</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="clausetype.md#readme">clausetype</A></td>
  <td><code>string</code></td>
  <td>✅ Clause type details (e.g. Verbless, Minor)</td>
  <td>`<code></code>VerbElided`</td>
</tr>
<tr>
  <td><A HREF="junction.md#readme">junction</A></td>
  <td><code>string</code></td>
  <td>✅ Junction data related to a wordgroup</td>
  <td>`<code></code>apposition`</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> ``</td>
</tr>
<tr>
  <td><A HREF="wgclass.md#readme">wgclass</A></td>
  <td><code>string</code></td>
  <td>✅ Class of the wordgroup (e.g. cl, np, vp)</td>
  <td><code>np</code> <code>cl</code></td>
</tr>
<tr>
  <td><A HREF="wglevel.md#readme">wglevel</A></td>
  <td><code>integer</code></td>
  <td>🆗 Number of the parent wordgroups for a wordgroup</td>
  <td><code>5</code> <code>4</code></td>
</tr>
<tr>
  <td><A HREF="wgnum.md#readme">wgnum</A></td>
  <td><code>integer</code></td>
  <td>✅ Wordgroup number (counted per book)</td>
  <td><code>2</code> <code>3</code></td>
</tr>
<tr>
  <td><A HREF="wgrole.md#readme">wgrole</A></td>
  <td><code>string</code></td>
  <td>✅ Syntactical role of the wordgroup (abbreviated)</td>
  <td>`<code></code>adv`</td>
</tr>
<tr>
  <td><A HREF="wgrolelong.md#readme">wgrolelong</A></td>
  <td><code>string</code></td>
  <td>✅ Syntactical role of the wordgroup (full)</td>
  <td>`<code></code>Adverbial`</td>
</tr>
<tr>
  <td><A HREF="wgrule.md#readme">wgrule</A></td>
  <td><code>string</code></td>
  <td>✅ Wordgroup rule information (e.g. Np-Appos, ClCl2, PrepNp)</td>
  <td><code>DetNP</code> ``</td>
</tr>
<tr>
  <td><A HREF="wgtype.md#readme">wgtype</A></td>
  <td><code>string</code></td>
  <td>✅ Wordgroup type details (e.g. group, apposition)</td>
  <td>`<code></code>group`</td>
</tr>
</tbody>
</table>

<h2>word</h2>

<table>
<thead>
<tr>
  <th>Feature</th>
  <th>Datatype</th>
  <th>Description</th>
  <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
  <td><A HREF="after.md#readme">after</A></td>
  <td><code>string</code></td>
  <td>✅ Characters (eg. punctuations) following the word</td>
  <td><code></code> <code>,</code></td>
</tr>
<tr>
  <td><A HREF="book.md#readme">book</A></td>
  <td><code>string</code></td>
  <td>✅ Book name (in English language)</td>
  <td><code>Luke</code> <code>Matthew</code></td>
</tr>
<tr>
  <td><A HREF="booknumber.md#readme">booknumber</A></td>
  <td><code>integer</code></td>
  <td>✅ NT book number (Matthew=1, Mark=2, ..., Revelation=27)</td>
  <td><code>3</code> <code>5</code></td>
</tr>
<tr>
  <td><A HREF="bookshort.md#readme">bookshort</A></td>
  <td><code>string</code></td>
  <td>✅ Book name (abbreviated)</td>
  <td><code>Luke</code> <code>Acts</code></td>
</tr>
<tr>
  <td><A HREF="case.md#readme">case</A></td>
  <td><code>string</code></td>
  <td>✅ Gramatical case (Nominative, Genitive, Dative, Accusative, Vocative)</td>
  <td>`<code></code>nominative`</td>
</tr>
<tr>
  <td><A HREF="chapter.md#readme">chapter</A></td>
  <td><code>integer</code></td>
  <td>✅ Chapter number inside book</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="containedclause.md#readme">containedclause</A></td>
  <td><code>string</code></td>
  <td>🆗 Contained clause (WG number)</td>
  <td>`<code></code>2`</td>
</tr>
<tr>
  <td><A HREF="degree.md#readme">degree</A></td>
  <td><code>string</code></td>
  <td>✅ Degree (e.g. Comparitative, Superlative)</td>
  <td>`<code></code>comparative`</td>
</tr>
<tr>
  <td><A HREF="gloss.md#readme">gloss</A></td>
  <td><code>string</code></td>
  <td>✅ English gloss</td>
  <td><code>the</code> <code>and</code></td>
</tr>
<tr>
  <td><A HREF="gn.md#readme">gn</A></td>
  <td><code>string</code></td>
  <td>✅ Gramatical gender (Masculine, Feminine, Neuter)</td>
  <td>`<code></code>masculine`</td>
</tr>
<tr>
  <td><A HREF="lemma.md#readme">lemma</A></td>
  <td><code>string</code></td>
  <td>✅ Lexeme (lemma)</td>
  <td><code>ὁ</code> <code>καί</code></td>
</tr>
<tr>
  <td><A HREF="lex_dom.md#readme">lex_dom</A></td>
  <td><code>string</code></td>
  <td>✅ Lexical domain according to Semantic Dictionary of Biblical Greek, SDBG (not present everywhere?)</td>
  <td><code>092004</code> ``</td>
</tr>
<tr>
  <td><A HREF="ln.md#readme">ln</A></td>
  <td><code>string</code></td>
  <td>✅ Lauw-Nida lexical classification (not present everywhere?)</td>
  <td><code>92.24</code> ``</td>
</tr>
<tr>
  <td><A HREF="markafter.md#readme">markafter</A></td>
  <td><code>string</code></td>
  <td>🆗 Text critical marker after word</td>
  <td>`<code></code>—`</td>
</tr>
<tr>
  <td><A HREF="markbefore.md#readme">markbefore</A></td>
  <td><code>string</code></td>
  <td>🆗 Text critical marker before word</td>
  <td>`<code></code>—`</td>
</tr>
<tr>
  <td><A HREF="markorder.md#readme">markorder</A></td>
  <td><code>string</code></td>
  <td>Order of punctuation and text critical marker</td>
  <td>`<code></code>0`</td>
</tr>
<tr>
  <td><A HREF="monad.md#readme">monad</A></td>
  <td><code>integer</code></td>
  <td>✅ Monad (smallest token matching word order in the corpus)</td>
  <td><code>1</code> <code>2</code></td>
</tr>
<tr>
  <td><A HREF="mood.md#readme">mood</A></td>
  <td><code>string</code></td>
  <td>✅ Gramatical mood of the verb (passive, etc)</td>
  <td>`<code></code>indicative`</td>
</tr>
<tr>
  <td><A HREF="morph.md#readme">morph</A></td>
  <td><code>string</code></td>
  <td>✅ Morphological tag (Sandborg-Petersen morphology)</td>
  <td><code>CONJ</code> <code>PREP</code></td>
</tr>
<tr>
  <td><A HREF="nodeID.md#readme">nodeID</A></td>
  <td><code>string</code></td>
  <td>✅ Node ID (as in the XML source data)</td>
  <td>`<code></code>common`</td>
</tr>
<tr>
  <td><A HREF="normalized.md#readme">normalized</A></td>
  <td><code>string</code></td>
  <td>✅ Surface word with accents normalized and trailing punctuations removed</td>
  <td><code>καί</code> <code>ὁ</code></td>
</tr>
<tr>
  <td><A HREF="nu.md#readme">nu</A></td>
  <td><code>string</code></td>
  <td>✅ Gramatical number (Singular, Plural)</td>
  <td><code>singular</code> ``</td>
</tr>
<tr>
  <td><A HREF="number.md#readme">number</A></td>
  <td><code>string</code></td>
  <td>✅ Gramatical number of the verb (e.g. singular, plural)</td>
  <td><code>singular</code> ``</td>
</tr>
<tr>
  <td><A HREF="otype.md#readme">otype</A></td>
  <td><code>string</code></td>
  <td>No feature description</td>
  <td><code>singular</code> ``</td>
</tr>
<tr>
  <td><A HREF="person.md#readme">person</A></td>
  <td><code>string</code></td>
  <td>✅ Gramatical person of the verb (first, second, third)</td>
  <td>`<code></code>third`</td>
</tr>
<tr>
  <td><A HREF="punctuation.md#readme">punctuation</A></td>
  <td><code>string</code></td>
  <td>✅ Punctuation after word</td>
  <td>`<code></code>,`</td>
</tr>
<tr>
  <td><A HREF="ref.md#readme">ref</A></td>
  <td><code>string</code></td>
  <td>✅ Value of the ref ID (taken from XML sourcedata)</td>
  <td><code>1CO 10:1!1</code> <code>1CO 10:1!10</code></td>
</tr>
<tr>
  <td><A HREF="reference.md#readme">reference</A></td>
  <td><code>string</code></td>
  <td>✅ Reference (to nodeID in XML source data, not yet post-processes)</td>
  <td><code>1CO 10:1!1</code> <code>1CO 10:1!10</code></td>
</tr>
<tr>
  <td><A HREF="roleclausedistance.md#readme">roleclausedistance</A></td>
  <td><code>string</code></td>
  <td>⚠️ Distance to the wordgroup defining the syntactical role of this word</td>
  <td><code>0</code> <code>1</code></td>
</tr>
<tr>
  <td><A HREF="sentence.md#readme">sentence</A></td>
  <td><code>integer</code></td>
  <td>✅ Sentence number (counted per chapter)</td>
  <td><code>3</code> <code>4</code></td>
</tr>
<tr>
  <td><A HREF="sp.md#readme">sp</A></td>
  <td><code>string</code></td>
  <td>✅ Part of Speech (abbreviated)</td>
  <td><code>noun</code> <code>verb</code></td>
</tr>
<tr>
  <td><A HREF="sp_full.md#readme">sp_full</A></td>
  <td><code>string</code></td>
  <td>✅ Part of Speech (long description)</td>
  <td><code>Noun</code> <code>Verb</code></td>
</tr>
<tr>
  <td><A HREF="strongs.md#readme">strongs</A></td>
  <td><code>string</code></td>
  <td>✅ Strongs number</td>
  <td><code>3588</code> <code>2532</code></td>
</tr>
<tr>
  <td><A HREF="subj_ref.md#readme">subj_ref</A></td>
  <td><code>string</code></td>
  <td>🆗 Subject reference (to nodeID in XML source data, not yet post-processes)</td>
  <td>`<code></code>n46003022002`</td>
</tr>
<tr>
  <td><A HREF="tense.md#readme">tense</A></td>
  <td><code>string</code></td>
  <td>✅ Gramatical tense of the verb (e.g. Present, Aorist)</td>
  <td>`<code></code>aorist`</td>
</tr>
<tr>
  <td><A HREF="type.md#readme">type</A></td>
  <td><code>string</code></td>
  <td>✅ Gramatical type  of noun or pronoun (e.g. Common, Personal)</td>
  <td>`<code></code>common`</td>
</tr>
<tr>
  <td><A HREF="unicode.md#readme">unicode</A></td>
  <td><code>string</code></td>
  <td>✅ Word as it apears in the text in Unicode (incl. punctuations)</td>
  <td><code>καὶ</code> <code>ὁ</code></td>
</tr>
<tr>
  <td><A HREF="verse.md#readme">verse</A></td>
  <td><code>integer</code></td>
  <td>✅ Verse number inside chapter</td>
  <td><code>10</code> <code>12</code></td>
</tr>
<tr>
  <td><A HREF="voice.md#readme">voice</A></td>
  <td><code>string</code></td>
  <td>✅ Gramatical voice of the verb (e.g. active,passive)</td>
  <td>`<code></code>active`</td>
</tr>
<tr>
  <td><A HREF="word.md#readme">word</A></td>
  <td><code>string</code></td>
  <td>✅ Word as it appears in the text (excl. punctuations)</td>
  <td><code>καὶ</code> <code>ὁ</code></td>
</tr>
<tr>
  <td><A HREF="wordlevel.md#readme">wordlevel</A></td>
  <td><code>string</code></td>
  <td>🆗 Number of the parent wordgroups for a word</td>
  <td><code>6</code> <code>7</code></td>
</tr>
<tr>
  <td><A HREF="wordrole.md#readme">wordrole</A></td>
  <td><code>string</code></td>
  <td>✅ Syntactical role of the word (abbreviated)</td>
  <td><code>adv</code> <code>v</code></td>
</tr>
<tr>
  <td><A HREF="wordrolelong.md#readme">wordrolelong</A></td>
  <td><code>string</code></td>
  <td>✅ Syntactical role of the word (full)</td>
  <td><code>Adverbial</code> <code>Verbal</code></td>
</tr>
<tr>
  <td><A HREF="wordtranslit.md#readme">wordtranslit</A></td>
  <td><code>string</code></td>
  <td>🆗 Transliteration of the text (in latin letters, excl. punctuations)</td>
  <td><code>kai</code> <code>en</code></td>
</tr>
<tr>
  <td><A HREF="wordunacc.md#readme">wordunacc</A></td>
  <td><code>string</code></td>
  <td>✅ Word without accents (excl. punctuations)</td>
  <td><code>και</code> <code>ο</code></td>
</tr>
</tbody>
</table>
