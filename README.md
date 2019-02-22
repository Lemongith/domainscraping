# Domainscrapy Project

Scrapy Project for Domain Website (https://domain.com.au). Based on Python. Will scrapy the sold units within a particular Postcode with particular result page (20 by default). All search result (inc. Soldprice, Address, Beds, Baths, Carpark, Space, URL) will be saved into db file. 

## Getting Started

This code run on Python with some particular MODs. And use SQLite to save result. 
Note: Also includes a Dockerfile which can be composed to a Docker image based on Python:3 with necessary MODs.

1. Specify the Postcode and Page range you want to scrapy
2. It will extract data from HTML Requests (searching for Apartment or House&Townhouse has two different functions)
3. Then will verify if record is duplicated, new record will be inserted into a separate Table [e.g.p2020] in db file (test.db by default) via SQLite3. 
4. After crawling all pages, it will sleep 24hrs [by default] then start again.

### Prerequisites

1.Install python (Or Install Docker and compose the Dockerfile)
2.Install SQLite3

### Installing

Copy all files into same path

Line 100 - change the Unit type you want scrapy[get_content_apt] or [get_content_house]

Line 86/87 - define the postcode and page range

Line 112 - define the scrapy frequency between pages

Line 123 - define the scrapy code run daily or ....(default is 86400 seconds=24hrs)

## Deployment

1.Open SQLite3 and create a .db file.(or use the docker image CLI:docker build -t python-image .)

2.Run code.py to start scrapy. (or CLI:docker run -it --rm --name my-scrapy -v /home/[your code.py path]:/usr/src/myapp -w /usr/src/myapp python-image python code.py)

## Authors

**Hugh Tan**(https://github.com/Lemongith) lemontan.hugh@gmail.com

## Acknowledgments

Thanks for the Udemy Python Course [the-modern-python3-bootcamp]
