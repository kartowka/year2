import os
import re
from collections import Counter
#txt open
f_txt=open(os.getcwd()+'/'+'text.txt','r')
to_list=[]
for line in f_txt:
    a=re.split('[.,!?' '\n1-9]',line.lower())
    to_list.extend(a)
s=set(to_list)
s.remove('')
f_txt.close()


# dictionary open
f_dict=open(os.getcwd()+'/'+'dictionary.txt','r')
mydict={}
for line in f_dict:
    mydict=eval(line)
f_dict.close()

def check_if_exist(tuple_list,first,second):
    temp_list=second.split()
    for _,key in enumerate(temp_list):
        if key in first:
            tuple_list.append((key,temp_list.count(key),first[key]))
        else:
            tuple_list.append((key,temp_list.count(key),{}))

f_words=open(os.getcwd()+'/'+'words.txt','w')
tuple_list=[]
for line in s:
    check_if_exist(tuple_list,mydict,line)
tuple_list.sort(reverse=True)
f_words.write(repr(tuple_list))
f_words.close()
