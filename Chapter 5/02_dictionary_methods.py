myDict = {
    "fast": "In a quick manner", 
    "aditya": "A learner",
    "marks": [1,2,5] ,
    "anotherdict": {'harry' : 'Player'},
    1: 2
}

#Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary
print(myDict.items()) # Prints the (key, value) for all the contents of the dictionary
print(myDict)
updateDict ={
    "Ashray": "Friend",
    "Smriti": "Sister"

}
myDict.update(updateDict) #Updates the dictionary by adding key-value pairs from updateDict
print(myDict)