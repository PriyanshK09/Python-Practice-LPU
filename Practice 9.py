#Kilometer to Mile converter or Vice Versa

start = int(input("Which Unit you want to Input, Press 1 for KM & 2 for Miles :- "))

if start==1:
    x = float(input("Enter the value in KM here : "))
    miles = x*0.621
    print("The value in Miles will be : " , miles)

if start==2:
    x = float(input("Enter the value in Miles here : "))
    km = x*1.609
    print("The value in KM will be : " , km)

else:
    print("Wrong Input")
