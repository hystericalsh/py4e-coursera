#ex_11_02
fname = input ("Enter the File Name")
fhand = open (fname)
import re
lst = []


#`New Revision: 39772`
for lx in fhand:
    lx = lx.rstrip ()
    y = re.findall ("New Revision: ([0-9]+)", lx)
    if len (y)>0:
        lst = lst + y

count = 0
tot = 0
for num in lst:
    num = float (num)
    count = count + 1
    tot = tot+ (num)

print (tot/count)
