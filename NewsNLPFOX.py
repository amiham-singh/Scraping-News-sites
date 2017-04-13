from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd
import re
import xlwt

def dateAF(u): 
  try:
      d=re.findall(r'.*(\d{4})/(\d{2})/(\d{2})/',u)[0] # find regex n link u, findall returns touple, the matches and the gorups, hence [0] to return only the match
      dt=datetime.date(int(d[0]),int(d[1]),int(d[2]))
      return (dt > datetime.date(2017,1,19)) and (dt < datetime.date(2017,2,21))
  except:
         return False
         
def dateBF(u): 
  try:
      d=re.findall(r'.*(\d{4})/(\d{2})/(\d{2})/',u)[0] # find regex n link u, findall returns touple, the matches and the gorups, hence [0] to return only the match
      dt=datetime.date(int(d[0]),int(d[1]),int(d[2]))
      return (dt > datetime.date(2016,12,19)) and (dt < datetime.date(2017,1,20))
  except:
         return False

def Pol(u):
    if  "/politics/" in u:
        return True
    else:
        return False
p = re.compile('.*trump.*')         
url = "http://www.foxnews.com/sitemap.xml?idx=32"

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data, "xml")
finalistAf1=[]
finalistAf1= [x.text for x in soup.findAll("loc") if dateAF(x.text) if Pol(x.text) if p.match(x.text) ]

#%%
book = xlwt.Workbook(encoding="utf-8")
sheet = book.add_sheet("Sheet 1", cell_overwrite_ok=True)  
row = 0

for x in finalistAf:
    d=re.findall(r'\d{4}/\d{2}/\d{2}',x)
    sheet.write(row,0,x)
    sheet.write(row,1,d)
    row = row + 1
    
book.save("FoxAf.xls")
