
# Project Time

# Greeting message
print("Welcome to the tip calculator.\n")

# getting the total bill
total_bill = float(input("what was the total bill? $"))

# getting the % tip
tip_percentage = int(input("What % tip would you like to give? 10, 12, or 15 "))



# Getting the number of total people
total_persons = int(input("How many people to split the bill? "))

final_bill = total_bill + (total_bill * (tip_percentage / 100))

print(tip_percentage / 100)

each_person_pays = round(final_bill / total_persons, 2)

print(f"Each person should pay: ${each_person_pays}")

