# Data types

# String
# integer
# float
# boolean34

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
two_digit_number = str(two_digit_number)
# first = two_digit_number[0]
# second = two_digit_number[1]
f = int(two_digit_number[0]) + int(two_digit_number[1])
print(f)



# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


age = int(age)

Days = 365*90
months = 12 * 90
week = int(Days/12)/7
yearweek = int(365/7)
print(yearweek)
Daysleft_to_go = Days-(365*age)
months_to_go = months-(12*age)
weeks_to_go = week-(age*yearweek)
print(f"you have {Daysleft_to_go} days, {months_to_go} weeks , and {weeks_to_go} months left")




#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

finbill = int(input("bill val " ))
noofpeop = input("no of pepo ")
tip = finbill*(12/100)
each_bill = int(finbill)/int(noofpeop)+float(tip)
print(round(each_bill, 2))
