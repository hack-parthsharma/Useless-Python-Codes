# Title: Get HTML code of any website using Python.
# Author: @CodeProgrammer "On Telegram" || @PythonSy "On Instagram".
"""
you need to install bs4 by using this command in the terminal:
pip install bs4
for more codes you can visit our channel on Telegram: @CodeProgrammer
"""

import requests
from bs4 import BeautifulSoup

url = "https://python.org"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.prettify())
