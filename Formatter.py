import time
from os import system, name
from urllib.parse import urlparse
Duties = "null"
lis = ["gyazo.com", "prntscr.com", "prnt.sc", "imgur.com", "i.gyazo.com", "floomby.io", "cdn.discordapp.com"]

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

NoteRequested = False
# Variables ^

print("AEGIS Duty State Formatter by SpaceRanger! ")
Username =input("Username: ")
Duties =input("State your duties: ")
#Duties ^
Timezone =input("Timezone: ")

DutyScr =input("Duty Screenshot: ")
ParseDutyScr = urlparse(DutyScr)

if ParseDutyScr.netloc in lis:
  print("URL Allowed")
else:
  print("This isn't a valid URL! Please try again!")
  print("Showing your saved work:")
  print(Username)
  print(Duties)
  print(DutyScr)

clear()
print("Upper paragraph complete...")

print("Make sure you use 24 hours format!")
TimeS =input("Enter Time Started Value: ")
TabS =input("Tablist Started: ")
ParseS = urlparse(TabS)

if ParseS.netloc in lis:
  print("URL Allowed")
else:
  print("This isn't a valid URL! Please try again!")
  print("Showing your saved work:")
  print(Username)
  print(Duties)
  print(DutyScr + "\n")
  print(TimeS)
  print(TabS)


TimeE =input("Enter Time Ended Value:")
TabE =input("Tablist Ended:")
ParseE = urlparse(TabE)

if ParseE.netloc in lis:
  print("URL Allowed")
else:
  print("This isn't a valid URL! Please try again!")
  print("Showing your saved work:")
  print(Username)
  print(Duties)
  print(DutyScr + "\n")
  print(TimeS + Timezone)
  print(TabS + "\n")
  print(TimeE + Timezone) 
  print(TabE + "\n")


NoteR =input("Have a note? (y/n): ")
if NoteR == "y":
  NoteRequested = True
  Note =input("Write your note here: ")

clear()
print("Username: " + Username)
print("Duty: " + Duties)
print(DutyScr + "\n")
print("Time Started: " + TimeS)
print("Tablist Started: " + TabS + "\n")
print("Time Ended: " + TimeE)
print("Tablist Ended: " + TabE + "\n")
if NoteRequested == True:
  print("Note: " + Note)
