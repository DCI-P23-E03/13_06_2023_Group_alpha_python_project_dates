from datetime import datetime, timedelta, time, timezone
import calendar 
import pytz
# Import needed Modules
#Design User Input Menu
menu = input("""We're all about time today. What to you want to do?
[1] What time is it?)
[2] What UNIX time is it?
[3] What is your favorite date?
[4] Leapyear time?
[5] How much time has passed?
[6] Calendar
[7] What time is it in...?
[8] What time is it on the other side of the planet
[9] Tell me a joke
[10] Surprise: \n\t\n""")
#Variables to use in several functions            
current_time = datetime.now()
current_year = int(datetime.strftime(current_time, "%Y"))
current_month = int(datetime.strftime(current_time,"%m"))
#Define menu options
def menu_1() : # current time, nicely formatted
    print(f"It is {current_time.strftime('%A,%d.%B.%Y, %H:%M:%S')}.")
# current time as a formatted UNIX time without decimals    
def menu_2(): 
    print(int(current_time.timestamp()))
# display user input date (string) as a datetime object    
def menu_3(): 
    userdate = input("Please enter a date in the following format dd-mm-YYYY: ")
    print(type(userdate))
    userdate_obj = datetime.strptime(userdate,"%d-%m-%Y")
    print(userdate_obj)
    print(type(userdate_obj))
#Leapyear
def menu_4(): 
    current_leap = calendar.isleap(current_year)
    next_leap = ((current_year//4+1)*4) #calculate next leap
    leapcountup = datetime(next_leap,1,1,00,00,00) - current_time
    print(next_leap)   
    if current_leap == False:
        if next_leap%400 == 0 or next_leap%100 != 0 and next_leap%4 == 0: # resolve gregorian calendar irritations
            print(f"{current_year} is not a leap year. The next leapyear is {next_leap} and will start in {leapcountup.days} days")
        else:
            print("The next leap year could not be correctly determined...brushing up my math skills.")
    else:
        print(f"{current_year} is a leap year. The next leapyear will start in {leapyearcountup}")
def menu_5 ():
    t1 = input("Input a first date in the following format 'yyyy-mm-dd HH:MM:SS'")
    t2 = input("Input another date in the following format 'yyyy-mm-dd HH:MM:SS'") 
    #convert input strings to objects
    t1_obj = datetime.strptime (t1,"%Y-%m-%d %H:%M:%S")
    t2_obj = datetime.strptime (t2,"%Y-%m-%d %H:%M:%S")
    tdelta = abs(t1_obj-t2_obj) #calculate timedelta, make it absolute to work correctly no matter if first or second value is bigger
    print("How do you want the time that has passed displayed?")
    choice = input("Please choose \n[1] seconds \n[2] days \n[3] years :")
    if choice == "1":
        print (f"The number of seconds between {t1} and {t2} is {tdelta.seconds} seconds")
    elif choice == "2":
        print (f"The number of days between {t1} and {t2} is{tdelta.days} days")
    elif choice == "3":
        print (f"The number of years between {t1} and {t2} is {round(tdelta.days/365.25)} years")
    else:
        print("Please choose a valid format.")
#display calendar        
def menu_6():
    print("Do you want to see this months calendar or another time?")
    choice = input(" Choose 'now' for the current month or type a date in the folling format 'yyyy-mm': ")
    if choice == "now":
        print(f"Year: {current_year}"+"\t"+f"Month:{current_month}")
        print(calendar.month(current_year, current_month))
    elif choice != "now":
        mcalendar = datetime.strptime(choice, "%Y-%m")
        print(f"Year: {mcalendar.year}"+"\t"+f"Month:{mcalendar.month}")
        print(calendar.month(int(mcalendar.year), int(mcalendar.month)))
    else:
        print("Please choose a valid option!")
#Timezone Conversion
def menu_7():



#Create Menu Tree as an if/else condition                 
if menu == "1":
    menu_1()
elif menu == "2":
    menu_2()
elif menu == "3":
    menu_3()       
elif menu == "4":
    menu_4()
elif menu == "5":         
    menu_5()
elif menu == "6":
    menu_6()
elif menu == "7":
    menu_7()        
else:
    print("Please make a valid choice.")    