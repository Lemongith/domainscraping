import random
import time
import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime
from pytz import timezone

def get_content_apt(
        postcode,
        page=1,
        url='https://www.domain.com.au/sold-listings/?ptype=apartment&excludepricewithheld=1&ssubs=1'):
    url = url + '&postcode=' + str(postcode) + '&page=' + str(page)
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    return soup


def get_content_house(
        postcode,
        page=1,
        url='https://www.domain.com.au/sold-listings/?ptype=duplex,free-standing,new-home-designs,new-house-land,semi-detached,terrace,town-house,villa&excludepricewithheld=1&ssubs=1'):
    url = url + '&postcode=' + str(postcode) + '&page=' + str(page)
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    return soup

# def connect_db(file,table_name):
# 	conn=sqlite3.connect(file)
# 	c=conn.cursor()
# 	query_create='CREATE TABLE '+table_name+' (price TEXT ,address_line_1 TEXT ,address_line_2 TEXT ,sold_date TEXT ,beds TEXT ,baths TEXT ,carpark TEXT ,space TEXT ,link TEXT);'
# 	c.execute(query_create)


# extract link, address, price, Sold_date, beds, baths, carpark, type,
# postcode, space
def extract_data(content):
    list = content.find_all(class_="search-results__listing")
    current_page_result = []
    for d in list:
        if d.find(class_="listing-result__price"):  # too kickout advertise
            if d.find(class_="listing-result__price"):
                price = d.find(class_="listing-result__price").get_text()
            if d.find(class_="address-line1"):
                address_line_1 = d.find(class_="address-line1").get_text()
            if d.find(class_="address-line2"):
                address_line_2 = d.find(class_="address-line2").get_text()
            if d.find(class_="listing-result__tag is-sold"):
                sold_date = d.find(
                    class_="listing-result__tag is-sold").get_text()
            # to get beds, baths, carpark, space
            bbcs = d.find_all(
                class_="property-feature__feature-text-container")
            beds=baths=carpark=space='null'
            if bbcs:
            	for item in bbcs:
            		if 'Bed' in item.get_text():
            			beds=item.get_text()
            		elif 'Bath' in item.get_text():
            			baths=item.get_text()
            		elif 'Parking' in item.get_text():
            			carpark=item.get_text()
            		elif 'm²' in item.get_text():
            			space=item.get_text()


            else:
                pass
            link = d.find("a")["href"]
            
            current_page_result.append([price,
                                        address_line_1,
                                        address_line_2,
                                        sold_date,
                                        beds,
                                        baths,
                                        carpark,
                                        space,
                                        link])
        else:
            pass
    return current_page_result


def main():
	while 1:
	    conn = sqlite3.connect('test.db')
	    c = conn.cursor()
	    #query_create='CREATE TABLE data (price TEXT, address_line_1 TEXT, address_line_2 TEXT, Sold_date TEXT, beds TEXT, baths TEXT, carpark TEXT, space TEXT, link TEXT);'
	    # c.execute(query_create)
	    postcode_range = [2000, 2007, 2008, 2009, 2010, 2011, 2015, 2016, 2017, 2018, 2019, 
	    2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049] # scrapy postcode range
	    page_range = 20  # scrapy page range for a postcode
	    #query_insert = 'INSERT INTO data VALUES (?,?,?,?,?,?,?,?,?);'
	    #query_verify = 'SELECT * FROM data WHERE link=?;'
	    for p in postcode_range:
	    	query_insert = 'INSERT INTO p' + str(p) +' VALUES (?,?,?,?,?,?,?,?,?);'
	    	query_create = 'CREATE TABLE p' + str(p) + ' (price TEXT, address_line_1 TEXT, address_line_2 TEXT, Sold_date TEXT, beds TEXT, baths TEXT, carpark TEXT, space TEXT, link TEXT);'
	    	try:
	    		c.execute(query_create)
	    	except:
	    		pass
	    	else:
	    		pass
	    	for page in range(1, page_range+1):
	        	page_result = extract_data(get_content_apt(p, page))
	        	for result in page_result:
	        		link = result[8]
	        		#verify duplicate#
	        		query_verify = 'SELECT * FROM p'+ str(p) +' WHERE link=?;'
	        		c.execute(query_verify, (link,))
	        		verify_result = c.fetchone()
	        		if verify_result:
	        			print('Record Exists'+ ' PostCode- '+str(p) +' Page-'+ str(page))
	        		else:
	        			c.execute(query_insert, result)
	        			print('working on PostCode-' + str(p) +' Page-'+ str(page))
	        	time.sleep(random.randint(10, 20))
	    	try:
	        	c.execute('CREATE TABLE LOG VALUES (PostCode TEXT, Page TEXT, TIME TEXT);')
	    	except:
	        	pass
	    	else:
	        	pass
	    	current_time=datetime.datetime.now(timezone('Australia/Sydney')).strftime('%Y-%m-%d %H:%M:%S')
	    	c.execute('INSERT INTO LOG VALUES (?,?,?);',(p,page,current_time))
	    conn.commit()
	    conn.close()
	    time.sleep(86400)

if __name__ == '__main__':
    main()

