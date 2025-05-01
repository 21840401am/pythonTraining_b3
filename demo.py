import keyword
from os import name

print(keyword.kwlist)
print("softkeyword list",keyword.softkwlist)
print("keywords count",len(keyword.kwlist))
deef = 67
case = 67
print("is import a keyword in python: ",keyword.iskeyword("import"))
print("case variable value",case )

my_variable = "python"
var = 2
variable2 = "java"
# print(my_variable, variable2, sep='@')

def add_num(a,b) -> int:
    
    print(a+b)
    print(a+b)
    
with open("file1.txt", "w") as f :
    print(my_variable, variable2, sep='@', file=f)

for i in range(5):
    ''' for loop will iterate over every element in the range
    and it prints the output to the console with space seperated'''
    print(i, end=" ",\
    flush=True)
    (print(i, end=" ",
    flush=True))
    
    
    
    
    
    
my_variable : int = "python"
var = "2"
var2 : float= 2.5567
var3 : bool = True
# print(type(var)) #This is pritning the datatype of var variablet



x = 0
if x > 0:
    print("Positive number")  # Correctly indented
    print("Positive number")  # Correctly indented
else:
  print("Non-positive number")  

name = int(4.5678)
name = 4.5678
print(name)
print(type(name))

x, y, z = "Orange", "Banana", "Cherry"
x, y, z = y,z,x
print(x,y,z, sep=" ")

list1 = [1, 2]
list2 = [3, 4]
list1, list2 = list2, list1
print(list1, list2)

list1 = [1, 2, 3, 4, 5]
a, b, c, *d = list1
print("a, b, c, d", a, b, c, d)
a, b, *c, d = list1
print("a, b, c, d", a, b, c, d)
*a, b, c, d = list1
print("a, b, c, d", a, b, c, d)

tuple1 = (1, 2, 3, 4, 5)
print(type(tuple1))
a, b, *c, d = tuple1
print( "a, b, *c, d",a, b, c, d)

language = "python"
a, b, *c, d = language
print( "printing values of variable a, b, *c, d",a, b, c, d)

list1 = [1, 2, 3, 4, 5]
a, b, *c = list1
print(a,b, c)

list1 = [1, 2, 3, 4, 5]
a, b, *_ = list1
print(a,b)

list1 = [1, 2]
list2 = [3, 4]
merged = (*list1, *list2)
print(merged)
print(type(merged))

string = "AB"
numbers = [1, 2]
merged = [*string, *numbers]
print(merged)

x = y = z = "Orange"
print(x)
print(y)
print(z)

name = "scala"
print("107",name)
del name
print(name)

PI = 3.144
















    
    
    
    
    
    
    
    
    
    
    
    













