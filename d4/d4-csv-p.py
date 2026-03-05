import csv_functions

file_name= "./d4/my_db.csv"

header = ["NR CRT", "NAME", "AGE", "GRADE"]
csv_functions.init_db(file_name, header)

data = [
    [ "Alana", 22, "B"],
    [ "BobConstructorul", 67, "A"],
    [ "Claudiu", 26, "C"],
    [ "Deli", 21, "A"],
    [ "Ed", 23, "B"],
]
csv_functions.add_db(file_name, data)

inp_item = input("Search an item: ")
csv_functions.search_db(file_name, inp_item)

inp_item = input("Delete an item: ")
csv_functions.delete_db(file_name,inp_item)

updated_record = ["Rando", 20, "C"]
csv_functions.upd_db(file_name,"2",updated_record)
