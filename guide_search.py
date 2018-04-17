#day 1 of the 100 days of code

#print("hello, world!!")

#Hitchhiker's Guide to the Galaxy
'''
Project phase 1: Create a program that takes an input string, looks for a match in wikipedia, and pulls up the result
    in the terminal
Future phases will add support for voice input (for search), and computer voice output (to read wiki entry to user)
'''

#imports
import wikipedia #imports wikipedia library
import textwrap #used to format wiki text to improve readability
from gtts import gTTS #importing gTTs module for text to speech conversion
import os #imported to play converted audio


############################################
#Input block
#guide_search = 'douglas adams' #static search string
print("Welcome to Wikipedia")
print("options:\n(input text) --> search\n(quit)--> exits program")
guide_search = input("Search the Guide for:   ")
if guide_search == "quit":
    exit()
############################################
############################################
# looking up wiki entry specified by input string
############################################
summ_para = wikipedia.summary(guide_search)
summ_para_split = str.splitlines(summ_para)
for lines in range(0, len(summ_para_split)):
    line = textwrap.fill(summ_para_split[lines], initial_indent = '    ')
    print(line)
print("\n\n Please wait for audio\n") #reminds user to wait for audio
############################################
'''Temporarily commented out to improve speed of testing
############################################
# Using gTTs to read wiki text
############################################
# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
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