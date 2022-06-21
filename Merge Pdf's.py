# Title: Merge multiple PDFs to one PDF usong Python.
# Author: @CodeProgrammer "On Telegram" || @PythonSy "On Instagram".
"""
you need to install PyPDF2 by using this command in the terminal:
pip install PyPDF2
for more codes you can visit our channel on Telegram: @CodeProgrammer.
"""
from PyPDF2 import PdfFileMerger

# Choose the path and name of the pdf files you want to merge
pdfs = ['python.pdf', 'django.pdf', 'tkinter.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
