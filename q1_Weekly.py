# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:06:15 2019

@author: Kaushik
"""

from selenium import webdriver
import time
import q1_splist as c
import threading

def getData(self):
    for company in piece:
	    option = webdriver.ChromeOptions()
	    option.add_argument("--incognito")
	    option.add_experimental_option("prefs",{"download.default_directory":r"D:\Msit\DADV\visualization_exam\weekly_data"})
	    
	    browser = webdriver.Chrome(r"D:\Msit\DADV\visualization_exam\chromedriver.exe",chrome_options=option)
	    browser.get("https://finance.yahoo.com/quote/"+company+"/history?period1=1431887400&period2=1558117800&interval=1d&filter=history&frequency=1wk")
	    browser.maximize_window()
	    browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a').click()
	    time.sleep(10)
	    browser.quit()  
        
slices = [c.tickers[x: x+50] for x in range(0, len(c.tickers), 50)]
print (slices)
for piece in slices:
    threading.Thread(target=getData, args=[piece]).start()