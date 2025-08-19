# <SGZ> diary

# User needs to verify themselves
# (This is a personal diary, )


#=====================================================================
# Printing word by word
def printWordByWord(word):
    for i in range(len(word)):
        print(word[i], sep='', end='', flush=True); sleep(0.1)
    print()

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
    print()

    # Prints lock (by row)
    printWordByWord(lock)

# Login pass check
def loginCheck(locker):
    invalidTries = 3

    while invalidTries > 0:
        password = str(input("Please enter password: "))
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

    wait = "Please wait a moment"
    printWordByWord(wait)
    time.sleep(0.5)

    loadDots = "..."
    printWordByWord(loadDots)
    time.sleep(1)
    print()

    greet = "Welcome to <SGZ> diary"
    printWordByWord(greet)

#=====================================================================
# List of weeks
weekList = ["Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"]

# User chooses day of the week
def weekday():
    print("(Weekday)")

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
    print("(Emotion)")

#=====================================================================
# List of weather
weatherList = ["Sunny", "Partial cloudy", "Cloudy", 
            "Overcast", "Rain", "Drizzle", 
            "Snow", "Stormy", "Fog",
            
            "Earthquake", "Flood", "Volcanic eruption",
            "Tsunami", "Sandstorm", "Hurricane"]

# User choose weather
def weather():
    print("(Weather)")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
#=====================================================================
# Proceed only after password = correct
# (Combining all components in here)
def main():
    print("(Main)")
    
    loading()
    weekday()
    emotion()
    weather()

#===========================
# Main program
#===========================
import csv
import time
from time import sleep
from pprint import pprint

# Warm welcome
hello = "Welcome"
printWordByWord(hello)
print()

# Check login
loginCheck(locker)

input()