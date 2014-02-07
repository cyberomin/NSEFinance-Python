NSEFinance-Python
=================

Python Library for NSEFinance



```python
from nsefinance import NSEFinance
stocks = NSEFinance()

> Available keys :
> [u'high', u'symbol', u'value', u'deals', u'date', u'low', u'units', u'close', u'open', u'change']

result = stocks.get_daily_list()
for i in range(len(result)):
	print result[i]['close'] 


result = stocks.get_by_symbol("OANDO")
for i in range(len(result)):
	print result[i]['close']


symbol = "OANDO"
result = stocks.get_by_symbol(symbol,"2014-02-06")
print result[symbol]['close']
```




Full documentation of for the api is available at [http://nsefinance.com/docs](http://nsefinance.com/docs)