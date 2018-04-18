############################################
#  H2G2 project
############################################
'''
This script does the following:
    1. Looks up a user-input search term on Wikipedia
    2. Allows the user to specify whether the guide should return the article summary or full-text
    3. Allows the user to specify whether the guide should also read the selected entry back to them

When executed, the program initialization should go as follows:

--------  DON'T PANIC  -------
Welcome to the Hitchhiker's Guide to the Galaxy!
options:
(input text) --> search
(quit)--> exits program
Search the Guide for: --> <search term goes here>
Would you like the summary? Or the full entry?
<select 'summary' or 'full'>

'''
############################################
#  imports
############################################
import wikipedia #  imports wikipedia library
import textwrap #  used to format wiki text to improve readability
from gtts import gTTS #  importing gTTs module for text to speech conversion
import os #  imported to play converted audiocommit,


############################################
#  Input block
############################################
#  guide_search = 'douglas adams' #static search string
print("\n--------  DON'T PANIC  -------")
print("Welcome to the Hitchhiker's Guide to the Galaxy!")
print("options:\n(inputpi text) --> search\n(quit)--> exits program")
guide_search = input("Search the Guide for: -->")
if guide_search == "quit":
    exit()
print("Would you like the summary? Or the full entry?")
report = input()
############################################
#  looking up guide entry summary
############################################
if report == "summary":
    print("got it: summary\n")
    summ_para = wikipedia.summary(guide_search)
    page = wikipedia.page(guide_search)  #  grabbing page info to extract title
    summ_para_split = str.splitlines(summ_para)
    entry_title = page.title
    print("---------- " + entry_title + " ----------")
    for lines in range(0, len(summ_para_split)):
        line = textwrap.fill(summ_para_split[lines], initial_indent = '    ')
        print(line)
############################################
#  looking up guide entry full text
############################################
elif report == "full":
    print("got it: full entry\n")
    full_entry = wikipedia.page(guide_search) #  grabs full wiki page
    full_entry_text = full_entry.content #  returns text-only from wiki page
    full_entry_split = str.splitlines(full_entry_text)
    entry_title = full_entry.title
    print("---------- " + entry_title + " ----------")
    for lines in range(0, len(full_entry_split)):
        line = textwrap.fill(full_entry_split[lines], initial_indent = '    ')
        print(line)
############################################
#  exit statement
############################################
else:
    print("Sorry, i don't understand. Please reinitialize and try again.")
    exit()

print("\n\n Please wait for audio\n")  # reminds user to wait for audio
############################################


############################################
'''Temporarily commented out to improve speed of testing
############################################
# Using gTTs to read wiki text
############################################
# Language in which you want to convert
language = 'en'

# Passing the text and language to th   e engine,
# here we have marked slow=False. Whi   ch tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text = summ_para, lang = language, slow = False)

# Saving the converted audio in a mp3 file named
# test
yay = myobj.save("test.mp3")

# Playing the converted file
os.system("test.mp3")
#need a way to close the mp3 after playing
#os.close()
'''