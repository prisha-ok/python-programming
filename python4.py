# TOPIC 5: Dictionaries:

# accessing dictinary values using keys
'''d={}
d[1]="ramesh"
d[2]="suresh"
d[3]="mukesh"
print(d)'''

# handling keyerror in dictionary
""" d={1:"ramesh",2:"suresh",3:"kumar"}
if 3 in d:
    print(d[3])
else:
    print("invalid key") """

# EXAMPLE : employee info program
""" d={}
n=int(input("enter number of employees"))
i=1
while i<=n:
    name=input("enter employee name:")
    salary=input("enter employee salary")
    d[name]=salary
    i=i+1
for x in d:
    print("the name is : ",x,"and his salary is : ",d[x]) """

# deleting or removing elements in a dictionary
""" d={1:"hello",2:"world",3:"okay"}
print(d)
del d[1]    # DEL IS A KEYWORD 
print(d)"""

""" d={1:"hello",2:"world",3:"okay"}
print(d)
del(d[2])   # DEL AS A FUNCTION
print(d) """

""" d={1:"hello",2:"world",3:"okay"}
print(d)
d.clear()
print(d) """

# list of tuples
""" t1="ok"
t2="okie"
t3="okayuu"
l1=[t1,t2,t3]
print(l1) """

# get() method
""" d={1:"GLA mathura",2:"GLA noida",3:"GLA london"}
print(d.get(4,"No GLA"))    #shows absense- if i remove "No GLA" then i would get none
if d.get(4):
    print("hi")
else:
    print("hello") """

# pop() method
""" d={1:"GLA mathura",2:"GLA noida",3:"GLA london"}
d.pop(2)             # no sequence in dictionary thus, pop() i.e without arguement doesnt work
print(d) """

# popitem() method
'''d={1:"GLA mathura",2:"GLA noida",3:"GLA london"}
d.popitem()
print(d)'''

# keys() method
'''d={1:"harry",2:"bellingham",3:"jude"}
print(d)
for k in d.keys():
    print(k)'''

# values() method
'''d={1:"harry",2:"bellingham",3:"jude"}
print(d)
for k in d.values():
    print(k)'''

# items() method - picks the item and values in form of a tuple
'''d={1:"harry",2:"bellingham",3:"jude"}
print(d)
for k,v in d.items():
    print(k,"---",v)'''

# copy() method - deep copy is made
'''d1={1:"harry",2:"bellingham",3:"jude"}
d2=d1.copy()
print(d1)
print(d2)
print(id(d1))
print(id(d2))'''

# DICTIONARY COMPREHNSION:
""" sqaures={a:a*a for a in range(1,6)}
print(sqaures) """

""" d={x:x*x for x in range(1,10) if (x*x)%3==0}
print(d) """

