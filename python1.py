l.=[3,7,[1,4,'hello']]

l[2][2]='goodbye'

print(l)

d1={'simple_key':'hello'}

print(d1['simple_key'])

d2={'k1':{'k2':'hello'}}

print(d2['k1']['k2'])

d3={'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d3['k1'][0]['nest_key'][1][0])


mylist=[1,1,1,1,1,2,2,2,2,3,3,3,3]

converted=set(mylist)
print(converted)

age=4
name="Sammy"
print("Hello my dog`s name is {a} and he is {b} years old".format(a=name,b=age))
