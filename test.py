name = "Gabi"
print(f"Hello {name}")

# Logical operators
a = 5
b = 8
print((a > b) and True)
print((a > b) or True)
print(not False)


# Bitwise operators
c = 7
d = 4
print(f"We have c = {c} and d = {d} ")
print("c & d = ", c & d)
print("c | d = ", c | d)
print("c ^ d = ", c ^ d)
print("~d = ", ~d)
print("c>>1= ", c >> 1)
print("c<<1= ", c << 1)


# Special operators
x = c
print(c is x)

word = "Peach"
print("is 'a' in Peach? ", 'a' in word)
print('p' not in word)



n1 = input("n1 = ")
n2 = input("n2 = ")
print("Is {} > {}? {}".format(n1,n2,n1>n2))