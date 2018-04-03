#ex_11_01
fname = input ("enter file name ")
fhand = open (fname)
counts= dict()
num = []
import re
count = 0
regex=input ("Enter the Regular Expression")
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
for lx in fhand:
    lx = lx.rstrip()
    if re.search (regex,lx):
        #print (lx)
        count = count +1

print (fname, "has",count, "lines matched", regex )
