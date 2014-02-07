NSEFinance-Python
=================

Python Library for NSEFinance


<pre><code>
from nsefinance import NSEFinance
stocks = NSEFinance()



result = stocks.get_daily_list()
for i in range(len(result)):
	print result[i]['close'] 




result = stocks.get_by_symbol("OANDO")
for i in range(len(result)):
	print result[i]['close']




symbol = "OANDO"
result = stocks.get_by_symbol(symbol,"2014-02-06")
print result[symbol]['close']

</code></pre>


Full documentation of for the api is available at http://nsefinance.com/docs