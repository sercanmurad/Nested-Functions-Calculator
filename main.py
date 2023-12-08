def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

def calculator(n1,n2, func):
  return func(n1,n2)

number1=int(input("Please enter first number:"))
number2=int(input("Please enter second number:"))
result=calculator(number1,number2,add)
print(result)