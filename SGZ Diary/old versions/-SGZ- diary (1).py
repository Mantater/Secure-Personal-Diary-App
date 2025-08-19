diary = []
from time import sleep
hello = "Welcome"
for i in range(7):
   print(hello[i], sep='', end='', flush=True); sleep(0.05)
print ()
import time
time.sleep(0.5)
loop = True
while loop:
   password = str(input("Please enter password: "))
   if password != 'Password123':
       print ("[Password invalid]")
       print ()
       time.sleep(0.5)
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
       for i in range(22
                      ):
           print(line_12[i], sep='', end='', flush=True); sleep(0.01)
       print ()
       #
       line_13 = " 10011010010110011001 "
       for i in range(22):
           print(line_13[i], sep='', end='', flush=True); sleep(0.01)
       print ()
       loop = False
   elif password == 'Mars05':
       print ("[Password correct]")
       print ()
       time.sleep(0.5)
       from time import sleep
       wait = "Please wait a moment..."
       for i in range(23):
           print(wait[i], sep='', end='', flush=True); sleep(0.1)
       print ()
       from time import sleep
       dots = "....."
       for i in range(5):
           print(dots[i], sep='', end='', flush=True); sleep(0.5)
       print ()
       time.sleep(1)
       from time import sleep
       greet = "Welcome to <SGZ> diary"
       for i in range(22):
           print(greet[i], sep='', end='', flush=True); sleep(0.05)
       print ()
       loops = True
       while loops:
           time.sleep(1)
           day = str(input("How was your day?: "))
           diary.append(day)
           print (diary)
           time.sleep(1)
           days = str(input("\nDo you want to add another one (y or n)? :"))
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
           if days == 'n':
               from time import sleep
               bye = "See you next time!"
               for i in range(18):
                   print(bye[i], sep='', end='', flush=True); sleep(0.05)
               print ()
               loops = False
               loop = False
input ()