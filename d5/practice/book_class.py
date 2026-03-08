# title string
# author string
# year int
# method get_info() -> formatted string with book details
# create 2 obj and print their details using get_info()


class Book:
    title = ""
    author = ""
    year = 0

    def __init__(self, title: str, author: str, year : int):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        print(f"TITLE: {self.title}, AUTHOR: {self.author}, YEAR: {self.year} ")
    


