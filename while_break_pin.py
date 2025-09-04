Pin = 1234

while True:
    user_input = int(input("input your pin to see super secret stuff").strip())
    if  Pin == user_input: 
        break 
    else:
        count_mistakes += 1
        if count_mistakes >=3:
            print("you type the wrong pin 3 times")
            print("now you will never see the secret")
            break

        print("wrong pin")
        print(f"You made {count_mistakes}mistakes.")
        print("if you make 3 pin mistakes you will never ssee the super secret stuff")

        print("try again")

if count_mistakes < 3:
    print("your pin is corect")
    print("here is the super secret stuff")
    print("cats like to sleep is a big secret")   

