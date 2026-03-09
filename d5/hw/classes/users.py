import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../../.."))
sys.path.append(root_dir)

from d4 import json_functions as j_func  # noqa


class Users:
    def __init__(self):
        self.file = "users.json"
        j_func.init_db(self.file)

    def add(self, name: str, email: str):
        new_user = {"name": name, "email": email}
        return j_func.add_db(self.file, new_user)

    def list(self):
        return j_func.get_db(self.file)

    def get(self, user_id: int):
        return j_func.search_db(self.file, user_id)

    def delete(self, user_id: int):
        j_func.delete_db(self.file, user_id)