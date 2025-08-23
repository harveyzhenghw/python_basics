''' january, february - 150$
● march, april - 199$
● may, june - 249$
● july, august, september - 299$
● october - 249$
● november, december - 199$'''
print("hello welcome to the park")
month = input("input the month: ").strip().lower()

if month == ("january") or month == ("febuary"):
    print("the price is 150 usd")
elif month == ("march") or month == ("april"):
    print("the price is 199 usd")
elif month == ("may") or month == ("june"):
    print("the price is 249 usd")
elif month == ("july") or month == ("august") or month == ("september"):
    print("the price is 299 usd")
elif month == ("october"):
    print("the price is 249 usd")
elif month == ("november") or month == ("december"):
    print("the price is 299 usd")
else:
    print("that is not a month")
