import calendar, datetime

def print_calender():
    while True:
        Input_month=input("Input a year and a month (yyyy/mm) or type \"now\" for current month: ")

        if Input_month=="now":
            Y=datetime.datetime.now().year
            M=datetime.datetime.now().month
            break

        try:
            Some_date=datetime.datetime.strptime(Input_month,"%Y/%m")
            Y=Some_date.year
            M=Some_date.month
            break
        except ValueError:
            print("Invalid date")

    print(calendar.month(Y,M))