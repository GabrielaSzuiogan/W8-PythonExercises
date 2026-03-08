#reads from txt (p1 + p2)
def read_file(file_name : str):
    with open(file_name, "r") as file:
        content = file.read()
    return(content)

#writes content in a file (p1)
def write_content(file_name : str, file_content : str):
    with open(file_name, "w") as file:
        file.write(file_content)
    print("Content added!")



#add: delete content
def delete_content(file_name :str):
    with open(file_name, "w") as file:
        file.write("")
    print("Content deleted!")


#read line by line (p2)
def read_file_lines(file_name : str):
    word_list = []
    with open(file_name, "r") as file:
        for line in file:
            word_list.extend(line.split())
    print(f"There are {len(word_list)} words")
