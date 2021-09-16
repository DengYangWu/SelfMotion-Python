#coding=UTF-8
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}

url = 'https://www.zhihu.com/hot'

page_req = requests.get(url,headers=headers)
soup = BeautifulSoup(page_req.text,'html.parser')
