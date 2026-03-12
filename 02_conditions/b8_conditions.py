# age = 20
# if age > 18:
#     print("you can vote")
# else:
#     print("hi kid, you need to study politics !")

# marks = int(input("enter your marks"))
# if marks > 80:
#     print("Grade A")
# elif marks > 70:
#     print("Grade B")
# elif marks > 60:
#     print("Grade C")
# else:
#     print("why not study!")

# snack = input("Enter your preferred order cookies/samosa: ").lower()

# if snack == "samosa" or snack == "cookies":
#     drink = input("Hi, we have chai/coffee").lower()
#     if drink == "chai" or drink == "coffee":
#         print(f"you meal of {snack} and drinks {drink} is preparing")
#     else:
#         print(f"your meal {snack} is preparing")
# else:
#     print("order is invalid")

# username = "ankur"
# password = "xyz@123"
# if username == "ankur":
#     if password == "xyz@123":
#         print("Login successful")
#     else:
#         print("check password again!")
# else:
#     print("user not found")

total_amount = int(input("enter total amout"))
delivery_fees = 0
if total_amount > 300:
    delivery_fees = 0
else:
    delivery_fees += 30

print(total_amount + delivery_fees)