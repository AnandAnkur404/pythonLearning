# numbers = [1,2,34, -2, -9,-8,9,89,5,-4]
# count = 0
# for i in numbers:
#     if i>0:
#         count+=1
# print(count)

# for i in range(10):
#     if i%2==0:
#         print(i)

#to find first repeated char in string
# input_str = "teeter"
# for char in input_str:
#     if input_str.count(char) == 1:
#         print("this is the char which is repeated one time only: ", char)

#check if number is prime
# number = 45
# isPrime = True

# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             isPrime = False
#             break
# print(isPrime)

# to check whether list contains duolicate item or not
# item_list = ["apple", "stawberry", "banana", "guava"]
# unique_item = set()
# for item in item_list:
#     if item in item_list:
#         print("This is duplicate item")
#         break
#     unique_item.add(item)

# for item in unique_item:
#     print(item, end="")

#loops

#range(takes two arguments last we dont include it)
# for token in range(1, 11):
#     print(f"here is your chai. for the token number: {token}")

# enumerate used to give numbering of all the item in the list, also we can start with particular index

# name_list = ["ankur", "carls", "frenz", "himalayan"]
# for indx, item in enumerate(name_list, start=1):
#     print(f"{indx} and {item}")


#zip() used to iterate over several iterator parallel producing tuples with an item from each one
# names = ["ankur", "ali", "sam", "abraham"]
# bills = [20, 90, 50, 80]
# for name, amount in zip(names, bills):
#     print(f"name is {name}, amount is {amount}")

# r = range(5)
# print(r)
# print(type(r))
# l = list(r)
# print(l)
# print(type(l))

# r = range(10, 20, 2) # start from 10, till 19 and add 2 at each step
# l = list(r)
# print(l)
# table
# for table in range(2, 7):
#     for i in range(1, 11):
#         print(table, "x", i, "=", table*i)
#     print()

# square printing
# for i in range(5):
#     for j in range(5):
#         print("* ", end="")
#     print()

# upper triangular matrix
# for i in range(5):
#     for j in range(i+1):
#         print("* ", end="")
#     print()

# method 2
# for i in range(5):
#     for j in range(5):
#         if i>j or i==j:
#             print("* ", end="")
#     print()

# lower triangular
for i in range(5, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()

# number matrix
# rows = 5

for row in range(1, 6):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()
   
# while loop palindrom number

# sum of a number
# number = int(input("enter number"))
# n = number
# sum=0
# while number>0:
#     rem = number%10
#     sum = sum * 10 + rem
#     number //= 10
# print(sum)
# to count number
# count = 0
# while number > 0:
#     count += 1
#     number //=10
# print(count)

# # range 
# list(range(5, 10))
# list(range(0, 10, 3))
# list(range(-10, -100, -30))

# for i in range(1, 20):
#     if i % 2 == 0:
#         continue
#     print(f"your number is :{i}")

