print("hi, welcome to GNIOT")
print("hi", 10, 40.8)
print()
#end=
print("hi welcome to ", end="")
print("python learning")

#sep=
# print(27, 2, 2026, sep="-")

# a = 10
# b = a
# a = a + 20
# print(id(a))
# print(id(b))
# print(a)
# print(b)

#numeric data
#int, float, bool, complex

isValid = True #1
isLoggedIn = False #0

print(True + True) #2
print(True + False) #1
print(True + 6) #7
print(False + False) #0

x = 20.8
print(type(x))
x = int(x)
print(type(x))
print(x)

# b = "abc"
# b = int(b)
# print(b) invalid literal for int() with base 10: 'abc'

# x = int(input("enter value x:"))
# y = int(input("enter value y:"))

# print(type(x))
# print(type(y))
# print(x + y)

# x = int(x)
# y = int(y)

print("ha"*3)

#arithmatic operators
# x = 10
# y = 5

# print(x + y)
# print(x - y)
# print(x * y)
# print(y / x)
# print(y // x)

# print(x ** y)
# print(x % y)

# #2 comparison operator <, <=, >, >=, ==, !=
# print(x == y)
# print(x > y)
# print(x != y)

# a = "apple"
# b = "anana"
# print(a < b)

#logical operator and (&), or(|), not (~)

a = 90
b = 30
print(a & b)
print(a | b)
print(~a)

#bitwise <<, >>, xor
a = 10
b = 20

a = a<<1 #a + 2^1
print(a)
a = a<<2
print(a)
a = a<<3
print(a)

#right shift
b = b>>1
b = b>>2
print(b)

#xor
a = 5
b = 6
a = a ^ b
b = a ^ b
a = a ^ b
print(a)
print(b)

a, b = b, a
print(a)
print(b)


#assignment operator +=, -=, *=, /=, **=, //=

# a += 10

#identity operator is , not is

# x = 10
# y = 30
# x = b
# print(x is y)
# print(x is b)
# print(x is not y)

#membership operator in and not in
# a = "gfg"
# print("G" in a) #False

# print("gf" not in a) #False

x = 10
print(x)

#formmated string
print(f"hi this value of x: {x}")

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

x = 20 + 30 * 3
print(x)

y = (20 + 30) * 3
print(y)