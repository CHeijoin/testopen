# -*- coding: utf-8 -*-
# @Author  : zuwei


import requests, json
import re
import unittest
import sys,os,time
from common.my_MD5andBase64 import API_skybusauth
from common.logger import Log
from common.excel_pub import ExcelUtil
from common.apply_token import applyToken

reload(sys)
sys.setdefaultencoding('utf-8')

data = "C:\\apiTestForintfc\\testTodispose\\config"

excelPath = os.path.join(data, "case.xlsx")
EXCEL = ExcelUtil(excelPath, 'Sheet1')
global token
token = applyToken().my_Token()
# global null
# null=''

class rt_interface(unittest.TestCase):
    log = Log()
    # print "token是%s"%token
    # @unittest.skip(u'我很喜欢你，但是不爱你')
    def test_RT(self):
        u'测试RT令牌无效1'
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        aa = EXCEL.rowlist(0)
        bda=EXCEL.dict_api(5,0)
        if bda['isResult'] == 1:
            bda['isResult'] = "true"
        else:
            bda['isResult'] = "false"
        bda['token']=token
        bda['timestamp']=now
        # bda['ibeFlag']=""
        # bda['type']=""
        bb =bda
        self.intdiscrp =aa[1]
        # print self.intdiscrp
        self.log.info(self.intdiscrp + "---------start---------")
        # self.url = aa[1]
        self.url ="http://172.29.50.67:7060/sbe"
        # print self.url
        self.payload =bb
        # print self.payload
        # self.payload2=json.load(self.payload)
        # self.ccmytoken = eval(self.payload.replace("self.token", token))
        # print "990000000000"
        # print "ccmytoken:%s"%self.ccmytoken
        # MD5加密拿到skybusAuth
        self.ttestdMD5 = API_skybusauth()
        self.md5dd = self.ttestdMD5.skybus_md5(token,self.payload)
        # print self.md5dd
        self.headers = {"Content-Type": "application/json;charset=utf-8",
                        "skybusAuth": self.md5dd
                        }
        self.r = requests.post(self.url, json=self.payload, headers=self.headers, allow_redirects=False, verify=False)

        # 判断返回是否正确，正则表达式去提取"pnrcode":"HT4DKY"

        # print self.r.content
        jkd=self.r.json()
        io8=jkd["airsegs"]
        print "respone:%s"%jkd
        print type(io8)
        print io8
        self.log.info(self.intdiscrp + "--"+self.r.content)
        self.t = re.findall(r'"resultCode":(.+?),', self.r.content)
        self.ACTresults = self.t[0]
        # print self.t[0]
        # 期望值
        self.hope ="0"
        # print self.hope
        try:
            self.aa = self.assertEqual(self.t[0], self.hope, msg="预期结果和实际结果不符")
        except() as e:
            self.log.info(self.intdiscrp + str(e))

            raise

        self.log.info(self.intdiscrp + "------------end--------------------")



if __name__ == '__main__':
    unittest.main()
