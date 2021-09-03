print("kavitas")
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup


url = "https://www.catch.com.au/product/devanti-smart-led-tv-43-inch-43-4k-uhd-hdr-lcd-slim-thin-screen-netflix-youtube-5692588/?sid=Devanti%20Smart%20LED%20TV%2055%22%20Inch%204K%20UHD%20HDR%20LCD%20Slim%20Thin%20Screen%20Netflix&sp=1&st=32&srtrev=sj-85i0872zd8adj1cu3hkb1q.click"
req = requests.get(url)
soup = BeautifulSoup(req.content , 'html.parser')
#print(soup)
link=soup.find('div',{'class':'seller-info__description'}).find('a').get('href')
print(link)
seller_name = soup.find('div',{'class':'seller-info__description'}).find('a').text
print(seller_name)

requests=requests.get(link)
soup2  =BeautifulSoup(requests.content,'html.parser')
print(soup2)
category  = soup2.find('div',{'class':'seller-ribbon-badge__level'}).text
print(category)
rating  = soup2.find('div',{'class':'seller-ribbon-badge__ranking'}).text
print(rating)
