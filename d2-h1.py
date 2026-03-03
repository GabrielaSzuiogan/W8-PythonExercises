passw = input("Introduceti o parola: ")

if len(passw) > 8:
    if any(c.isupper() for c in passw):
        if any(c.isdigit() for c in passw):
            print("Strong password!")
        else:
            print("Password should contain at least a digit!")
    else:
         print("Password should contain at least an uppercase!")
else:
    print("Password too weak!")