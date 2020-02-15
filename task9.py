'''
In mathematics, the factorial of an integer n, denoted by n! is the following
product:
n!=1×2×...×n
For the given integer n
calculate the value n!. Don't use math module in this exercise.

'''



def factorial_int_num(number):
    factorial = 1
    for i in range(2, number+1):
        factorial *= i
    print(factorial)

factorial_int_num(5)