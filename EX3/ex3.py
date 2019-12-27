import os
import inflect
"""to use this module please download pip install inflect
    Example answer: 'the' because it appears at least eleven times.
    this module change integer to a word"""
with open(os.getcwd()+'/'+'words.txt') as f:
    text=f.read()
f.close()
mylist=eval(text)
at_least_appears=5
at_least_belongs=1
p = inflect.engine()
for item in mylist:
    if len(item[2])>at_least_belongs:
        if item[1]>=at_least_appears:
            print("'{}' because it belongs to at least {} categories and because it appears at least {} times.".format(item[0],p.number_to_words(len(item[2])),p.number_to_words(item[1])))
        else:
            print("'{}' because it belongs to at least {} categories.".format(item[0],p.number_to_words(len(item[2]))))
    elif item[1]>=at_least_appears:
        print("'{}' because it appears at least {} times.".format(item[0],p.number_to_words(item[1])))
