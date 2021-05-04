import random

def primary():
    print("Keep it logically awesome.")

    f = open("C:\\Users\Admin\OneDrive\Projekte\Atom Projekte\Python\Github\quotes.txt")
    quotes = f.readlines()
    f.close()

    print(quotes[13])

if __name__== "__main__":
    primary()


 
