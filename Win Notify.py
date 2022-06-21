# Title: Windows Notification using Python.
"""
you need to install win10toast by using this command in the terminal:
pip install win10toast
for more codes you can visit our channel on Telegram: @CodeProgrammer.
"""
from win10toast import ToastNotifier

def windows_popup (title, content, duration=5000):
    toast= ToastNotifier()
    toast.show_toast(title, content, duration=duration)

if __name__ == '__main__':
    windows_popup("Hello", "From @CodeProgrammer")
