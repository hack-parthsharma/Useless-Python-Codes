# Title: Convert from Excel File to CSV File using Python.
# Author: @CodeProgrammer "On Telegram" || @PythonSy "On Instagram".
"""
you need to install xlrd by using this command in the terminal:
pip install xlrd
for more codes you can visit our channel on Telegram: @CodeProgrammer.
"""
import xlrd
import csv

def csv_from_excel():
    # Choose the path and filename of the Excel file you want to convert to csv file
    wb = xlrd.open_workbook('scheduling.xlsx')
    # Choose the name of the slice in the selected Excel file that you want to convert to csv
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('your_csv_file.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

# runs the csv_from_excel function:
csv_from_excel()