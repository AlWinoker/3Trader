# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 11:41:44 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 21:05:31 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:56:08 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 11:17:54 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 10:10:29 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 09:27:01 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 00:23:56 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 22:21:47 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 21:51:38 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 15:57:33 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 13:20:08 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 10:21:24 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 12:45:56 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 08:34:38 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 07:44:57 2022

@author: 14015
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 10:52:07 2022

@author: 14015
"""
import requests
import matplotlib.pyplot as plt
import numpy as np
import time 
from urllib.parse import urljoin, urlencode
import json
import hmac
import hashlib
import random

from binance.client import Client

#tickerPairs = ['USDT','BUSDUSDT','ETHUSDT','BTCBUSD','BTCUSDC','USDCUSDT','ETHBUSD','MATICUSDT','ETHBTC','USDCBUSD','SOLUSDT','BURGERUSDT','AAVEUSDT','AVAXBUSD','BNBUSDT','RUNEBUSD','VIDTUSDT','ETHUSDC','LRCUSDT','MATICBUSD','WAVESUSDT','ADAUSDT','BURGERBUSD','SHIBBUSD','SOLBUSD','CHZUSDT','BTCGBP','BNBBUSD','UNIUSDT','BTCEUR','ETHEUR','UNFIUSDT','SNXUSDT','LUNCBUSD','DOTBUSD','MATICBTC','SHIBUSDT','XRPUSDT','SCRTUSDT','DYDXUSDT','SANDUSDT','LUNAUSDT','BAKEUSDT','PERPUSDT','JASMYUSDT','ONEUSDT','XMRUSDT','EGLDUSDT','FILUSDT','ELFUSDT','BTCSTUSDT','LUNABUSD','XTZUSDT','ATOMUSDT','TROYBUSD','SUSHIUSDT']
#tickerPairs = ['BTCBUSD','BTCUSDT','BUSDUSDT','ETHUSDT','VGXUSDT','SOLUSDT','BTCUSDC','ETHBUSD','BNBUSDT','ETHBTC','USDCUSDT','BURGERUSDT','MATICUSDT','ADAUSDT','ADAUSDT','BTCEUR','USDCBUSD','BNBBUSD','KMDUSDT','AVAXBUSD','GMTUSDT','USTCBUSD','SOLBUSD','WINUSDT','ADABUSD','BURGERBUSD','AAVEUSDT','UNIUSDT','VGXBTC','ETHUSDC','XRPUSDT','SHIBUSDT','USDTTRY','ETHEUR','FTMUSDT','LUNCBUSD','APEUSDT','TRXUSDT','MATICBUSD','SANDUSDT','DOGEUSDT','DOTUSDT','GALAUSDT','LINKUSDT','RUNEUSDT','XRPBUSD','NEARUSDT','FILUSDT','WTCUSDT','JASMYUSDT','STPTBUSD','BUSDTRY','DYDXUSDT','OGNUSDT','WAVESUSDT','ANCUSDT','LDOUSDT','ICPUSDT','MANAUSDT','VIDTUSDT','RUNEBUSD','AVAXUSDT','BTCTRY','ATOMUSDT','BEAMUSDT','LTCUSDT','APEBUSD','BTCGBP','ETHGBP','CHZUSDT','REIUSDT','FLMUSDT','SANDBUSD','AVAXTRY','NEARBUSD','BTCSTUSDT','SHIBBUSD','DOTBUSD','CKBUSDT','UNFIUSDT','GMTBUSD','LUNAUSDT','EGLDUSDT','AUDUSDT','ETHTRY','VETUSDT','ZILUSDT','SRMUSDT','ONEUSDT','CRVUSDT','BNBBTC','LUNABUSD','BTCAUD','TROYBUSD','PEOPLEUSDT','ANCBUSD','USDTBRL','KEYBUSD','OPUSDT','GBPUSDT','WRXUSDT','QNTUSDT','OCEANUSDT','XTZUSDT','TUSDUSDT','BUSDBRL','LTCBUSD','ALGOUSDT','ARUSDT','BCHUSDT','ROSEUSDT','AAVEBUSD','USDTDAI','ADXUSDT','BTCSTBUSD','BTCBRL','ETCUSDT','SHIBTRY','AXSUSDT','MINAUSDT','RSRUSDT','COMPUSDT','LDOBUSD','BTTCUSDT','DOGEBUSD','ATOMBUSD','ACHBUSD','SNXUSDT','AUDBUSD','ZECUSDT','BELUSDT','TLMUSDT','ICPBUSD','XRPBTC','XMRUSDT','GALABUSD','MBLUSDT','SCRTUSDT','TVKUSDT','PNTUSDT','ALICEUSDT','KMDBTC','SLPUSDT','BTCDOWNUSDT','LEVERUSDT','WAVESBTC','XMRBTC','REIBUSD','WBTCBTC','BELTRY','YFIIUSDT','RUNEBTC','RUNEBTC','WOOUSDT','SUNUSDT','CTXCUSDT','NULSUSDT','PAXGBUSD','STPTUSDT','HIGHUSDT','NMRUSDT','SOLUSDC','TRXBUSD','STORJUSDT','LINKBTC','GRTUSDT','BNBETH','ETHDAI','LINKBUSD','KEYUSDT','MATICBTC','ELFUSDT','XLMUSDT','PAXGUSDT','EOSUSDT','LRCUSDT','SOLBTC','ETHDOWNUSDT','FTMBUSD','BAKEUSDT','FTTUSDT','GALUSDT','VGXETH','WINBUSD','VIDTBUSD','PYRUSDT','EPXUSDT','ETHAUD','MOVRUSDT','JSTUSDT','JASMYBUSD','PERPUSDT','SUSHIUSDT','CKBBUSD','ENSUSDT','ADABTC','THETAUSDT','DARUSDT','AVAXBTC','ENJUSDT','UNIBUSD','LTCBTC','UNFIBUSD','BTCUPUSDT','ENJUSDT','MIRUSDT','SOLEUR','DCRUSDT','ETHUPUSDT','DOTBTC','CAKEUSDT','LITUSDT','YFIUSDT','HOTUSDT','DASHUSDT','IMXUSDT','IOTXUSDT','WAVESBUSD','VTHOUSDT','ROSEBUSD','GBPBUSD','FTTBUSD','USDTBIDR','EGLDBUSD','LINKUPUSDT','WTCBTC','FILBUSD','ADAUPUSDT','UMAUSDT','WRXBUSD','GLMRUSDT','OPBUSD','OPBUSD','COCOSTRY','CVXUSDT','UNIBTC','IOTAUSDT','SCRTBUSD','CELOUSDT','BIFIUSDT','SPELLUSDT','LOOMBTC','IOSTUSDT','IDEXUSDT','AXSBUSD','SOLTRY','VITEUSDT','ONEBUSD','DYDXBUSD','GMTTRY','MANABUSD','KLAYUSDT','TRXBTC','WANUSDT','ELFBUSD','BLZUSDT','KDABUSD','QTUMUSDT','CELRUSDT','MASKUSDT','SANDBTC','AAVEBTC','EPXBUSD','FIROUSDT','SPELLTRY','SXPUSDT','MFTUSDT','CHRUSDT','XRPUSDC','HBARUSDT','LITBUSD','BADGERUSDT','SSVBTC','TRBUSDT','DOGEBTC','OXTUSDT','SANTOSTRY','USDTUAH','RVNUSDT','KAVAUSDT','DUSKUSDT','VETBUSD','WNXMUSDT','FTMTRY','BTCDAI','NBSUSDT','BETHETH','SKLUSDT','ADAUSDC','TLMTRY','1INCHUSDT','OMUSDT','QNTBUSD','ATOMBTC','GMTBTC','DODOUSDT','XRPEUR','ADADOWNUSDT','COTIUSDT','ARPATRY','RENUSDT','SFPUSDT','BELBUSD','KP3RUSDT','BNXUSDT','BNBEUR','TLMBUSD','ELFBTC','RLCUSDT','AUDIOUSDT','BEAMBTC','HNTUSDT','LEVERBUSD','AERGOBUSD','JASMYBTC','ONTUSDT','SANTOSUSDT','ANKRUSDT','ATAUSDT','ARPAUSDT','MKRUSDT','OGUSDT','CHZBUSD','UGNBUSD','RAMPUSDT','BCHBUSD','DOTDOWNUSDT','BUSDBIDR','DOTUPUSDT','LINKDOWNUSDT','KSMUSDT','CTSIUSDT','WAVESTRY','RUNEETH','SUPERUSDT','APEBTC','RADUSDT','STRAXUSDT','MULTIUSDT','TVKBUSD','ZILBUSD','ILVUSDT','PERPBUSD','QNTBTC','GTOUSDT','SRMBUSD','JOEUSDT','LINAUSDT','LINKETH','API3USDT','LOKAUSDT','OMGUSDT','BTCSTBTC','MANABTC','NMRBUSD','QIUSDT','ALGOBUSD','FETUSDT','BNBUSDC']
#tickerPairs = ['ZRXUSDT','1INCHUSDT','AAVEUSDT','GHSTUSDT','ACAUSDT','AGLDUSDT','ALCXUSDT','ACHUSDT','ALGOUSDT','TLMUSDT','ADXUSDT','FORTHUSDT','ANKRUSDT','APEUSDT','API3USDT','ANTUSDT','ASTRUSDT','AUDIOUSDT','REPUSDT','AVAXUSDT','AXSUSDT','BADGERUSDT','BNTUSDT','BALUSDT','BANDUSDT','BONDUSDT','BATUSDT','BICOUSDT','BTCUSDT','BCHUSDT','BTTUSDT','FIDAUSDT','ADAUSDT','CTSIUSDT','LINKUSDT','CHZUSDT','CHRUSDT','CVCUSDT','COMPUSDT','CVXUSDT','ATOMUSDT','COTIUSDT','CRVUSDT','DAIUSDT','DASHUSDT','MANAUSDT','DENTUSDT','DOGEUSDT','DYDXUSDT','EGLDUSDT','ENJUSDT','MLNUSDT','EOSUSDT','ETHUSDT','ETCUSDT','ENSUSDT','FTMUSDT','FETUSDT','FILUSDT','FLOWUSDT','FXSUSDT','GALAUSDT','GTCUSDT','GNOUSDT','FARMUSDT','ICXUSDT','IDEXUSDT','RLCUSDT','IMXUSDT','INJUSDT','ICPUSDT','JASMYUSDT','KAVAUSDT','KEEPUSDT','KP3RUSDT','KSMUSDT','KNCUSDT','LDOUSDT','LSKUSDT','LTCUSDT','LPTUSDT','LRCUSDT','MCUSDT','MULTIUSDT','ALICEUSDT','MKRUSDT','MASKUSDT','MINAUSDT','MIRUSDT','XMRUSDT','GLMRUSDT','MOVRUSDT','NANOUSDT','NEARUSDT','NMRUSDT','OCEANUSDT','OMGUSDT','OXTUSDT','OGNUSDT','PAXGUSDT','PERPUSDT','PHAUSDT','PLAUSDT','DOTUSDT','MATICUSDT','POWRUSDT','QTUMUSDT','QNTUSDT','RAYUSDT','RENUSDT','RNDRUSDT','REQUSDT','XRPUSDT','SCRTUSDT','KEYUSDT','SRMUSDT','SHIBUSDT','SCUSDT','SOLUSDT','SPELLUSDT','XLMUSDT','GMTUSDT','STORJUSDT','SUSHIUSDT','RADUSDT','FISUSDT','SUPERUSDT','RAREUSDT','SNXUSDT','USTUSDT','TVKUSDT','XTZUSDT','GRTUSDT','SANDUSDT','RUNEUSDT','TUSDT','TRIBEUSDT','TRXUSDT','UNIUSDT','UNFIUSDT','UMAUSDT','USDCUSDT','WAVESUSDT','WOOUSDT','YFIUSDT','ZECUSDT']
tickerPairs = ['BTCUSDT']
loopcount = 0
theta = [0]*3000
theta_0 = 0
success = 0
total = 0
completelist = []

API_KEY = 
SECRET_KEY = 
BASE_URL = 'https://api.binance.us'

client = Client(API_KEY, SECRET_KEY, tld='us')
headers = {
    'X-MBX-APIKEY': API_KEY
}


class BinanceException(Exception):
    def __init__(self, status_code, data):

        self.status_code = status_code
        if data:
            self.code = data['code']
            self.msg = data['msg']
        else:
            self.code = None
            self.msg = None
        message = f"{status_code} [{self.code}] {self.msg}"

        # Python 2.x
        # super(BinanceException, self).__init__(message)
        super().__init__(message)
        
  
    
def getLast1000Trades(ii):
    resp = requests.get('https://www.binance.com/api/v3/trades?symbol='+ii)
    return resp.json()


def getOrderBook(ii):
    resp = requests.get('https://www.binance.com/api/v3/trades?symbol='+ii)
    return resp.json()



def splitResponseIntoTimeQuantityPrice(response):
    timecheck =  []
    quantity = []
    price = []
    
    for i in response:
        timecheck.append(i['time'])
        #if i['isBuyerMaker'] == True:
        quantity.append(-float(i['qty']))
        #if i['isBuyerMaker'] == False:
          #  quantity.append(float(i['qty']))
        price.append(float(i['price']))    
    return(timecheck,quantity,price)







def mergeSameTimeQuantityEntries(timecheck,quantity):
    quantityfix = [0]
    timefix = []
    timefix.append(timecheck[0])
    count = 0
     
    for i in range(0, len(quantity)):
        if timecheck[i]==timefix[count]:
            quantityfix[count]=float(quantityfix[count])+float(quantity[i])
        else:
            count = count+1
            timefix.append(timecheck[i])
            quantityfix.append(float(quantity[i]))

    return(timefix,quantityfix)







def getLinearRegressionSlope(y,x):
    linearFit = quantfit=np.polyfit(x,y,1)
    d1 = np.poly1d(linearFit)
    return(d1[1])


def timeSinceOldestResponseOrderInSeconds(response):
    #Time in seconds
    stopwatch = time.time()-response[0]['time']/1000
    #Return time in seconds
    return stopwatch

def getCoinPrice(ticker):
    
    
    
    #######GET PRICE    
    PATH = '/api/v3/ticker/price'
    params = {
        'symbol': ticker+'USDT'
    }
    
    url = urljoin(BASE_URL, PATH)
    r2 = requests.get(url, headers=headers, params=params)
        
    return r2.json()['price']


            
def getPriceTotal(ticker):        
    pricelist = getOrderBook(ticker)
    price1 = 0
    weights = 0
    for i in pricelist:
        price1 = price1 + float(i['price'])*(float(i['qty']))
        weights = weights + (float(i['qty']))
    return price1/weights

def getPriceBids(ticker):        
    pricelist = getOrderBook(ticker)
    price1 = 0
    weights = 0
    for i in pricelist:
        if not i['isBuyerMaker']:
            price1 = price1 + float(i['price'])*(float(i['qty']))
            weights = weights + (float(i['qty']))
    return price1/weights

def getPriceAsks(ticker):        
    pricelist = getOrderBook(ticker)
    price1 = 0
    weights = 0
    for i in pricelist:
        if i['isBuyerMaker']:
            price1 = price1 + float(i['price'])*(float(i['qty']))
            weights = weights + (float(i['qty']))
    return price1/weights



def buyCrypto():
    PATH = '/api/v3/order'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': 'BTCUSDT',
        'side': 'BUY',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': quantity,
        'price': price,
        'recvWindow': 5000,
        'timestamp': timestamp
    }
    
    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    
    url = urljoin(BASE_URL, PATH)
    r = requests.post(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        print(json.dumps(data, indent=2))
        return r.json()
        
    # else:
    #     raise BinanceException(status_code=r.status_code, data=r.json())

def sellCrypto():
    PATH = '/api/v3/order'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': 'BTCUSDT',
        'side': 'SELL',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': quantity,
        'price': price,
        'recvWindow': 5000,
        'timestamp': timestamp
    }
    
    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    
    url = urljoin(BASE_URL, PATH)
    r = requests.post(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        print(json.dumps(data, indent=2))
    # else:
    #     raise BinanceException(status_code=r.status_code, data=r.json())  
        
def buyMarketCrypto():
    PATH = '/api/v3/order'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': 'BTCUSDT',
        'side': 'BUY',
        'type': 'MARKET',
       # 'timeInForce': 'GTC',
        'quantity': quantity,
        #'price': price,
        'recvWindow': 5000,
        'timestamp': timestamp
    }
    
    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    
    url = urljoin(BASE_URL, PATH)
    r = requests.post(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        print(json.dumps(data, indent=2))
        return r.json()
        
    else:
        raise BinanceException(status_code=r.status_code, data=r.json())

def sellMarketCrypto():
    PATH = '/api/v3/order'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': 'BTCUSDT',
        'side': 'SELL',
        'type': 'MARKET',
        #'timeInForce': 'GTC',
        'quantity': quantity,
        #'price': price,
        'recvWindow': 5000,
        'timestamp': timestamp
    }
    
    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    
    url = urljoin(BASE_URL, PATH)
    r = requests.post(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        print(json.dumps(data, indent=2))        
    # else:
    #     raise BinanceException(status_code=r.status_code, data=r.json())



def cancel(order):
    PATH = '/api/v3/order'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': 'BTCUSDT',
        'orderId': order,
        'timestamp': timestamp
    }
    
    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    
    url = urljoin(BASE_URL, PATH)
    r = requests.delete(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        print(json.dumps(data, indent=2))
        
def cancelAll():
    PATH = '/api/v3/openOrders'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': 'BTCUSDT',
        
        'timestamp': timestamp
    }
    
    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    
    url = urljoin(BASE_URL, PATH)
    r = requests.delete(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        print(json.dumps(data, indent=2))
                

        
coin = 'BTCUSDT'

window = 10**-13
window = 1
beginAt = 10
###################################################################################
#Get x
timer = time.time()
askprice1 = getPriceAsks(coin)
pricedifferenceaverage = 0
pricedifferencearray = []
roundNumber = 0
testtimes = 0
placeOrder = 0
stucksale = 0
buyordernumber = 0
tossit=0
newQuantityindollars=20
sleeper = time.time()
guess = 0
askprice2=10000000
pricedifferencearray=[0,0]
c=0
accelerationarray = [0,0]
timer = time.time()
while True:   

    askprice1 = getPriceAsks(coin)
    
    askprice2 = getPriceBids(coin)
    
    velocity = askprice2-askprice1
    pricedifferencearray.append(velocity)
    
    acceleration = pricedifferencearray[-1]-pricedifferencearray[-2]
    accelerationarray.append(acceleration)
    
    jerk = accelerationarray[-1]-accelerationarray[-2]
    if velocity>0 and acceleration>0 and jerk>0 and pricedifferencearray[-2]>0:
        print([velocity,acceleration])
        
        a = float(client.get_asset_balance(asset='USDT')['free'])
        
        quantity = round(a/askprice2,6)
        quantity = round(11/askprice2,6)
        #print(quantity)
        
        price=round(askprice2+pricedifferencearray[-2]/10,2)
        buyordernumber = buyCrypto()
       # print(price)
        #time.sleep(1)
        if type(buyordernumber)!=type(None):
            cancel(buyordernumber['orderId'])
            
        quantity = round(float(client.get_asset_balance(asset='BTC')['free']),6)
        print(price)
        #price=round(askprice2+pricedifferencearray[-2]/5,2)
        price=round(price+0.01,2)
        print(price)
        sellCrypto()
        #print(time.time()-timer)
        # if time.time()-timer>3600*8:
        #     timer = time.time()
        if a<10:
            cancelAll()
        print(a)
        
   # askprice2 = getPriceBids(coin)

    
    

