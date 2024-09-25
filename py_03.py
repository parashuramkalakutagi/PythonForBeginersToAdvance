list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)


#Tuples are immutable and can not be modified after creation.

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)



#range: returns a sequence of numbers as specified by the user. If not specified by the user then it starts from 0 by default and increments by 1.

sequence1 = range(0,10)
for i in sequence1:
    print(i)



#dict: a dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
print(dict1.values())
print(dict1.keys())
print(dict1.get("name"))

dict2 = dict1.copy()
print(dict2.get("name"))





#bytes: bytes() function is used to convert objects into byte objects, or create empty bytes object of the specified size.

name = "my name is parashuram kalakutagi"
array = bytes(name, 'utf-16')
print(array)


#Converting string to bytes
string1 = "this is my string "
exm = bytes(string1, 'utf-16')
print(exm)

#Creating bytes of given size
byytes = bytes(6)
print(byytes)


#memoryview: memoryview() function returns a memory view object from a specified object.

stringg = bytes("my name is pk",'utf-8')
memo = memoryview(stringg)
print(list(memo[0:]))



