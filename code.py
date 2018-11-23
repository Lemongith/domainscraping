import random
import time
import requests
from bs4 import BeautifulSoup
import re

def get_content_apt(postcode, page=1,url='https://www.domain.com.au/sold-listings/?ptype=apartment&excludepricewithheld=1&ssubs=1'):
	url=url+'&postcode='+str(postcode)+'&page='+str(page)
	content=requests.get(url)
	soup=BeautifulSoup(content.text, 'html.parser')
	return soup

def get_content_house(postcode, page=1,url='https://www.domain.com.au/sold-listings/?ptype=duplex,free-standing,new-home-designs,new-house-land,semi-detached,terrace,town-house,villa&excludepricewithheld=1&ssubs=1'):
	url=url+'&postcode='+str(postcode)+'&page='+str(page)
	content=requests.get(url)
	soup=BeautifulSoup(content.text, 'html.parser')
	return soup

def extract_data(content): # extract link, address, price, Sold_date, beds, baths, carpark, type, postcode, space
	list=content.find_all(class_="search-results__listing")
	for d in list:
		if d.find(class_="listing-result__price"):
			price=d.find(class_="listing-result__price").get_text()
			address_line_1=d.find(class_="address-line1").get_text()
			address_line_2=d.find(class_="address-line2").get_text()
			sold_date=d.find(class_="listing-result__tag is-sold").get_text()
			bbcs=d.find_all(class_="property-feature__feature-text-container")
			beds=bbcs[0].get_text()
			baths=bbcs[1].get_text()
			carpark=bbcs[2].get_text()
			if len(bbcs)==4:
				space=bbcs[3].get_text()
			else:
				space=[]
			# url=d.find(class_="listing-result__carousel-lazy")["href"]
			link=d.find("a")["href"]
			
			print(price,address_line_1,address_line_2,sold_date,beds,baths,carpark,space)
		else:
			pass
content=get_content_apt(2121,2)
extract_data(content)

