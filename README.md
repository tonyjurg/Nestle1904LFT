[![Project Status: Abandoned – Initial development has started, but there has not yet been a stable, usable release; the project has been abandoned and the author(s) do not intend on continuing development.](https://www.repostatus.org/badges/latest/abandoned.svg)](https://www.repostatus.org/#abandoned) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10182594.svg)](https://doi.org/10.5281/zenodo.10182594) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)


# Text-Fabric Nestle 1904 Greek New Testament (based on LowFat XML node)

<div class="box" style="border: 1px solid #333;">
<b>Important:</b> This Text-Fabric version has been superseded by the functionaly enhanced <A HREF="https://centerblc.github.io/N1904/">N1904‑TF</A> dataset. This repository is archived as a reference implementation.
</div>

## Quick starters
* [Install, load and use Text-Fabric in Jupyter Notebook](https://nbviewer.org/github/tonyjurg/Nestle1904LFT/blob/main/docs/usecases/load_text_fabric.ipynb)
* [Read about Text-Fabric, the project, this dataset, and the features](https://tonyjurg.github.io/Nestle1904LFT/)
* [Understand the conversion process](https://nbviewer.org/github/tonyjurg/Nestle1904LFT/tree/main/resources/converter/).

## Repository overview

This repository contains (a copy of) the sourcedata, conversion tools and final dataset of a Text-Fabric implementation of the Nestle 1904 Greek New Testament (based on LowFat XML node).

The source data for the conversion are the XML LowFat files representing the macula-greek version of Eberhard Nestle's 1904 Greek New Testament (British Foreign Bible Society 1904, 7th edition 1913). The starting dataset is formatted according to Syntax diagram markupinitially prepared by the Asia Bible Society and currently made available by [Biblica, Inc](https://www.biblica.com/). The most recent source data can be found on [GitHub](https://github.com/Clear-Bible/macula-greek/tree/main/Nestle1904/lowfat).

The following directories contain the actual (base) Text-Fabric featureset:
 * [app](app#readme): app config data.
 * [tf](tf/#readme): the actual dataset (each version in separate folder).
 * [doc](docs/home.md#readme): the documentation for the dataset.

Additional (optional) Text-Fabric featureset:
 * [BOL](add_features/BOL): Bible Online Learner additonal featureset
 
Additionaly provided:
 * [resources](resources#readme): production tools and related data files.
 * [usecases](docs/usecases#readme): examples of using this Text-Fabric dataset.

## Sources
 
See [here](https://archive.org/details/the-greek-new-testament-nestle-1904-us-edition/mode/2up) a scan of the orginal publication: Nestle, Eberhard. Η Καινή Διαθήκη Novum Testamentum Graece (New York: Fleming H. Revell Company, 1904). The 1913 reprint is available [here](https://archive.org/details/hkainediathekete00lond/).
 
Attribution: "MACULA Greek Linguistic Datasets, available at [github.com/Clear-Bible/macula-greek](https://github.com/Clear-Bible/macula-greek)". See [here](docs/legal.md#readme) for licence of the source data.
