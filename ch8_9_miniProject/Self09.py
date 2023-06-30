import time
import bs4
import urllib.request
import ssl
import pymysql
from tkinter import *
from tkinter import messagebox

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
imgLinkUrl,title,link,price,gift= "","","","",""

null = None
## 함수 선언 부분
def insertData(title,price,gift,link,imgLinkUrl) :
    con, cur = None, None
    data = ""
    data0,data1, data2, data3, data5, data6 = "", "", "",  "", "",""
    sql=""

    con = pymysql.connect(host='127.0.0.1', user='root', password='mysql1234', database='aladin', charset='utf8')
    cur = con.cursor()

    data1 = title;  
    data2 = price; 
    data3 = gift; 
    # data4 = eprice;
    data5 = link;
    data6 = imgLinkUrl;
       
    try :
        
        print(null)
        print(data1)
        print(data2)
        print(data3)
        # print(data4)
        print(data5)
        print(data6)
        sql = "INSERT INTO bookstore (title,price,gift,link,imgLinkUrl)  VALUES('"+ data1 + "','" + data2 + "','" + data3 + "','"+ data5 +"','"+data6+ "')"
        print("sql 실행전 ")
        cur.execute(sql)
        
    except :
        print("예외 발생")
        
        # messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else :
        print("성공")
        # messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()
##

page = 2
aladinlUrl = "https://www.aladin.co.kr/shop/wbrowse.aspx?CID=50917&page="
while True :
    bookUrl = aladinlUrl + str(page)
    page += 1
    htmlObject = urllib.request.urlopen(aladinlUrl,context=ssl_context)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
    
    tag_list = bsObject.findAll('div', {'class': 'browse-right'})

    print('###### 알라딘 정보 #######')
    
    for tag in tag_list :

        title = tag.find('a', {'class': 'bo3'}).text
        price = tag.find('span', {'class': 'ss_p2'}).text
        # gift = tag.find('a', {'class': 'ss_ht1'}).text
        
        if gift != None :
            gift = tag.find('span', {'class': 'ss_ht1'}).text
        else :
            gift = '존재x'


        # if eprice != None :
        #     eprice = tag.find('div', {'class': 'ss_book_list'}).text
        # else :
        #     eprice = '존재x'


        link = tag.find('a', {'class': 'bo3'})['href']
        imgLink = tag.find('div',{'class':'flipcover_in'})
        
        if imgLink != None:
            imgLinkUrl = imgLink.find('img')['src']
        else :
            imgLinkUrl = '이미지가 존재 하지 않음'
        
    
        print("데이터 추가 전")
        insertData(title,price,gift,link,imgLinkUrl)
        print(title,price,gift,link,imgLinkUrl)
  
        

    time.sleep(600)