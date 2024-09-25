#Python Variables

name = "Abhishek"   #type str
age = 20            #type int
passed = True       #type bool

print(name, age, passed)



Color = "yellow"    #valid variable name
cOlor = "red"       #valid variable name
_color = "blue"     #valid variable name

#5color = "green"    #invalid variable name
#$color = "orange"   #invalid variable name




#Local Variable:

icecream = "Vanilla"    #global variable
def foods():
    vegetable = "Potato"    #local variable
    fruit = "Lichi"         #local variable
    print(vegetable , " is a local variable value.")
    print(icecream ," is a global variable value.")
    print(fruit , " is a local variable value.")

foods()



#Global Varible :
icecream = "Vanilla"    #global variable
def foods():
    vegetable = "Potato"    #local variable
    fruit = "Lichi"         #local variable
    print(vegetable + " is a local variable value.")

foods()
print(icecream + " is a global variable value.")
print(fruit + " is a local variable value.")
