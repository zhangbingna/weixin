import xlrd,xlwt
from xlutils3 import copy
class ReadExcel(object):
    def __init__(self, excelPath, sheetName="account"):
        self.path = excelPath
        self.data = xlrd.open_workbook(excelPath)
    def writeAlias(self):
        rd = xlrd.open_workbook(self.path)
        wd = copy.copy(rd)
        ws = wd.get_sheet(0)
        print(ws.write(5,2,"123"))
        ws.writer()
        print(wd.save(self.path))

        #ws.write(5, 1, "123")
        #wd.save(self.path)
        print(ws)


if __name__ == "__main__":
    filepath = "E://PyCharm-Project//_tmp_robertzhan.xls"
    data = ReadExcel(filepath)

    data.writeAlias()