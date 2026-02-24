print("Hello world")

x = 20
y = 30

print(x) #20
print(y) #30

#comment

""" doc sting 
multiline comment 
and doumenting some features.

"""

a, b = 40, 50

y = 90
z = 90
print(y) #90
print(a,b)

print(f"value of x is {x} and value of y is {y}") #string interpolation

print(id(x))
print(id(y))
print(id(90))
print(id(30))


#Operators

print( x + y) # 110
print( x - y) 
print( x* y)
print( y/x)
print( y // x)
b = 3
v = 4
print( b ** v) 

# user input
#x = input("enter any value x")


print(x)
#y = input("enter any value y")
print(y)

print(x + y)
#print(type(x))
#print(type(y))

#type casting

# 1. implicit type cast
a = 10
b = 20.8
print(a + b) # 30.8 

#2. Explicit type cast
x = int(input("enter any number x"))
y = int(input("enter value y"))
print(x + y)


a = 10
b = a 
a = a + 1

print(b) #10
print(a) #11

print(id(a))
print(id(b))

#data type 
#1 numeric 
# int 
# float 
price = 40.90
tax = 50.9

# bool
islogged = True # 1
isloggedout = False # 0

print(islogged)
print(isloggedout)

# complex number
e = 6 + 5j



# str
a = "ankur"

v = None

x=-2
y=3
print(x**y) #-(2**3) -8 ** has highest precedence that -

list
#Ordered collection of elements
#Mutable (can change)
#Allows duplicate values
#Can store mixed data types

nums = [10, 20, 30, 40]
print(nums[0])        # 10
nums.append(50)
nums[1] = 99
print(nums)          # [10, 99, 30, 40, 50]


#tuples
#Ordered collection
#Immutable (cannot change after creation)
#Allows duplicates
#Can store mixed data types

point = (10, 20)

print(point[0])      # 10
# point[0] = 99      # Error (immutable)

#dict
student = {
    "name": "Amit",
    "age": 21,
    "marks": 85
}

print(student["name"])     # Amit

student["marks"] = 90
student["city"] = "Delhi"

print(student)

#set
#Unordered collection
#Mutable
#Stores only unique elements
#No indexing (because unordered)
ids = {1, 2, 3, 3, 4}
print(ids)   # {1, 2, 3, 4}

ids.add(5)
print(ids)

user = {
    "id": 101,
    "name": "Rohit",
    "skills": ["Python", "SQL"],
    "location": ("Delhi", "India"),
    "tags": {"developer", "backend"}
}

print(user["skills"][0])        # Python
print(user["location"][1])      # India
print("backend" in user["tags"])  # True


x=10
y=10
print(x is y)




