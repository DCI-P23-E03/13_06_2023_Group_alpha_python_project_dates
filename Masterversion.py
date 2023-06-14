from datetime import datetime, timedelta, timezone, date
import calendar 
from pytz import timezone
import random
#run pip install timezonefinder
from timezonefinder import TimezoneFinder
#run pip install geopy, pip install geopanda
from geopy.geocoders import Nominatim
import pyjokes
tf = TimezoneFinder()
geolocator = Nominatim(user_agent="geoapiExercises")
# Import needed Modules
#Design User Input Menu

#Variables to use in several functions            
current_time = datetime.now()
current_year = int(datetime.strftime(current_time, "%Y"))
current_month = int(datetime.strftime(current_time,"%m"))
#Define menu options
def menu_1() : # current time, nicely formatted
    print(f"It is {current_time.strftime('%A, %d/%m/%Y, %H:%M:%S')}.")
# current time as a formatted UNIX time without decimals    
def menu_2(): 
    print(f"The current UNIX time is {int(current_time.timestamp())}.")
# display user input date (string) as a datetime object    
def menu_3(): 
    userdate = input("Please enter a date in the following format dd-mm-YYYY: ")
    #print(type(userdate))
    try:
        userdate_obj = datetime.strptime(userdate,"%d-%m-%Y")
        #print(userdate_obj)
        print(f"We just converted {userdate} which is a {type(userdate)} object to {userdate_obj} which is a {type(userdate_obj)} object.")
    except ValueError:
        print ("Invalid date, please try again.")    
