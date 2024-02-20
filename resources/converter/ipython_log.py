# IPython log file

import pandas as pd
import sys                       # System
import os                        # Operating System
from os import listdir
from os.path import isfile, join
import time
import pickle
import re                        # Regular Expressions
from lxml import etree as ET
from tf.fabric import Fabric
from tf.convert.walker import CV
from tf.parameters import VERSION
from datetime import date
import pickle
import unicodedata
from unidecode import unidecode
import openpyxl
# set script version number
scriptVersion='0.7'
scriptDate='February 20, 2024'

# Define the source and destination locations 
BaseDir = '..\\'
XmlDir = BaseDir+'xml\\20240210\\'
PklDir = BaseDir+'pickle\\20240210\\'
XlsxDir = BaseDir+'excel\\20240210\\'
CsvDir = BaseDir+'csv\\20240210\\'
# note: create output directory prior running the scripts!

#         key: filename,       [0]=bookLong,   [1]=bookNum,  [3]=bookShort
bo2book = {'01-matthew':       ['Matthew',         '1',        'Matt'],
           '02-mark':          ['Mark',            '2',        'Mark'],
           '03-luke':          ['Luke',            '3',        'Luke'],
           '04-john':          ['John',            '4',        'John'],
           '05-acts':          ['Acts',            '5',        'Acts'],
           '06-romans':        ['Romans',          '6',        'Rom'],
           '07-1corinthians':  ['I_Corinthians',   '7',        '1Cor'],
           '08-2corinthians':  ['II_Corinthians',  '8',        '2Cor'],
           '09-galatians':     ['Galatians',       '9',        'Gal'],
           '10-ephesians':     ['Ephesians',       '10',       'Eph'],
           '11-philippians':   ['Philippians',     '11',       'Phil'],
           '12-colossians':    ['Colossians',      '12',       'Col'],
           '13-1thessalonians':['I_Thessalonians', '13',       '1Thess'],
           '14-2thessalonians':['II_Thessalonians','14',       '2Thess'],
           '15-1timothy':      ['I_Timothy',       '15',       '1Tim'],
           '16-2timothy':      ['II_Timothy',      '16',       '2Tim'],
           '17-titus':         ['Titus',           '17',       'Titus'],
           '18-philemon':      ['Philemon',        '18',       'Phlm'],
           '19-hebrews':       ['Hebrews',         '19',       'Heb'],
           '20-james':         ['James',           '20',       'Jas'],
           '21-1peter':        ['I_Peter',         '21',       '1Pet'],
           '22-2peter':        ['II_Peter',        '22',       '2Pet'],
           '23-1john':         ['I_John',          '23',       '1John'],
           '24-2john':         ['II_John',         '24',       '2John'],
           '25-3john':         ['III_John',        '25',       '3John'],     
           '26-jude':          ['Jude',            '26',       'Jude'],
           '27-revelation':    ['Revelation',      '27',       'Rev']}
# Load specific set of variables for the walker

from tf.fabric import Fabric
from tf.convert.walker import CV

# setting some TF specific variables
BASE = os.path.expanduser('~/github')
ORG = 'tonyjurg'
REPO = 'Nestle1904LFT'
RELATIVE = 'tf'
TF_DIR = os.path.expanduser(f'{BASE}//{ORG}//{REPO}//{RELATIVE}')
VERSION = f'{scriptVersion}'
TF_PATH = f'{TF_DIR}//{VERSION}'
TF = Fabric(locations=TF_PATH, silent=False)
cv = CV(TF)
###############################################
#   Common helper functions                   #
###############################################

def sanitize(input):
    """
    Sanitizes the input data to handle missing or undefined values.

    This function is used to ensure that float values and None types are converted to empty strings.
    Other data types are returned as-is. This is particularly useful in data processing and conversion
    tasks where missing data needs to be handled gracefully.

    Parameters:
      input: The data input which can be of any type.

    Returns:
      str: An empty string if the input is a float or None, otherwise returns the input as-is.
    """
    if isinstance(input, float) or isinstance(input, type(None)):
        return ''
    else:
        return input


