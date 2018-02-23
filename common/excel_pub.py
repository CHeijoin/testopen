# coding:utf-8
import xlrd
import sys

reload(sys)
sys.setdefaultencoding('utf-8')



class ExcelUtil(object):

    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # get titles
        self.row = self.table.row_values(0)
        self.col = self.table.col_values(0)
        # get rows number
        self.rowNum = self.table.nrows
        # get columns number
        self.colNum = self.table.ncols
        # the current column
        self.curRowNo = 1

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo :
            return False
        else:
            return True

    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r

    def rowlist(self, i):
        # 按行读取存为list,去除空字符
        rowlist = self.table.row_values(i)
        n = rowlist.count("")
        for i in range(n):
            rowlist.remove(u'')
        return rowlist

    def collist(self, o):
        # 按列读取存为list,去除空字符
        collist = self.table.col_values(o)
        n = collist.count("")
        for i in range(n):
            collist.remove(u'')
        return collist

    def readasdict(self):
        d = {}
        col = self.table.col_values(0)
        nrows = self.table.nrows
        for i in range(nrows):
            val = self.rowlist(i)[1:]
            if len(val) == 1:
                 d[col[i]] = val[0]
            else:
                d[col[i]] = val
        return d

    def readaslitbyrow(self, i, j):
        l = []
        s = self.rowlist(i)
        e = self.rowlist(j)
        for i in range(1, len(s)):
            d = {}
            d[s[0]] = s[i]
            d[e[0]] = e[i]
            l.append(d)
        return l




    def dict_api(self, row, col):
        u'api接口输入的参数'
        self.mkrow = row
        self.mkcol = col
        # print self.mkrow
        # print self.mkcol
        if self.rowNum <= 1:
            print ("excel表总行数小于1")
        else:
            s = {}

            for i in range(self.mkcol, self.colNum - 1):
                # print "i是 是%d" % i
                self.keys = self.table.col_values(i)
                self.values = self.table.col_values(i + 1)
                for j in range(self.mkrow - 1, self.rowNum):
                    # print "j是：%d" % j
                    self.rowkey = self.keys[j]
                    # print "key为：%s" % self.rowkey
                    self.rowvalue = self.values[j]
                    s[self.rowkey] = self.rowvalue
                    # print s
                return s

if __name__=="__main__":
    import os
    # filepath = "C:\\ptest\\my_interfacetest01\\my_case\\case.xlsx"
    sheetName = "Sheet1"
    data = "C:\\apiTestForintfc\\testTodispose\\config"
    excelPath = os.path.join(data, "case.xlsx")
    data = ExcelUtil(excelPath, sheetName)
    aa = data.dict_api(5,0)
    if aa['isResult']==1:
        aa['isResult']="True"
    else:
        aa['isResult']="False"
    print aa




    # u = excel.readasdict()
    # s = u["locator"]
    # for i in s:
    #     print i
