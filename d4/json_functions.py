import json

#show file content
def show_db(file_name: str):
    with open(file_name, "r") as file:
        data = json.load(file)
        for row in data:
            print(row)

#initialise
def init_db(file_name: str):
    with open(file_name, "w") as file:
        json.dump([], file)
    print("\nDatabase initialized!")

def upd_id(file_name : str):
    with open(file_name, "r") as file:
        data = json.load(file)
        if len(data) == 0:
            return 1
        return data[-1]["id"] + 1
    
#add data
def add_db(file_name : str, added_data: list):
    with open(file_name, "r") as file:
        data = json.load(file)
    next_id = upd_id(file_name)
    for item in added_data:
        new_data = {"id" : next_id}
        new_data.update(item)
        data.append(new_data)
        next_id += 1

    with open(file_name, "w") as file:
        json.dump(data, file)

    print("\nNew data added!")
    show_db(file_name)

#search record
def search_db(file_name: str, search_item: str):
    aux = False
    with open(file_name, "r") as file:
        data = json.load(file)
        for row in data:
            for val in row.values():
                if str(search_item) == str(val):
                    print(f"Item found in record {row['id']}: {row}")
                    aux = True
                    break

    if not aux:
        print("Item not found!")

# delete_record
def delete_db(file_name: str, delete_item: str):
    file_content = []
    aux = False
    
    with open(file_name, "r") as file:
        data = json.load(file)
            
        for row in data:
            found_in_row = False
            for val in row.values():
                if str(delete_item) == str(val):
                    found_in_row = True
                    aux = True
                    break
            if not found_in_row:
                file_content.append(row)
                    
        if not aux:
            print("Item not found to delete the record!")
        else:
            print("\nRecord deleted!")
            with open(file_name, "w") as file:
                json.dump(file_content, file)
            show_db(file_name)
            
