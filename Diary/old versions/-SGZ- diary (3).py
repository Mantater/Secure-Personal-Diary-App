#SGZ diary
lock = ["        110010        ",
       "   0010        1010   ",
       "  0110          1000  ",
       " 1110            0001 ",
       " 010              100 ",
       " 110              011 ",
       " 10001[01001100]00111 ",
       " 00011[01101111]11010 ",
       " 01011[01100011]01100 ",
       " 01101[01101011]10001 ",
       " 10010[01100101]10100 ",
       " 10101[01100100]10011 ",
       " 10011010010110011001 "]
datelist = []
weklist = ["1:Mon  2:Tue  3:Wed  4:Thur  5:Fri  6:Sat  7:Sun"]
emo = ["1: depressed",
        "2: worried",
        "3: sad",
        "4: scared",
        "5: hurt",
        "6: angry",
        "7: confused",
        "8: normal",
        "9: happy",
        "10: surprised",
        "11: excited"]
wea = ["1: Sunny",
        "2: Rainy",
        "3: Snowy",
        "4: Stormy",
        "5: Windy",
        "6: Cloudy",
        "7: Foggy",
        "8: Partly cloudy"]
notes = []
#diary = open("diary.txt","rw")
 
def locker(lock):
    from time import sleep
    locked = "Locked"
    for i in range(len(locked)):
        print(locked[i], sep='', end='', flush=True); sleep(0.1)
    print ()
    time.sleep(0.1)
    #
    for i in range(len(lock)):
        print(lock[i], sep='', end='\n', flush=True); sleep(0.1)
    print ()
    time.sleep(0.1)

    return()

def greeting():
    time.sleep(0.5)
    from time import sleep
    wait = "Please wait a moment"
    for i in range(len(wait)):
        print(wait[i], sep='', end='', flush=True); sleep(0.1)
    time.sleep(0.5)
    dots = "..."
    for i in range(len(dots)):
        print(dots[i], sep='', end='', flush=True); sleep(0.5)
    print ()
    time.sleep(1)
    greet = "Welcome to <SGZ> diary"
    for i in range(len(greet)):
        print(greet[i], sep='', end='', flush=True); sleep(0.05)
    print ()

    return()

def wek(weklist, notes):
    loopw = True
    while loopw == True:
        print(weklist)
        week = int(input("Week (only numbers):"))
        if week == 1:
            print("Week: Mon")
            notes.append("Month: Mon")
            loopw = False
        elif week == 2:
            print("Week: Tue")
            notes.append("Month: Tue")
            loopw = False
        elif week == 3:
            print("Week: Wed")
            notes.append("Month: Wed")
            loopw = False
        elif week == 4:
            print("Week: Thur")
            notes.append("Month: Thur")
            loopw = False
        elif week == 5:
            print("Week: Fri")
            notes.append("Month: Fri")
            loopw = False
        elif week == 6:
            print("Week: Sat")
            notes.append("Month: Sat")
            loopw = False
        elif week == 7:
            print("Week: Sun")
            notes.append("Month: Sun")
            loopw = False
        elif week<1 or week>7:
            print("Invalid number, please try again.")
            loopw = True      
  
    return (weklist, notes)

def timedate(datelist, notes):
    #day
    loopd = True
    while loopd == True:
        d = int(input("Day ({dd}/mm/yyyy): "))
        if d>31 or d<1:
            print("(Limit day: 1 - 31)")
            loopd = True
        elif d<31 or d>1:
            loopd = False
    #month
    loopm = True
    while loopm == True:
        m = int(input("Month (dd/{mm}/yyyy): "))
        if m>12 or m<1:
            print("(Limit month: 1 - 12)")
            loopm = True
        elif m<31 or m>1:
            loopm = False
    #year
    loopy = True
    while loopy == True:
        y = int(input("Year (dd/mm/{yyyy}): "))
        if y>5000 or y<1:
            print("(Limit Year: 1 - 5000)")
            loopy = True
        elif y<31 or y>1:
            loopy = False
  
    x = ("Date:" + str(d) +"/"+ str(m) +"/"+ str(y))
    print("DATE:",d,"/",m,"/",y)
    notes.append(x)

    return(datelist, notes)

