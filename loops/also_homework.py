height = int(input("select height: "))

for i in range(height):
    spaces = ''*(height - i - 1)
    asterisks = '* ' * (i + 1)
    print(spaces + asterisks)
    pass