import os
import re
basedir="/home/tjurg/github/tonyjurg/n1904_lft/" 

# set should NOT include comma behind filename
SET = set(
    """
	01-matthew.xml
	02-mark.xml
	03-luke.xml
	04-john.xml
	05-acts.xml
	06-romans.xml
	07-1corinthians.xml
	08-2corinthians.xml
	09-galatians.xml
	10-ephesians.xml
	11-philippians.xml
	12-colossians.xml
	13-1thessalonians.xml
	14-2thessalonians.xml
	15-1timothy.xml
	16-2timothy.xml
	17-titus.xml
	18-philemon.xml
	19-hebrews.xml
	20-james.xml
	21-1peter.xml
	22-2peter.xml
	23-1john.xml
	24-2john.xml
	25-3john.xml
	26-jude.xml
	27-revelation.xml
    """.strip().split()
)

bookcounter=0


for files in SET:
	inputfile=basedir+"input_raw_xml/"+files
	outputfile=basedir+"xml/input_xml/"+files
	sentencecounter=0
	bookcounter+=1
	#print ('trying to open: '+inputfile)
	#print ('output file:'+outputfile)
	try: 
		input = open(inputfile, mode="r", encoding="utf-8")
	except:
		print (inputfile,'not found')
		break
	try:
		output = open(outputfile, mode="w",  encoding="utf-8")
	except:
		print ("create file",outputfile)
	while True:
		lines = input.readlines()
		if not lines:
			break
		for line in lines:
			final=line
			
			if 'milestone ' in line:
				final=re.sub(r'<mile.*stone>'," sentence-text=\"", line)
				if len(final)<=30: final=''
			
			if '<p>' in line:
				# the <p> tag signals a sentence
				final=final.replace('<p>','')
				startgreeksentence=True
				
			if '</p>' in line:
				final=final.replace('</p>','\">')
				startgreeksentence=False
				
			if '<sentence>' in line:
				sentencecounter+=1
				final=final.replace('<sentence>','<sentence sentence_number=\"{}\" '.format(sentencecounter))
			
			if '</w>' in line:
				final=line.replace('\">',"\" word=\"")
				final=final.replace('</w>','\"> \n</word>')
			

			if ' ref=' in line:
				parts = re.sub(r'[!: ]'," ", line).split()
				j=0
				for items in parts:
					if 'ref=' in items: 
						final= line+" \n book=\""+parts[j][5:]+"\" \n chapter=\""+parts[j+1]+"\" \n verse=\""+parts[j+2]+"\" \n word_in_verse=\""+parts[j+3]+" \n "
					j+=1
					
			if '<w ' in line:
				final=final.replace('<w '," <word ")
					


				
			if 'book ' in line:
				final=line.replace('lang=\"el\" id=',' book_num=\"{}\" book_short='.format(bookcounter))
			output.write(final)

	input.close()
	output.close()


