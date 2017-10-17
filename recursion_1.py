#! /usr/bin/env python3

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

num = float(input("Write the number you want to get the factorial : "))
print(factorial(num))