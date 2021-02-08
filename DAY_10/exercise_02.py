# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num_1 = int(input("Enter First Number?: "))
for symbol in operations:
    print(symbol)
operation = input("Pick an Operation from the line above:")
num_2 = int(input("Enter Second Number?: "))
calculation_function = operations[operation]
answer = calculation_function (num_1, num_2)

print(f"{num_1} {operation} {num_2} = {answer}")

