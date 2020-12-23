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
            for i in range(1, self.rowNum):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(i)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                xls.append(s)
        return xls

    def username(self):
        r = []
        for i in range(1, self.rowNum):
            values = self.table.row_values(i)
            s = values[0]
            r.append(s)
        return r

    def password(self, username):
        for i in range(1, self.rowNum-1):
            values = self.table.row_values(i)
            if values[0] == username:
                password_name = values[1]
            else:
                continue
        return password_name

    def writer(self, alias, col):
        wd = copy.copy(self.data)
        ws = wd.get_sheet(0)
        j = 1

        for s in alias:
            cell = self.table.cell(j, col)
            if cell is None:
                ws.write(j, col, s)
            else:
                cell = ""
                ws.write(j, col, s)
            j += 1
        wd.save(self.path)


if __name__ == "__main__":
    filepath = "E://PyCharm-Project//_tmp_robertzhan.xls"
    data = ReadExcel(filepath, "account")
    print(data.dict_data())
    #print(data.rowNum)
    #print(data.username())
    #data.writer([1, 2, 3])
    print(data.password("wxid_sgn2s6rkvcun12"))
