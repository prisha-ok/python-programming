# TOPIC-6: SETS - partially mutable

""" s={1,2,3,4,5}
print(type(s))
print(s) """

# creating set with heterogenous elements
""" s={1,2,3,"okay",89.90,True}
print(type(s))
print(s) """

# creating set using range function
""" s=set(range(5))
print(s) """

# imp.
""" l1="python programming"
d={}
for x in l1:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
d={k:v for k,v in d.items() if v>1}
print(d)
l1=list(d.keys()) """

# creating empty set in python
""" d={}
print(type(d))
s=set()
print(type(s)) """

# METHODS OF A SET:
# add() method - only one element added
""" s={1,2,3,4}
s.add(5)
print(s) """

# update() method - multiple elements added
""" s={10,20,30}
l=[40,50,60,10]
s.update(l,range(5))
print(s) """

# copy() method
'''s={10,20,30}
s1=s.copy()
print(s1)'''

# pop() method
'''s={40,10,30,20}
print(s)
print(s.pop())
print(s)'''

# remove() method
""" s={40,30,10,20}
'''s.remove(60)'''     # KeyError: 60
s.remove(10)
print(s) """

# discard() method - no error if element is not present
""" s={10,30,20}
s.discard(89)
print(s)
 """

# clear() method
""" s={10,20,50,30}
s.clear()
print(s) """

# MATHEMATICAL OPERATIONS ON A SET:
# python doesnt support bit wise operator but it uses them for set operations #

# Union() method - x|y
""" x={10,20,30,40}
y={30,40,50,60}
x.union(y)
print(x.union(y)) """

# Intersection() method - x&y
""" x={10,20,30,40}
y={30,40,50,60}
print(x&y)     # union
print(x|y)     # intersection """

# Difference() method
""" x={10,20,30,40}
y={30,40,50,60}
print(x.difference(y))
print(x-y) """

# Symmetric difference() method
""" x={10,20,30,40}
y={30,40,50,60}
print(x.symmetric_difference(y))
print(x^y) """

# Set Comprehension
""" s={x*x for x in range(5)}
print(s) """

# Concept of Frozen Set
vowels=('a','e','i','o','u')
fSet=frozenset(vowels)
print(fSet)
print(type(fSet))
# this is a comment