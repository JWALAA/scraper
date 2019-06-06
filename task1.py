from selenium import webdriver
from selenium.webdriver.support.ui import Select
import json

url="http://psleci.nic.in/"

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome Beta\\Application\\chrome.exe"
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(url)

State1=Select(driver.find_element_by_id("ddlState"))
print(len(State1.options))
state = State1.options

for i in State1.options:
    print(i.text)

l3={}

for i in range(1,len(State1.options)):
    district=[]
    l2={}
    State1=Select(driver.find_element_by_id("ddlState"))
    State1.options[i].click()
    District1=Select(driver.find_element_by_id("ddlDistrict"))
    for a in District1.options:
        district.append(a.text)
    district=district[1:]
    for j in range(1,len(District1.options)):
        l1={}
        District1=Select(driver.find_element_by_id("ddlDistrict"))
        District1.options[j].click()
        ac1=Select(driver.find_element_by_id("ddlAC"))
        ac=[]
        for a in z.options:
            ac.append(a.text)
        ac=ac[1:]
        for k in range(1,len(ac1.options)):
            ac1=Select(driver.find_element_by_id("ddlAC"))
            ac1.options[k].click()
            l=Select(driver.find_element_by_id("ddlPS"))
            pollst=[]
            for a in l.options:
                pollst.append(a.text)
            pollst=pollst[1:]
            try:
                l1[ac[k]]=pollst
            except:
                print("AC Error")
        try:
            l2[district[j]]=l1
        except:
            print("District Error")
    try:
        l3[state[i].text]=l2
    except:
        print("State Error")    

with open("poll.json", "a") as write_file:
    json.dump(l3, write_file, indent=4)
