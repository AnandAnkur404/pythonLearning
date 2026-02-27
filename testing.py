print(2.3+2.3)
#this is how list are created
#list are mutable
#list are ordered and indexed

l=[20, 30, 40,5, "hi ankur"]
l[-1] = 20
print(l)
print(l[1:3]) # index 1 and 2 are included 3 are excluded

#set
s={10, 20, 30.8, "geeksforgeeks"}
s.add("809")
print(s)

#Operators
#arithematic operators

a=10
b=3
print(a+b)

#string multiplication
print('Ha ' * 3)                    # HaHaHa
print('-' * 30) 

print(2 | 3) #logical or
print(2 and 3) #it will take last value bcz both are true

print(0 and "Hello")
print(1 and "Hello")
print(0 or "hi")
print(1 or "hello")


#conversion
print(bin(23))
print(oct(89))
print(hex(189))

w=10000909981
print(id(w))
print(id(10000909981))
#id gives identity of object , that’s an optimization / compiler behavior, not a language rule.

#logical operators
print(0 or 'hello') #hello
print(5 or 'hi') #5
print(0 and 'hi') # 0
print(5 and 'hihihi') #hihihi

#is and is not is identity operator
#is check id is same or not 
#== check if value is same or not 
#in and not in is membership operator
#if that value is present in that list/set/string etc or not


