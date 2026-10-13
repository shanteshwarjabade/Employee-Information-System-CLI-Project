#EmpView.py
import pickle

def viewsinglemployee():
    # geting all records file in list in list
    records=[]
    with open("emp.pickle",'rb') as fp:
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #locating record for viewing single emp details
    res=False
    empno=int(input("Enter Employee Number to view Details:"))
    for record in records:
        if(record[0]==empno):
            rec=record
            res=True
            break
    print("-" * 70)
    if(res):
        print("\temployee number:",record[0])
        print("\temployee name:",record[1])
        print("\temployee sal:",record[2])
    else:
        print("\temployee number doesn't exist in file")

def viewallemployee():
    with open("emp.pickle",'rb') as fp:
        print("-"*70)
        print("\teno\t\tname\t\tsal")
        print("-" * 70)
        while True:
            try:
                records=pickle.load(fp)
                for record in records:
                    print("\t{}".format(record),end="\t")
                print()
            except EOFError:
                break
