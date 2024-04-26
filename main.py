print("Welcome to the tip calculator")
bill = float(input("What was the bill? "))
tip = float(input("How much tip would you like to give? "))
people = float(input("How many people to split the bill? "))

tip_for_one = bill / people / 100 * tip
bill_for_one_person = bill / people + tip_for_one
print(bill_for_one_person)

rounded_bill_for_1 = format(bill_for_one_person, ".2f")

print(f"Each person should pay: ${rounded_bill_for_1}")
