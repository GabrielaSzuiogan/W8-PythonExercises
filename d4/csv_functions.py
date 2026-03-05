import csv

#view_records
def show_db(file_name = str):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    file.close()

#init_db
def init_db(file_name = str, file_header = str):
    with open(file_name, "w") as file:
        writer = csv.writer(file)
        writer.writerow(file_header)
    file.close()
    print("\nHeader added!")
    show_db(file_name)


#add_record
def add_db(file_name = str, data = str):
    with open(file_name, "a") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    file.close()
    print("\nRecord added!")
    show_db(file_name)


#search_record
def search_db(file_name = str, search_item = str):
    aux = False
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if search_item in row:
                print(f"Item found in record {row[0]}: {row}")
                aux = True
    if aux is False:
        print("Item not found!")
    file.close()

#delete_record
def delete_db(file_name = str, delete_item = str):
    file_content = []
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if delete_item not in row:
                file_content.append(row)
    if len(file_content) == 0:
        print("Item not found to delete the record!")
    else: 
        print("Record deleted!")
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(file_content)
        show_db(file_name)
# ---- hw1
#update_record

#auto_incr

#schema