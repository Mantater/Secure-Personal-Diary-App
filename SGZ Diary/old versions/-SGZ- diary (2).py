#SGZ diary
datelist = []
weklist = []
emo = []
wea = []
notes = []
#diary = open("diary.txt","rw")
 
 
def locker(time):
   from time import sleep
   lock = "Locked"
   for i in range(6):
       print(lock[i], sep='', end='', flush=True); sleep(0.1)
   print ()
   time.sleep(0.1)
   #
   print ()
   from time import sleep
   line_1 = "        110010        "
   for i in range(22):
       print(line_1[i], sep='', end='', flush=True); sleep(0.01)
   print ()
   #
   line_2 = "   0010        1010   "
   for i in range(22):
       print(line_2[i], sep='', end='', flush=True); sleep(0.01)
   print ()
   #
   line_3 = "  0110          1000  "
   for i in range(22):
       print(line_3[i], sep='', end='', flush=True); sleep(0.01)
   print ()
   #
   line_4 = " 1110            0001 "
   for i in range(22):
       print(line_4[i], sep='', end='', flush=True); sleep(0.01)
   print ()
   #
   line_5 = " 010              100 "
   for i in range(22):
       print(line_5[i], sep='', end='', flush=True); sleep(0.01)
   print ()
   #
   line_6 = " 110              011 "
   for i in range(22):
       print(line_6[i], sep='', end='', flush=True); sleep(0.01)
   print ()
   #
   line_7 = " 10001[01001100]00111 "
   for i in range(22):
       print(line_7[i], sep='', end='', flush=True); sleep(0.01)
   print ()
   #
   line_8 = " 00011[01101111]11010 "
   for i in range(22):
       print(line_8[i], sep='', end='', flush=True); sleep(0.01)
   print ()
   #
   line_9 = " 01011[01100011]01100 "
   for i in range(22):
       print(line_9[i], sep='', end='', flush=True); sleep(0.01)
   print ()
   #
   line_10 = " 01101[01101011]10001 "
   for i in range(22):
       print(line_10[i], sep='', end='', flush=True); sleep(0.01)
   print ()
   #
   line_11 = " 10010[01100101]10100 "
   for i in range(22):
       print(line_11[i], sep='', end='', flush=True); sleep(0.01)
   print ()
   #
   line_12 = " 10101[01100100]10011 "
   for i in range(22):
       print(line_12[i], sep='', end='', flush=True); sleep(0.01)
   print ()
   #
   line_13 = " 10011010010110011001 "
   for i in range(22):
       print(line_13[i], sep='', end='', flush=True); sleep(0.01)
   print ()
 
   return(time)
 
 
def greeting(time):
   time.sleep(0.5)
   from time import sleep
   wait = "Please wait a moment"
   for i in range(20):
       print(wait[i], sep='', end='', flush=True); sleep(0.1)
   from time import sleep
   time.sleep(0.5)
   dots = "..."
   for i in range(3):
       print(dots[i], sep='', end='', flush=True); sleep(0.5)
   print ()
   time.sleep(1)
   from time import sleep
   greet = "Welcome to <SGZ> diary"
   for i in range(22):
       print(greet[i], sep='', end='', flush=True); sleep(0.05)
   print ()
 
   return(time)
 
 
def wek(weklist):
   loopw = True
   while loopw == True:
       print("1:Mon  2:Tue  3:Wed  4:Thur  5:Fri  6:Sat  7:Sun")
       week = int(input("Week (only numbers):"))
       if week == 1:
           print("Week: Mon")
           weklist.append("Mon")
           loopw = False
       elif week == 2:
           print("Week: Tue")
           weklist.append("Tue")
           loopw = False
       elif week == 3:
           print("Week: Wed")
           weklist.append("Wed")
           loopw = False
       elif week == 4:
           print("Week: Thur")
           weklist.append("Thur")
           loopw = False
       elif week == 5:
           print("Week: Fri")
           weklist.append("Fri")
           loopw = False
       elif week == 6:
           print("Week: Sat")
           weklist.append("Sat")
           loopw = False
       elif week == 7:
           print("Week: Sun")
           weklist.append("Sun")
           loopw = False
       elif week<1 or week>7:
           print("Invalid number, please try again.")
           loopw = True       
      
   return (weklist)
 
 
def timedate(datelist):
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
       if y>2021 or y<1:
           print("(Limit Year: 1 - 2021)")
           loopy = True
       elif y<31 or y>1:
           loopy = False
          
   x = (d,m,y)
   print("DATE:",d,"/",m,"/",y)
   datelist.append(x)
  
   return(datelist)
 
 
