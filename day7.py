 # Hangman Game



import random

check = ["apple", "maongo", "banana"]
chose_a_word = random.choice(check)
print(chose_a_word)

alpha = input("one alphabet\n")

for i in chose_a_word:
    if i == alpha:
        print("right")
    else:
        print("wrong")


