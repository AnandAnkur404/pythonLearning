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

