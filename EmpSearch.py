# EmpSearch.py
import pickle


def searchemployee():
    # geting all records file in list in list
    records = []
    with open("emp.pickle", 'rb') as fp:
        while True:
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    # locating record for searching
    res = False
    empno = int(input("Enter employee number for searching:"))
    for record in records:
        if record[0]==empno:
            res = True
            break
    # for i in range(len(records)):
    #     if (records[i][0] == empno):
    #         res = True
    #         break
    print("-" * 70)
    if (res):
        print("\tEmployee details exist--valid")
    else:
        print("\tEmployee details does not exist in file")
    print("-" * 70)