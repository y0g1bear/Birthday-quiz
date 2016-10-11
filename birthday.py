"""
birthday.py
Author: John Warhold
Credit: 
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todayborn = datetime.today().month
todayday = datetime.today().day

name = input( "Hello, what is your name?")
born = input(" Hi " + name + ", what was the name of the month you were born in?")
year = int(input( " And what year were you born in, " + name + "? " ))
day = int(input("And the day? "))

if day == 31 and born == "October":
    print("You are born on Halloween")

if born == todayborn and day == todayday:
    print("Happy birthday!")
else:
    if year > 1980 and year <1989:
    deca = "eighties" 
    if year > 1990 and year <= 1999:
    deca = "nineties" 
    if year <1980:
    deca = "stoneage"
    if year > 2000:
    deca = "two thousands"
    if born == "December" or born == "January" or born == "February":
    print(name + ", you are a winter baby of the " + deca)
    if born == "March" or born == "April" or born == "May":
    print(name +", you are a spring baby of the " + deca)
    if born == "June" or born == "July" or born == "August":
    print(name + ", you are a summer baby of the " + deca)
    if born == "September" or born == "October" or born == "November":
    print(name + ", you are a fall baby of the " + deca)
    
    