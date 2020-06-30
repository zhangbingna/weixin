#coding=utf-8

import xlrd,xlwt
from xlutils3 import copy


class ReadExcel(object):
    def __init__(self, excel_path, sheet_name):
        self.path = excel_path
        self.data = xlrd.open_workbook(excel_path)

        self.table = self.data.sheet_by_name(sheet_name)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            xls = []
            j = 1
            for i in range(0, self.rowNum):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                xls.append(s)
                j += 1
        return xls

    def username(self):
        r = []
        j = 1
        for i in range(self.rowNum-1):
            values = self.table.row_values(j)
            s = values[0]
            r.append(s)
            j += 1
        return r

    def password(self, username):
        for i in range(0, self.rowNum):
            if self.table.cell(i, 0).value == username:
                password = self.table.cell(i, 1).value
            else:
                continue
        return password

    def writer(self, alias):
        wd = copy.copy(self.data)
        ws = wd.get_sheet(0)
        j = 1

        for s in alias:
            cell = self.table.cell(j, 5)
            if cell is None:
                ws.write(j, 5, s)
            else:
                cell = ""
                ws.write(j, 5, s)
            j += 1
        wd.save(self.path)


if __name__ == "__main__":
    filepath = "E://PyCharm-Project//_tmp_robertzhan.xls"
    data = ReadExcel(filepath, "account")
    #print(data.dict_data())
    #print(data.username())
    #data.writer([1, 2, 3])
    data.password("wxid_sgn2s6rkvcun12")
