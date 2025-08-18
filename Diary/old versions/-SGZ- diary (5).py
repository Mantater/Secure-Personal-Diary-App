# <SGZ> diary

# User needs to verify themselves with password

#=====================================================================
def filewrite(notes):
 
    with open("Dairy1.txt", "w", newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(notes)):
            spamwriter.writerow([notes[i]])

#=====================================================================
# Printing word by word
def printWordByWord(word):
    for i in range(len(word)):
        print(word[i], sep='', end='', flush=True); sleep(0.1)

#=====================================================================
# Checking input type error
class ValidityCheck():
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def validity(self):

        global userInput

        inputCorrect = False
        while inputCorrect == False:

            # Check type validity
            typeCheck = True
            while typeCheck:
                try:
                    userInput = int(input("\nPlease choose an option: "))
                    typeCheck = False
                except ValueError:
                    print("[Invalid integer! Please enter choice number]")
        
            # Check range validity
            if userInput < self.min or userInput > self.max:
                print("[Invalid number]")
            else:
                inputCorrect = True
                return(userInput)

#=====================================================================
# Show user this lock when password != correct
lock = ["        110010        \n",
       "   0010        1010   \n",
       "  0110          1000  \n",
       " 1110            0001 \n",
       " 010              100 \n",
       " 110              011 \n",
       " 10001[01001100]00111 \n",
       " 00011[01101111]11010 \n",
       " 01011[01100011]01100 \n",
       " 01101[01101011]10001 \n",
       " 10010[01100101]10100 \n",
       " 10101[01100100]10011 \n",
       " 10011010010110011001 "]

# Shows user lock image
def locker(lock):
    # Tells user it is locked (by word)
    locked = "---Locked---"
    printWordByWord(locked)
    print("\n")

    # Prints lock (by row)
    printWordByWord(lock)

# Login pass check
def loginCheck(locker):
    invalidTries = 3

    while invalidTries > 0:
        # Tell user times of login tries
        print("You have " + str(invalidTries) + " tries left")

        # User input password
        password = str(input("Please enter password (Case sensitive): "))
        if password != 'Password123':
            print("[Password invalid]")
            print()
            invalidTries -= 1

        elif password == 'Password123':
            print("[Password correct]")
            main()
            invalidTries = -1

    if invalidTries == 0:    
        print()
        time.sleep(0.5)
        locker(lock)

    return(locker)

#=====================================================================
# Loading screen
def loading():
    time.sleep(0.5)

    print()
    wait = "Preparing"
    printWordByWord(wait)
    time.sleep(0.5)

    loadDots = "..."
    for i in range(len(loadDots)):
        print(loadDots[i], sep='', end='', flush=True); sleep(0.5)
    time.sleep(1)
    print("\n")

    splitLine = "---------------------------------------------------------"
    print(splitLine)
    greet = "Welcome to <SGZ> diary\n"
    printWordByWord(greet)

#=====================================================================
# Check year type
def checkYearType(year):
    if (year % 4 == 0 and 
        year % 100 != 0 or 
        year % 400 == 0):

        print("Year type = Leap year")

    else:
        print("Year type = Common year")

# User enter date
# Check validity of date
def date():
    dateValid = False
    while dateValid == False:
        try:
            yyyy = int(input("Year (1871-now): "))
            checkYearType(yyyy)
            mm = int(input("Month (1-12): "))
            dd = int(input("Day (1-31): "))
            datetime.datetime(year=1871, month=1, day=1) < datetime.datetime(year=yyyy,month=mm,day=dd) <= datetime.datetime.now()
            dateValid = True
        except ValueError:
            print("[Invalid date!]")

#=====================================================================
# List of weeks
weekdayList = ["Monday",
               "Tuesday",
               "Wednesday",
               "Thursday",
               "Friday",
               "Saturday",
               "Sunday"]

# User chooses day of the week
def weekday():
    print("\n---Day Of The Week---\n",
          "1: Monday\n",
          "2: Tuesday\n",
          "3: Wednesday\n",
          "4: Thursday\n",
          "5: Friday\n",
          "6: Saturday\n",
          "7: Sunday")

    # Checks validity of user's input
    week = ValidityCheck(1, 7)
    weekdayInput = week.validity()

    print("Weekday: " + weekdayList[userInput - 1])
    notes.append("Week: " + weekdayList[userInput - 1])
#=====================================================================
# List of emotions
emotionList = ["Joy", 
               "Love", 
               "Surprise", 
               "Fear", 
               "Anger", 
               "Sadness"]

# User choose emotions
def emotion():
    print("\n-------Emotions------\n",
          "1: Joy\n",
          "2: Love\n",
          "3: Surprise\n",
          "4: Fear\n",
          "5: Anger\n",
          "6: Sadness")

    # Checks validity of user's input
    userEmotion = ValidityCheck(1, 6)
    emotionInput = userEmotion.validity()

    print("Emotion: " + emotionList[userInput - 1])
    notes.append("Emotion: " + emotionList[userInput - 1])

#=====================================================================
# List of weather
weatherList = ["Sunny", "Partial cloudy", "Cloudy", 
               "Overcast", "Rain", "Drizzle", 
               "Snow", "Stormy", "Fog",
               "Earthquake", "Flood", "Volcanic eruption",
               "Tsunami", "Sandstorm", "Hurricane"]

# User choose weather
def weather():
    print("\n--------Weather------\n",
          "_________Normal________\n",
          "1: Sunny\n", "2: Partial cloudy\n", "3: Cloudy\n", 
          "4: Overcast\n", "5: Rain\n", "6: Drizzle\n", 
          "7: Snow\n", "8: Stormy\n", "9: Fog\n",
          
          "___Natural disaster____\n",
          "10: Earthquake\n", "11: Flood\n", "12: Volcanic eruption\n",
          "13: Tsunami\n", "14: Sandstorm\n", "15: Hurricane")

    # Checks validity of user's input
    userWeather = ValidityCheck(1, 15)
    weatherInput = userWeather.validity()

    print("Weather: " + weatherList[userInput - 1])
    notes.append("Weather: " + weatherList[userInput - 1])

#=====================================================================
# User enter notes
def note():
    userText = input("\nNote(s): \n")
    notes.append("Notes: " + userText)

#=====================================================================
# Quit
def bye():
    goodbye = "See you next time!"
    printWordByWord(goodbye)
    print("\n")

    print("Diary:\n", notes)


#=====================================================================
# Proceed only after password = correct
# (Combining all components in here)
def main():

    # Head
    loading()
    print()

    # Body
    date()          # Next -> calculate year = leap/common
    weekday()       #      -> find how many days in that month
    emotion()       #      -> calculate which weekday
    weather()
    note()
    print()

    # Foot
    bye()
    filewrite(notes)

#===========================
# Main program
#===========================
import csv
import time
import datetime
from time import sleep

# User's diary list
notes = []

# Warm welcome
hello = "Welcome"
printWordByWord(hello)
print("\n")

# Check login
loginCheck(locker)

input()