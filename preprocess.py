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


for files in SET:
	inputfile=basedir+"input_raw_xml/"+files
	outputfile=basedir+"xml/input_xml/"+files
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
			
			if ' ref=' in line:
				parts = re.sub(r'[!: ]'," ", line).split()
				j=0
				for items in parts:
					if 'ref=' in items: 
						final= line+" \n book=\""+parts[j][5:]+"\" \n chapter=\""+parts[j+1]+"\" \n verse=\""+parts[j+2]+"\" \n word_in_verse=\""+parts[j+3]+" \n "
					j+=1
					
					
			if 'milestone ' in line:
				fullline=line
				parts = re.sub(r'[!: \"]'," ", line).split()
				j=0
				for items in parts:
					if 'id=' in items: 
						section= " <verse \n book=\""+parts[j+1]+"\" \n chapter=\""+parts[j+2]+"\" \n verse=\""+parts[j+3]+"\"> </verse>\n"
						break
					j+=1
				final=re.sub('<mile.*stone>',section,line)
				#print ('milestone:',final)
			if 'book ' in line:
				final=line.replace('id=',' book_short=')
			output.write(final)

	input.close()
	output.close()


