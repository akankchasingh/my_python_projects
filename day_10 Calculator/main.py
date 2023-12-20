
print("Welcome to Akankcha's calculator!")
#add
def add(n1, n2):
    return n1 + n2
#subtract
def subtract(n1, n2):
    return n1 - n2
#multiply
def multiply(n1, n2):
    return n1 * n2
#divide
def divide(n1, n2):
    return n1 / n2

operations = {  "+": add,
                "-": subtract,
                "*": multiply,
                "/": divide}

should_continue = True

first_num = float(input("Enter the first number: "))
while should_continue:
    second_num = float(input("Enter the second number: "))
    print("The operations available are: ")
    for keys in operations:
        print(keys)

    input_operation = input("Enter an operation from the above set: ")
    answer = operations[input_operation](first_num,second_num)
    print(f"The result is {first_num} {input_operation} {second_num} = {answer}")
    # Re-calculation on the answer
    repeat = input("Do you want to continue calculation on the result? Y or N: ").upper()
    if repeat == "Y":
        first_num = answer
    else:
        should_continue = False

print("Thank you for using Akankcha's calculator")


