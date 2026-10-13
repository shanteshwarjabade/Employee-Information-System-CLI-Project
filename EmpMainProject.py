#EmpMainProject.py
from EmpAdd import addemployee
from EmpDelete import deleteemployee
from EmpMenu import menu
from EmpSearch import searchemployee
from EmpUpdate import updateemployee
from EmpView import viewsinglemployee, viewallemployee

while True:
    try:
        menu()
        ch=int(input("Enter your choice: "))
        match(ch):
            case 1:
                addemployee()
            case 2:
                deleteemployee()
            case 3:
                updateemployee()
            case 4:
                viewsinglemployee()
            case 5:
                viewallemployee()
            case 6:
                searchemployee()
            case 7:
                print("\tTHX FOR USING CLS PROJECT")
                break

    except ValueError:
        print("\tDON'T ENTER STR/ALNUM/---TRY AGAIN")
