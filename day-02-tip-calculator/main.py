#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
float_total_bill= float(total_bill)
tip = input("How much tip would you like to give? 10, 12, or 15? ")
float_tip = float(tip)
people = input("How many people to split the bill? ")
int_people = int(people)

each_person = (float_total_bill*(1 + float_tip/100))/int_people

print(f"Each person should pay: ${round(each_person, 2)}")
