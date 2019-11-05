'''
Disclaimer: This script is for educational purposes only
Simple webscraper on modelpress website
'''

import requests
import urllib.request
import os
import sys
from bs4 import BeautifulSoup


def get_container(url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.find_all('figure', class_='img left')
    else:
        sys.exit("[~] Invalid Response Received.")


def main():
    os.chdir("")  # Location of directory
    # Modelpress URL here example:'https://mdpr.jp/interview/detail/1882790'
    html = get_container("")
    img_url = []
    for a in html:
        if a.img:
            img_url.append(a.img['src'][:99])
    for img in img_url:
        file_name = img.split('/')[-1]
        print("Downloading file:%s" % file_name)
        r = requests.get(img, stream=True)
        with open(file_name, 'wb') as f:
            for chunk in r:
                f.write(chunk)


if __name__ == "__main__":
    main()
