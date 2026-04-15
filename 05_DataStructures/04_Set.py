# Set in python
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Sets are written with curly brackets.

collection = {1,2,3,4,5,5,5,'Hello', 'Hello'}
print(collection) # duplicate values are not allowed in set
print(type(collection)) # <class 'set'>
print(len(collection)) # length of the set


# Syntax to create an empty set
empty_set = {} # Empty dictionary, not a set
print(type(empty_set)) # <class 'dict'>

empty_set = set()
print(empty_set) #Empty set
print(type(empty_set)) # <class 'set'>

# Set Methods
collection.add(6) # add an element to the set
print(collection)
collection.remove(3) # remove an element from the set
print(collection)
collection.discard(10) # remove an element from the set if it is present, otherwise
print(collection)
collection.pop() # remove a random element from the set
print(collection)
collection.update({7,8,9}) # add multiple elements to the set
print(collection)
collection.clear() # clear the set
print(collection)

# Set Operations
collection1 = {1,2,3,4,5}
collection2 = {1,10,9,4,5}
print(collection1.union(collection2)) # union of two sets
print(collection1.intersection(collection2)) # intersection of two sets
print(collection1.symmetric_difference(collection2)) # symmetric difference of two sets
print(collection1.difference(collection2)) # difference of two sets 