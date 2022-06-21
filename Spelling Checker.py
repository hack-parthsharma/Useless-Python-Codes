# Title: Spelling Checker in Python.
# Author: @CodeProgrammer "On Telegram" || @PythonSy "On Instagram".
"""
you need to install PyPDF2 by using this command in the terminal:
pip install PyPDF2
for more codes you can visit our channel on Telegram: @CodeProgrammer.
"""
from textblob import TextBlob

# Type text that contains spelling errors
a = "comuter programing is gret"
print("Orginal Text: " + str(a))

b = TextBlob(a)
print("Corrected Text: " + str(b.correct()))
