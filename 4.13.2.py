import requests
from bs4 import BeautifulSoup
r=requests.get('http://finance.yahoo.com/q/cp?s=%5EDJI+Component')
'''
print(r.encoding)
print(r.apparent_encoding)
print(r.text)'''
re=requests.get('https://query1.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=eYi30si2JPB&lang=en-US&region=US&symbols=DD%2CAAPL%2CCSCO%2CCVX%2CVZ%2CJPM%2CJNJ%2CMRK%2CPFE%2CUNH%2CMSFT%2CIBM%2CV%2CUTX%2CTRV%2CGE%2CKO%2CNKE%2CGS%2CMMM%2CDIS%2CMCD%2CINTC%2CCAT%2CPG%2CXOM%2CAXP%2CHD%2CBA%2CWMT&fields=messageBoardId%2ClongName%2CshortName%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2Cuuid&corsDomain=finance.yahoo.com')
#print(re.encoding)
#print(re.apparent_encoding)
#print(re.text)

resp = re.json()
print(resp)

for stock in resp['quoteResponse']['result']:
    print(stock['symbol'], stock['longName'], stock['regularMarketPrice']['fmt'])
#http://deerchao.net/tutorials/regex/regex.htm正则表达式教学