#Leapyear
def menu_4(): 
    def check_leap(Year):
        if calendar.isleap(Year):
            print(f"The year, {Year} is a leap one.")
        else:
            print(f"The year, {Year} is a not leap one.")  

    def until_leap(DateTime):
        Year=DateTime.year
        print(f"The year you asked about is: {Year}")
        NextLeap=4*(Year//4+1)
        if (NextLeap%100 == 0 and NextLeap%400 !=0):
            NextLeap+=4
        print(f"The next leap year is: {NextLeap}")    
        NextLeapDate=datetime(NextLeap,1,1,0,0,0)
        ToNextLeap=NextLeapDate - DateTime
        print(f"Till the next leap year: {ToNextLeap.days} days")

    flag=0
    while (flag==0):
        input_date = input("Enter a date (yyyy/mm/dd) or type \"now\" for current date: ")
        if input_date=="now":
            Some_date=datetime.now()
            break
        try:
            Some_date=datetime.strptime(input_date,"%Y/%m/%d")
            flag=1
        except ValueError:
            print("Invalid date")

    check_leap(Some_date.year)
    until_leap(Some_date)
def menu_5 ():
    t1 = input("Input a first date in the following format 'yyyy-mm-dd HH:MM:SS': ")
    t2 = input("Input another date in the following format 'yyyy-mm-dd HH:MM:SS': ") 
    #convert input strings to objects
    try:
        t1_obj = datetime.strptime (t1,"%Y-%m-%d %H:%M:%S")
        t2_obj = datetime.strptime (t2,"%Y-%m-%d %H:%M:%S")
        tdelta = abs(t1_obj-t2_obj) #calculate timedelta, make it absolute to work correctly no matter if first or second value is bigger
        print("How do you want the time that has passed displayed?")
        choice = input("Please choose \n[s] seconds \n[d] days \n[y] years :")
        if choice == "s":
            print (f"The number of seconds between {t1} and {t2} is {int(tdelta/timedelta(seconds=1))} seconds")
        elif choice == "d":
            print (f"The number of days between {t1} and {t2} is {round(tdelta.days+tdelta.seconds/86400), 4} days")
        elif choice == "y":
            print (f"The number of years between {t1} and {t2} is {round(tdelta/timedelta(days=365.25), 4)} years.")
        else:
            print("Please choose a valid format.")
    except ValueError:
        print("Wrong format, please try again.") 
#display calendar        
def menu_6():
    while True:
        print("Do you want to see this months calendar or another time?")
        choice = input("Choose 'now' for the current month or type a date in the following format 'yyyy-mm': ")
        if choice == "now":
            print(f"Year: {current_year}"+"\t"+f"Month:{current_month}")
            print(calendar.month(current_year, current_month))
            break

        elif choice != "now":
            try:
                mcalendar = datetime.strptime(choice, "%Y-%m")
                print(f"Year: {mcalendar.year}"+"\t"+f"Month:{mcalendar.month}")
                print(calendar.month(int(mcalendar.year), int(mcalendar.month)))
                break
            except ValueError:
                print("Please choose a valid option!")
#Timezone Conversion
def menu_7():
    choice = input("""What time is it in
    [1]Tokyo / Japan
    [2]Dublin / Ireland
    [3]San Franciso / USA
    [4]Berlin / Germany
    [5]Johannesburg / South Africa\n
    Input a number: """)
    if choice == "1":
        localtime = current_time.astimezone(timezone('Japan'))
        place = "Tokyo /Japan"
        #print(f"The current time in Tokyo / Japan is {datetime.strftime(ttokyo,'%H:%m')}")
    elif choice == "2":
        localtime = current_time.astimezone(timezone('Europe/Dublin'))
        place = "Dublin / Ireland"
        #print(f"The current time in Dublin / Ireland is {datetime.strftime(tdublin,'%H:%m')}")    
    elif choice == "3":
        localtime = current_time.astimezone(timezone('America/Los_Angeles'))
        place = "San Francisco / USA"
        #print(f"The current time in San Francisco / USE is {datetime.strftime(tsanfran,'%H:%m')}") 
    elif choice == "4":
        localtime = current_time.astimezone(timezone('Europe/Berlin'))
        place =  "Berlin /Germany"
        #print(f"The current time in Berlin / Germany is {datetime.strftime(tberlin,'%H:%m')}") 
    elif choice == "5":
        localtime = current_time.astimezone(timezone('Africa/Johannesburg'))
        place = "Johannesburg / South Africa"
        #print(f"The current time in Johannesburg / South Africa is {datetime.strftime(tjohan,'%H:%m')}") 
    else:
        print("Please make a valid choice.")   
    print(f"The current time in {place} is {datetime.strftime(localtime,'%H:%M:%S %Z')}.")                     
#What time is it at the other end of the world                   
def menu_8():
    user_location = input ("Where are you at, please enter 'City, Country': ")
    #convert userlocation into coordinates (longitude and latitude) 
    location = geolocator.geocode(user_location)
    try:
        userlat = location.latitude
        userlong = location.longitude
        #print(userlat, userlong)
        # Calculate Antipode
        anti_latitude = -location.latitude
        anti_longitude = location.longitude%360-180    
        #print(anti_latitude)
        #print(anti_longitude)
        #Determine Usertimezone.
        user_timezone = tf.timezone_at(lng=userlong, lat=userlat)
        #print(current_time.astimezone (timezone(str(user_timezone))))
        #print(user_timezone)
        heretime =current_time.astimezone(timezone(str(user_timezone))).replace(tzinfo=None)
        #Determine Antipode Timezone
        anti_timezone = tf.timezone_at(lng = anti_longitude, lat= anti_latitude)
        #print(anti_timezone)
        #Determine Time in Antipod Timezone
        tantipode = current_time.astimezone(timezone(str(anti_timezone)))
        #print(tantipode)
        there = tantipode.replace(tzinfo=None) # Remove Timezone Information from Antipode Time (Otherwise timediff will be 0)
        # Determine if Antipod is east or west as this influence the direction of calculation
        timediff = there - heretime # Converting Timedifference to hours
        #print(round(timediff/timedelta(hours=1),2))
        print(f"You picked {user_location} at {userlat} latitude and {userlong} longitude.\nYour current time is {current_time.astimezone (timezone(str(user_timezone)))}.\nThe antipode is at {anti_latitude} latitude and {anti_longitude} longitude.\nThe current time there is {tantipode} which is a {round(timediff/timedelta(hours=1),2)} hour difference.")
    except AttributeError:
        print("Not a place.")    
#Tell me a joke
def menu_9():
    print(pyjokes.get_joke(language='en'))
#Surprise
def menu_10():
    birthday =  input ("When were you born? Please enter date in the following format 'dd-mm-yyyy': ")
    try:    
        print("\n")
        birthdate = datetime.strptime(birthday, "%d-%m-%Y")
        birthyear = int(datetime.strftime(birthdate, "%Y"))
        rat = [1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020]
        ox = [1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021]
        tiger =[1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022]
        rabbit = [1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023]
        dragon = [1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024]
        snake = [1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025]
        horse = [1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026]
        goat = [1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027]
        monkey = [1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028]
        rooster = [1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029]
        dog = [1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030]
        pig = [1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031]
        animal = ""
        if birthyear in rat:
            animal = "Rat"
            p_traits = "quick-witted, resourceful, versatile, kind"
        elif birthyear in ox:
            animal = "Ox"
            p_traits = "diligent, dependable, strong, determined"
        elif birthyear in tiger:
            animal = "Tiger"
            p_traits = "brave, confident, competitive"
        elif birthyear in rabbit:
            animal = "Rabbit"
            p_traits = "quiet, elegant, kind, responsible"
        elif birthyear in dragon:
            animal = "Dragon"
            p_traits = "confident, intelligent, enthusiastic"
        elif birthyear in snake:
            animal = "Snake"
            p_traits = "enigmatic, intelligent, wise"
        elif birthyear in horse:
            animal = "Horse"
            p_traits = "Animated, active, energetic"
        elif birthyear in goat:
            animal = "Goat"
            p_traits = "calm, gentle, sympathetic"
        elif birthyear in monkey:
            animal = "Monkey"
            p_traits = "sharp, smart, curious"
        elif birthyear in rooster:
            animal = "Rooster"
            p_traits = "observant, hardworking, courageous"
        elif birthyear in dog:
            animal = "dog"
            p_traits = "lovely, honest, prudent"
        elif birthyear in pig:
            animal = "Pig"
            p_traits = "compassionate, generous, diligent"
        else:
            print("You can't be that old! Or not born yet!?!")    
        if animal !="":
            print(f"You were born in {birthyear} - the year of the {animal}.\n{animal}\'s are said to be {p_traits}.\n")
        #Determine Zodiac Zign
        if birthdate.month == 2 and birthdate.day == 29:
            zodiac = "Pisces"
        else:    
            ordday = date.toordinal(birthdate.replace(year=1999))-date.toordinal(date(1998,12,31))   #return datenumber in the year 1999(non leap)
            if ordday <=19 or ordday > 355:
                zodiac = "Capricorn" 
            elif ordday > 19  and ordday <= 49:
                zodiac = "Aquarius"
            elif ordday > 49  and ordday <= 79:
                zodiac = "Pisces"
            elif ordday > 79  and ordday <= 109:
                zodiac = "Aries"
            elif ordday > 109  and ordday <= 140:
                zodiac = "Taurus"
            elif ordday > 140  and ordday <= 171: 
                zodiac = "Gemini"
            elif ordday > 171  and ordday <= 203: 
                zodiac = "Cancer"
            elif ordday > 203  and ordday <= 234: 
                zodiac = "Leo"
            elif ordday > 234  and ordday <= 265: 
                zodiac = "Virgo"
            elif ordday > 265  and ordday <= 295: 
                zodiac = "Libra"
            elif ordday > 295  and ordday <= 325: 
                zodiac = "Scorpio"
            else: 
                zodiac = "Sagittarius"                    
        print (f"Your Zodiac Sign is {zodiac}. Enjoy this knowledge.\n")
        #How long have you been alive?
        alive = current_time - birthdate # timediff til birthday, age
        print(f"You have been around for {alive.days} days.\n")
        if birthdate.month != 2 and birthdate.day != 29:
            if current_time.replace(hour=0, minute=0, second=0, microsecond=0) > birthdate.replace(year = current_year):
                untilbirthday = birthdate.replace(year = current_year+1) - current_time.replace(hour=0, minute=0, second=0, microsecond=0)
                print(f"Your next birthday will come up in {untilbirthday.days} day(s).")
            elif current_time.replace(hour=0, minute=0, second=0, microsecond=0) < birthdate.replace(year = current_year):
                untilbirthday = birthdate.replace(year = current_year) - current_time.replace(hour=0, minute=0, second=0, microsecond=0)
                print(f"Your next birthday will come up in {untilbirthday.days} day(s).")   
            else:
                print("Happy Birthday!")
        else:
                print("You poor soul. Only a proper birthday every 4 years.")

    except ValueError:
        print("Please enter a valid date.")



#Create Menu Tree as an if/else condition
while True:
    menu = input("""\n\nWe're all about time today. What to you want to do?
    [1] What time is it?
    [2] What UNIX time is it?
    [3] Pick a date
    [4] Leapyear time?
    [5] How much time has passed?
    [6] Calendar
    [7] What time is it in...?
    [8] What time is it on the other side of the planet
    [9] Tell me a joke
    [10] Surprise 
    Press [q] any time to exit.\n\n""")                 
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
    elif menu == "8":
        menu_8()
    elif menu == "9":
        menu_9()
    elif menu =="10":
        menu_10()
    elif menu.lower() =="q":
        break                    
    else:
        print("Please make a valid choice.")    