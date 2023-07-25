import os
import re
from tf.convert.xml import XML

# set should NOT include comma behind filename
TEST_SET = set(
    """
    24-2john.xml
	25-3john.xml
    """.strip().split()
)

AUTHOR = "Evangelists and apostles"
TITLE = "Greek New Testament"
INSTITUTE = "ETCBC (Eep Talstra Centre for Bible and Computer)"

GENERIC = dict(
    author=AUTHOR,
    title=TITLE,
    institute=INSTITUTE,
    language="el",
    converters="Tony",
    sourceFormat="XML (lowfat)",
    descriptionTf="Nestle 1904 edition",
)




def transform(text):
    #this is where we could hook in on the xml data (it seems to be the whole file at once)
	# differentiate between attribute 'id' in book node and sentence node. Replace 'id' 
	# manipulation has already done by preprossessing script
    return text


X = XML(
    sourceVersion="",
    testSet=TEST_SET,
    generic=GENERIC,
    transform=transform,
    tfVersion="0.1.1",
)

X.run(os.path.basename(__file__))
