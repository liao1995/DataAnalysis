from bs4 import BeautifulSoup
import urllib.request
from time import sleep
from datetime import datetime
def getGoldPrice():
	url = "http://gold.org"
	req = urllib.request.urlopen(url)
	page = req.read()
	scraping = BeautifulSoup(page)
	price = scraping.findAll("dd", attrs={"class":"value"})[0].text
	return price

with open("goldPrice.out", "w") as f:
	for x in range(0, 60):
		sNow = datetime.now().strftime("%I:%M:%S%p")
		str = "{0}, {1} \n".format(sNow, getGoldPrice())
		print(str)
#		f.write("{0}, {1} \n".format(sNow, getGoldPrice()))
		f.write(str)
		sleep(59)
