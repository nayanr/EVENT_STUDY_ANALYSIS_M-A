from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from datetime import date
import pandas as pd
import datetime
import time

data = pd.read_excel('result.xlsx')
df1 =  pd.DataFrame(data)
count = 1 
for index, row in df1.iterrows():
  urla = 'https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.aspx?scripcode='
  urlb = row['Scrip Code']
  urlb = str(urlb)
  urlc = '&flag=sp&Submit=G'
  url = urla+urlb+urlc
  print(url)
  print(count)
  if(count>0):
    
    
    page  = requests.get(url)
    driver = webdriver.Chrome()
    driver.get(url)

    fdate = row['DATE ON YEAR ago']
    fdate = fdate.strftime('%d/%m/%Y')
    fdate = fdate.strip()
    tdate = row['DATE one month AGO']
    tdate = tdate.strftime('%d/%m/%Y')
    tdate = tdate.strip()

    
    print(tdate)

    print(fdate)

    
    driver.execute_script("document.getElementById('ctl00_ContentPlaceHolder1_txtFromDate').value = ''")
    

    driver.execute_script("""var fdate = arguments[0];document.getElementById('ctl00_ContentPlaceHolder1_txtFromDate').value += fdate""",fdate)


        
    driver.execute_script("document.getElementById('ctl00_ContentPlaceHolder1_txtToDate').value = ''")
    

    driver.execute_script("""var tdate = arguments[0];document.getElementById('ctl00_ContentPlaceHolder1_txtToDate').value += tdate""",tdate)
    
    
    driver.find_element_by_name("ctl00$ContentPlaceHolder1$btnSubmit").click()
    driver.find_element_by_name("ctl00$ContentPlaceHolder1$btnDownload").click()
    time.sleep(5)
    driver.quit()  

  count = count + 1

    
    


