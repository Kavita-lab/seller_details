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
category = ''
rat = 0
def get_page(url):
    req = requests.get(url)
    if not req.ok:
        print("Server responded: ", req.status_code)
    else:
        soup = BeautifulSoup(req.content,'html.parser')
    return soup


def get_detail_data(soup,seller):
    seller_name = seller
    #try:
    #    seller_name  = soup.find("div",{"class":"mbg vi-VR-margBtm3"}).text.strip().split(' ')[0]
    #    print("Seller name :", seller_name)
    #except:    
    #    seller_name = ''
    try:
        sel_rat = soup.find("span",{"class":"mbg-l"}).find('a').text.strip()
        print("Seller rating count :",sel_rat)
        
    except:
        sel_rat = ''
    try:
        pos_rating  = soup.find("div",{"id":"si-fb"}).text.strip()
        pos_rating = re.sub('\xa0',' ',pos_rating)
        print("Feedback :",pos_rating)
    except:
        pos_rating = ''
    try:
       link =soup.find('div',{'class':'bdg-90'}).find('a').get('href')
       print("Seller Page Link :",link)
       ss = get_page(link)
       neutral = ss.find('div',{'class':'fl scores col-3'}).text.strip().split()[0]
       #print(neutral)
       p_nu_ne = re.findall(r'\d+',neutral)
       positive = p_nu_ne[0]
       

       try:
          full_data = ss.find('div',{'class':'dsr fl col-3'}).text
          #print(full_data)
          review_feedback = re.findall(r'\d+',full_data)
         
       except:
           full_data = ''
       
       
       
       
       
       
    except:
        link = ''
        
    
    data = {
        'sellerName' :seller_name,
        'rating': sel_rat,
        'feedback':pos_rating ,
        'link':link,
        'positive':0,
        'neutral':0,
        'negative':0,
        'communication': 'NA',
        'postageCharge':'NA' ,
        'feedbackratingdesc':'NA',
        'postageTime':'NA'
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
    review = 0
    s = HTMLSession()
    r = s.get(url)
    try:
        sellerName =r.html.xpath('//*[@id="sellerProfileTriggerId"]',first = True).text

    except:
        sellerName = ''
    try:
        review = r.html.xpath('//*[@id="acrPopover"]',first = True).text
        rating = r.html.xpath('//*[@id="productDetails_detailBullets_sections1"]',first=True).text
        #print(rating)
    except:
        rating = ''
    #get_url()
    #seller = seller_info
    #print(seller)
    print(review)    
    data = {
        'sellerName':sellerName,
        'rating':'NA',
        'feedback':review,
        'negative':0,
        'feedbackratingdesc':'NA',
        'postageCharge':'NA',
        'link':'NA',
        'positive':0,
        'communication':'NA',
        'nuetral':0,
        'postageTime':'NA'
        



        }
    post_data(data)


def get_catch_data(soup):
     
    global category
    global rat
    try:
        seller_name = soup.find('div',{'class':'seller-info__description'}).find('a').text
        print(seller_name)
    except:
        seller_name = ''
        
    try:
        link=soup.find('div',{'class':'seller-info__description'}).find('a').get('href')
        print(link)
        soup2 = get_page(link)
        try:
            category  = soup2.find('div',{'class':'seller-ribbon-badge__level'}).text
            print(category)
        except:
            category = ''
        try:
            rat  = soup2.find('div',{'class':'seller-ribbon-badge__ranking'}).text
            print(rating)
        except:
            rat = ''

            
    except:
        link = ''
    data = {
        'rating':'NA',
        'negative':0,
        'feedbackratingdesc': category,
        'nuetral':0,
        'feedback ':rat,
        'sellerName' :seller_name,
        'link':link,
        'positive':0,
        'communication':'NA',
        #'neutral':'NA',
        'postageTime':0,
        'postageCharge':'NA'
        }
    print(data)
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
         #}
       
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
        seller_nam = Seller_info_data['sellerName']
        print(Seller_info_data['link'])
        links = Seller_info_data['link']
        
        
    else:
        print("Data not available")
        sleep(4)
    return links ,seller_nam
def main():
    
    
    while True:
        links, name = get_url()

        print(name)
        print(links)
        links = links
        #links = get_url()
        if 'ebay' in links:
           url= links
           soup = get_page(url)
           if soup:
               dataa = get_detail_data(soup,name)
           else:
               print("None")
        elif 'amazon' in links:
             url = links
             dataa = get_amazon_data(url)
        elif 'catch' in links:
             dataa  = get_catch_data(links)
        
        
    
  
    
    
if __name__ == '__main__':
    url="https://tcesffb3s8.execute-api.ap-south-1.amazonaws.com/dev/seller"
    main()
    