def ExpandRole(input):
    """
    Expands syntactic role abbreviations into their full descriptive names.

    This function is particularly useful in parsing and interpreting syntactic structures, especially
    in the context of language processing. The expansion is based on the syntactic categories at the clause
    level as described in "MACULA Greek Treebank for the Nestle 1904 Greek New Testament" (page 5 & 6, section 2.4).

    Parameters:
      input (str): Abbreviated syntactic role label.

    Returns:
      str: The expanded, full descriptive name of the syntactic role. Returns an empty string for unrecognized inputs.
    """
    roleExpansions = {
        "adv": 'Adverbial',
        "io":  'Indirect Object',
        "o":   'Object',
        "o2":  'Second Object',
        "s":   'Subject',
        "p":   'Predicate',
        "v":   'Verbal',
        "vc":  'Verbal Copula',
        "aux": 'Auxiliar'
    }
    return roleExpansions.get(input, '')

def ExpandSP(input):
    """
    Expands Part of Speech (POS) label abbreviations into their full descriptive names.

    This function is utilized for enriching text data with clear, descriptive POS labels.
    The expansions are based on the syntactic categories at the word level as described in 
    "MACULA Greek Treebank for the Nestle 1904 Greek New Testament" (page 6 & 7, section 2.2).

    Parameters:
      input (str): Abbreviated POS label.

    Returns:
      str: The expanded, full descriptive name of the POS label. Returns an empty string for unrecognized inputs.
    """
    posExpansions = {
        'adj':  'Adjective',
        'conj': 'Conjunction',
        'det':  'Determiner',
        'intj': 'Interjection',
        'noun': 'Noun',
        'num':  'Numeral',
        'prep': 'Preposition',
        'ptcl': 'Particle',
        'pron': 'Pronoun',
        'verb': 'Verb'
    }
    return posExpansions.get(input, '')



def removeAccents(text):
    """
    Removes diacritical marks (accents) from Greek words or any text.

    This function is particularly useful in text processing where diacritical marks need to be
    removed, such as in search functionality, normalization, or comparison of strings. It leverages
    Unicode normalization to decompose characters into their base characters and diacritics, and then
    filters out the diacritics.

    Note: This function can be applied to any text where Unicode normalization is applicable.

    Parameters:
      text (str): The text from which accents/diacritical marks need to be removed.

    Returns:
      str: The input text with all diacritical marks removed.
    """
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

###############################################
#          The director routine               #
###############################################

