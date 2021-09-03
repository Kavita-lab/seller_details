from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
url = "https://www.dicksmith.com.au/da/buy/samsung-galaxy-s20-fe-dual-sim-8gb-ram-128gb-cloud-navy-international-model-08806090761683/"
req = requests.get(url)
soup = BeautifulSoup(req.content,'html.parser')
if soup:
    print("ok")
seller_Name = soup.find('div',{'class':'_1-itK _24yQk'}).find('a').text
print(seller_Name)

