#-*-coding:utf-8-*-

import ddt,os,json
import unittest
from common.excel_pub import ExcelUtil

# testDate=[{"usename":"owddd","psw":"111111111134"},
#           {"usename":"iuer","psw":"2232222"},
#           {"usename":"uuood","psw":"0i7734"},
#           ]

sheetName = "Sheet1"
data = "C:\\apiTestForintfc\\testTodispose\\config"
excelPath = os.path.join(data, "apitestcase.xlsx")
data = ExcelUtil(excelPath, sheetName)
testDate=data.data_testcase3()
print type(testDate)
print testDate


@ddt.ddt
class kdiieree(unittest.TestCase):
    def setUp(self):
        print "start"
    def tearDown(self):
        print "end"
    @ddt.data(*testDate)
    def test_daii(self,value):
        print type(value)
        print value['testcaseID']


    # @ddt.data(*testDate)
    # @ddt.unpack
    # def test_daii2(self,a,b,c,d):
    #     print "dier===%s"%a
    #     print "dier2===%s" %b
    #     print "dier3===%s" %c
    #     print "dier4===%s" %d
    #     self.data = b
    #     self.caseName = c
    #     self.excelPath = os.path.join(self.data, self.caseName)
    #     self.f = open(self.excelPath)
    #     self.data = self.f.read()
    #     # print data
    #     self.f.close()
    #     # self.payload =json.loads(self.data)
    #
    #     self.payload2 = json.loads(self.data,encoding='GB2312')
    #     print self.payload2


if __name__=="__main__":
    aa=kdiieree().test_daii
    # print aa.test_daii

