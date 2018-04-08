# -*- coding: utf-8 -*-
# @Author  : zuwei


import requests
import re
import sys,time
from common.my_MD5andBase64 import API_skybusauth
from common.logger import Log
# from common.excel_pub import ExcelUtil

reload(sys)
sys.setdefaultencoding('utf-8')


biosSN="d41d8cd98f00b204e9800998ecf8427e"
# 测试地址帐号
# accountname="chenjie1"
# psw="chenjie1"
# url = "http://172.29.50.67:7060/sbe"


# 生产地址帐号
accountname="dataservice01"
psw="gzapisupport1"
url = "http://113.108.131.149:8060/sbe"
basetoken = accountname + "#" + API_skybusauth().my_md5(psw) + "#" + biosSN
# print "basetoken:%s"%basetoken
clientInfo = API_skybusauth().my_base64(basetoken)
print "clientInfo:%s"%clientInfo
now = time.strftime("%Y-%m-%d %H:%M:%S")

class applyToken():
    log=Log()

    #挂起帐号
    def ACCOUNT_DEACTIVE(self):
        self.param1={"clientInfo": clientInfo,
                    "serviceName": "ACCOUNT_DEACTIVE",
                    "timestamp": now,
                    "token": ""
                    }
        self.r1 = requests.post(url, json=self.param1, allow_redirects=False, verify=False)
        # print self.r1.content
    #激活帐号
    def ACCOUNT_ACTIVE(self):
        self.param2={"clientInfo":clientInfo,
                     "serviceName": "ACCOUNT_ACTIVE",
                     "timestamp": now,
                     "token":""
                     }
        self.r2 = requests.post(url, json=self.param2, allow_redirects=False, verify=False)
        # print self.r2.content
    #申请令牌
    def APPLY_TOKEN(self):
        global mytoken
        self.param3={"authenticator": clientInfo,
                     "serviceName": "APPLY_TOKEN",
                     "timestamp": now,
                     "token":""
                     }
        self.r3 = requests.post(url, json=self.param3, allow_redirects=False, verify=False)
        print self.r3.content
        # self.t = re.findall(r'"token":"(.*)","timestamp', self.r3.content)
        self.t = re.findall(r'"token":"(.+?)",', self.r3.content)
        aa = self.t[0]
        if aa =="null":
            print "未申请到令牌"
        else:
            mytoken=aa.replace('"','')
            # mytoken=aa
            # print mytoken
        # print mytoken
        return mytoken




    #申请令牌一溜儿
    def my_Token(self):

        applyToken().ACCOUNT_DEACTIVE()
        applyToken().ACCOUNT_ACTIVE()
        self.my_token=self.APPLY_TOKEN()
        print "令牌是：%s"%self.my_token
        return self.my_token



if __name__=='__main__':
#     # applyToken().ACCOUNT_DEACTIVE()
#     # applyToken().ACCOUNT_ACTIVE()
#     # applyToken().APPLY_TOKEN()
    applyToken().my_Token()