def emotion(emo):
   loop = True
   while loop:
       import time
       print()
       print("1: depressed",
             "\n2: worried",
             "\n3: sad",
             "\n4: scared",
             "\n5: hurt",
             "\n6: angry",
             "\n7: confused",
             "\n8: normal",
             "\n9: happy",
             "\n10: surprised",
             "\n11: excited")
       print()
       feeling = int(input("Please enter your feelings from 1-11: "))
       if feeling > 11:
           print ("Invalid number. Please try again.")
           time.sleep(1)
       if feeling < 1:
           print ("Invalid number. Please try again.")
           time.sleep(1)
       if feeling == 1:
          print ("{You feel depressed}")
          emo.append("depressed")
          loop = False
       if feeling == 2:
          print ("{You feel worried}")
          emo.append("worried")
          loop = False
       if feeling == 3:
          print ("{You feel sad}")
          emo.append("sad")
          loop = False
       if feeling == 4:
          print ("{You feel scared}")
          emo.append("scared")
          loop = False
       if feeling == 5:
          print ("{You feel hurt}")
          emo.append("hurt")
          loop = False
       if feeling == 6:
          print ("{You feel angry}")
          emo.append("angry")
          loop = False
       if feeling == 7:
          print ("{You feel confused}")
          emo.append("confused")
          loop = False
       if feeling == 8:
          print ("{You feel normal}")
          emo.append("normal")
          loop = False
       if feeling == 9:
          print ("{You feel happy}")
          emo.append("happy")
          loop = False
       if feeling == 10:
          print ("{You feel surprised}")
          emo.append("surprise")
          loop = False
       if feeling == 11:
          print ("{You feel excited}")
          emo.append("excited")
          loop = False
         
   return(emo)
 
 
def weath(wea):
 
   loop = True
   while loop:
       import time
       print()
       print("1: Sunny",
             "\n2: Rainy",
             "\n3: Snowy",
             "\n4: Stormy",
             "\n5: Windy",
             "\n6: Cloudy",
             "\n7: Foggy",
             "\n8: Partly cloudy")
       weather = int(input("Please enter the weather from 1-8: "))
       if weather > 8:
           print ("Invalid number. Please try again.")
           time.sleep(1)
       if weather < 1:
           print ("Invalid number. Please try again.")
           time.sleep(1)
       if weather == 1:
          print ("Sunny")
          wea.append("Sunny")
          loop = False
       if weather == 2:
          print ("Rainy")
          wea.append("Rainy")
          loop = False
       if weather == 3:
          print ("Snowy")
          wea.append("Snowy")
          loop = False
       if weather == 4:
          print ("Stormy")
          wea.append("Stormy")
          loop = False
       if weather == 5:
          print ("Windy")
          wea.append("Windy")
          loop = False
       if weather == 6:
          print ("Cloudy")
          wea.append("Cloudy")
          loop = False
       if weather == 7:
          print ("Foggy")
          wea.append("Foggy")
          loop = False
       if weather == 8:
          print ("Partly cloudy")
          wea.append("Partly cloudy")
          loop = False
 
   return(wea)
 
 
def inner(notes, emo, wek, timedate, weath, time, listofdiary):
   loops = True
   while loops:
       time.sleep(1)
       timedate(datelist)
       print()
       wek(weklist)
       weath(wea)
       print()
       emotion(emo)
       print()
       text = input("Note(s): \n")
       notes.append(text)
       time.sleep(1)
       days = str(input("\nDo you want to add another one (y or n)? "))
       if days == 'y':
           from time import sleep
           yes = "\nPlease wait a moment..."
           for i in range(23):
               print(yes[i], sep='', end='', flush=True); sleep(0.1)
           print ()
           time.sleep(1)
           from time import sleep
           dot = ". . ."
           for i in range(5):
               print(dot[i], sep='', end='', flush=True); sleep(0.1)
           print ()
           listofdiary(notes, emo, wek, timedate, weath, time)
           loops = True
       if days == 'n':
           from time import sleep
           bye = "See you next time!"
           for i in range(18):
               print(bye[i], sep='', end='', flush=True); sleep(0.05)
           print ()
           listofdiary(notes, emo, wek, timedate, weath, time)
           loops = False
 
   return(notes, emo, wek, timedate, weath, time, listofdiary)
  
  
def listofdiary(notes, emo, wek, timedate, weath, time):
   for i in range(3):
       print()
   print("Diary:")
   print()
   print("DATE:",datelist,
         "\nWeek:",weklist,
         "\nWeather:",wea,
         "\nFeelings:",emo,
         "\nNote(s):",notes)
   #diary.write()
 
   return(notes, emo, wek, timedate, weath, time)
 
 
def secur(time, locker, inner):
   loop = True
   while loop:
      password = str(input("Please enter password: "))
      if password != 'Password123':
          print ("[Password invalid]")
          print ()
          time.sleep(0.5)
          locker(time)
          loop = False
      elif password == 'Password123':
          print ("[Password correct]")
          print ()
          greeting(time)
          print()
          inner(notes, emo, wek, timedate, weath, time, listofdiary)
      loop = False
 
   return(time, locker, inner)
      
 
#   Main program
 
from time import sleep
hello = "Welcome"
for i in range(7):
  print(hello[i], sep='', end='', flush=True); sleep(0.05)
print ()
import time
time.sleep(0.5)
secur(time, locker, inner)
 
input ()


