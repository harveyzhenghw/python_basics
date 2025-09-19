num = 10

while num >= 10:

    print (num)
    num += 1
    user_input = input("type Y for exit")
    if user_input == "y" or user_input == "Y":
        break


print("loop ended because of break")