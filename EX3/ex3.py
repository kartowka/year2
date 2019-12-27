import os

with open(os.getcwd()+'/'+'words.txt') as f:
    text=f.read()
f.close()
mylist=eval(text)

print(type(mylist))

for item in mylist:
    if item[1]>=5:
        print(item)
