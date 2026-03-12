# loop 
# for i in seq/range()/enumerate()/zip()

num = [-1, 9, 8, 7, 10, 72, 90]
for i in num:
    # print(i, end=" ")
    if i % 2 == 0:
        print(i)

# question to count vowel
s = input("enter your string ")
count = 0
vowel = "aieouAEIOU"
for char in s:
    if char in vowel:
        count = count + 1
print(count)

# r = range(4)
# print(r)
# l = list(r)
# print(l)

for i in range(5):
    print(i, end=" ")

for i in range(20, 0, -2):
    print(i, end=" ")

n = int(input("enter number"))
fact = 1
for i in range(1, n + 1):
    fact = fact * i

print(fact)

for row in range(5):
    for col in range(5):
        print(row, end=" ")
    print()

for row in range(5):
    for col in range(5):
        print("* ", end=" ")
    print()

for row in range(5):
    for col in range(row + 1):
        print("* ", end=" ")
    print()

# for row in range(5, 0, -1):
#     for col in range(5):

enumerate()
name = ["ankur", "ali", "python", "gniot"]
for idx, i in enumerate(name, start=2):
    print(idx, i)

names = ["ankur", "ali", "python", "gniot"]
bills = [20, 10, 0, 90]

for name, bill in zip(names, bills):
    print(name, bill, sep=": ")
