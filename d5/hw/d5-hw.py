from classes import books, users, user_books

users = users.Users()
books = books.Books()
user_books = user_books.UserBooks(books)


users.add("Alice", "alice@example.com")
users.add("Bob", "bob@example.com")
books.add("1984", "George Orwell", 1949)
books.add("Python Crash Course", "Eric Matthes", 2015)


user_books.add_book(1, 1) 
user_books.add_book(1, 2) 
user_books.add_book(1, 1)  #duplicate

print("\nAlice's current books:")
for book in user_books.get_books(1):
    print(f"{book['title']} by {book['author']}")

user_books.remove_book(1, 1)

print("\nAlice's books after returning '1984':")
for book in user_books.get_books(1):
        print(f"{book['title']} by {book['author']}")