import os
import inflect

with open(os.getcwd()+'/'+'words.txt') as f:
    text=f.read()
f.close()
mylist=eval(text)

print(type(mylist))
p = inflect.engine()
for item in mylist:
    if item[1]>=5:
        print("{} because it belongs to at least {} categories".format(item[0],p.number_to_words(len(item[2]))))
        #return ("the solution was found after {} iteration: {}".format(min_iter,x0))
