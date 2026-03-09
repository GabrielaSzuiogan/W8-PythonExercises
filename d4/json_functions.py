import json

#show file content
def get_db(file_name: str):
    with open(file_name, "r") as file:
        return json.load(file)

#init
def init_db(file_name: str):
    with open(file_name, "w") as file:
        json.dump([], file)
    print("\nDatabase initialized!")

#update db
def upd_db(file_name: str, data: list):
    with open(file_name, "w") as file:
        json.dump(data, file)

#update next id
def upd_id(file_name : str):
    data = get_db(file_name)
    if len(data) == 0:
        return 1
    return data[-1]["id"] + 1
    
#add data
def add_db(file_name : str, added_data: dict):
    data = get_db(file_name)
    new_id = upd_id(file_name)
    added_data["id"] = new_id
    
    data.append(added_data)
    upd_db(file_name, data)
    return new_id

#search record
def search_db(file_name: str, search_id: int):
    aux = False
    data = get_db(file_name)
    for row in data:
        if row.get("id") == search_id:
            print(f"Item found: {row}")
            aux = True
            break
    if not aux:
        print("Item not found!")

# delete_record
def delete_db(file_name: str, delete_id: int):
    data = get_db(file_name)
    new_data = []
    
    for row in data:
        if row.get("id") != delete_id:
            new_data.append(row)
            
    upd_db(file_name, new_data)
