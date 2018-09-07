import requests

from bs4 import BeautifulSoup


#url ="www.astrospeak.com/horoscope/gemini"
#r  = requests.get("https://" +url)
#data = r.text
#soup =BeautifulSoup(data, "html.parser")



#rows =soup.find('div',{"id" : "sunsignPredictionDiv"})

#print bars.text

def  speak_gemini(url):
   r  = requests.get("https://" +url)
   data = r.text
   soup =BeautifulSoup(data, "html.parser")

   rows =soup.find('div',{"id" : "sunsignPredictionDiv"})

   bars = rows.find('div', attrs={'class': 'lineHght18'})
   return bars.text.strip().split("\n")[0]


