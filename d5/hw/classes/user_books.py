import os
import sys

from d5.hw.classes import books

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../../.."))
sys.path.append(root_dir)

from d4 import json_functions as j_func  # noqa



class UserBooks:
    def __init__(self, books_instance : books.Books ):
        self.file = "userbooks.json"
        j_func.init_db(self.file)
        self.books_table = books_instance

    def add_book(self, id_user: int, id_book: int):
        if self.has_read_book(id_user, id_book):
            print(f"Duplicate!: User {id_user} already has Book {id_book}.")
            return

        new_relation = {"id_user": id_user, "id_book": id_book}
        j_func.add_db(self.file, new_relation)

    def get_books(self, id_user: int):
        relations = j_func.get_db(self.file)
        user_books_details = []

        for row in relations:
            if row.get("id_user") == id_user:
                book_id = row.get("id_book")
                book_details = self.books_table.get(book_id)
                if book_details:
                    user_books_details.append(book_details)

        return user_books_details

    def has_read_book(self, id_user: int, id_book: int):
        relations = j_func.get_db(self.file)
        for row in relations:
            if row.get("id_user") == id_user and row.get("id_book") == id_book:
                return True
        return False

    def remove_book(self, id_user: int, id_book: int):
        relations = j_func.get_db(self.file)
        new_relations = []
        
        for row in relations:
            if not (row.get("id_user") == id_user and row.get("id_book") == id_book):
                new_relations.append(row)
                
        j_func.upd_db(self.file, new_relations)