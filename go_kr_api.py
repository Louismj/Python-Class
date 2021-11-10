from datetime import date, timedelta
import urllib
from ipython_genutils.py3compat import encode
import requests 
from urllib.request import urlopen, Request 
from urllib.parse import urlencode, unquote, quote_plus 
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame 


import json 
import pandas as pd


'''
url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList'
# ServiceKey = Decoding 인증키 사용 
# 종관기상관측 지점명(stnIds) 131은 청주 
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'LkzEsrCIjgmCrmRxABGtrVUQZMnAWW6FBEZZkiYSBjGW7/6DP7Ha2xN0GkI0i5EhTrbTm+g8+D67YejiChLteA==', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '999', quote_plus('dataType') : 'JSON', quote_plus('dataCd') : 'ASOS', quote_plus('dateCd') : 'HR', quote_plus('startDt') : '20200101', quote_plus('startHh') : '01', quote_plus('endDt') : '20200601', quote_plus('endHh') : '01', quote_plus('stnIds') : '131' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request, timeout=60).read() # get bytes data 
data = json.loads(response_body) # convert bytes data to json 
print(data)

with open('./data/131_청주.json', 'w', encoding='utf-8') as file :
        json.dump(data, file, ensure_ascii=False, indent='\t')
'''



### 천리안 위성 API ### 

from datetime import timedelta
import datetime

now = datetime.datetime.now()

fullDate = now.strftime('%Y%m%d')
print(fullDate)

before_one_day = now - timedelta(days=1)
before_one_day = before_one_day.strftime('%Y%m%d')
print(before_one_day)

nowDate = now.strftime('%m%d')
filename = 'ir105' + '_' + nowDate
# filename = 'vi006' + '_' + nowDate

print(nowDate)



url = 'http://apis.data.go.kr/1360000/SatlitImgInfoService/getInsightSatlit'
# ServiceKey = Decoding 인증키 사용 
# 기상청 위성영상 천리안 위성조회서비스
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'LkzEsrCIjgmCrmRxABGtrVUQZMnAWW6FBEZZkiYSBjGW7/6DP7Ha2xN0GkI0i5EhTrbTm+g8+D67YejiChLteA==', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('dataType') : 'JSON', quote_plus('sat') : 'G2', quote_plus('data') : 'ir105', quote_plus('area') : 'ko', quote_plus('time') : before_one_day })


request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request, timeout=60).read() # get bytes data 
data = json.loads(response_body) # convert bytes data to json 
print(data)


with open('./data/external/천리안_위성/'+ filename + '.json', 'w', encoding='utf-8') as file :
        json.dump(data, file, ensure_ascii=False, indent='\t')

