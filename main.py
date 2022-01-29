#Calculator app

def addition(n1, n2):
  return n1 + n2

def multiplication(n1, n2):
  return n1 * n2

def division(n1, n2):
  return n1 / n2

def subtraction(n1, n2):
  return n1- n2

tasks = {
  "+": addition,
  "*": multiplication,
  "/": division,
  "-": subtraction

}

num1 = int(input("Type your first number: "))
num2 = int(input("Type your second number: "))


for operator in tasks:
  print(operator)

tasks_operator = input("Select from the line above: ")


calculate_tasks = tasks[tasks_operator]
result=calculate_tasks(num1, num2)

print(f"{num1} {tasks_operator} {num2} = {result}")
