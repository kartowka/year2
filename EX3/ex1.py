import os
mydict={}
unsupported_char=['-']
for file in os.listdir(os.getcwd()+'/txts'):
    """take the names and input data to dictionary"""
    if file.endswith(".txt"):
        file_name_value=str(file[:-4])
        f=open(os.getcwd()+'/txts/'+file,'r')
        list=[]
        for line in f:
            if [ele for ele in unsupported_char if(ele in line)]:
                pass
            else:
                list.extend(line.lower().split())
        for _,key in enumerate(list):
            mydict.setdefault(key,[]).append(file_name_value)
        f.close()
for key,val in mydict.items():
    convert_to_set=set()
    convert_to_set=set(val)
    mydict[key]=convert_to_set
f=open(os.getcwd()+'/dictionary.txt','w')
f.write(str(mydict))
f.close()
