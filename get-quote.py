import random

def primary():

    with open("C:\\Users\Admin\OneDrive\Projekte\Atom Projekte\Python\Github\quotes.txt", "r") as f:
        lines = f.readlines()
        #f.write("This has been added!\n")

    #del(lines[14])



    with open("C:\\Users\Admin\OneDrive\Projekte\Atom Projekte\Python\Github\quotes.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != "This has been added!":
                f.write(line)

    #quotes = f.readlines()
    #last = len(quotes) - 1
    #rnd = random.sample(range(0, last), 2)
    #print(quotes[rnd[0]], quotes[rnd[1]])
    print(lines)



if __name__== "__main__":
    primary()
