import csv_functions
import json_functions

file_type = input("Choose file type between CSV and JSON: ")

if file_type.lower() == "csv":
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
elif file_type.lower() == "json":
    print("Choosed json")
    file_name = "./d4/my_db.json"
    json_functions.init_db(file_name)

    data = [
        {"name": "Alana", "age": 22, "grade": "B"},
        {"name": "BobConstructorul", "age": 67, "grade": "A"},
        {"name": "Claudiu", "age": 26, "grade": "C"},
        {"name": "Deli", "age": 21, "grade": "A"},
        {"name": "Ed", "age": 23, "grade": "B"},
    ]
    json_functions.add_db(file_name, data)

    inp_item = input("Search an item: ")
    json_functions.search_db(file_name, inp_item)

    inp_item = input("Delete an item: ")
    json_functions.delete_db(file_name, inp_item)


else:
    print("Not a valid file type choice!")