# question 1: to check entered age comes in which category
# age = int(input("Enter your age : "))

# if age < 13:
#     print("hi child")
# elif age < 20:
#     print("this is teen, welcome in wanna be adult life")
# elif age < 60:
#     print("Hi boomers")
# else:
#     print("Ooh seniors, let god bless you!")

#question 2: ticket pricing

# age = 20
# day = input("enter days of a week")

# if day == "wednesday":
#     if age > 13:
#         print("tickect price is 10$")
#     else:
#         print("Ticket pirce is 6$")
# else:
#     if age > 13:
#         print("tickect price is 12$")
#     else:
#         print("Ticket pirce is 8$")

# price = 12 if age >= 19 else 8
# day = "wednesday"
# if day == "wednesday": 
#     price -= 2
# print("Price is $", price)

# Question 3. Grade calculator
# grade = 109
# if grade >= 101:
#     print("Check your grade again from your teacher")
#     exit()
# if grade > 90:
#     print("Grade A+")
# elif grade > 80:
#     print("Grade A")
# elif grade > 70:
#     print("Grade B")
# elif grade > 60:
#     print("Grade C")
# elif grade > 50:
#     print("Grade D")
# else:
#     print("you can study to score grade c at least.")

# question 4. fruit rippen or not

# color1="brown"
# fruit = "banana"
# if fruit == "banana":
#     if color1=="Green":
#         print("Unripe")
#     elif color1=="brown":
#         print("Ripe")
#     else:
#         print("not to eat")

#Weather

# weather = "Sunny"
# if weather == "Sunny":
#     activity = "Go for a walk"
# elif weather == "Rainy":
#     activity = "Read a book"
# else:
#     activity = "build a snowman ball"
# print(activity)

#question 1: smart kettle notification system
# is_kettle_boiled = True
# if is_kettle_boiled: #this evaluates as true or false
#     print("Kettle done! Time to make coffee")
# else:
#     print("Do nothing")

# #Question 2: snacks suggestions system for customers
# snack = input("Enter your preffered snacks ").lower() #convert user input into lower case. 
# # print(f"user said : {snack}")
# if snack == "cookies" or snack == "samosa":
#     print("your order is preparing!")
# else:
#     print("we are only serving cookies and samosa")

#Question 3: Tea stall- different price for different cup size Chai price calculator
# cup_size = input("enter cup size from (small / medium / large)").lower()
# if cup_size == "small":
#     print("kindly pay 10")
# elif cup_size == "medium":
#     print("kindly pay 15")
# elif cup_size == "large":
#     print("kindly pay 20")
# else:
#     print("Unkown cup size")

#question 4: thermostat alert system
# device_status = "active"
# temperature = 39
# if device_status == "active":
#     if temperature > 35:
#         print("Temperature is high!")
#     else:
#         print("Temperature is normal")
# else:
#     print("device is offline")

#Question 5: Delivery fees waiver system
# order_amount = int(input("Enter total order amount: "))
# delivery_fees = 0
# if order_amount > 300:
#     delivery_fees = 0
# else:
#     delivery_fees = 30

# #using ternary operator
# delivery_fees = 0 if order_amount > 300 else 30

# print(f"Your delivery fees is : {delivery_fees}")

# question 6. Train seat type
# match and case 
# seat_type = input("enter your seat type (sleeper/AC/general/luxuary)").lower()

# match seat_type:
#     case "ac":
#         print("your preferred seat type is ac")
#     case "sleeper":
#         print("your preferred seat type is ac")
#     case "general":
#         print("general seat")
#     case "luxury":
#         print("here is your luxury seat type")