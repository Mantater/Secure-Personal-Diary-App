import sqlite3
import time
import datetime
from time import sleep

from PasswordManager import PasswordManager

#=====================================================================
# Database Setup
def init_db():
    conn = sqlite3.connect("Diary.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            weekday TEXT,
            notes TEXT,
            feelings TEXT,
            reflection TEXT,
            plans TEXT,
            extra TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_entry(entry):
    conn = sqlite3.connect("Diary.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO entries (date, weekday, notes, feelings, reflection, plans, extra)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, entry)
    conn.commit()
    conn.close()

#=====================================================================
# Printing word by word
def printWordByWord(word):
    for i in range(len(word)):
        print(word[i], sep='', end='', flush=True)
        sleep(0.05)

#=====================================================================
# Lock ASCII
lock = [
"        110010        \n",
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
" 10011010010110011001 ",
]

def locker(lock):
    print("--------Locked--------")
    for row in lock:
        print(row, end='')

#=====================================================================
# Login pass check
def loginCheck():
    invalidTries = 3

    # Initialize your password manager
    pm = PasswordManager()

    # For demo purposes, set the password hash (do this once and save the hash in practice)
    stored_hash = pm.set_password("Password123")  # hash the password
    pm.hashed_password = stored_hash  # assign to manager

    while invalidTries > 0:
        print("***You have " + str(invalidTries) + " tries left***")
        password = input("Please enter password (Case sensitive): ")

        if pm.verify_password(password):
            print("[Password correct]")
            time.sleep(1)
            body()
            return
        else:
            print("[Password invalid]\n")
            invalidTries -= 1

    # If all tries used
    print()
    time.sleep(0.5)
    locker(lock)

#=====================================================================
# Auto find day of the week
def week(dateNow):
    weekday = dateNow.strftime("%A")
    print("Weekday: " + weekday)
    return weekday

#=====================================================================
# Save today's date
def date():
    dateNow = datetime.datetime.now()
    userDate = dateNow.strftime('%Y-%m-%d')
    print("\nDate:", userDate)
    weekday = week(dateNow)
    return userDate, weekday

#=====================================================================
def note():
    print("\nBrief summary of what happened today.")
    return input("Note(s): \n")

def feelings():
    print("\nThoughts and feelings about today's events.")
    print("""
Points to help:
- How did you feel during those events?
- What you're worried about, happy about, or proud of?
- Any emotional release? (venting)
          """)
    return input("Thoughts & Feelings: \n")

def reflection():
    print("\nReflection on today's events.")
    print("""
Points to help:
- Lessons learnt from the day.
- Things you'd do differently.
- Gratitude note. (What you're thankful for)
          """)
    return input("Reflection: \n")

def plans():
    print("\nPlans and goals for tomorrow.")
    print("""
Points to help:
- What you want to achieve tomorrow, or in the future.
- Any tasks or events you need to prepare for.
- Goals you want to set for yourself. (Long-term or short-term)
          """)
    return input("Plans & Goals: \n")

def extra():
    print("\nExtra notes or thoughts.")
    print("""
Points to help:
- Anything else you want to add that doesn't fit in the other sections.
- Random thoughts, ideas, or observations.
- Quotes, jokes, or anything you find interesting.
          """)
    return input("Extra Notes: \n")

#=====================================================================
def bye():
    goodbye = "See you next time!"
    printWordByWord(goodbye)
    print("\n")

#=====================================================================
def body():
    # Head
    userDate, weekday = date()

    # Body
    userNotes = note()
    userFeelings = feelings()
    userReflection = reflection()
    userPlans = plans()
    userExtra = extra()

    # Save to database
    entry = (userDate, weekday, userNotes, userFeelings, userReflection, userPlans, userExtra)
    save_entry(entry)

    print("\nAll notes saved successfully!")

    # Foot
    bye()

#===========================
# Main program
#===========================
def main():
    init_db()  # make sure DB is ready
    printWordByWord("Welcome to the SGZ Diary!")
    print("\n")
    loginCheck()
    input("\nPress Enter to exit...")

main()
