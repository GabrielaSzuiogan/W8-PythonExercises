import csv

#view_records
def show_db(file_name = str):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


#init_db
def init_db(file_name = str, file_header = str):
    with open(file_name, "w") as file:
        writer = csv.writer(file)
        writer.writerow(file_header)
    print("\nHeader added!")
    show_db(file_name)


#add_record
def add_db(file_name : str, data : str):
    next_id = upd_id(file_name)
    full_content = []
    for row in data:
        full_content.append([next_id] + row)
        next_id += 1
        
    with open(file_name, "a") as file:
        writer = csv.writer(file)
        writer.writerows(full_content)
    print("\nRecord added!")
    show_db(file_name)


#search_record
def search_db(file_name : str, search_item : str):
    aux = False
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if search_item in row:
                print(f"Item found in record {row[0]}: {row}")
                aux = True
    if aux is False:
        print("Item not found!")

#delete_record
def delete_db(file_name : str, delete_item : str):
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
def upd_db(file_name : str, select_record : str, new_record : list[str]):
    file_content = []
    aux = False
    with open(file_name, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if select_record in row:
                row = [row[0]] + new_record
                aux = True
            file_content.append(row)
    
    if not aux:
        print("Item not found")
    else: 
        print("\nRecord updated!")
        with open(file_name, "w") as file:
            writer = csv.writer(file)
            writer.writerows(file_content)
        show_db(file_name)
    

#auto_incr
def upd_id(file_name :str):
    with open(file_name, "r") as file:
        reader = list(csv.reader(file))
        if len(reader) <= 1:
            return 1
        last_id = int(reader[-1][0])
        return last_id + 1


#schema