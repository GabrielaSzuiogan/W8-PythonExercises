passw = input("Introduceti o parola: ")

if len(passw) > 8:
    if not passw.islower():
        if not passw.isalpha():
            print("Strong password!")
        else:
            print("Password should contain at least a digit!")
    else:
         print("Password should contain at least an uppercase!")
else:
    print("Password too weak!")