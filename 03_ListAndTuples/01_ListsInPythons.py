marks = [2,34,56,4]   # marks[0], marks[1]

student = ["Karan" , 85 , "Delhi"] # student[0], student[1]

len(student) # returns length

#Slice --> marks[0:3] #3 is not included

#Methods --> 
list = [2,3,5]
list.append(4)  #adds one elements at the end [2,1,3,4]
print(list)
list.sort() # sorts in ascending order [1,2,3]
list.sort(reverse = True) # sorts in descending order [3,2,1]
list.reverse()  #reverse list [3, 1, 2]
list.insert(1 , 9) #insert element at index
print(list)

list.remove(9) #removes 9 [2,3,4,5]
print(list)
list.pop(2) #removes element at idx
print(list)
