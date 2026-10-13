#EmpDelete.py
import pickle

def deleteemployee():
    #geting all records file in list in list
    records=[]
    with open("emp.pickle",'rb') as fp:
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #locating emp for deleting emp details
    res=False
    empno=int(input("Enter employee number for deleting record:"))
    for i in range(len(records)):
        if (records[i][0]==empno):
            recordindex=i
            res=True
            break
    print("-"*70)
    if(res):
        records.pop(recordindex) #delete emp details
        #rewrite all record to file
        with open("emp.pickle",'wb') as fp:
            for record in records:
                pickle.dump(record,fp)
        print("\temployee record deleted successfully--verify")
    else:
        print("\temployee number not found in file")
    print("-" * 70)
