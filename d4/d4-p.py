import file_functions

#p1
file_content = file_functions.read_file("./d4/source.txt")
file_destination = "./d4/copy.txt"

file_functions.write_content(file_destination, file_content)
# file_functions.delete_content(file_destination)

#p2
file_functions.read_file_lines("./d4/story.txt")
