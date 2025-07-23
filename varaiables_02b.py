#float => int the decimal part of the number is cut off

a = int(5.5)
print(a,type(a))
a = int(False)
print(a,type(a))
a = int("10")
print(a,type(a))


b = float(55)
print(b,type(b))
b = float(False)
print(b,type(b))
b = float("10")
print(b,type(b))
b = float("3.1415")
print(b,type(b))



c = bool(55)
print(c,type(c))
c = bool(False)
print(c,type(c))
c = bool("")
print(c,type(c))
c = bool("3.1415")
print(c,type(c))
c = bool("5")
print(c,type(c))



d = str(55)
print(d,type(d))
d = str(False)
print(d,type(d))
d = str("")
print(d,type(d))
d = str("3.1415")
print(d,type(d))
d = str("5")
print(d,type(d))