# Tuple in Python

# major Deference with lists and tuples 
# lists ---> mutable -->[]
# tuples ---> immutable -->()


tup = (2,3,4,5)

# tup[0] = 5 # that give error because not allowed

tup = (9)  
print(type(tup))
tup = (9.0)  
print(type(tup))
tup = ("gg")  
print(type(tup))
tup = (9,)  
print(type(tup))
tup = (2,3,4,5) 
print(type(tup))
tup = (2,3,4,5,) 
print(type(tup))




#Tuple Methods....
print(tup.index(5)) # returns index of first occurrence = 3
print(tup.count(3)) # counts total occurrences = 1
print((tup + (6,7))) # concatenation of tuples = (2,3,4,5,6,7)
