import json
import urllib2

class NSEfinance(object):

	url = "http://127.0.0.1/api/stocks"

	def __init__(self):
		pass

	#Main Data Handler
	def _data(self,symbol=None,date=None):
		if not symbol:
			data = urllib2.urlopen(self.url).read()

		elif symbol and not date:
			url = self.url +"/"+ str(symbol)
			data = urllib2.urlopen(url).read()

		elif symbol and date:
			url = self.url +"/"+ str(symbol) +"/"+ str(date)
			data = urllib2.urlopen(url).read()
		return data

	#Get daily result 
	def get_daily_list(self):
		data = self._data()
		finalResult = json.loads(data)
		return finalResult


	#Get by symbol and Date
	def get_by_symbol(self,symbol=None,date=None):
		if not symbol:
			raise ValueError("Symbol not supplied")

		elif not date:
			data = self._data(symbol)
			finalResult = json.loads(data)
			return finalResult

		elif symbol and date:
			data = self._data(symbol,date)
			finalResult = json.loads(data)
			return finalResult


if __name__ == "__main__":
	stocks = NSEfinance()
	print stocks.get_by_symbol()