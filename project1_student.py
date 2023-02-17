import csv
def tocsv(x):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(['Name','Age','Contact number','Blood Group'])
            writer.writerow(x)
ct=1
while True:
    lst=[]
    print("----Enter Details for student #",ct,"----")
    name=input("Enter Name:")
    age=input("Enter Age:")
    c_num=input("Enter Contact Number:")
    b_g=input("Enter blood group:")
    print("Check the entered info")
    print("Name:{}\nAge:{}\nContact Number:{}\nBlood Group:{}".format(name,age,c_num,b_g))
    t=input("Is the info correct(yes/no):")
    if t=='yes':
        lst.append(name)
        lst.append(age)
        lst.append(c_num)
        lst.append(b_g)
        tocsv(lst)
        ck=input("Do you wanna countinue(yes/no):")
        if ck=='no':
            break
        else:
            ct+=1
    else:
        print("---PLEASE REENTER THE VALUE---")
