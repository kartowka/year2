import os
with open(os.getcwd()+'/'+'words.txt') as f:
    text=eval(f.read())
f.close()
at_least_appears=5
at_least_belongs=1
mydict={}
for item in text:
    if len(item[2])>at_least_belongs:
        if item[1]>=at_least_appears:
            mydict[item[0]]='because it belongs to at least two categories and because it appears at least five times.'
        else:
            mydict[item[0]]='because it belongs to at least tow categories.'
    elif item[1]>=at_least_appears:
        mydict[item[0]]='because it appears at least five times.'
for k,v in mydict.items():
    print(f"'{k}' {v}")