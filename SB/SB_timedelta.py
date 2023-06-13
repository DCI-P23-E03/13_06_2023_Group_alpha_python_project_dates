import datetime

def Represent_timedelta(TimeDelta):
    while True:
       choice=input("Seconds (s)/Days (d)/Years (y)?: ")
       if (choice.lower()=="s" or choice.lower()=="d" or choice.lower()=="y"):
           break
    if choice=="s":
        print(f" The interval is {TimeDelta.days*86400+TimeDelta.seconds} seconds.")
    elif choice=="d":
        print(f"The interval is {TimeDelta.days+TimeDelta.seconds/86400} days")
    else:
        print(f"The interval is {TimeDelta.days/365+TimeDelta.seconds/365/86400} years. (A year is viewed as 365 days)")

def find_timedelta():
    flag=0
    while flag==0:
        try:
            date1= input("Enter first date (yyyy-mm-dd hh:mm:ss): ")
            datetime_object1=datetime.datetime.fromisoformat(date1)
            flag=1
        except ValueError:
            print("Wrong format, try again")
    flag=0
    while flag==0:
        try:
            date2= input("Enter second date (yyyy-mm-dd hh:mm:ss): ")
            datetime_object2=datetime.datetime.fromisoformat(date2)
            flag=1
        except ValueError:
            print("Wrong format, try again")


    timedelta=(datetime_object2-datetime_object1)
    Represent_timedelta(timedelta)




   
#print(f"The number of hours between {date1} and {date2} is {timedelta.days * 24 + timedelta.seconds / 3600}")