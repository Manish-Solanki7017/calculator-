# Define a function for each operation
def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def mul(x, y):
  return x * y

def div(x, y):
  if y == 0:
    raise ValueError("Cannot divide by zero!")
  return x / y

# Define a main function to handle user input
def calculator():
  print("Simple Arithmetic Calculator")
  print("----------------------------")

  while True:
    # Get user input
    num1 = float(input("Enter the first number: "))
    op = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Perform the operation
    if op == "+":
      result = add(num1, num2)
    elif op == "-":
      result = sub(num1, num2)
    elif op == "*":
      result = mul(num1, num2)
    elif op == "/":
      result = div(num1, num2)
    else:
      print("Invalid operator!")
      continue

    # Print the result
    print(f"{num1} {op} {num2} = {result:.2f}")

    # Ask if user wants to continue
    response = input("Do you want to continue? (y/n): ")
    if response.lower() != "y":
      break

# Call the main function
calculator()