def director(cv):
    
    ###############################################
    #   Innitial setup of data etc.               #
    ###############################################
    NoneType = type(None)      # needed as tool to validate certain data
    IndexDict = {}             # init an empty dictionary
    WordGroupDict={}           # init a dummy dictionary
    PrevWordGroupSet = WordGroupSet = []
    PrevWordGroupList = WordGroupList = []
    RootWordGroup = 0
    WordNumber=FoundWords=WordGroupTrack=0
    # The following is required to recover succesfully from an abnormal condition
    # in the LowFat tree data where a <wg> element is labeled as <error>
    # this number is arbitrary but should be high enough not to clash with 'real' WG numbers
    DummyWGN=200000  # first dummy WG number
    
    # Following variables are used for textual critical data 
    criticalMarkCharacters = "[]()—"
    punctuationCharacters = ",.;·"
    translationTableMarkers = str.maketrans("", "", criticalMarkCharacters)
    translationTablePunctuations = str.maketrans("", "", punctuationCharacters)
    punctuations=('.',',',';','·')
    
    for bo,bookinfo in bo2book.items(): 
        
        ###############################################
        #   start of section executed for each book   #
        ###############################################
        
        # note: bookinfo is a list! Split the data
        Book        = bookinfo[0]  
        BookNumber  = int(bookinfo[1])
        BookShort   = bookinfo[2]
        BookLoc     = os.path.join(PklDir, f'{bo}.pkl') 
        
        # load  data for this book into a dataframe. 
        # make sure wordorder is correct
        print(f'\tWe are loading {BookLoc}...')
        pkl_file = open(BookLoc, 'rb')
        df_unsorted = pickle.load(pkl_file)
        pkl_file.close()
        
        '''
        Fill dictionary of column names for this book 
        sort to ensure proper wordorder
        '''
        ItemsInRow=1
        for itemName in df_unsorted.columns.to_list():
            IndexDict.update({'i_{}'.format(itemName): ItemsInRow})
            # This is to identify the collumn containing the key to sort upon
            if itemName=="id": SortKey=ItemsInRow-1
            ItemsInRow+=1
        
        df=df_unsorted.sort_values(by=df_unsorted.columns[SortKey])
        del df_unsorted

        # Set up nodes for new book
        ThisBookPointer = cv.node('book')
        cv.feature(ThisBookPointer, book=Book, booknumber=BookNumber, bookshort=BookShort)
        
        ThisChapterPointer = cv.node('chapter')
        cv.feature(ThisChapterPointer, chapter=1, book=Book)
        PreviousChapter=1
        
        ThisVersePointer = cv.node('verse')
        cv.feature(ThisVersePointer, verse=1, chapter=1, book=Book)
        PreviousVerse=1
        
        ThisSentencePointer = cv.node('sentence')
        cv.feature(ThisSentencePointer, sentence=1, headverse=1, chapter=1, book=Book)
        PreviousSentence=1

        ###############################################
        # Iterate through words and construct objects #
        ###############################################
        
        for row in df.itertuples():
            WordNumber += 1
            FoundWords +=1
                       
            # Detect and act upon changes in sentences, verse and chapter 
            # the order of terminating and creating the nodes is critical: 
            # close verse - close chapter - open chapter - open verse 
            NumberOfParents = sanitize(row[IndexDict.get("i_parents")])
            ThisSentence=int(row[IndexDict.get("i_Parent{}SN".format(NumberOfParents-1))])
            ThisVerse = sanitize(row[IndexDict.get("i_verse")])
            ThisChapter = sanitize(row[IndexDict.get("i_chapter")])
            
            if (ThisVerse!=PreviousVerse):
                cv.terminate(ThisVersePointer)
            
            if (ThisSentence!=PreviousSentence):
                cv.terminate(ThisSentencePointer)
                             
    
            if (ThisChapter!=PreviousChapter):
                cv.terminate(ThisChapterPointer)
                PreviousChapter = ThisChapter
                ThisChapterPointer = cv.node('chapter')
                cv.feature(ThisChapterPointer, chapter=ThisChapter, book=Book)
                
            if (ThisVerse!=PreviousVerse):
                PreviousVerse = ThisVerse  
                ThisVersePointer = cv.node('verse')
                cv.feature(ThisVersePointer, verse=ThisVerse, chapter=ThisChapter, book=Book)
                
            if (ThisSentence!=PreviousSentence):
                PreviousSentence=ThisSentence
                ThisSentencePointer = cv.node('sentence')
                cv.feature(ThisSentencePointer, sentence=ThisSentence, headverse=ThisVerse, chapter=ThisChapter, book=Book)       
        
            ###############################################
            #         analyze and process <WG> tags       #
            ###############################################
                    
            PrevWordGroupList=WordGroupList
            WordGroupList=[]  # stores current active WordGroup numbers
            
            for i in range(NumberOfParents-2,0,-1): # important: reversed itteration!
                
                _WGN=int(row[IndexDict.get("i_Parent{}WGN".format(i))])                             
                if _WGN!='':
                     WGN=int(_WGN)
                if WGN!='':
                     WGclass=sanitize(row[IndexDict.get("i_Parent{}Class".format(i))])
                     WGrule=sanitize(row[IndexDict.get("i_Parent{}Rule".format(i))])
                     WGtype=sanitize(row[IndexDict.get("i_Parent{}Type".format(i))])
                     if WGclass==WGrule==WGtype=='':
                         WGclass='empty'
                     else:
                         #print ('---',WordGroupList)
                         if WGN not in WordGroupList:
                             WordGroupList.append(WGN) 
                             #print(f'append WGN={WGN}')
                         WordGroupDict[(WGN,0)]=WGN
                         if WGrule[-2:]=='CL' and WGclass=='':  
                             WGclass='cl*'  # to simulate the way Logos presents this condition
                         WordGroupDict[(WGN,6)]=WGclass
                         WordGroupDict[(WGN,1)]=WGrule
                         WordGroupDict[(WGN,8)]=WGtype
                         WordGroupDict[(WGN,3)]=sanitize(row[IndexDict.get("i_Parent{}Junction".format(i))])
                         WordGroupDict[(WGN,2)]=sanitize(row[IndexDict.get("i_Parent{}Cltype".format(i))])
                         WordGroupDict[(WGN,7)]=sanitize(row[IndexDict.get("i_Parent{}Role".format(i))])
                         WordGroupDict[(WGN,9)]=sanitize(row[IndexDict.get("i_Parent{}Appos".format(i))])  # appos is not pressent any more in the newer dataset. kept here for the time being...
                         WordGroupDict[(WGN,10)]=NumberOfParents-1-i  # = number of parent wordgroups     
            if not PrevWordGroupList==WordGroupList:
                #print ('##',PrevWordGroupList,WordGroupList,NumberOfParents)
                if RootWordGroup != WordGroupList[0]:
                    RootWordGroup = WordGroupList[0]
                    SuspendableWordGoupList = []
                    # we have a new sentence. rebuild suspendable wordgroup list
                    # some cleaning of data may be added here to save on memmory... 
                    #for k in range(6): del WordGroupDict[item,k]
                for item in reversed(PrevWordGroupList):
                   if (item not in WordGroupList):
                         # CLOSE/SUSPEND CASE
                         SuspendableWordGoupList.append(item)
                         #print ('\n close: '+str(WordGroupDict[(item,0)])+' '+ WordGroupDict[(item,6)]+' '+ WordGroupDict[(item,1)]+' '+WordGroupDict[(item,8)],end=' ')                     
                         cv.terminate(WordGroupDict[(item,4)])
                for item in WordGroupList:
                    if (item not in PrevWordGroupList):
                         if (item in SuspendableWordGoupList):
                              # RESUME CASE
                              #print ('\n resume: '+str(WordGroupDict[(item,0)])+' '+ WordGroupDict[(item,6)]+' '+WordGroupDict[(item,1)]+' '+WordGroupDict[(item,8)],end=' ') 
                              cv.resume(WordGroupDict[(item,4)])
                         else:
                              # CREATE CASE
                              #print ('\n create: '+str(WordGroupDict[(item,0)])+' '+ WordGroupDict[(item,6)]+' '+ WordGroupDict[(item,1)]+' '+WordGroupDict[(item,8)],end=' ')
                              WordGroupDict[(item,4)]=cv.node('wg')
                              WordGroupDict[(item,5)]=WordGroupTrack
                              WordGroupTrack += 1
                              cv.feature(WordGroupDict[(item,4)], wgnum=WordGroupDict[(item,0)], junction=WordGroupDict[(item,3)], 
                                         clausetype=WordGroupDict[(item,2)], wgrule=WordGroupDict[(item,1)], wgclass=WordGroupDict[(item,6)], 
                                         wgrole=WordGroupDict[(item,7)],wgrolelong=ExpandRole(WordGroupDict[(item,7)]),
                                         wgtype=WordGroupDict[(item,8)],wglevel=WordGroupDict[(item,10)])
     
            # These roles are performed either by a WG or just a single word.
            Role=row[IndexDict.get("i_role")]
            ValidRoles=["adv","io","o","o2","s","p","v","vc","aux"]
            DistanceToRoleClause=0
            if isinstance (Role,str) and Role in ValidRoles: 
                # Role is assign to this word (uniqely)
                WordRole=Role
                WordRoleLong=ExpandRole(WordRole)
            else:
                # Role details needs to be taken from some uptree wordgroup 
                WordRole=WordRoleLong=''
                for item in range(1,NumberOfParents-1):
                    Role = sanitize(row[IndexDict.get("i_Parent{}Role".format(item))])
                    if isinstance (Role,str) and Role in ValidRoles: 
                        WordRole=Role        
                        WordRoleLong=ExpandRole(WordRole)
                        DistanceToRoleClause=item
                        break
                        
            # Find the number of the WG containing the clause definition
            for item in range(1,NumberOfParents-1):
                WGrule = sanitize(row[IndexDict.get("i_Parent{}Rule".format(item))])
                if row[IndexDict.get("i_Parent{}Class".format(item))]=='cl' or WGrule[-2:]=='CL':  
                    ContainedClause=sanitize(row[IndexDict.get("i_Parent{}WGN".format(item))])
                    break

            ###############################################
            #         analyze and process <W> tags        #
            ###############################################
                
            # Determine syntactic categories at word level. 
            PartOfSpeech=sanitize(row[IndexDict.get("i_class")])
            PartOfSpeechFull=ExpandSP(PartOfSpeech)
            
            # The folling part of code reproduces feature 'word' and 'after' that are
            # currently containing incorrect data in a few specific cases.
            # See https://github.com/tonyjurg/Nestle1904LFT/blob/main/resources/identifying_odd_afters.ipynb
            # Get the word details and detect presence of punctuations
            # it also creates the textual critical features

            rawWord=sanitize(row[IndexDict.get("i_unicode")])
            cleanWord= rawWord.translate(translationTableMarkers)
            rawWithoutPunctuations=rawWord.translate(translationTablePunctuations)
            markBefore=markAfter=PunctuationMarkOrder=''
            if cleanWord[-1] in punctuations:
                punctuation=cleanWord[-1]
                after=punctuation+' '
                word=cleanWord[:-1]
            else:
                after=' '
                word=cleanWord
                punctuation=''
            if rawWithoutPunctuations!=word:
                markAfter=markBefore=''
                if rawWord.find(word)==0:
                    markAfter=rawWithoutPunctuations.replace(word,"")
                    if punctuation!='':
                        if rawWord.find(markAfter)-rawWord.find(punctuation)>0:
                            PunctuationMarkOrder="3" # punct. before mark
                        else:
                            PunctuationMarkOrder="2" # punct. after mark.
                    else:
                        PunctuationMarkOrder="1" #no punctuation, mark after word
                else:
                    markBefore=rawWithoutPunctuations.replace(word,"")
                    PunctuationMarkOrder="0" #mark is before word
                    
            # Some attributes are not present inside some (small) books. The following is to prevent exceptions.
            degree='' 
            if 'i_degree'  in IndexDict: 
                degree=sanitize(row[IndexDict.get("i_degree")]) 
            subjref=''
            if 'i_subjref' in IndexDict: 
                subjref=sanitize(row[IndexDict.get("i_subjref")]) 

                    
            # Create the word slots
            this_word = cv.slot()
            cv.feature(this_word, 
                    after=         after,
                    unicode=       rawWord,
                    word=          word,
                    wordtranslit=  unidecode(word),
                    wordunacc=     removeAccents(word),
                    punctuation=   punctuation,
                    markafter=     markAfter,
                    markbefore=    markBefore,
                    markorder=     PunctuationMarkOrder,
                    monad=         FoundWords,
                    orig_order=    sanitize(row[IndexDict.get("i_wordOrder")]),
                    book=          Book,
                    booknumber=    BookNumber,
                    bookshort=     BookShort,
                    chapter=       ThisChapter,
                    ref=           sanitize(row[IndexDict.get("i_ref")]),
                    sp=            PartOfSpeech,
                    sp_full=       PartOfSpeechFull,
                    verse=         ThisVerse,
                    sentence=      ThisSentence,
                    normalized=    sanitize(row[IndexDict.get("i_normalized")]),
                    morph=         sanitize(row[IndexDict.get("i_morph")]),
                    strongs=       sanitize(row[IndexDict.get("i_strong")]),
                    lex_dom=       sanitize(row[IndexDict.get("i_domain")]),
                    ln=            sanitize(row[IndexDict.get("i_ln")]),
                    gloss=         sanitize(row[IndexDict.get("i_gloss")]),
                    gn=            sanitize(row[IndexDict.get("i_gender")]),
                    nu=            sanitize(row[IndexDict.get("i_number")]),
                    case=          sanitize(row[IndexDict.get("i_case")]),
                    lemma=         sanitize(row[IndexDict.get("i_lemma")]),
                    person=        sanitize(row[IndexDict.get("i_person")]),
                    mood=          sanitize(row[IndexDict.get("i_mood")]),
                    tense=         sanitize(row[IndexDict.get("i_tense")]),
                    number=        sanitize(row[IndexDict.get("i_number")]),
                    voice=         sanitize(row[IndexDict.get("i_voice")]),
                    degree=        degree,
                    type=          sanitize(row[IndexDict.get("i_type")]),
                    reference=     sanitize(row[IndexDict.get("i_ref")]),     
                    subj_ref=      subjref,
                    nodeID=        sanitize(row[IndexDict.get("i_id")]),
                    wordrole=      WordRole,
                    wordrolelong=  WordRoleLong,
                    wordlevel=     NumberOfParents-1,
                    roleclausedistance = DistanceToRoleClause,
                    containedclause = ContainedClause
                    )
            cv.terminate(this_word)   
   
        
        '''
        wrap up the book. At the end of the book we need to close all nodes in proper order.
        '''   
        # close all open WordGroup nodes
        for item in WordGroupList:
            #cv.feature(WordGroupDict[(item,4)], add some stats?)
            cv.terminate(WordGroupDict[item,4])

        cv.terminate(ThisSentencePointer)
        cv.terminate(ThisVersePointer)
        cv.terminate(ThisChapterPointer)      
        cv.terminate(ThisBookPointer)

        # clear dataframe for this book, clear the index dictionary
        del df
        IndexDict.clear()
        #gc.collect()
        
        ###############################################
        #    end of section executed for each book    #
        ###############################################

    ###############################################
    #      end of director function               #
    ###############################################
        