def emotion(emo, notes):
    loop = True
    while loop:
        print()
        pprint(emo)
        feeling = int(input("Please enter your feelings from 1-11: "))
        if feeling > 11 or feeling < 1:
            print ("Invalid number. Please try again.")
            time.sleep(1)
        elif feeling == 1:
            print ("{You feel depressed}")
            notes.append("Feelings: depressed")
            loop = False
        elif feeling == 2:
            print ("{You feel worried}")
            notes.append("Feelings: worried")
            loop = False
        elif feeling == 3:
            print ("{You feel sad}")
            notes.append("Feelings: sad")
            loop = False
        elif feeling == 4:
            print ("{You feel scared}")
            notes.append("Feelings: scared")
            loop = False
        elif feeling == 5:
            print ("{You feel hurt}")
            notes.append("Feelings: hurt")
            loop = False
        elif feeling == 6:
            print ("{You feel angry}")
            notes.append("Feelings: angry")
            loop = False
        elif feeling == 7:
            print ("{You feel confused}")
            notes.append("Feelings: confused")
            loop = False
        elif feeling == 8:
            print ("{You feel normal}")
            notes.append("Feelings: normal")
            loop = False
        elif feeling == 9:
            print ("{You feel happy}")
            notes.append("Feelings: happy")
            loop = False
        elif feeling == 10:
            print ("{You feel surprised}")
            notes.append("Feelings: surprise")
            loop = False
        elif feeling == 11:
            print ("{You feel excited}")
            notes.append("Feelings: excited")
            loop = False
      
    return(emo, notes)

def weath(wea, notes):
    loop = True
    while loop:
        print()
        pprint(wea)
        weather = int(input("Please enter the weather from 1-8: "))
        if weather > 8 or weather < 1:
            print ("Invalid number. Please try again.")
            time.sleep(1)
        elif weather == 1:
            print ("Sunny")
            notes.append("Weather: Sunny")
            loop = False
        elif weather == 2:
            print ("Rainy")
            notes.append("Weather: Rainy")
            loop = False
        elif weather == 3:
            print ("Snowy")
            notes.append("Weather: Snowy")
            loop = False
        elif weather == 4:
            print ("Stormy")
            notes.append("Weather: Stormy")
            loop = False
        elif weather == 5:
            print ("Windy")
            notes.append("Weather: Windy")
            loop = False
        elif weather == 6:
            print ("Cloudy")
            notes.append("Weather: Cloudy")
            loop = False
        elif weather == 7:
            print ("Foggy")
            notes.append("Weather: Foggy")
            loop = False
        elif weather == 8:
            print ("Partly cloudy")
            notes.append("Weather: Partly cloudy")
            loop = False

    return(wea, notes)

def inner(notes, emo, wek, timedate, weath, listofdiary):
 
    time.sleep(1)
    timedate(datelist, notes)
    print()
    wek(weklist, notes)
    weath(wea, notes)
    print()
    emotion(emo, notes)
    print()
    text = input("Note(s): \n")
    notes.append("Notes: " + text)
    time.sleep(1)
    bye = "\nSee you next time!"
    for i in range(18):
        print(bye[i], sep='', end='', flush=True); sleep(0.05)
    print ()
    listofdiary(notes, emo, wek, timedate, weath)
    
    return(notes, emo, wek, timedate, weath, listofdiary)
 
def listofdiary(notes, emo, wek, timedate, weath):
    for i in range(3):
        print()
    print("Diary:")
    print(notes)
 
    return(notes, emo, wek, timedate, weath)

def secur(locker, inner):
    loop = True
    while loop:
        password = str(input("Please enter password: "))
        if password != 'Password123':
            print ("[Password invalid]")
            print ()
            time.sleep(0.5)
            locker(lock)
            loop = False
        elif password == 'Password123':
            print ("[Password correct]")
            print ()
            greeting()
            print()
            inner(notes, emo, wek, timedate, weath, listofdiary)
            loop = False
 
    return(locker, inner)
     
def filewrite(notes):
 
    with open("Dairy.txt", "w", newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(notes)):
            spamwriter.writerow([notes[i]])
  

#===========================
# Main program
#===========================

import csv
import time
import pprint
from pprint import pprint
 
from time import sleep
hello = "Welcome"
for i in range(7):
    print(hello[i], sep='', end='', flush=True); sleep(0.05)
print ()
time.sleep(0.5)
secur(locker, inner)
filewrite(notes)
input ()