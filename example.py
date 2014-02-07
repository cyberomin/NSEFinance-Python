from nsefinance import NSEFinance

stocks = NSEFinance()



"""
Available keys :
[u'high', u'symbol', u'value', u'deals', u'date', u'low', u'units', u'close', u'open', u'change']

"""
#Get closing prices for all the symbols for the trading day.
result = stocks.get_daily_list()
for i in range(len(result)):
	print result[i]['close'] 



#Get the closing price for the last 5 trading day for a symbol
result = stocks.get_by_symbol("OANDO")
for i in range(len(result)):
	print result[i]['close']




#Get the closing price for a particular symbol on a particular day
symbol = "OANDO"
result = stocks.get_by_symbol(symbol,"2014-02-06")
print result[symbol]['close']