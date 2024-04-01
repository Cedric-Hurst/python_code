from art import logo
from replit import clear

def add(num1, num2):
  return num1 + num2
def subtract(num1, num2):
  return num1 - num2
def divide(num1, num2):
  return num1 / num2
def multiply(num1, num2):
  return num1 * num2

ops = {
  "+" : add,
  "-" : subtract,
  "/" : divide,
  "*" : multiply,
      }
def calculator():
  print(logo)
  calculator_running = True
  num1 = float(input("What's the first number?: "))
  
  while calculator_running:
    print("+\n-\n*\n/\n")
    operation = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    
    ops_function = ops[operation]
    answer = ops_function(num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
    
    cont = input(f"Type 'y' to continue with {answer} or'n' to start over ").lower()
    if cont == 'y':
      num1 = answer
    else:
      clear()
      calculator_running = False
      calculator()
calculator()
