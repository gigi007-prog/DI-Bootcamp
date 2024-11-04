#exercise 1
#my_fav_numbers={19,7,5,3,11,13}
#my_fav_numbers.add(1)
#my_fav_numbers.add(9)
#my_fav_numbers.discard(13)

#friend_fav_numbers={4,2,6,8}
#our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
#print(our_fav_numbers)

#exercise2
#you cant add on once a tuple is created

#exercise 3
#basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#basket.pop(0)
#basket.pop(2)
#basket.append("Kiwi")
#basket.insert(0,"Apples")
#amount_apples=basket.count("Apples")
#print(amount_apples)
#basket.clear()
#print(basket)

#Exercise 4
#an integer is a whole number and a float is a number with a dot like 1.5
#float_list = [1.5 + 0.5 * i for i in range(8)]
#print(float_list)

#Exercise 5
#for number in range(1, 21):
    #print(number)

#for number in range(1,21):
    #if (number %2 == 0):
        #print(number)

#Exercise 6
#my_name="Gigi"
#while True:
    #user_name=input("Please write your name here")
    #if user_name==my_name:
        #print("Hello World!")
        #break
    #else:
        #print("Try again.")

#Exercise 7
#fruits_in=input("Please list your favorite fruits with space between each fruit")
#favorite_fruits=fruits_in.split()

#choose_a_fruit=input("Choose one fruit")

#if choose_a_fruit in favorite_fruits:
     #print("You chose one of your favorite fruits! Enjoy!")
#else:
    #print("You chose a new fruit. I hope you enjoy.")

#Exercise 8
#topping=[]
#while True:
    #toppings=input("Write a pizza topping if you want to stop type quit  ")
    #if toppings == 'quit':
    #    break
    #else:
       # topping.append(toppings)
       # print(f"I'll add {toppings} to your pizza!")

#pizza_price=10
#topping_price=2.5
#price_in_total= pizza_price +(len(topping)*topping_price)

#print("\nYour pizza has these toppings:")
#for toppings in topping:
#    print(f"- {toppings}")

#print(f"\nTotal price: ${price_in_total:.2f}")

#Exercise 9 
# cost=0
# number_family_members=int(input("How many family members in your family?"))

# for _ in range(number_family_members):
#     age = int(input("Enter the age of the family member: "))

#     if age <3:
#          price_ticket=0
#     elif 3 <= age <= 12:
#         price_ticket = 10
#     else:
#          price_ticket=15
#     cost += price_ticket


# print(f"The total cost of the tickets is:{cost}")

# teens=['Catherine','Mike','Charles','Linda']
# print("List of teenagers before:", teens)

# teenagers_permitted= []
# for a in teens:
#      age = int(input(f"Enter the age of {a}: "))
#      if 16 <= age <= 21: 
#         teenagers_permitted.append(a)  
#      else:
#         print(f"{a} is not permitted to watch the movie.")

# print("Teenagers that are permitted:", teenagers_permitted)

#Exercise 10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches=[]
empty=True
while sandwich_orders:
    now_sandwich=sandwich_orders.pop()
    finished_sandwiches.append(now_sandwich)
    print("I made your", now_sandwich)
    

print(finished_sandwiches)
