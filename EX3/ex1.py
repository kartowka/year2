import os
mydict={}
for file in os.listdir("/home/kartowka/Desktop/EX3/txts"):
    """take the names and input data to dictionary"""
    if file.endswith(".txt"):
        file_name_value=str(file[:-4])
        f=open("/home/kartowka/Desktop/EX3/txts/"+file,'r')
        list=[]
        for line in f:
            list.extend(line.lower().split())
        #list_to_set=set(list)
        #print(list_to_set)
        for _,key in enumerate(list):
            mydict.setdefault(key,[]).append(file_name_value)
        f.close()
for key,val in mydict.items():
    convert_to_set=set()
    convert_to_set=set(val)
    mydict[key]=convert_to_set
print(mydict["orange"])
f=open("/home/kartowka/Desktop/EX3/dictionary.txt",'w')
for k, v in mydict.items():
    f.write(str(k)+' '+str(v)+'\n')
f.close()
