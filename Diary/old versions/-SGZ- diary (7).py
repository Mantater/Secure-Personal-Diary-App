# <SGZ> diary

#=====================================================================
def filewrite(notes):
 
    header = ["Date","Weekday","Emotion","Weather","Notes"]

    with open('Dairy.txt', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        
        # Print header for field
        spamwriter.writerow(header)
        for i in range(len(notes)):
            spamwriter.writerow(notes[i])

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
# User needs to verify themselves with password
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
        print("***You have " + str(invalidTries) + " tries left***")

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
    greet = "Welcome to <SGZ> diary"
    printWordByWord(greet)

#=====================================================================
# User enter date
# Save today's day
def date(i):
    dateNow = datetime.datetime.now().date()
    userDate = dateNow.strftime('%Y-%m-%d')
    # Tells user the date
    print("\nDate:", userDate)
    notes[i].append(userDate)
    week(dateNow, i)

#=====================================================================
# Auto find day of the week
def week(dateNow, i):
    # Check today's weekday
    weekday = dateNow.strftime("%A")
    # Teels user the weekday
    print("Weekday: " + weekday)
    notes[i].append(weekday)

#=====================================================================
# List of emotions
emotionList = ["Joy", 
               "Love", 
               "Surprise", 
               "Fear", 
               "Anger", 
               "Sadness"]

# User choose emotions
def emotion(i):
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
    notes[i].append(emotionList[userInput - 1])

#=====================================================================
# List of weather
weatherList = ["Sunny", "Partial cloudy", "Cloudy", 
               "Overcast", "Rain", "Drizzle", 
               "Snow", "Stormy", "Fog",
               "Earthquake", "Flood", "Volcanic eruption",
               "Tsunami", "Sandstorm", "Hurricane"]

# User choose weather
def weather(i):
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
    notes[i].append(weatherList[userInput - 1])

#=====================================================================
# User enter notes
def note(i):
    userText = input("\nNote(s): \n")
    notes[i].append(userText)

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

    again = True
    while again:

        notes.append([])
        index = len(notes) - 1

        # Ask if user would like to get
        # Body
        date(index)          # Next -> calculate year = leap/common
        emotion(index)       #      -> find how many days in that month
        weather(index)       #      -> calculate which weekday
        note(index)
        print()

        # Ask user if they would like to add another record
        choice = input("Would you like to add another record? ")
        choice.lower()
        if choice in ('y','yes'):
            again = True
        else:
            again = False

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