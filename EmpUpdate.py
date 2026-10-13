#EmpUpdate.py
import pickle

def updateemployee():
    # geting all records file in list in list
    records=[]
    with open("emp.pickle",'rb') as fp:
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break

    #locating record for updating salary
    res=False
    empno=int(input("Enter employee number for updating sal: "))
    for i in range(len(records)):
        if(records[i][0]==empno):
            recordind=i
            res=True
            break
    print("-" * 70)
    if(res):
        print("\tEmployee number already exists file")
        newsal=float(input("Enter new employee sal: "))
        records[recordind][2]=newsal
        # rewrite all record to file
        with open("emp.pickle", 'wb') as fp:
            for record in records:
                pickle.dump(record, fp)
        print("-" * 70)
        print("\temployee sal update successfully--verify")
    else:
        print("\temployee number not found in file")
    print("-" * 70)