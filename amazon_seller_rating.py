from requests_html  import HTMLSession

url="https://www.amazon.com.au/Samsung-Galaxy-G780F-Unlocked-Android/dp/B08MBFDP9T/ref=sr_1_1?crid=12SLL422ZXXWS&dchild=1&keywords=samsung+galaxy+s20&qid=1625823797&sprefix=sumsung+galaxy%2Caps%2C516&sr=8-1"
url2 ="https://www.amazon.com.au/Samsung-Galaxy-G780F-Unlocked-Android/dp/B08MBFDP9T/ref=sr_1_1?crid=12SLL422ZXXWS&dchild=1&keywords=samsung+galaxy+s20&qid=1625823797&sprefix=sumsung+galaxy%2Caps%2C516&sr=8-1"
def get_data(url):
    s = HTMLSession()
    r = s.get(url)
    rating = {
        'Seller_Name':r.html.xpath('//*[@id="sellerProfileTriggerId"]',first = True).text,
        'Ranking':r.html.xpath('//*[@id="productDetails_detailBullets_sections1"]',first=True).text
        



        }
    print(rating)

get_data(url2)    
    
