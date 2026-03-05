# Remove duplicates
def rem_dupl(li):
    return set(li)

in_li = [1,2,"ab", "a", "A", "ab",2, 10]
print(rem_dupl(in_li))

#Cea mai mare varsta
def varsta_mare(li):
    max_v = 0
    name = ""
    for it in li:
        if it[1] > max_v:
            max_v = it[1]
            name = it[0]
    return name

li = [("Andrei", 20), ("Maria", 191), ("Cristi", 22), ("Simo", 19)]
print("Cea mai mare varsta o are", varsta_mare(li))

#frecv din tuplu
def nr_frecv(li):
    if not li:
        return None
    freq = {}
    for it in li:
        freq[it] = freq.get(it, 0) +1
    return max(freq, key=freq.get)

print("Cel mai frecvent numar: ", nr_frecv((1,2,3,1,1,2,1,3)))

# frecv din text
def string_frecv(li):
    if not li:
        return None
    freq = {}
    words = li.split()
    for it in words:
        freq[it] = freq.get(it, 0) +1
    
    max_i = max(freq, key=freq.get)
    max_v = freq[max_i]
    return (max_i, max_v)
    
i, v = string_frecv("apple banana apple orange banana apple")
print(f"Cel mai frecvent cuvant -{i}- apare de -{v}- ori " )


#rev dict
def rev(dict):
    new_dict = {}
    for key, value in dict.items():
        new_dict[value] = key
    return new_dict

init_dict = {
    "A" : 22,
    "B" : 25,
    "C" : 21,
    "D" : 29
}
print("Dictionarul initial: ", init_dict)
print("Dictionarul reversat: ", rev(init_dict))
