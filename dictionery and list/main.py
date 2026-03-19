
from functions import data
from functions import users
import os
import time 

def program_menu()->None:
        print(
    """
    ================================================
    \n
    e - exsit
    q - add a test user
    w - add user
    r - data inf
    \n
    ================================================
    """)


def main(): 
    loaded_data:list[dict] = data.read_data()
    while True:
        program_menu()
        inp = input("- ").lower().strip()
        if inp == "e":
            print("The program has finished running")
            data.save_data(loaded_data)
            break
        elif inp == "q":
            loaded_data.append(data.create_test_user())
        elif inp == "w":
            new_user = users.add_new_user(loaded_data)
            loaded_data.append(new_user)
            data.save_data(loaded_data)
        elif inp == "r":
            data.print_all_data(loaded_data)
        elif inp == "t":
            pass
        elif inp == "y":
            pass
        elif inp == "u":
            pass
        elif inp == "i":
            pass
        elif inp == "o":
            pass
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("There is no such command")
            time.sleep(2)


if __name__ == '__main__':
    main()

# loaded_data:list[dict] = data.read_data()
# i=0
# for slownik in loaded_data:
#     print(f"{i} --- {slownik.get("id")} --- {slownik.get("name")}")
#     i+=1
# inp = int(input(":"))
# loaded_data.pop(inp)
# print(loaded_data)