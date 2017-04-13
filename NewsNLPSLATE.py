from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd
import re
import xlwt

def dateAF(u): 
  try:
      d=re.findall(r'(\d{4})-(\d{2})-(\d{2})',u)[0] # find regex n link u, findall returns touple, the matches and the gorups, hence [0] to return only the match
      dt=datetime.date(int(d[0]),int(d[1]),int(d[2]))
      return (dt > datetime.date(2017,1,19)) and (dt < datetime.date(2017,2,21))
  except:
         return False
         
def dateBF(u): 
  try:
      d=re.findall(r'(\d{4})-(\d{2})-(\d{2})',u)[0] # find regex n link u, findall returns touple, the matches and the gorups, hence [0] to return only the match
      dt=datetime.date(int(d[0]),int(d[1]),int(d[2]))
      return (dt > datetime.date(2016,12,19)) and (dt < datetime.date(2017,1,20))
  except:
         return False

def trump(u):
    p = re.compile('.*trump.*')
    if p.match(u):
        return True
    else:
        return False
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")  
cl= 0
row = 0       
url = "http://www.slate.com/articles/news_and_politics/politics.sitemap.1.xml"

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data, "xml")

#finalistBf2 = [x.text for x in soup.findAll("loc") if dateBF(x.text) if cnnPol(x.text) if p.match(x.text) ]
for url in soup.findAll('url'):
    
    loctag = url.contents[0]
    timetag = url.contents[1]
    
    if trump(loctag.contents[0]):
#        
       if dateAF(timetag.contents[0]):
           sheet1.write(row,0,str(loctag.contents[0]))
           sheet1.write(row,1,str(timetag.contents[0]))
           row = row + 1
#            
book.save("slateAf.xls")
#%%
