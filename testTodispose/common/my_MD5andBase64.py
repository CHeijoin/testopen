# -*- coding: utf-8 -*-
# @Author  : zuwei


import md5,base64
import sys

import json
reload(sys)

sys.setdefaultencoding('utf-8')


class API_skybusauth():


    def skybus_md5(self,tokend,jsonbody):
        bb=json.dumps(jsonbody)
        a=tokend+"_"+bb
        a1 = md5.new()
        # print a1
        a1.update(a.encode(encoding='utf-8'))
        # print a1
        skybusauth=a1.hexdigest()
        # print skybusauth
        return skybusauth


    def my_md5(self,sourced):
        u'md5的加密1'
        b1=md5.new()
        b1.update(sourced.encode(encoding='utf-8'))
        my_md4res=b1.hexdigest()
        return my_md4res


    def my_base64(self,x):
        u'base64加密'
        bs1=base64.b64encode(x)
        # print bs1

        return bs1





# 883db800a20fc96aaab04f44df777d13

#
# if __name__=="__main__":
#
#     jsonbody = {"class": "com.travelsky.sbeclient.obe.request.PNRRequest",
#                 "ibeFlag": "",
#                 "isResult": "true",
#                 "officeNo": "ufo099",
#                 "pnrNo": "HT4DKY",
#                 "serviceName": "SBE_RT",
#                 "timestamp": "2018-02-01",
#                 "token": "Y2hlbmppZTEjMjAxOC0wMi0wMiAxMTo0NTozOA==",
#                 "type": ""
#                 }
#     tokend="Y2hlbmppZTEjMjAxOC0wMi0wMiAxMTo0NTozOA=="
#
#     print "883db800a20fc96aaab04f44df777d13"
#     print API_skybusauth().skybus_md5(tokend,jsonbody)
#     print API_skybusauth().my_md5("14333")
#     print "62ef6dc6cdbfc1c60305b7d3d9a420a6"
#     print "ODhfODgzNDM="
#     API_skybusauth().my_base64("88_88343")
