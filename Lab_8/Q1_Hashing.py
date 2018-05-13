# https://www.python-course.eu/dictionaries.php

def add_new(dic):
    myMatric = raw_input("Enter your Matric number: ")
    myName = (raw_input("Enter your name: "))
    dic[myMatric] = myName
    return dic

def del_dict(dic):
    keys = raw_input("\nMatric number to delete: ")
    del dic[keys]
    return dic
def print_dict(dic):
    myMatric = dic.keys()
    myName = dic.values()
    for i in range(len(myMatric)):
        print "\nMatric: ", myMatric[i], "\nName: ", myName[i]

if __name__ == "__main__":
    listDic = {'WEK130013': 'Jason', 'WEK130025': 'Billy', 'WEK130020': 'Kim'}
    while True:
        inCMD = raw_input("\n1 = Print list\n2 = Delete existing student"
        "\n3 = Add new Student\n0 = Quit\nEnter cmd: ")
        if inCMD == '2':
            listDic = del_dict(listDic)
        elif inCMD == '1':
            print_dict(listDic)
        elif inCMD == '3':
            listDic = add_new(listDic)
        else:
            break
