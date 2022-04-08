from xlutils.copy import copy
import xlrd
import xlwt

file_path="C:\\"
book = xlrd.open_workbook("C:\hola_python.xls",formatting_info=True)
sh = book.sheet_by_index(0)
wb = copy(book)
w_sheet = wb.get_sheet(0)
for rx in range(sh.nrows):
    print(sh.row(rx)[0])
    w_sheet.write(1,0,"TEST DE ESCRITO XLWR")
    wb.save(file_path + "writed.xls")