###############################################
#            Output definitions               #
###############################################

# define TF dataset granularity
slotType = 'word'  

# dictionary of config data for sections and text formats
otext = { 
        'fmt:text-orig-full':     '{word}{after}',
        'fmt:text-normalized':    '{normalized}{after}',
        'fmt:text-unaccented':    '{wordunacc}{after}',
        'fmt:text-transliterated':'{wordtranslit}{after}', 
        'fmt:text-critical':      '{unicode} ',
        'sectionTypes':'book,chapter,verse',
        'sectionFeatures':'book,chapter,verse',
        'structureFeatures': 'book,chapter,verse',
        'structureTypes': 'book,chapter,verse',
        }

# configure provenance metadata
generic = {  # dictionary of metadata meant for all features
        'textFabricVersion': '{}'.format(VERSION),  #imported from tf.parameter
        'xmlSourceLocation': 'https://github.com/tonyjurg/Nestle1904LFT/tree/main/resources/xml/20240210',
        'xmlSourceDate': 'February 10, 2024',
        'author': 'Evangelists and apostles',
        'availability': 'Creative Commons Attribution 4.0 International (CC BY 4.0)',
        'converters': 'Tony Jurg',
        'converterSource': 'https://github.com/tonyjurg/Nestle1904LFT/tree/main/resources/converter',
        'converterVersion': '{} ({})'.format(scriptVersion,scriptDate),
        'dataSource': 'MACULA Greek Linguistic Datasets, available at https://github.com/Clear-Bible/macula-greek/tree/main/Nestle1904/nodes',
        'editors': 'Eberhart Nestle (1904)',
        'sourceDescription': 'Greek New Testment (British Foreign Bible Society, 1904)',
        'sourceFormat': 'XML (Low Fat tree XML data)',
        'title': 'Greek New Testament (Nestle1904LFT)'
         }

