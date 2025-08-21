match_win = int((input("input the number of matches you won")))
match_lose = int((input("input the number of matches you lost")))
MVP = int((input("input the number of times you won the MVP")))

if match_win >= 10 and match_win > match_lose or MVP >= 7:
    print("you passed to the next round")
else:
    print("you didn't pass")