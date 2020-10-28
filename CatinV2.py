#Start of program.
#Needed to change title of the window.
import ctypes
#Change name of window.
ctypes.windll.kernel32.SetConsoleTitleW("Words to Catin V2")
#Needed for printing "program quit" if hit Ctrl + C.
try:
    #Tells user how to quit.
    print("Press Ctrl + C to quit.")
    #Repeat indefinitely.
    while True:
        #Ask for the word user wants to convert.
        mystring = str(input('Enter a word to convert to Catin V2 (one word at a time or program will break.): '))
        #Convert input into catin v2.
        mystring = mystring[-2:] + mystring[1:] + "a" + mystring[:1] + "a"
        #Return the converted word to the user.
        print("Catin V2 word:",mystring)
#Runs the print when Ctrl + C is hit.
except KeyboardInterrupt:
    #Tells you program was quit by user.
    print("Program quit. Hope you use again!")
#End of program.
