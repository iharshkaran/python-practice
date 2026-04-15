# Dictionary in Python

info = {
    "name" : "Rahul",
    "age" : 19,
    "marks" : { # nested dictionary
        "Electronics" : 85,
        "Maths" : 90,
        "PPS" : 80
    },
    "Skills" : ["Python", "Java", "C++"],
    "city" : "Delhi",
    "is_student" : True
}

print(info)
print("\n")
print(type(info))
print("\n")

print(info["name"]) # to access value of key "name"
print("\n")
info["age"] = 20 # to update value of key "age"
print(info)
print("\n")
info["country"] = "India" # to add new key-value pair
print(info)
print("\n")
print(info["marks"]["Maths"]) # to access value of nested dictionary key "Maths"
print("\n")
print(len(info)) # to get number of key-value pairs in the dictionary
print("\n")

print(list(info.keys())) # to get all keys in the dictionary
print("\n")
print(list(info.values())) # to get all values in the dictionary
print("\n")
print(list(info.items())) # to get all key-value pairs in the dictionary as a list of tuples
print("\n")



# Dictionary Methods
print(info.keys()) # returns all keys in the dictionary
print("\n")
print(info.values()) # returns all values in the dictionary
print("\n")
print(info.items()) # returns all key-value pairs in the dictionary
print("\n")
print(info.get("name")) # returns value of key "name"
print("\n")
print(info.get("country", "Not Found")) # returns value of key "country" or "Not Found" if key is not present
print(info.pop("city")) # removes key "city" and returns its value
print("\n")
print(info.popitem()) # removes and returns the last key-value pair added
print("\n") 
info.update({"age": 21, "country": "India"}) # updates existing key "age" and adds new key "country"
print(info)
info.clear() # clears the dictionary
print(info)