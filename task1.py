from selenium import webdriver
import bs4
import pandas as pd
import requests

#res = requests.get('http://psleci.nic.in')
State = []#to store state/UT
District =[]
AC = []

driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
driver.get("http://psleci.nic.in")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('div',href=True, attrs={'class':'style1'}):
    State=a.find('div', attrs={'style1':'ddlState'})
    District=a.find('div', attrs={'style1':'ddlDistrict'})
    AC=a.find('div', attrs={'style1':'ddlAC'})
State.append(name.text)
District.append(districts.text)
AC.append(AC.text)

df = pd.DataFrame({'State': name,'District':prices,'AC':AC}) 
df.to_csv('C:\\Users\\behl\\Desktop\\vote.csv', index=False, encoding='utf-8')