#1
def is_even(numb):
    return numb%2==0 and True

numb = int(input("Enter a number: "))
print(is_even(numb))

#2
def find_max(a, b):
    if a > b:
        return a
    else:
        return b
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print(find_max(a,b))


#3
def count_vowels(phrase):
    count = 0
    for c in phrase:
        if c.lower() in 'aeiou':
            count += 1
    return count

phr = input("Write something: ")
nr= count_vowels(phr)
print(f"Phrase contains {nr} vowels")

#4
def sum_nr(ls):
    sum = 0
    for item in ls:
        if type(item) == int or type(item) == float:
            sum += item
    return sum

result = sum_nr([2,3,"f",4,"33"])
print(f"result= {result}")

#5 
def find_nr(nr, ls):
    return str(nr) in ls and True

li = input("Enter elements separated by space: ").split()
print("List:", li)
nr = int(input("Find: "))
print(find_nr(nr,li))