'''Mukund Prasanna 02/06/2026'''
import csv
import os
try:
    f=open("Emp.csv",'x')
except:
    f=open("Emp.csv",'r')
f.close()
while True:
    print("Choose from the following options:")
    print("1)Reset the file")
    print("2)Add more records")
    print("3) Display All")
    print("4) Search for a particular employee")
    print("5) Display the details of all the employees within a given range of salaries")
    print("6) Create a new csv file with new name and move all records of a particular department employees to new file")
    print("7) Sort the employees as per their salary and display all the information")
    print("8) Exit")
    option=input("Please choose one of the following options")
    if option=='1':
        f=open("Emp.csv",'w')
        f.close()
        print("File Reset\n")
    elif option=='2':
        f=open("Emp.csv",'a',newline='')
        Name=input("Enter Employee Name")
        ID=input("Enter Employee ID")
        Sal=int(input("Enter Employee Salary"))
        Dep=input("Enter Emplyee Department")
        fin=csv.writer(f)
        fin.writerow([Name,ID,Sal,Dep])
        f.close()
        print("Record added\n")
    elif option=='3':
        f=open("Emp.csv",'r')
        data = [row for row in csv.reader(f) if len(row) == 4]
        print(f"{'EName':<10}{'EmpID':<10}{'Salary':<10}{'Department':<10}")
        for i in data:
            print(f"{i[0]:<10}{i[1]:<10}{i[2]:<10}{i[3]:<10}")
        f.close()
        print()
    elif option=='5':
        low=int(input("Enter lower limit of range"))
        up=int(input("Enter upper limit of range"))
        f=open("Emp.csv",'r')
        data = [row for row in csv.reader(f) if len(row) == 4]
        datar=[]
        for i in data:
            if low<=int(i[2])<=up:
                datar.append(i)
        print(f"{'EName':<10}{'EmpID':<10}{'Salary':<10}{'Department':<10}")
        for i in datar:
            print(f"{i[0]:<10}{i[1]:<10}{i[2]:<10}{i[3]:<10}")
        f.close()
        print()
    elif option=='4':
        f=open("Emp.csv",'r')
        data = [row for row in csv.reader(f) if len(row) == 4]
        while True:
            print("Choose how to search:")
            print("1) By Name")
            print("2) By ID")
            Smode=input("Enter option")
            if Smode=='1':
                NS=input("Enter Employee name to search")
                for i in data:
                    if i[0]==NS:
                        print("Employee Found\n")
                        print(f"{'EName':<10}{'EmpID':<10}{'Salary':<10}{'Department':<10}")
                        print(f"{i[0]:<10}{i[1]:<10}{i[2]:<10}{i[3]:<10}")
                        break
                else:
                    print("Employee not found")
                f.close()
                break
            elif Smode=='2':
                NID=input("Enter Employee ID to search")
                for i in data:
                    if i[1]==NID:
                        print("Employee Found\n")
                        print(f"{'EName':<10}{'EmpID':<10}{'Salary':<10}{'Department':<10}")
                        print(f"{i[0]:<10}{i[1]:<10}{i[2]:<10}{i[3]:<10}")
                        break
                else:
                    print("Employee not found")
                    break
                f.close()
                break
            else:
                print("Option Invalid\n")
    elif option=='7':
        f=open("Emp.csv",'r')
        data=sorted([row for row in csv.reader(f) if len(row) == 4], key=lambda x:int(x[2]))
        print(f"{'EName':<10}{'EmpID':<10}{'Salary':<10}{'Department':<10}")
        for i in data:
            print(f"{i[0]:<10}{i[1]:<10}{i[2]:<10}{i[3]:<10}")
        print()
    elif option=='8':
        print("Thank you for using this program :)\nHave a nice day")
        break
    elif option=='6':
        NewFile=input("Enter new csv file name(wihtout extension)")+".csv"

        MoveDep=input(f"Enter name of the department to move to {NewFile}")
        f1=open("Emp.csv",'r')
        f2=open(NewFile,'w',newline='')
        f3=open("temp.csv",'w',newline='')  
        f2in=csv.writer(f2)
        f3in=csv.writer(f3)
        Emp=[row for row in csv.reader(f1) if len(row) == 4]
        EmpDep=[]
        Retain=[]
        for i in Emp:
            if i[3]==MoveDep:
                EmpDep.append(i)
                continue
            Retain.append(i)
        f2in.writerows(EmpDep)
        f3in.writerows(Retain)
        f1.close()
        f2.close()
        f3.close()
        os.remove("Emp.csv")
        os.rename("temp.csv","Emp.csv")
        print("Records moved succesfully\n")
    else:
        print("Please Enter a valid option")
    
            
        
        
                
    
