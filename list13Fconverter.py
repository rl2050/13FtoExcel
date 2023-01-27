import xlsxwriter
import pdfplumber
import numpy as np
from config import *



def converting13fTolist(pdfName):

    list13fSec = []
    print(pdfName)

    #opening PDF file
    with pdfplumber.open(pdfName) as pdf:
        pageCount = len(pdf.pages)

        #looping through pages
        for x in range(startPageNumber, pageCount):
            print('processing page', x)
            progress = round(x / pageCount * 100,1)

            page = pdf.pages[x]
            lines = page.extract_tables(table_settings=pdfSettings)
            lines = lines[0]

            #removes the first 3 rows of the table
            for x in range(0,3):
                lines.pop(0)

            #remove spaces from CUSIP code
            y= 0
            for x in lines:
                lines[y][0] = x[0].replace(" ", "")
                y = y + 1

            #add 13f securlity to list
            for x in lines:
                list13fSec.append(x)

    # delete last line
    del list13fSec[-1]

    return list13fSec

def toExcelFile(list13fSec):
    #creating excel file
    with xlsxwriter.Workbook( pdfName[:-3] +'.xlsx') as workbook:
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        worksheet.write_row('A1', ['CUSIP NO','', 'ISSUER NAME', 'ISSUER DESCRIPTION', 'STATUS'], bold)
        for row_num, data in enumerate(list13fSec):
            worksheet.write_row(row_num+1, 0, data)
        worksheet.set_column('A:A', 12)
        worksheet.set_column('B:B', 1.5)
        worksheet.set_column('C:C', 35)
        worksheet.set_column('D:D', 21)
        worksheet.set_column('E:E', 8)

def toCSVfile(list13fSec):
    #creating csv file
    #current location of folder
    # file name + location
    fileName = pdfName[:-3] +'.csv'
    np.savetxt(fileName,  
        list13fSec, 
        delimiter =",",  
        fmt ='% s') 

if __name__ == '__main__':
    listof13fSec = converting13fTolist(pdfName)
    toExcelFile(listof13fSec)
    toCSVfile(listof13fSec)
