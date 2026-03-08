import book_class
import vehicle_class

print("\n--BOOK PRACTICE--")
book1 = book_class.Book("1984", "George Orwell", 1949 )
book1.get_info()

book2 = book_class.Book("To Kill a Mockinbird", "Harper Lee", 1960 )
book2.get_info()


print("\n--VEHICLE PRACTICE--")
car = vehicle_class.Car("Toyota", 1949, "Petrol")
car.display_info()