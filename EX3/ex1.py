import os
mydict={}
files_list=['cities.txt','colors.txt','fruit.txt','names.txt']
for file in os.listdir(os.getcwd()):
    """take the names and input data to dictionary"""
    if file in files_list:
        print(file)
        file_name_value=str(file[:-4])
        f=open(os.getcwd()+'/'+file,'r')
        list=[]
        for line in f:
            list.extend(line.lower().split())
        for _,key in enumerate(list):
            if not key.isalpha():
                pass
            else:
                mydict.setdefault(key,set()).add(file_name_value)
        f.close()
f=open(os.getcwd()+'/dictionary.txt','w')
f.write(repr(mydict))
f.close()
