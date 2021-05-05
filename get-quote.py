import random


def primary():

    User_input = input("Would you like to \"add\" or \"delete\" a quote?")
    if User_input == "add":
        with open("C:\\Users\Admin\OneDrive\Projekte\Atom Projekte\Python\Github\quotes.txt", "a") as f:
            User_input = input("What would you like to add?")
            f.write(f"This has been added by a user: {User_input}\n")

    elif User_input == "delete":
        with open("C:\\Users\Admin\OneDrive\Projekte\Atom Projekte\Python\Github\quotes.txt", "r") as f:
            lines = f.readlines()
            User_input = input("Which line would you like to delete?")
            User_input = User_input.strip("-")

        if "-" in User_input:
            print(User_input)
            two_numbers = list(map(int, User_input.split("-")))
            print(two_numbers)
            if max(User_input) <= len(lines):


        if User_input.isnumeric():
            User_input = int(User_input)
            if User_input <= len(lines):
                del(lines[User_input - 1])
                with open("C:\\Users\Admin\OneDrive\Projekte\Atom Projekte\Python\Github\quotes.txt", "w") as f:
                    for line in lines:
                        f.writelines(line)
            else:
                print("Sorry you can't delete a line that doesn't exist...")
        else:
            print("You have to input a number!")
    else:
        print("I can't understand that...")


    # with open("C:\\Users\Admin\OneDrive\Projekte\Atom Projekte\Python\Github\quotes.txt", "w") as f:
        # for line in lines:
        # if line.strip("\n") != "This has been added!":
        # f.write(line)
    # quotes = f.readlines()
    # last = len(quotes) - 1
    # rnd = random.sample(range(0, last), 2)
    # print(quotes[rnd[0]], quotes[rnd[1]])
    # print(lines)
if __name__ == "__main__":
    primary()
