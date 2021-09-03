from requests_html import HTMLSession
import re
url = "https://www.ebay.com.au/itm/124757521636?_trkparms=ispr%3D1&hash=item1d0c20b4e4:g:OTkAAOSwGr1gubwu&amdata=enc%3AAQAGAAACkPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsSxXDXcCydCuSj2Tq2S%252F3GnsQrM%252B4ZLpPF6nChut9aX07LmGudrFlFVOTkAv%252FixMkcGAnnYwX2FNe2NND7qDVc8kpT%252FLJSDS%252BIkzUgSvfhPQbKwC8frnNAjbDMqedzHscqvYad%252BVOHEIpMPe%252F6ZPcLUDx6svonqqaQFylJw4iWnhhAxtVC5s%252FerstAgZPmHDnQcWGUYdIuPPG0bI7Y4I%252FV0Ps2mWIq2OxduaZ7zdbtVdthZ7B9HHPLoPwkRb1a8ptDuY4qZSsEbM0ED4kywhYkJ8bXc4l8K3xf5NBMktzoFxaHHFr2LPlIW%252Bw%252FLs20p4AaJxtji%252BkUs7NCIKqGuip1fjnRolNh0YfOednPYZ6QosBMksEXfLrm%252B%252BSfDeOPXpisAUDlqMqS3EsD3qNYCO2yzsNoo09WHuHlL0ncOw3dkTHzpHyy22pNIG1JTtQQ%252Bro9Q4v4ykz9szuTJ%252BaisKprQek3hnVd6CNhZe%252B4LuESka3l7FUYPWLW2qUs%252FgJo%252F2GUhBisy%252F2w%252F02yiXKuDPS5mQzoFp14UJCHEVWs0hQHPHvmiMWUyfHP%252BRdaIV73jBgvfHWdwpLG9cXsfb6vX5fTUYO%252FJlXwV1cDW6YnhBUhHd%252B81TAyq1UGuF0dYCMw9EzJWqHqRSINBjUwWiMeQudZStBZIJ0WFKO01hSWzQn%252B2XoPgSCBC1cf0ZgCct5cNFYYShZ2pe7VKeNnsTZOdtxxSvRVJvaJa9gavWw3N5qNnj5JOlJoXldzJk5KhfreEsi7h%252FzidKFFkV8JcXW%252BktIcPVNzxDk7l4JP4CxA3l6EMm76DqOVE%252Brf39hxCod3ua22%7Campid%3APL_CLK%7Cclp%3A2334524"
s = HTMLSession()
r = s.get(url)
#seller_name =  r.html.xpath('//*[@id="RightSummaryPanel"]',first = True).text
name =  r.html.find('span.mbg-nw')[0].text
review_rate = r.html.select('span.mbg-l')[0].getText()[1:5]
ratings_details = r.html.find('div#si-fb')[0].text
rate = r.html.xpath('//*[@id="RightSummaryPanel"]',first =True).text
count = re.sub(r'()','',review_rate)

print(name)
print(review_rate)
#print(int(review_rate))
#print(ratings_details)
#print(rate)