# set datatype of feature (if not listed here, they are ususaly strings)
intFeatures = {  
         'booknumber',
         'chapter',
         'verse',
         'sentence',
         'wgnum',
         'orig_order',
         'monad',
         'wglevel'
         }

# per feature dicts with metadata
# icon provides guidance on feature maturity (✅ = trustworthy, 🆗  = usable, ⚠️ = be carefull when using)
featureMeta = {  
                 'after':       {'description': '✅ Characters (eg. punctuations) following the word'},
                 'book':        {'description': '✅ Book name (in English language)'},
                 'booknumber':  {'description': '✅ NT book number (Matthew=1, Mark=2, ..., Revelation=27)'},
                 'bookshort':   {'description': '✅ Book name (abbreviated)'},
                 'chapter':     {'description': '✅ Chapter number inside book'},
                 'verse':       {'description': '✅ Verse number inside chapter'},
                 'headverse':   {'description': '✅ Start verse number of a sentence'},
                 'sentence':    {'description': '✅ Sentence number (counted per chapter)'},
                 'type':        {'description': '✅ Wordgroup type information (e.g.verb, verbless, elided, minor)'},
                 'wgrule':      {'description': '✅ Wordgroup rule information (e.g. Np-Appos, ClCl2, PrepNp)'},
                 'orig_order':  {'description': '✅ Word order (in source XML file)'},
                 'monad':       {'description': '✅ Monad (smallest token matching word order in the corpus)'},
                 'word':        {'description': '✅ Word as it appears in the text (excl. punctuations)'},
                 'wordtranslit':{'description': '🆗 Transliteration of the text (in latin letters, excl. punctuations)'},
                 'wordunacc':   {'description': '✅ Word without accents (excl. punctuations)'},
                 'unicode':     {'description': '✅ Word as it apears in the text in Unicode (incl. punctuations)'},
                 'punctuation': {'description': '✅ Punctuation after word'},
                 'markafter':   {'description': '🆗 Text critical marker after word'},
                 'markbefore':  {'description': '🆗 Text critical marker before word'},
                 'markorder':   {'description': ' Order of punctuation and text critical marker'},
                 'ref':         {'description': '✅ Value of the ref ID (taken from XML sourcedata)'},
                 'sp':          {'description': '✅ Part of Speech (abbreviated)'},
                 'sp_full':     {'description': '✅ Part of Speech (long description)'}, 
                 'normalized':  {'description': '✅ Surface word with accents normalized and trailing punctuations removed'},
                 'lemma':       {'description': '✅ Lexeme (lemma)'},
                 'morph':       {'description': '✅ Morphological tag (Sandborg-Petersen morphology)'},
                                 # see also discussion on relation between lex_dom and ln 
                                 # @ https://github.com/Clear-Bible/macula-greek/issues/29
                 'lex_dom':     {'description': '✅ Lexical domain according to Semantic Dictionary of Biblical Greek, SDBG (not present everywhere?)'},
                 'ln':          {'description': '✅ Lauw-Nida lexical classification (not present everywhere?)'},
                 'strongs':     {'description': '✅ Strongs number'},
                 'gloss':       {'description': '✅ English gloss'},
                 'gn':          {'description': '✅ Gramatical gender (Masculine, Feminine, Neuter)'},
                 'nu':          {'description': '✅ Gramatical number (Singular, Plural)'},
                 'case':        {'description': '✅ Gramatical case (Nominative, Genitive, Dative, Accusative, Vocative)'},
                 'person':      {'description': '✅ Gramatical person of the verb (first, second, third)'},
                 'mood':        {'description': '✅ Gramatical mood of the verb (passive, etc)'},
                 'tense':       {'description': '✅ Gramatical tense of the verb (e.g. Present, Aorist)'},
                 'number':      {'description': '✅ Gramatical number of the verb (e.g. singular, plural)'},
                 'voice':       {'description': '✅ Gramatical voice of the verb (e.g. active,passive)'},
                 'degree':      {'description': '✅ Degree (e.g. Comparitative, Superlative)'},
                 'type':        {'description': '✅ Gramatical type  of noun or pronoun (e.g. Common, Personal)'},
                 'reference':   {'description': '✅ Reference (to nodeID in XML source data, not yet post-processes)'},
                 'subj_ref':    {'description': '🆗 Subject reference (to nodeID in XML source data, not yet post-processes)'},
                 'nodeID':      {'description': '✅ Node ID (as in the XML source data)'},
                 'junction':    {'description': '✅ Junction data related to a wordgroup'},
                 'wgnum':       {'description': '✅ Wordgroup number (counted per book)'},
                 'wgclass':     {'description': '✅ Class of the wordgroup (e.g. cl, np, vp)'},
                 'wgrole':      {'description': '✅ Syntactical role of the wordgroup (abbreviated)'},
                 'wgrolelong':  {'description': '✅ Syntactical role of the wordgroup (full)'},
                 'wordrole':    {'description': '✅ Syntactical role of the word (abbreviated)'},
                 'wordrolelong':{'description': '✅ Syntactical role of the word (full)'},
                 'wgtype':      {'description': '✅ Wordgroup type details (e.g. group, apposition)'},
                 'clausetype':  {'description': '✅ Clause type details (e.g. Verbless, Minor)'},
                 'wglevel':     {'description': '🆗 Number of the parent wordgroups for a wordgroup'},
                 'wordlevel':   {'description': '🆗 Number of the parent wordgroups for a word'},
                 'roleclausedistance': {'description': '⚠️ Distance to the wordgroup defining the syntactical role of this word'},
                 'containedclause': {'description': '🆗 Contained clause (WG number)'}
                 }


