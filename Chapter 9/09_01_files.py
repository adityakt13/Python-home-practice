# Use open function to read the content of a file!
# f = open('sample.txt', 'r')
f = open('sample.txt') # by default the mode is 'r'
# data = f.read()
data = f.read() # will read only first 5 characters of the file
print(data)
f.close()