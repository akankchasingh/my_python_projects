print("Welcome to the Akankcha's tip calculator")
bill = int(input("What was the total bill ?:"))
number = int(input("How many people do you want to divide the bill into? : "))
tip_percent = int(input("How much tip do you want to pay in percentage : 10, 12 or 15 ?: "))
tip_value = (tip_percent/100) * bill
total_bill = round((bill+tip_value),2)

print(f"The total bill is Rs {total_bill}")
each_bill = total_bill / number
print(f"Each person has to pay Rs {each_bill}")



