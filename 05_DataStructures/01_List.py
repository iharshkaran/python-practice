# Lists in Python

marks = [2,34,56,4,99,78]   # marks
student = ["Raj" , 85 , "Delhi"] # student

#Slicing
print(marks[0:3]) #3 is not included
print(marks[:4]) # from start to index 3
print(student[1:]) # from index 1 to end
print(marks[::2]) # from start to end with a step of 2

# Methods
list = [2,3,5,1,7,8]
print(list)

list.append(4)  #adds one elements at the end [2,1,3,4]
print(list)
list.sort() # sorts in ascending order [1,2,3]
print(list)
list.sort(reverse = True) # sorts in descending order [3,2,1]
print(list)
list.reverse()  #reverse list [3, 1, 2]
print(list)
list.insert(1 , 9) #insert element at index
print(list)
list.remove(9) #removes 9 [2,3,4,5]
print(list)
list.pop(2) #removes element at idx
print(list)
list.clear() #clears the list
print(list) 
 

