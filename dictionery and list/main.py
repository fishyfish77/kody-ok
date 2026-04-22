from functions import data
from functions import users
import os
import time 

def program_menu()->None:
        print(
    """
    ================================================
    \n
    e - exit
    q - add a test user
    w - add user
    r - data inf
    t - add/remove grade(s)
    y - find user by id
    u - find user by name
    i - delete user by id
    o - update user's name
    p - update user's surname
    a - update user's dob
    s - check if name is taken
    d - show 1 user
    f - count all users
    g - count users with missing name
    h - avg math grades for user
    j - avg polish grades for user
    k - avg english grades for user
    l - avg all grades for user
    z - show the best user in the chosen subject
    x - avg grade in chosen subject for all students 
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
            users.add_or_remove_grades(loaded_data)
            data.save_data(loaded_data)
        elif inp == "y":
            user_id=int(input("enter user id: "))
            user = users.find_user_by_id(loaded_data,user_id)
            if user != None:
                print(f"found user with this id: {user}")
            else:
                print("user not found")
        elif inp == "u":
            name=input("enter users name: ")
            user = users.find_users_by_name(loaded_data,name)
            if user != None:
                print(f"found user(s) with this name: {user}")
            else:
                print("user(s) not found")
        elif inp == "i":
            user_id=int(input("enter user id: "))
            users.delete_user_by_id(loaded_data, user_id)
            data.save_data(loaded_data)
        elif inp == "o":
            user_id=int(input("enter user id: "))
            new_name=str(input("enter new name: "))
            users.update_user_name(loaded_data,user_id,new_name)
            data.save_data(loaded_data)
        elif inp=="p":
            user_id=int(input("enter user id:"))
            new_surname=str(input("enter new surname: "))
            users.update_user_surname(loaded_data,user_id,new_surname)
            data.save_data(loaded_data)
        elif inp=="a":
            user_id=int(input("enter user id: "))
            new_birth_date=str(input("enter new dob: "))
            users.update_user_birth_date(loaded_data,user_id,new_birth_date)
            data.save_data(loaded_data)
        elif inp=="s":
            name=str(input("enter name: "))
            surname=str(input("enter surname: "))
            users.is_name_taken(loaded_data,name,surname)
        elif inp=="d":
            user_id=int(input("enter user id: "))
            user=users.find_user_by_id(loaded_data,user_id)
            if user:
                users.show_one_user(user)
            else:
                print("user not found, data cannot be shown")
        elif inp=="f":
            print(f"number of users:{users.count_all_users(loaded_data)}")
        elif inp=="g":
            print(f"users with missing name: {users.count_users_with_missing_name(loaded_data)}")
        elif inp=="h":
            user_id=int(input("enter user id: "))
            user = users.find_user_by_id(loaded_data,user_id)
            if user:
                average_math=users.average_math_for_user(user)
                if average_math==None:
                    print("no math average available")
                else:
                    print(f"math average for this user: {average_math}")
            else:
                print("user not found, average cannot be shown")
        elif inp=="j":
            user_id=int(input("enter user id: "))
            user = users.find_user_by_id(loaded_data,user_id)
            if user:
                average_polish=users.average_polish_for_user(user)
                if average_polish==None:
                    print("no polish average available")
                else:
                    print(f"polish average for this user: {average_polish}")
            else:
                print("user not found, average cannot be shown")
        elif inp=="k":
            user_id=int(input("enter user id: "))
            user = users.find_user_by_id(loaded_data,user_id)
            if user:
                average_eng=users.average_eng_for_user(user)
                if average_eng==None:
                    print("no english average available")
                else:
                    print(f"english average for this user: {average_eng}")
            else:
                print("user not found, average cannot be shown")
        elif inp=="l":
            user_id=int(input("enter user id: "))
            user = users.find_user_by_id(loaded_data,user_id)
            if user:
                ovr_average = users.overall_average_for_user(user)
                if ovr_average==None:
                    print("cant calculate the average")
                else:
                    print(f"the overall average for user is: {ovr_average}")
            else:
                print("no user found, average cannot be calcuated")
        elif inp=="z":
            subject=input("enter subject: ")
            best_student=users.best_student_in_subject(loaded_data,subject)
            if best_student:
                print(f"the best student in {subject} is: {best_student}")
            else:
                print("no students found, cannot show the best one")
        elif inp=="x":
            subject=input("enter subject: ")
            average=users.subject_average_for_all_users(loaded_data,subject)
            if average:
                print(f"the average grade in {subject} for all students is: {average}")
            else:
                print("no students/grades found, cannot calculate the average")
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
