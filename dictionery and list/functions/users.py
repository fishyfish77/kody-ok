from . import *
from random import randint

def generate_unique_id(data: list[dict]) -> int:
    lst_id = []
    for user in data:
        lst_id.append(user.get("id"))
    new_id = randint(1, 1000000)
    while new_id in lst_id:
        new_id = randint(1, 1000000)
    return new_id

def add_new_user(data: list[dict])-> dict:
    return {
        "id": generate_unique_id(data),
        "name": input("Enter name: ").strip().lower() or None,
        "surname":input("Enter surname: ").strip().lower() or None,
        "date of birth":input("date of birth").strip().lower() or None,
        "grades mathematics": [],
        "grades polish": [], 
        "grades english":[]        
    }

def add_or_remove_grades(data: list[dict])->None:
    user_id = int(input("enter id: "))
    aor = input("add or remove: ")
    inp=input("enter subject: ")
    if aor == "add":
        lst_grades = int(input("enter grade: "))
        if inp == "math":
            for user in data:
                if user.get("id") == user_id:
                    user["grades mathematics"].append(lst_grades)
                    break
        elif inp == "polish":
            for user in data:
                if user.get("id") == user_id:
                    user["grades polish"].append(lst_grades)
                    break
        elif inp == "english":
            for user in data: 
                if user.get("id") == user_id:
                    user["grades english"].append(lst_grades)
                    break
        else:
            print("subject does not exist")
            return
    elif aor == "remove":
        if inp == "math":
            for user in data:
                if user.get("id") == user_id:
                    user["grades mathematics"].clear()
                    break
        elif inp == "polish":
            for user in data:
                if user.get("id") == user_id:
                    user["grades polish"].clear()
                    break
        elif inp == "english":
            for user in data: 
                if user.get("id") == user_id:
                    user["grades english"].clear()
                    break
        else:
            print("subject does not exist")
            return
    else:
        print("cmd does not exist")
        return

def find_user_by_id(data: list[dict], user_id: int) -> dict|None:
    for user in data:
        if user.get("id") == user_id:
            # print(f'{user}')
            return user
    return None

def find_users_by_name(data: list[dict], name: str) -> list[dict]:
    users =[]
    nic=[]
    for user in data:
        if user.get("name") == name:
            users.append(user)
        else:
            nic.append(user)
    return users

def delete_user_by_id(data: list[dict], user_id: int) -> bool:
    for user in data:
        if user.get("id")==user_id:
            data.remove(user)
            print("update succeeded")
            return True
    return False

def update_user_name(data: list[dict], user_id: int, new_name: str) -> bool:
    for user in data:
        if user.get("id")==user_id:
            user["name"]=new_name
            print("update succeeded")
            return True
    return False

def update_user_surname(data: list[dict], user_id: int, new_surname: str) -> bool:
    for user in data:
        if user.get("id")==user_id:
            user["surname"]=new_surname
            print("update succeeded")
            return True
    return False

def update_user_birth_date(data: list[dict], user_id: int, new_birth_date: str) -> bool:
    for user in data:
        if user.get("id")==user_id:
            user["date of birth"]=new_birth_date
            print("update succeeded")
            return True
    return False

def is_name_taken(data: list[dict], name: str, surname: str) -> bool:
    for user in data:
        if user.get("name")==name and user.get("surname")==surname:
            print("name and surname taken")
            return True
        elif user.get("name")==name and user.get("surname")!=surname:
            print("name taken")
        elif user.get("name")!=name and user.get("surname")==surname:
            print("username taken")
    print("name and username not taken")
    return False

def show_one_user(user: dict) -> None:
    for k,v in user.items():
        print(f"{k} ------ {v}")

def count_all_users(data: list[dict]) -> int:
    i=0
    for user in data:
        if user:
            i+=1
    return i

def count_users_with_missing_name(data: list[dict]) -> int:
    n=0
    for user in data:
        name=user.get("name")
        if name == None or len(name) == 0:
            n+=1
    return n

def  average_math_for_user(user: dict) -> float | None:
    grades=user.get("grades mathematics")
    if grades==None or len(grades)==0:
        return None
    return sum(grades)/len(grades)


def  average_polish_for_user(user: dict) -> float | None:
    grades=user.get("grades polish")
    if grades==None or len(grades)==0:
        return None
    return sum(grades)/len(grades)


def  average_eng_for_user(user: dict) -> float | None:
    grades=user.get("grades english")
    if grades==None or len(grades)==0:
        return None
    return sum(grades)/len(grades)

def overall_average_for_user(user: dict) -> float | None:
    math=average_math_for_user(user)
    polish=average_polish_for_user(user)
    eng=average_eng_for_user(user)
    if math == None or polish == None or eng==None:
        return None
    else:
        return (math+polish+eng)/3

def best_student_in_subject(data: list[dict], subject: str) -> dict | None:
    subject=input("enter subject: ")
    if subject =="math":
        best_student=None
        best_avg=0
        for user in data:
            avg=average_math_for_user(user)
            if avg != None and avg > best_avg:
                best_avg=avg
                best_student=user
                return best_student
    elif subject =="polish":
        best_student=None
        best_avg=0
        for user in data:
            avg=average_polish_for_user(user)
            if avg != None and avg > best_avg:
                best_avg=avg
                best_student=user
                return best_student
    elif subject =="english":
        best_student=None
        best_avg=0
        for user in data:
            avg=average_eng_for_user(user)
            if avg != None and avg > best_avg:
                best_avg=avg
                best_student=user
                return best_student

def subject_average_for_all_users(data: list[dict], subject: str) -> float | None:
    subject=input("enter subject: ")
    if subject=="math":
        sum_avg=0
        i=0
        for user in data:
            avg=average_math_for_user(user)
            if avg != None:
                sum_avg+=avg
                i+=1
        if i==0:
            return None
        return sum_avg/i
    elif subject=="polish":
        sum_avg=0
        i=0
        for user in data:
            avg=average_polish_for_user(user)
            if avg != None:
                sum_avg+=avg
                i+=1
        if i==0:
            return None
        return sum_avg/i
    elif subject=="english":
        sum_avg=0
        i=0
        for user in data:
            avg=average_eng_for_user(user)
            if avg != None:
                sum_avg+=avg
                i+=1
        if i==0:
            return None
        return sum_avg/i
