people = {
    "Alice": {"age": 30, "city": "New York"},
    "Bob": {"age": 25, "city": "Los Angeles"},
    "Charlie": {"age": 35, "city": "Chicago"}
}

def oldest_pers(p):
    aux_dict = {}
    for index, value in p.items():
        aux_dict[index] = value["age"]
    return max(aux_dict, key=aux_dict.get)

print("Oldest person from dict:",oldest_pers(people))


def find_city(p):
    li = []
    for index, value in p.items():
        if value["city"] == "New York":
            li = index
    return li
print("Who lives in NY:", find_city(people))

