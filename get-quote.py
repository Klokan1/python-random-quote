import random

def primary():

    f = open("C:\\Users\Admin\OneDrive\Projekte\Atom Projekte\Python\Github\quotes.txt")
    quotes = f.readlines()
    f.close()

    last = len(quotes) - 1
    rnd = random.sample(range(0, last), 2)
    print(quotes[rnd[0]], quotes[rnd[1]])

    

if __name__== "__main__":
    primary()
