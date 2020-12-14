fin = open("datasets/books-logotexnia.csv", "rt")
#output file to write the result to
fout = open("datasets/books-logotexnia2.csv", "wt")
#for each line in the input file
for final in fin:
	#print(line)
	newLine = final.split("\"")

	nLine = newLine[len(newLine)-1]
	#print(nLine)
	line = nLine
	#read replace the string and write to output file
	if(len(line.split(";"))==1):
		fout.write(final.replace('\n', ';\n'))
		#print("true")
	else:
		fout.write(final)
		print(len(line.split(";")))
#close input and output files
fin.close()
fout.close()