import os
from tf.convert.xml import XML


TEST_SET = set(
    """
    26-jude.xml
    """.strip().split()
)

AUTHOR = "Evangelists and apostles"
TITLE = "Greek New Testament"
INSTITUTE = "ETCBC (Eep Talstra Centre for Bible and Computer)"

GENERIC = dict(
    author=AUTHOR,
    title=TITLE,
    institute=INSTITUTE,
    language="nl",
    converters="Dirk Roorda et al. (Text-Fabric)",
    sourceFormat="XML (lowfat)",
    descriptionTf="Nestle 1904 edition",
)


def transform(text):
    return text


X = XML(
    sourceVersion="",
    testSet=TEST_SET,
    generic=GENERIC,
    transform=transform,
    tfVersion="0.1",
)

X.run(os.path.basename(__file__))
