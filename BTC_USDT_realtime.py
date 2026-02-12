# 이전에 알아낸 실시간 비트코인 BTC / USD 가격으로 
# 실시간 환율을 계산하여
# 지금 비트코인 가격을 원화로 표시하시오

# py 파일로 저장하여 python3로 실행할 수 있도록 하시요.

import requests as req

BTC_url = "https://api4.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
BTC_res = req.get(BTC_url).json()

USD_url = "https://oapi.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=45cPFv2JJj2IKkjXjU5H8QPWzLpIaUYS&data=AP01"
USD_res = req.get(USD_url).json()

KRW_BTC = float(BTC_res['price']) * float(USD_res[-1]['deal_bas_r'].replace(',',''))

print("현재 비트코인 가격은 원화로 %d 원 입니다." % KRW_BTC)

# print("현재 비트코인 가격은 원화로 %f 원 입니다" % .format(4))