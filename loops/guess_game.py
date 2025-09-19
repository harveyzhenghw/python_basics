import random


MIN = 1
MAX = 100

random_number = random.randint(MIN,MAX)

guess = None
turn_count = 0

print(f"Lets play a guessing game!")
while guess != random_number:
    guess = int(input("enter your number: "))
    turn_count += 1

    if guess < random_number:
        print("too small!!!")
    elif guess > random_number:
        print("too big!!!")

print("congratulations for guessing the correct number!!")
print(f"the number was {random_number}")
print(f"number of tries {turn_count}")