#Defining and calling the Python functions:

# creating my function:
#
# def addition(a, b):
#     c = a + b
#     # return c
#     print(c)
#
# addition(2, 3)
#
# # learned loops
# import random
#
#
# abz = []
# for ii in range(1, 5):
#     abc =random.randint(1, 100)
#     abz.append(abc)
#
# print(abz)

# a = int(input())
# b = int(input())
# while a > b:
#     print("rama rama")
# else:
#     print("this is joke ")
#


# import random
# a = random.randint(1, 100)
# a1 = random.randint(1, 79)
# while a > a1:
#     print("rama rama")
#     if a > a1:
#         print("infinite loop ")
#         break
# else:
#     print("this is joke ")




import random

def shout():
    a = random.randint(1, 100)
    b = random.uniform(1, 5)
    print(f"{a}+{b}")


shout()

ab = random.randint(1, 200)
while ab > 100:
    shout()
    if ab > 50:
        break





