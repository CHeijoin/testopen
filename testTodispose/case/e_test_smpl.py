# -*- coding: utf-8 -*-
# @Author  : zuwei


import requests, json
import re
import unittest
import sys
from common.my_MD5andBase64 import API_skybusauth
from common.logger import Log

reload(sys)
sys.setdefaultencoding('utf-8')


class rt_interface(unittest.TestCase):
    log = Log()

    # @unittest.skip(u'我很喜欢你，不想执行你')
    def test_RT(self):
        u'测试RT令牌无效1'
        self.intdiscrp = u'测试RT接口令牌无效1'
        self.log.info(self.intdiscrp + "---------start---------")

        self.url = "http://172.29.50.67:7060/sbe"
        self.payload = {"class": "com.travelsky.sbeclient.obe.request.PNRRequest",
                        "ibeFlag": "",
                        "isResult": "true",
                        "officeNo": "ufo099",
                        "pnrNo": "HT4DKY",
                        "serviceName": "SBE_RT",
                        "timestamp": "2018-02-01",
                        "token": "Y2hlbmppZTEjMjAxOC0wMi0wMiAxMTo0NTozOA==",
                        "type": ""
                        }
        self.token = "Y2hlbmppZTEjMjAxOC0wMi0wMiAxMTo0NTozOA=="

        # MD5加密拿到skybusAuth
        self.ttestdMD5 = API_skybusauth()
        self.md5dd = self.ttestdMD5.skybus_md5(self.token, self.payload)
        self.headers = {"Content-Type": "application/json;charset=utf-8",
                        "skybusAuth": self.md5dd
                        }
        self.r = requests.post(self.url, json=self.payload, headers=self.headers, allow_redirects=False, verify=False)

        # 判断返回是否正确，正则表达式去提取"pnrcode":"HT4DKY"

        print self.r.content
        self.t = re.findall(r'"errorDescription":"(.+?)"', self.r.content)
        self.ACTresults = self.t[0]
        print self.t[0]
        # 期望值
        self.hope = u"令牌无效"
        try:
            self.aa = self.assertEqual(self.t[0], self.hope, msg="预期结果和实际结果不符")
        except() as e:
            self.log.info(self.intdiscrp + str(e))

            raise

        self.log.info(self.intdiscrp + "------------end--------------------")

    def test_RT2(self):
        u'测试RT令牌无效2'

        self.intdiscrp = u'测试RT接口令牌无效2'
        self.log.info(self.intdiscrp + "---------start---------")
        self.url = "http://172.29.50.67:7060/sbe"
        self.payload = {"class": "com.travelsky.sbeclient.obe.request.PNRRequest",
                        "ibeFlag": "",
                        "isResult": "true",
                        "officeNo": "ufo099",
                        "pnrNo": "HT4DKY",
                        "serviceName": "SBE_RT",
                        "timestamp": "2018-02-01",
                        "token": "Y2hlbmppZTEjMjAxOC0wMi0wMiAxMTo0NTozOA==",
                        "type": ""
                        }
        self.token = "Y2hlbmppZTEjMjAxOC0wMi0wMiAxMTo0NTozOA=="
        # MD5加密拿到skybusAuth
        self.ttestdMD5 = API_skybusauth()
        self.md5dd = self.ttestdMD5.skybus_md5(self.token, self.payload)
        self.headers = {"Content-Type": "application/json;charset=utf-8",
                        "skybusAuth": self.md5dd
                        }
        self.r = requests.post(self.url, json=self.payload, headers=self.headers, allow_redirects=False, verify=False)

        # 判断返回是否正确，正则表达式去提取"pnrcode":"HT4DKY"

        print self.r.content
        self.t = re.findall(r'"errorDescription":"(.+?)"', self.r.content)
        self.ACTresults = self.t[0]
        print self.t[0]
        # 期望值
        self.hope = u"令牌无效1"

        try:
            self.aa = self.assertEqual(self.t[0], self.hope, msg="预期结果和实际结果不符")

        except(AssertionError) as e:
            self.log.error(self.intdiscrp + str(e))
            #try...except...后使用raise 将断言结果再次抛出，使得测试用例抛出faile
            raise

        self.log.info(self.intdiscrp + "------------end--------------------")


if __name__ == '__main__':
    unittest.main()
