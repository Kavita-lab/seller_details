from requests import get, post
import requests
from bs4 import  BeautifulSoup
import pandas as pd
import re
import json
import pika
from time import sleep
import os
from requests_html  import HTMLSession
url="https://tcesffb3s8.execute-api.ap-south-1.amazonaws.com/dev/seller"
def get_page(url):
    req = requests.get(url)
    if not req.ok:
        print("Server responded: ", req.status_code)
    else:
        soup = BeautifulSoup(req.content,'html.parser')
    return soup

def get_detail_data(soup):
    response = None
    uploaded = False
    upload = ''
    try:
        seller_name  = soup.find("div",{"class":"mbg vi-VR-margBtm3"}).text.strip().split(' ')[0]
        
      
    except:
        seller_name = ''
    try:
        sel_rat = soup.find("span",{"class":"mbg-l"}).find('a').text.strip()
       
      
    except:
        sel_rat = ''
    try:
        pos_rating  = soup.find("div",{"id":"si-fb"}).text.strip()
        pos_rating = re.sub('\xa0',' ',pos_rating)
       
    except:
        pos_rating = ''
    try:
       link =soup.find('div',{'class':'bdg-90'}).find('a').get('href')
       
       ss = get_page(link)
       neutral = ss.find('div',{'class':'fl scores col-3'}).text.strip().split()[0]
       #print(neutral)
       p_nu_ne = re.findall(r'\d+',neutral)
       
      

       try:
          full_data = ss.find('div',{'class':'dsr fl col-3'}).text
          #print(full_data)
          review_feedback = re.findall(r'\d+',full_data)
         
       except:
           full_data = ''
       
       
       rat1 = ss.find('div',{'class':'fl each'}).find('span',{'class':'dsr_count bold fl'}).text
       rat2 = ss.find('span',{'class':'dsr_type'}).text
      
       
       
       
    except:
        link = ''
    
        
    data = {
        'rating':pos_rating ,
        'negative':p_nu_ne[2],
        'feedbackratingdesc': sel_rat,
        'nuetral':p_nu_ne[1],
        'feedback ':review_feedback[0],
        'sellerName' :seller_name,
        'link':link,
        'positive':p_nu_ne[0],
        'communication':review_feedback[1],
        'neutral':p_nu_ne[1],
        'postageTime':review_feedback[2],
        #'postageCharge':review_feedback[3]
        
        }
    print(data)
    post_data(data)
    #response = post(url, json=data)
    #upload = data
    #uploaded = True
    #print(f'\n\nuploaded data:-\n{upload}\n\n')
    #sleep(5)
    #return response ,data
    #return data

    
def get_amazon_data(url):
    s = HTMLSession()
    r = s.get(url)
    data = {
        'sellerName':r.html.xpath('//*[@id="sellerProfileTriggerId"]',first = True).text,
        'rating':r.html.xpath('//*[@id="productDetails_detailBullets_sections1"]',first=True).text,
        'feedback':'',
        'negative':'',
        'feedbackratingdesc':'',
        'postageCharge':'',
        'link':'',
        'positive':'',
        'communication':'',
        'nuetral':'',
        'postageTime':''
        



        }
    post_data(data)

def post_data(data):
    response = None
    uploaded = False
    upload = ''
    #sub = {
        # "feedback":"something good",
        # "negative":3,
        # "feedbackratingdesc":"happening good",
        # "postageCharge":"555",
        # "rating":10,
        # "sellerName":"Amazon US",
        # "link":"http://amazon.com.au/somethinggood",
        # "positive":5,
        # "communication":"happy to interact with amazon",
        # "nuetral":2,
        # "postageTime":"555"
        # }
       
    response = post(url, json=data)
    upload = data
    uploaded = True
    print(f'\n\nuploaded data:-\n{upload}\n\n')
    sleep(5)
    return response        
   
def get_url():
    data_dict = get(url).json()
    if data_dict['responseCode'] ==200:
        print("Successfull")
        print(data_dict['responseMessage'])
        Seller_info_data = data_dict['sellerInfoPojo']
        print(Seller_info_data['sellerId'])
        print(Seller_info_data['sellerName'])
        print(Seller_info_data['link'])
        links = Seller_info_data['link']
        
        
    else:
        print("Data not available")
        sleep(4)
    return links
def main():
    #url2 ="https://www.amazon.com.au/Samsung-Galaxy-SM-G991U-128GB-Version/dp/B08N2FRMPN/ref=sr_1_1?crid=1A1ULATNHA635&dchild=1&keywords=samsung+s21&qid=1626165937&sprefix=samsung%2Caps%2C560&sr=8-1"
    #dataa = get_amazon_data(url2)
    links = get_url()
    if 'ebay' in links:
        url= links
        dataa = get_detail_data(get_page(url))
    
    elif 'amazon' in links:
        url = links
        
        dataa = get_amazon_data(url)
        
    
  
    
    
if __name__ == '__main__':
    main()
    
