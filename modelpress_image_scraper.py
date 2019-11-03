'''
Disclaimer: This script is for educational purposes only
Simple webscraper on modelpress website
Only works when the images are stored in square component
'''

import requests
import urllib.request
import os
import sys
from bs4 import BeautifulSoup

def get_container(url):
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.find_all('figure', class_ = 'square')
    else:
        sys.exit("[~] Invalid Response Received.")

def main():
    os.chdir("") # Location of directory
    html = get_container("") # Modelpress URL here example:'https://mdpr.jp/interview/detail/1882790'
    img_url = []
    for a in html:
        if a.img:
            img_url.append(a.img['src'][:99])
    for img in img_url:
        file_name = img.split('/')[-1]
        print("Downloading file:%s"%file_name)
        r = requests.get(img, stream=True)
        with open(file_name, 'wb') as f:
            for chunk in r:
                f.write(chunk)
    
if __name__ == "__main__":
    main()