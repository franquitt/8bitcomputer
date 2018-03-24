import math

hlt=128
mi=64
ri=32
ro=16
io=8
ii=4
ai=2
ao=1

eo=128
su=64
bi=32
oi=16
ce=8
co=4
j=2
je=1

free=0
firstchip=[]
secondchip=[]
def addDelimiterFirstChip():
	global firstchip
	firstchip.extend([mi, ro+ii])
def addDelimiterSecondChip():
	global secondchip
	secondchip.extend([co, ce])
def addCommand(toOne, toTwo):
	if(len(toOne)==3 and len(toTwo)==3):
		addDelimiterFirstChip()
		addDelimiterSecondChip()

		firstchip.extend(toOne)
		secondchip.extend(toTwo)
		firstchip.extend([free, free, free])
		secondchip.extend([free, free, free])
	else:
		print("ERROR")

# 0000
addCommand([free, free, free], [free, free, free])
#LDA load from mem to reg A 0001
addCommand([mi+io, ro+ai, free], [free, free, free])

#ADD load from mem to reg B, then add reg A & B and store in A  0010
addCommand([mi+io, ro, ai], [free, bi, eo])

#SUB load from mem to reg B, then substract reg A & B and store in A 0011
addCommand([mi+io, ro, ai], [free, bi, eo+su])

#STA load from reg A to mem 0100
addCommand([mi+io, ao+ri, free], [free, free, free])

#LDI load the instruction parameter value in reg A   0101
addCommand([io+ai, free, free], [free, free, free])

#JMP 0110
addCommand([io, free, free], [j, free, free])

#JE jump if equal 0111
addCommand([io, free, free], [je, free, free])


#LDIB load the instruction parameter value in reg B   1000
addCommand([io, free, free], [bi, free, free])
# 1001
addCommand([free, free, free], [free, free, free])
# 1010
addCommand([free, free, free], [free, free, free])
# 1011
addCommand([free, free, free], [free, free, free])
# 1100
addCommand([free, free, free], [free, free, free])
# 1101
addCommand([free, free, free], [free, free, free])


#OUT load from reg A to output register 1110
addCommand([ao, free, free], [oi, free, free])

#HLT  1111
addCommand([hlt, free, free], [free, free, free])




firstchip.extend(secondchip)
tot=""
count=0
for i in firstchip:
	val='{:X}'.format(i)
	if(len(val)==1):
		tot+="0"+val+" "
	else:
		tot+=val+" "
	count+=1
	if(count==16):
		count=0
		tot+="\n"
	
print(tot)
