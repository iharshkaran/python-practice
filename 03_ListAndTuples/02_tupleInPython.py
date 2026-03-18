# major Deference with lists and tuples 
# lists ---> mutable -->[]
# tuples ---> immutable -->()


tup = (2,3,4,5)

tup[0] = 5 # that give error because not allowed

# tup = (9)  type(tup) = integer
# tup = (9.0)  type(tup) = float
# tup = ("gg")  type(tup) = string
# tup = (9,)  type(tup) = tuple
# tup = (2,3,4,5)   type(tup) = tuple
# tup = (2,3,4,5,)   type(tup) = tuple




#Tuple Methods....

tup.index(3) # returns index of first occurrence = 1
tup.count(3) # counts total occurrences = 1