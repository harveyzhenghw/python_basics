# > grater then
# < less then
# == equal
# != not equal
# <= less then or equal
# >= grater then or equal

print(12 > 15) # False # ==, <, !=, <=
print(5 < 15000) # True # ==, >, >=, <=
print(120 != 120) # False # ==, >=, !=, <=
print(60 < 15) # False # ==, <, !=, >=
print(25.3421 == 25.3421) # True # ==, <, !=, <=

has_money = False
is_high_enough = True

print(is_high_enough and has_money)

# OR => means at least one need to be true

has_money = False
dad_will_give_money = False

print(has_money or dad_will_give_money)

# not is flipping the value

print(not has_money)

