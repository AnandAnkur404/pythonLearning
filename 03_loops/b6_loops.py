seat_type = input("kindly enter your seat type sleeper/ac/general/luxury").lower()

match seat_type:
    case "sleeper":
        print("Your seat type is sleeper")
        print(f"your seat type {seat_type}")
    case "ac":
        print("Your seat type ac")
    case "luxury":
        print("Your seat type is luxury")
    case "general":
        print("Your seat type is general")

username = "ank"
password = "ankur@123"
if username == "ankur":
    if password == "ankur@123":
        print("Login successful")
    else:
        print("password incorrect !")
else:
    print("username not found")

# for i in seq / range()/ enumerate() / zip()

num = [-1,23,59, -9, 8, 7, 9]
for i in num:
    # print(i, end=" ")
    # if i > 0:
    #     print(i)
    if i % 2 == 0:
        print(i)

# for i in range()sx
r = range(5) # range(0, 5) 0, 1, 2, 3,4
print(r)
l = list(r)
print(l)

r = range(3, 16) 
r = range(2, 20, 2) 
l = list(r)
print(l)
r= range(20, 0, -1)
l = list(r)
print(l)

for i in range(100):
    if i%5 == 0:
        continue
    elif i%2 == 0:
        break
    print(i)

# 0
# []
# ()
# ""
# set()

if 0:
    print("this is if")
else:
    print("this is else")

for row in range(5):
    for col in range(row + 1):
        print("* ", end=" ")
    print()

for row in range(5):
    for col in range(5):
        if row>= col:
            print("* ", end=" ")
    print()
    
n = 98765
count = 0
while n > 0:
    rem = n % 10
    count += 1
    n = n // 10
print(count)


    

