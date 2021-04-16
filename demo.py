import sys
import requests
import time
from bs4 import BeautifulSoup

URL="https://search.books.com.tw/search/query/key/{0}/cat/all"

def generate_search_url(url,keyword):
    url=url.format(keyword)
    return url

def get_resource(url):
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0;Win64;x64) ApplWebKit/537.36 (KHTML, like Gecko) Chrom/63.0.3239.132 Safari/537.36"}
    return requests.get(url,headers=headers)

def parse_html(html_str):
    if r.status_code == requests.codes.ok:
       r.encoding="utf8"
       soup=BeautifulSoup(r.text,"lxml")
    else:
        print("HTTP request error!!"+url)
        soup=None
    return soup


def web_scraping_bot(url):
    booklist=[]
    print("retrive data form Internet...")
    soup=parse_html(get_resource(url))
    if soup != None:
       tag_item=soup.find_all(class_="box_1") #找尋
       for item in tag_item:
           book=[]
           book.append(item.find("img")["alt"]) #書名
           [isbn,price]=get_ISBN_price(item.find("a")["href"])
           book.append(isbn)
           book.append(price)

           print(book)
           print("wait 2 sec")
           time.sleep(2)

def get_ISBN_price(url):
    url1="https:"+url
    soup=parse_html(get_resource(url1))
    isbnStr=""
    if soup!=None:
       bd=soup.find(class_="bd")
       lilist=bd.find(class_="lilist")
       print("lilist \n",lilist)
       price=0
       priceU1=soup.find("ul",{"class":"price"})
       for liData in lilist:
           print("liData\n\n",liData.text)
           if "ISBN" in liData.text


if __name__=="__main__":
    if len(sys.argv)>1:
       url=generate_search_url(URL,sys.argv[1])
       r=get_resource(url)
       booklist=web_scraping_bot(url)
       #for item in booklist:
           #print(item)



       #print(get_resource(urls).text)