###############################################
#            the main function                #
###############################################

good = cv.walk(
    director,
    slotType,
    otext=otext,
    generic=generic,
    intFeatures=intFeatures,
    featureMeta=featureMeta,
    warn=True,
    force=True
)

if good:
  print ("done")
# Load TF code

from tf.fabric import Fabric
from tf.app import use
# load the app and data
N1904 = use ("tonyjurg/Nestle1904LFT", version=scriptVersion, checkout="clone", hoist=globals())
with open(f'{TF_PATH}/otype.tf') as fh:
  print(fh.read())
with open(f'{TF_PATH}/otext.tf') as fh:
  print(fh.read())
# Define the repository
ORG = "tonyjurg"
REPO = "Nestle1904LFT"

# Added details for the release
MESSAGE = "New release"
DESCRIPTION = """
This release uses a new dataset. 

The main difference is in feature Strongs:
  * Some errors were corrected
  * composite words are now with two or more Strong values
  
This release has been published with the command `A.publish()`, a function in Text-Fabric.
"""
N1904.publishRelease(3, message=MESSAGE, description=DESCRIPTION)
get_ipython().run_line_magic('logstart', '')
N1904.publishRelease(3, message=MESSAGE, description=DESCRIPTION)
get_ipython().run_line_magic('logstop', '')
N1904.publishRelease(3, message=MESSAGE, description=DESCRIPTION)
get_ipython().run_line_magic('logstart', '')
N1904.publishRelease(3, message=MESSAGE, description=DESCRIPTION)
get_ipython().run_line_magic('logstop', '')
N1904.publishRelease(3, message=MESSAGE, description=DESCRIPTION)
