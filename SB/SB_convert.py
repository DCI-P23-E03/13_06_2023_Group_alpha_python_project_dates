import datetime

def convert():
    flag=0
    while (flag==0):
        input_date = input("Enter a date (yyyy/mm/dd): ")
        try:
            Some_date=datetime.datetime.strptime(input_date,"%Y/%m/%d")
            flag=1
        except ValueError:
            print("Invalid date")
    print(f"I converted {input_date} to {Some_date}")