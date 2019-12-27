import os
import re

with open(os.getcwd()+'/'+'text.txt') as f:
    text=f.read()
f.close()

text=re.split('[.,!?''\r\n1-9]',text.lower())
text=filter(None,text)
newlist=[]
for i in text:
    newlist.extend(i.split())

with open(os.getcwd()+'/'+'dictionary.txt') as f:
    text=f.read()
f.close()
mydict=eval(text)

f_words=open(os.getcwd()+'/'+'words.txt','w')
tuple_list=[]
for key in newlist:
    if key in mydict:
        tuple_list.append((key,newlist.count(key),mydict[key]))
    else:
        tuple_list.append((key,newlist.count(key),{}))
duplicates_remove=set()
sorted_list=[]
for t_first,t_second,t_third in tuple_list:
    if not t_first in duplicates_remove:
        duplicates_remove.add(t_first)
        sorted_list.append((t_first,t_second,t_third))
sorted_list.sort(reverse=True)
f_words.write(repr(sorted_list))
f_words.close()
