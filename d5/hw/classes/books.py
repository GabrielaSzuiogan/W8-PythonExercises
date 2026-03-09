import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../../.."))
sys.path.append(root_dir)

from d4 import json_functions as j_func  # noqa

class Books:
    def __init__(self):
        self.file = "books.json"
        j_func.init_db(self.file)

    def add(self, title: str, author: str, year: int):
        new_book = {"title": title, "author": author, "year": year}
        return j_func.add_db(self.file, new_book)

    def list(self):
        return j_func.get_db(self.file)

    def get(self, book_id: int):
        return j_func.search_db(self.file, book_id)

    def delete(self, book_id: int):
        j_func.delete_db(self.file, book_id)