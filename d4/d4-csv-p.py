import csv_functions

file_name= "./d4/my_db.csv"

header = ["NR CRT", "NAME", "AGE", "GRADE"]
csv_functions.init_db(file_name, header)

data = [
    [1, "Alana", 22, "B"],
    [2, "BobConstructorul", 67, "A"],
    [3, "Claudiu", 26, "C"],
    [4, "Deli", 21, "A"],
    [5, "Ed", 23, "B"],
]
csv_functions.add_db(file_name, data)

inp_item = input("Search an item: ")
csv_functions.search_db(file_name, inp_item)

inp_item = input("Delete an item: ")
csv_functions.delete_db(file_name,inp_item)
