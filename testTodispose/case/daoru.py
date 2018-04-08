# -*- coding: utf-8 -*-
# @Author  : zuwei


import requests, json
import re,os,time
import unittest
import sys,ddt
from common.my_MD5andBase64 import API_skybusauth
from common.logger import Log
from common.excel_pub import ExcelUtil
from common.apply_token import applyToken

reload(sys)
sys.setdefaultencoding('utf-8')

sheetName = "Sheet1"
data = "C:\\apiTestForintfc\\testTodispose\\config"
excelPath = os.path.join(data, "apitestcase.xlsx")
data = ExcelUtil(excelPath, sheetName)
testDate=data.data_testcase2()
# print type(testDate)
# print testDate

# EXCEL = ExcelUtil(excelPath, 'Sheet1')
global token
token = applyToken().my_Token()
print "token:%s"%token

# payload["token"]=token
# print payload
# print "类型2：%s"%type(payload)

# @ddt.ddt
class rt_interface(unittest.TestCase):
    log = Log()

    # @unittest.skip(u'我很喜欢你，不想执行你')
    # @ddt.data(*testDate)
    # @ddt.unpack
    def test_RT(self):
        u'测试用力'
        self.intdiscrp = u'测试RT接口令牌无效1'
        self.log.info(self.intdiscrp + "---------start---------")
        self.url = "http://172.29.50.67:7060/sbe"
        self.data = "C:\\apiTestForintfc\\testTodispose\\config\\testcase_tickservic"
        self.caseName="SBE_DETR_TKTNO_1.txt"
        self.excelPath = os.path.join(self.data, self.caseName)
        self.f = open(self.excelPath)
        self.data = self.f.read()
        print data
        self.f.close()
        # self.payload =json.loads(self.data)
        self.payload=json.loads(self.data,encoding='GB2312')
        self.payload["token"] = token
        print "tihuan%s"%self.payload
        # MD5加密拿到skybusAuth
        self.ttestdMD5 = API_skybusauth()
        self.md5dd = self.ttestdMD5.skybus_md5(token, self.payload)
        self.headers = {"Content-Type": "application/json;charset=utf-8",
                        "skybusAuth": self.md5dd
                        }
        self.r = requests.post(self.url, json=self.payload, headers=self.headers, allow_redirects=False, verify=False)
        # 判断返回是否正确，正则表达式去提取"pnrcode":"HT4DKY"
        print type(self.r.content)
        self.log.info(self.intdiscrp + "-接口的返回--" + self.r.content)
        self.hope = "卢敬铭"
        # self.hope =hope
        if self.hope in self.r.content:
            a = True
            self.log.info(self.intdiscrp + "测试结果----" + "pass" + "-----")
        else:
            a = False
            self.log.info(self.intdiscrp + "测试结果-----" + "false" + "-----")
        # print a
        self.log.info(self.intdiscrp + "---期待值--" + self.hope)
        try:
            self.aa = self.assertTrue(a, msg="预期结果和实际结果不符")
        except() as e:
            self.log.info(self.intdiscrp + str(e))
            raise
        time.sleep(2)
        self.log.info(self.intdiscrp + "------------end--------------------")


if __name__ == '__main__':
    unittest.main()
