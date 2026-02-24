print("hi welcome to python learning")
print("hi", 10, "gfg")

x = 10
print(type(x))

x = float(x)
print(type(x))

print(x)

# input() it pauses the exectution

#x = input("enter any value")
#print(x)
#print(type(x))

#y = input("Enter value y")
#print(y)

#print(x + y) # string will concate

#x = int(x)

#y = int(y)

#print(x + y)

# data type - int float bool complex
var = 10
a = 90

f = 30.9
c = 30 + 40j
print(type(c))


#end=
print("hi welcome to ", end="")
print("python learning")
print() # new line


#sep=
print(10, "hello",40, sep=",")
print(30, 8, 2026, sep="-")


#sequences - str, list, tuple
#set, dict

#list
list = [10, 20, "ankur", 40]
print(list) #[10, 20, 'ankur', 40]
print(list[1]) #20
list[0] = 90
print(list) #[90, 20, 'ankur', 40]
print(type(list)) #<class 'list'>
print(len(list))


#immutability
a = 10
b = 10
print(id(a))
print(id(b))

b = a
a = a + 10

print(id(a))
print(id(b))

#set unordered unique value, mutable
s = {10, "gfg", 70, 80}

s1 = {10, 20, 30}
s2 = {30, 40, 50}

print(s1 & s2) #intersection
print(s1 | s2)  #union

print(type(s)) #<class 'set'>
print(s) #{80, 10, 'gfg', 70}

print(s.add(90))
print(s)

#dict - unordered-that is why they don't have indexing, contains key value pair, mutable 
d = {"name": "ankur", "id": 20, 10: 26}
print(d)
print(type(d))
print(d["name"]) #ankur
d["name"] = "geeksforgeeks"
print(d["name"])

#operator +, -, *, /, //, **, %

#logical -> and, or, not

#conditional -> <, > <=, >=, ==, !=

#bitwise -> left shit (<<), right shift(>>)

#From highest (executed first) to lowest:
#() – Parentheses
#** – Exponentiation
#*, /, //, % – Multiplication, division
#+, - – Addition, subtraction
#Comparison – ==, !=, <, >, <=, >=
#Logical – not
#Logical – and
#Logical – or
#assignment operator

x = 10 + 2 * 4
print(x) #18

x = (10 + 2) * 4
print(x) #48

y = 2 ** 3 + 3 ** 2
print(y) # 11
y = 2 ** (3 * 2)
print(y)

w = 20 // (10 + 20) / 2
print(w) 

r=1 < 2 < 3 #( 1 < 2) and (2 < 3)
print(r)

#in or not in
x = "gfg"
print("G" in x) #false

print("f" not in x) #false

x=5
print(x<<1) # 5 * 2^1
print(x<<2) # 5 * 2^2
print(x<<3) # 5 * 2^3

y = 30
print(bin(y))

print(oct(y))
print(hex(y))

print(True or False)
print(False and True)

#tuple
t=(10, 30, "ankur")
print(type(t)) #<class 'tuple'>
t1 = 10, 20, "geeks", 90
print(type(t1)) #<class 'tuple'>
t2 = 10 
print(type(t2)) #<class 'int'>
t3 = 20,
print(type(t3)) #<class 'tuple'>
t4 = (10,)
print(type(t4)) #<class 'tuple'>

#t[1] = "gfg " # TypeError: 'tuple' object does not support item assignment
print(t)




