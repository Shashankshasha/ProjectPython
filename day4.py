# Randomisation & python List:

import random
#
# p = random.randint(1, 100)
# print(p)
# if p % 2 == 0:
#     print("Value is even")
# else:
#     print("this is odd")
#


# Head or tail
#
# a = random.randint(1, 2)
# if a == 1:
#     print("head")
# else:
#     print("tail")
#


# list of details fruilts:

# fruits = ["Strawberry", "Blueberry", "Raspebrry", "Blackberry", "Boysenberry", "Cranberry"]
# fruits[1]
# print(fruits)
# for i in fruits:
#     print(i)
# #
# rev = fruits
# rev.reverse()
# for i in rev:
#     print(i)


# Challange hotel bill
# testing split function

# fruits_str0 = "Strawberry, Blueberry, Raspebrry, Blackberry, Boysenberry, Cranberry"
# fruits_str = fruits_str0.split(",")
# fruits_strlen = len(fruits_str)
# # print(fruits_strlen)
# ran_choice = random.randint(0, fruits_strlen-1)
# person_to_pay = fruits_str[ran_choice]
# print(person_to_pay)



# fruits_choice = "Strawberry, Blueberry, Raspebrry, Blackberry, Boysenberry, Cranberry"
#
# choi = fruits_choice.split(", ")
# outchoi = random.choice(choi)
# print(outchoi)
#


# ROCK PAPER SCESSIORS


#  need to check back

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

az = [rock, paper, scissors]
print(az[0:-1])
length = len(az)
print(length)
complayer = random.choice(az)
print(complayer)
player = input("value game player  rock ,paper ,scissors :")

if complayer == player:
    print("draw ")
elif complayer == rock:
    print("complayer is winner")
elif complayer == scissors and player == paper:
    print("complayer is winner")
else:
    print("player is a winner :")









