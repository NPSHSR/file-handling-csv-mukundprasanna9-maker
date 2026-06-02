'''Mukund Prasanna 02/06/2026'''
import csv
try:
    f=open("Travel.csv",'x',newline='')
    fstart=csv.writer(f)
    fstart.writerows([["Switzerland","Lake Geneva","145000","12500","18000"],
                      ["America","Los Angeles","125000","42000","27000"],
                      ["Australia","Great Barrier Reef","200000","35000","16000"]])
    f.close()
except:
    pass
while True:
    print("Choose from one of the following options:-")
    print("1.Add More Rows")
    print("2.Display All")
    print("3.Display all the records and show the total cost to visit a place")
    print("4.Update the cost of visiting for a particular record")
    print("5.Delete a particular record")
    print("6.Exit")
    option=input("Enter Option:")
    if option=='1':
        f=open("Travel.csv",'a',newline='')
        fadd=csv.writer(f)
        N=int(input("Enter no. of rows to add"))
        for i in range(N):
            Country=input("Enter Country name")
            Place=input("Enter Place name")
            TC=int(input("Enter Travel Cost"))
            SFC=int(input("Enter Stay and Food Cost"))
            MC=int(input("Enter Misc Cost"))
            fadd.writerow([Country,Place,TC,SFC,MC])
            print("Row added\n")
        f.close()
    elif option=='2':
        f=open("Travel.csv",'r')
        data = [row for row in csv.reader(f) if len(row) == 5]
        print(f"{'Country':<10}{'Place':<10}{'Travel Cost':<10}{'Stay and Food Cost':<10}{'Misc Cost':<10}")
        for i in data:
            print(f"{i[0]:<10}{i[1]:<10}{i[2]:<10}{i[3]:<10}{i[4]:<10}")
        f.close()
        print()
    elif option=='3':
        f=open("Travel.csv",'r')
        data = [row for row in csv.reader(f) if len(row) == 5]
        print(f"{'Country':<10}{'Place':<10}{'Travel Cost':<10}{'Stay and Food Cost':<10}{'Misc Cost':<10}{'Total Cost':<10}")
        for i in data:
            TotCost=int(i[2])+int(i[3])+int(i[4])
            print(f"{i[0]:<10}{i[1]:<10}{i[2]:<10}{i[3]:<10}{i[4]:<10}{TotCost:<10}")
        f.close()
        print()
    elif option=='4':
        f=open("Travel.csv",'r')
        place=input("Enter name of place")
        data = [row for row in csv.reader(f) if len(row) == 5]
        f.close()
        f1=open("Travel.csv",'w')
        fupdate=csv.writer(f1)
        newdata=[]
        for i in data:
            if i[1]==place:
                print(f"Current details of {place}")
                print(f"{'Country':<10}{'Place':<10}{'Travel Cost':<10}{'Stay and Food Cost':<10}{'Misc Cost':<10}")
                print(f"{i[0]:<10}{i[1]:<10}{i[2]:<10}{i[3]:<10}{i[4]:<10}\n")
                NTC=int(input("Enter new travel cost"))
                NSFC=int(input("Enter new Stay and Food Cost"))
                NMC=int(input("Enter new misc cost"))
                newdata.append([i[0],i[1],NTC,NSFC,NMC])
                continue
            newdata.append(i)
        fupdate.writerows(newdata)
        print("Updated\n")
        f1.close()
    elif option=='5':
        f=open("Travel.csv",'r')
        place=input("Enter name of place's record to delete")
        data = [row for row in csv.reader(f) if len(row) == 5]
        f.close()
        f1=open("Travel.csv",'w')
        fupdate=csv.writer(f1)
        newdata=[]
        for i in data:
            if i[1]==place:
                continue
            newdata.append(i)
        fupdate.writerows(newdata)
        print("Deleted\n")
        f1.close()
    elif option=='6':
        print("Thank you for using this program")
        print("Have a nice day:)")
        break
    else:
        print("Invalid Option\n")
                
