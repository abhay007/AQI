# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:43:08 2019

@author: abhay
"""
import os
import time
import requests
import sys


def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month<10):
                url='https://en.tutiempo.net/climate/01-2001/ws-421810.html'.format(month
                                                                          ,year)
            else:
                url='https://en.tutiempo.net/climate/01-2001/ws-421810.html'.format(month
                                                                          ,year)
            texts=requests.get(url)
            text_utf=texts.text.encode('utf=8')
            
            if not os.path.exists("Data/delhi_Html_Data/{}".format(year)):
                os.makedirs("Data/delhi_Html_Data/{}".format(year))
            with open("Data/delhi_Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush()
        
if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))