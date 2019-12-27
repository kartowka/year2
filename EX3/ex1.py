import os
mydict={}
files_list=['cities.txt','colors.txt','fruit.txt','names.txt']
for file in os.listdir(os.getcwd()):
    """take the names and input data to dictionary"""
    if file in files_list:
        file_name_value=str(file[:-4])
        f=open(os.getcwd()+'/'+file,'r')
        list_of_values=[]
        for line in f:
            list_of_values.extend(line.lower().split())
        #list1=[]
        #list1=list(filter(lambda name:name.isalpha(),list2))
        for _,key in enumerate(list_of_values):
            if not key.isalpha():
               pass
            else:
               mydict.setdefault(key,set()).add(file_name_value)
        f.close()
f=open(os.getcwd()+'/dictionary.txt','w')
# mydict=repr(mydict)
f.write(repr(mydict))
f.close()
