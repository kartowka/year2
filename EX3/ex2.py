import os
import re
mydict={}
files_list=["text.txt"]#,"dictionary.txt"]
unsupported_chars=[',','.','?','!','\n']
for file in os.listdir(os.getcwd()):
    if file in files_list:
        f=open(os.getcwd()+'/'+file,'r')
        to_list=[]
        for line in f:
            a=re.split('[.,!?' '\n]',line.lower())
            #to_list.extend(a)
            to_list.extend(a)
        s=set(to_list)
        s.remove('')
        #newlist=list(filter(lambda i:i is not unsupported_chars,to_list))
        f.close()
        print(s)
        #print(newlist)
