import requests as req
url = "https://api4.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
res = req.get(url).text
print(res)
btc = res[29:34]
print(str(int(btc) * 1450) + '원') # 1억 1389만 6050원
won = str(int(btc) * 1450)

print(won)
# print(won[:1] +'억 ' + won[1:5] + '만 ' + won[5:] + '원')
print(((won[-12:8] +'억 ') if won[-12:-8] else "") + won[-8:-4] + '만 ' + won[-4:] + '원')