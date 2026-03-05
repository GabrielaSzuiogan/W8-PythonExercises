word = input("Introduceti un cuvant: ")
count = 0
print("Vowels found: ")
for c in word:
    if c in "aeiouAEIOU":
        count += 1
        print(c)
if count == 0:
    print(0)
else:
    print(f"Total: {count} vowels")
