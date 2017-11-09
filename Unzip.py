import zipfile
from xlrd import open_workbook
import csv
from io import StringIO

zfilePath = 'C:/Users/Kaixiang Wang/PycharmProjects/UnzipFile/'
zfileName = 'Libraries.io-open-data-1.0.1.zip'
fileName = 'dependencies-1.0.0-2017-06-15.csv'
zipFile = zipfile.ZipFile(zfilePath + zfileName)

with open(zipFile.read(fileName), 'rU') as projectFile:
    for row in projectFile:
        print(row[0])

# projectFile = StringIO(zipFile.read(fileName).decode())
# csvReader = csv.reader(projectFile)
# for row in csvReader:
#     print(row[0])
#     print(row[1])

def read_excel (filePath):
    wb = open_workbook(filePath)
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols

        items = []

        rows = []
        for row in range(1, number_of_rows):
            values = []
            for col in range(number_of_columns):
                value = (sheet.cell(row, col).value)
                try:
                    value = str(int(value))
                except ValueError:
                    pass
                finally:
                    values.append(value)