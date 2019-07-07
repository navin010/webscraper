import bs4
from bs4 import BeautifulSoup
import requests
import csv

#https://www.youtube.com/watch?v=rONhdonaWUo


def showPrice():
    r = requests.get('https://finance.yahoo.com/quote/FB?p=FB&guccounter=1')
    soup = bs4.BeautifulSoup(r.text, "xml")
    stock_value = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return stock_value

#while True:
    #print("The current price of Facebook stock is: " + showPrice())




with open('mycsv.csv','w', newline='') as file:
    csv_file = csv.writer(file)
    csv_file.writerow(['iteration','stock_price'])

    for i in range(1, 10):
        csv_file.writerow([i,showPrice()])