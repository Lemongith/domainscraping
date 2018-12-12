# Domainscrapy Project

Scrapy Project for Domain Website (https://domain.com.au). Based on Python. Will scrapy the sold units within a particular Postcode with particular result page (20 by default). All search result (inc. Soldprice, Address, Beds, Baths, Carpark, Space, URL) will be saved into SQL file. 

## Getting Started

This code run on Python with some particular MODs. And use SQLite to save result. 
Note: Also includes a Dockerfile which can be composed to a Docker image based on Python:3 with necessary MODs.

1. Specify the Postcode and Page range you want to scrapy
2. It will extract data from HTML Requests (search for Apartment or House&Townhouse has two different functions)
3. Then will verify if record duplicate, new record will be inserted into a separate Table [e.g.p2020] in SQL file (test.db by default) via SQLite3. 
4. After crawling all pages, it will sleep 24hrs [by default] then start again.

### Prerequisites

1.Install python (Or Install Docker and compose the Dockerfile)
2.Install SQLite3

### Installing

Copy all files into same path

## Deployment

1.Open SQLite3 and create a .db file.
2.Run code.py to start scrapy.

## Authors

**Hugh Tan**(https://github.com/Lemongith)

## Acknowledgments

Thanks for the Udemy Python Course [the-modern-python3-bootcamp]
