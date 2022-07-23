import requests
from lxml import etree
from bs4 import BeautifulSoup
import json


# Reading temperature of New York
URL = "http://localhost/pytest/index.html"

#"https://www.olx.pl/"
resp = requests.get(URL)

if resp.status_code == 200: 
    # Using BeautifulSouphtml.parser
    soup = BeautifulSoup(resp.text, 'lxml')

    #encode to UTF8
    # soup = soup.encode("utf-8")

    # finding parent <ul> tag
    parent = soup.find(id="mainpageAds").find("ul", id="gallerywide")
    
    # finding all <li> tags 
    descendant = parent.find_all("li", class_="fleft") 

    returnJson = []
    # printing the content in <li> tag

    for children in parent.find_all("li", class_="fleft") :
        image = ""
        if children.find('img'):
            image = children.find('img')['src']  
        
        location = ""
        relativedate = ""
        if children.find("ul").findAll("li"):
            dateLocation = children.find("ul").findAll("li")
            location = dateLocation[0].getText()
            relativedate = dateLocation[1].getText()

        tempJson = {"image":image, "link":children.find("a").get('href'), "title":children.find("strong").getText().strip(), "location":location, "relativedate":relativedate, "price":children.find("div", {"class":"price"}).getText().strip()}
        returnJson.append(tempJson)

json_data = json.dumps(returnJson)
print(json_data)
