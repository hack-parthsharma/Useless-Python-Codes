# Title: Get service provider name from Mobile NO using Python.
# Author: @CodeProgrammer "On Telegram" || @PythonSy "On Instagram".
"""
you need to install phonenumbers by using this command in the terminal:
pip install phonenumbers
for more codes you can visit our channel on Telegram: @CodeProgrammer
"""

import phonenumbers
from phonenumbers import carrier

mobileNo = input("Enter mobile number with country code: ")

service_provider = phonenumbers.parse(mobileNo)

print(carrier.name_for_number(service_provider, "en"))
