import file_functions

file_content = file_functions.read_file("./d4/source.txt")
file_destination = "./d4/copy.txt"

file_functions.write_content(file_destination, file_content)

file_functions.delete_content(file_destination)