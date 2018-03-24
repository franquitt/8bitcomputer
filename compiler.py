dic={"LDA":"0001","ADD":"0010","SUB":"0011","STA":"0100","LDI":"0101","JMP":"0110","JE":"0111","LDIB":"1000","OUT":"1110","HLT":"1111"}
file=open(input("source code file: "), "r")
for line in file.readlines():
	if(line!=""):
		line=line.replace("\n", "")
		instr=line
		param="0000"
		if(line.find(" ")!=-1):
			instr, param=line.split(" ")
		instr=dic[instr]
		param="{0:b}".format(int(param))
		param=( (4-len(param))*"0" ) + param
		print(instr+param)