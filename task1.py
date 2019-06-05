from selenium import webdriver
import bs4

State = []
District =[]
A_C = []

driver = webdriver.Chrome('C:\\Users\\behl\\AppData\\Local\\Programs\\Python\\Python36-32\Scripts\\chromedriver.exe')

driver.get("http://psleci.nic.in")

content = driver.page_source

soup = bs4.BeautifulSoup(content, 'html5lib')


for a in soup.findAll('div',attrs={'class':'style1'}):
    State1=a.find('select', attrs={'id':'ddlState'})
    District1=a.find('select', attrs={'id':'ddlDistrict'})
    A_C1=a.find('select', attrs={'id':'ddlAC'})
State.append(State1)
District.append(District1)
A_C.append(A_C1)

df = pd.DataFrame({'State': State,'District':District,'A_C':A_C})
df.to_csv('C:\\Users\\behl\\Desktop\\vote.csv', index=False, encoding='utf-8')
