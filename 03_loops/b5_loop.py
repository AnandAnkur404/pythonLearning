r = range(5)
print(r)
print(type(r))
l = list(r)
print(l)

# num = [1, -2, 8, -9, 8, 90, 6]
# for i in num:
#     if i % 2 == 0:
#         print(i, end=" ")

# for i in range(10, 0, -1):
#     print(i, end=" ")

# a = 0
# b = 1
# for i in range(10):
#     c = a + b
#     a = b
#     b = c
# print(c)
# count = 0
# for i in range(100):
#     if i%5 == 0:
#         continue
#     elif i%2 == 0:
#         count += 1
# print(count)

# for row in range(5):
#     for col in range(5):
#         print(col, end=" ")
#     print()

# star printing
# for row in range(5):
#     for col in range(5):
#         print("* ", end=" ")
#     print()

# for row in range(5):
#     for col in range(row + 1):
#         print("* ", end=" ")
#     print()

# for row in range(5):
#     for col in range(5):
#         # pass
#         if row >= col:
#             print("* ", end="")
#     print()

# while loop
# a = 0
# while a < 10:
#     a += 1
#     if a % 5 == 0:
#         break
# print(a)


# num = ["ankur", 12, 90, 9]
# for indx, i in enumerate(num):
#     print(f"{indx} of {i}")

names = ["ankur", "python", "learning"]
bills = [20, 30, 50]

for name, bill in zip(names, bills):
    print(f" your name is {name} and your bill is {bill}")
    print(name, bill)