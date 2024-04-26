# If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the tip calculator")
bill = float(input("What was the bill? "))
tip = float(input("How much tip would you like to give? "))
people = float(input("How many people to split the bill? "))

# Each person should pay (150.00 / 5) * 1.12 = 33.6

tip_for_one = bill / people / 100 * tip
bill_for_one_person = bill / people + tip_for_one
print(bill_for_one_person)


# Format the result to 2 decimal places = 33.60
rounded_bill_for_1 = format(bill_for_one_person, ".2f")

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


# Write your code below this line 👇

print(f"Each person should pay: ${rounded_bill_for_1}")
