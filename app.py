import requests
from bs4 import BeautifulSoup
import json
from sqlalchemy import false


# parse all URLs
def get_url (url = false):


    if not url:
        return false    
    headers = {
        'authority': 'www.amazon.com',
        'cache-control': 'max-age=0',
        'rtt': '300',
        'downlink': '1.35',
        'ect': '3g',
        'sec-ch-ua': '"Google Chrome"; v="83"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'aws-priv=eyJ2IjoxLCJldSI6MCwic3QiOjB9; session-id=139-7350741-1081713; ubid-main=135-9894765-6184621; lc-main=en_US; s_fid=0A4730DDD06B62E4-1DB478AB62143F35; regStatus=pre-register; x-main=hd2N9IEBuVL7il1dbkhEEHTQSf4Q7uviwjc2eikr0hRGGOyI2RYIiRsk3GvDKLSx; at-main=Atza|IwEBIJdoAZ4Y6j2IIGvC29t1ha634aK-p2kAl8rHhQRCSGMSU_nwQvM6fakAbYEjpVLPU4Jj0TwKvX70d6QnlouKPh0QwpHJG8rHUNVb-gmhS9shHM8fCJk45r1XW2FOSpLoM1iAO9kYIpOoW2M5We9xfdqlLuQBB-D5fQeO5Vqew4RnHesPNZuF4DQNlcqL7wrGjDY1JQKzlzARfATAuwaCy4jMD5bNmxpcWtTgNGrTtLpGv1Y-4Mnx2axxQYFgwpRNv_sPNZrMAfHdU7MX67HbyPyV3V21KAl8QNl0xE-lNl3myxnfyWH68Z5D-j501S7HWzkKxopy3SfGuwwZTjSVSVlnH4RmTwvEnW8W3tndcX6X1ETysYYXmO7TudIjtq7aUZqPBJe_MViePcWL3OV4q2b5; sess-at-main="TjcvTeXAA2dP6HOMGcG/n+Cdkr+peDBlNMOvfBz6oE0="; sst-main=Sst1|PQGR5AF9x4yS-iMft3B9aBzJC8v-e4M1kmB_3KS0pxtVTj1cH8hl3fajgigt6xEYhan-kUJuY5KNbteBgbiyDIRCs4ISve5MdRhDdoy7XKrVD1g5McZTyvdwYLfbTJbTUov51hOyPcE8BKpFL1bGpJiiJbZ0TV7Pyc6tkndogjneZATDErc4U08WE4LwPJxCiF-I-7Av4-JEfwH1ZQ81mz6rqy-K1o6bCMRRZ8kWuzrl0wobKsr4Sz0-m1K0waguIewhXNm4V4DLe8mn-_6I8_k9p9v3NiFRpp04v0Ptzw8V1ARo2U18t5f2nx54EXwHzvzOQlpeBVY2U0WpXDcKsU3C8Q; session-id-time=2082787201l; i18n-prefs=USD; x-wl-uid=1MwJyD7dRnGiVdHw1PKiwmoNP9S/0xy+3KAKCJl2fM5VOthLzEW3dzyeW4zdKAepcIxkXpJFkxWcafUXXcS0MeSyLyFoBkl3xnNPLiRK0Rq33AHw0gL3W1FDBUn9OcakOzJGVGKZRc5E=; s_vn=1614974634531%26vn%3D4; s_nr=1590823888871-Repeat; s_vnum=2022823888872%26vn%3D1; s_dslv=1590823888874; sp-cdn="L5Z9:FR"; session-token=3AIPjoIrP8ITt1e/KXLZGSlnOPpirrWotNpCpCEfNRCY9mCfAV169URMcAX8XECtxt/qJujUn66Oyz8KIFDMieNmSdzEKA0K8I4AqbzplslzVGtZ6rNg+XsX/Bdc3hxnB7tUqQhrbrtVUncdzUMN1c95vhL7p+AEog3iiDkhLch0VO+Sl8HkAdZ/63xrp0stAaUsYo1GgsOFGI8+3wJUp4CHrJnoj/0lqjCJCpgXTZfxJcfWy9KarcGAPkno+fuMQqMoShJdi8R+DZ9XmIMib1bsLwXnerZa; csm-hit=tb:GVY0F2K4G05TXW59KB9M+s-GVY0F2K4G05TXW59KB9M|1592424615451&t:1592424615452&adb:adblk_yes',
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200: 
        # Using BeautifulSouphtml.parser
        return BeautifulSoup(resp.text, 'lxml')
    else:
        return false

# get all ads details
def get_children (url = false):
    if not url:
        return false
    print(url)
    body = get_url(url)
    if body:    
        children = body.find("body").find("div", attrs={'id': 'root'})
        if not children:
            return false
        image = []
        images_box = children.find('div', attrs={'data-cy': "adPhotos-swiperSlide"}) 
        if not images_box:
            image = []
        else: 
            for link in images_box.findAll("img"):
                image.append(link.get('src'))

        price = children.find("div", attrs={"data-testid":"ad-price-container"})
        
        # add ads values
        tempJson = { "title":children.find("h1", attrs={"data-cy":"ad_title"}).getText().strip(),
        "description":children.find("div", attrs={"data-cy":"ad_description"}).getText().strip(), 
        "image":image,
        "price": "" if not price else price.text }
        return tempJson
    else:
        return false


# Get home page ads lists
URL = "https://www.olx.pl/" #"http://localhost/pytest/index.html"

soup = get_url(URL)
if soup: 
    # finding parent <ul> tag
    parent = soup.find(id="mainpageAds").find("ul", id="gallerywide")
    
    # finding all <li> tags 
    descendant = parent.find_all("li", class_="fleft") 

    #variable to store all ads details
    returnJson = []

    # getting ads content in <li> tag
    for child in parent.find_all("li", class_="fleft") :
        link = child.find("a").get('href')
        children = get_children(link)
        if children:
            returnJson.append(children)

    json_data = json.dumps(returnJson)
    with open('output.json', 'w') as f:
        print(json_data, file=f)  # Python 3.x
    print(json_data)
