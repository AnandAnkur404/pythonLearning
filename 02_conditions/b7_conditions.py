# age = 12
# if age>18:
#     print("you can vote")
# else:
#     print("you can't vote")

# marks = int(input("enter your marks"))

# if marks > 80:
#     print("Grade A")
# elif marks > 70:
#     print("Grade B")
# elif marks > 60:
#     print("Grade C")
# else:
#     print("fail!")

# questions

# age = int(input("enter age"))
# day = input("enter day").lower()
# if age > 12:
#     if day == "wednesday":
#         print("your ticekt price is 10$")
#     else:
#         print("your ticket price is 12$")
# else:
#     if day == "wednesday":
#         print("your ticekt price is 6$")
#     else:
#         print("your ticket price is 8$")

# question leap year
# question 
# snack = ["cookies", "samosa"]
# snack = input("Enter you preferred snacks samosa/cookies").lower()
# if "samosa" in snack or "cookies" in snack:
#     drink = input("Enter preferred dink coffee/chai").lower()
#     if drink == "coffee" or drink == "chai":
#         print(f"your {snack} and {drink} is preparing, Thanks for waiting!")
#     else:
#         print(f"you {snack} is preparing, Thanks for waiting!")
# else:
#     print("Out of stock")

# if total order of delivery > 300, delivery will be free else 30$

# total_amount = 600
# delivery_fees = 0
# if total_amount > 300:
#     delivery_fees = 0
# else:
#     delivery_fees += 30
# print(delivery_fees)


# delivery_fees = 0 if total_amount < 300 else 30
# print(delivery_fees)

seat_type = input("please enter your seat type ac/general/sleeper/luxury")

match seat_type:
    case "ac":
        print("your preferred seat type is ac")
    case "general":
        print("your preferred seat type is general")
    case "sleeper":
        # print("your preferred seat type is ac")
        pass
    case "luxury":
        print("your preferred seat type is ac")