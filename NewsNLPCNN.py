from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd
import re

def dateAF(u): #Function to check if the link is with in timeframe
  try:
      d=re.findall(r'.*(\d{4})/(\d{2})/(\d{2})/',u)[0] # find regex in link u, findall returns tuple, the matches and the gorups, hence [0] to return only the match
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

def cnnPol(u):#Check to see if it is CNN.com and if the link is from the politics section
    if "http://www.cnn.com/" in u and "/politics/" in u:
        return True
    else:
        return False
p = re.compile('.*trump.*')# Regex to match the word "trump" in the link         

url = "http://www.cnn.com/sitemaps/sitemap-articles-2017-01.xml" # Link to CNN's SiteMap

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data, "xml")
finalistBf=[]
finalistBf = [x.text for x in soup.findAll("loc") if dateBF(x.text) if cnnPol(x.text) if p.match(x.text) ]

  

#%%

#Writing it all into a file
df = pd.DataFrame(finalistBf)
df.to_excel('output.xlsx', header=False, index=False)     