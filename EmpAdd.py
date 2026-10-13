#EmpAdd.py  <----module name
import pickle
def addemployee():
    with open("emp.pickle","ab") as fp:
        #accepting emp detils from keyboard
            try:
                empno=int(input("Enter Employee Number:"))
                empname=input("Enter Employee Name:")
                empsal=float(input("Enter Employee Salary:"))
                lst=list() #empty list
                lst.append(empno)
                lst.append(empname)
                lst.append(empsal)
                #save iterable data into file
                pickle.dump(lst,fp)
                print("\tEmployee Details saved in file successfully--verify")
            except ValueError:
                print("\tDON'T ENTER STR/ALNUM FOR EMPNO,SAL")
