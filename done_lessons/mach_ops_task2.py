'''Create a program which asks the user for two numbers and then prints into the
terminal the result of division along with the remainder. F.e. for data 48, 10
program should output: 48 divided by 10 is equal to 4, remainder: 8.
Use fstring and integral division along with modulo.'''

num_1 = int(input("enter first number: "))
num_2 = int(input("enter second number: "))
quotient = (num_1//num_2)
remainder = (num_1%num_2)
print(f"{num_1} divided by {num_2} is equal to {quotient} and remainder: {remainder}")