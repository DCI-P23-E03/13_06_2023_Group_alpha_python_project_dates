import calendar, datetime

def check_leap(Year):
    if calendar.isleap(Year):
        print(f"The year, {Year} is a leap one.")
    else:
        print(f"The year, {Year} is a not leap one.")  

def until_leap(DateTime):
    Year=DateTime.year
    print(Year)
    NextLeap=4*(Year//4+1)
    if (NextLeap%100 == 0 and NextLeap%400 !=0):
        NextLeap+=4
    print(NextLeap)    
    NextLeapDate=datetime.datetime(NextLeap,1,1,0,0,0)
    ToNextLeap=NextLeapDate - DateTime
    print(f"Till the next leap year: {ToNextLeap}")

flag=0
while (flag==0):
    input_date = input("Enter a date (yyyy/mm/dd) or type \"now\" for current date: ")
    if input_date=="now":
        Some_date=datetime.datetime.now()
        break
    try:
        Some_date=datetime.datetime.strptime(input_date,"%Y/%m/%d")
        flag=1
    except ValueError:
        print("Invalid date")

check_leap(Some_date.year)
until_leap(Some_date)


