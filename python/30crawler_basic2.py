#!/usr/bin/env python
# coding: utf-8

# In[5]:


from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv
import datetime as d


# #### 50개의 책 데이터의 제목, 저자, 출판사, 출판일, 가격을 출력

# In[6]:


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.aladin.co.kr')

time.sleep(1)

# 순위를 누적할 변수
rank = 1

# 베스트셀러 탭 클릭
driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()

# selenium으로 전체 페이지 소스코드를 문자열로 가져오기
src = driver.page_source

# src 문자열 데이터를 html형태로 파싱
soup = BeautifulSoup(src, 'html')

# div를 가져오는데, class속성이 ss_book_box인것만 선택하여 리스트로 가져옴
div_list = soup.find_all('div', {'class': 'ss_book_box'})

for div in div_list :
    
    book_info = div.find_all("li") # book_box의 li부분만 다시 추출
    
    '''
    print(rank)
    print(book_info[0].text)
    print(book_info[1].text)
    print(book_info[2].text)
    print(book_info[3].text)
    print('-'*50)
    '''
    
    if book_info[0].text[0] != '[' :
        title = book_info[0].text # 제목
        author = book_info[1].text # 저자
        price = book_info[2].text # 가격
        
    else :
        title = book_info[1].text
        author = book_info[2].text
        price = book_info[3].text
        
    auth_info = author.split('| ') # |를 구분자로 문자를 잘라서 리스트로 반환
    pri_info = price.split(',  ')
    
    print(f'순위: {rank}')
    print(f'제목: {title}')
    print(f'저자: {auth_info[0]}')
    print(f'출판사: {auth_info[1]}')
    print(f'출판일: {auth_info[2]}')
    print(f'가격: {pri_info[0]}')
    print(f'마일리지: {pri_info[1]}')
    print('-'*50)
    
    rank += 1 # 랭크 누적
    
    


# #### 순위 탭 별로 데이터를 처리하기

# In[6]:


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.aladin.co.kr')

time.sleep(1)

# 순위를 누적할 변수
rank = 1

# 베스트 셀러탭 클릭
driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()


# 순위 탭을 실행하기 위한 반복
for x in range(3, 13) :

    # selenium으로 전체 페이지 소스코드를 가져오기
    src = driver.page_source

    # src문자열 데이터를 html형태로 파싱
    soup = BeautifulSoup(src, 'html')

    # div를 가져오는데, class속성이 ss_book_box
    # 리스트로 반환
    div_list = soup.find_all('div', {'class': 'ss_book_box'})

    for div in div_list : 

        book_info = div.find_all("li") #book_box의 li부분만 다시 추출

        '''
        print(rank)
        print(book_info[0].text )
        print(book_info[1].text )
        print(book_info[2].text )
        print(book_info[3].text )
        print("-" * 50)
        '''

        if book_info[0].text[0] != '[' :
            title = book_info[0].text # 제목
            author = book_info[1].text # 저자
            price = book_info[2].text # 가격
        else :
            title = book_info[1].text # 제목
            author = book_info[2].text # 저자
            price = book_info[3].text # 가격

        auth_info = author.split("|") # |를 구분자로 문자를 잘라서 리스트로 반환

        print(f'순위: {rank}')
        print(f'제목: {title}')
        print(f'저자: {auth_info[0]}')
        print(f'출판사: {auth_info[1]}')
        print(f'출판일: {auth_info[2]}')
        print(f'가격: {price.split(", ")[0] }')

        rank+=1 # 랭크 누적

        
    # 바깥 반복문의 범위    
    # 순위탭의 xpath 규칙성
    # //*[@id="newbg_body"]/div[3]/ul/li[3]/a
    # //*[@id="newbg_body"]/div[3]/ul/li[4]/a
    # //*[@id="newbg_body"]/div[3]/ul/li[5]/a
    # ...
    # //*[@id="newbg_body"]/div[3]/ul/li[11]/a

    # 11까지 클릭이 되어야 하고 12일떄 까지 반복해서 코드가 실행되어야 하기 때문에
    # range(3, 13)
    # 전체 페이지 소스를 구해오는 부분부터 반복
    try :
        driver.find_element_by_xpath(f'//*[@id="newbg_body"]/div[3]/ul/li[{x}]/a').click()
        time.sleep(1)
    except :
        print("-" * 100)
        break
    
    
    


# #### 수집한 데이터를 날짜별로 csv파일로 처리하기
# 1. csv파일 임포트, datetime임포트
# 2. withopen()으로 처리
# 3. csv.writer() 코드 추가

# In[10]:


now = d.datetime.today()
file_path = f'dataset/알라딘_베스트셀러_{now.year}_{now.month}_{now.day}.csv'

with open(file_path, mode='w', encoding='utf-8-sig', newline='') as f :

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.aladin.co.kr')

    time.sleep(1)

    # 순위를 누적할 변수
    rank = 1

    # 베스트 셀러탭 클릭
    driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()


    # 순위 탭을 실행하기 위한 반복
    for x in range(3, 13) :

        # selenium으로 전체 페이지 소스코드를 가져오기
        src = driver.page_source

        # src문자열 데이터를 html형태로 파싱
        soup = BeautifulSoup(src, 'html')

        # div를 가져오는데, class속성이 ss_book_box
        # 리스트로 반환
        div_list = soup.find_all('div', {'class': 'ss_book_box'})

        for div in div_list : 

            book_info = div.find_all("li") #book_box의 li부분만 다시 추출

            '''
            print(rank)
            print(book_info[0].text )
            print(book_info[1].text )
            print(book_info[2].text )
            print(book_info[3].text )
            print("-" * 50)
            '''

            if book_info[0].text[0] != '[' :
                title = book_info[0].text # 제목
                author = book_info[1].text # 저자
                price = book_info[2].text # 가격
            else :
                title = book_info[1].text # 제목
                author = book_info[2].text # 저자
                price = book_info[3].text # 가격

            auth_info = author.split("|") # |를 구분자로 문자를 잘라서 리스트로 반환
            
            '''
            print(f'순위: {rank}')
            print(f'제목: {title}')
            print(f'저자: {auth_info[0]}')
            print(f'출판사: {auth_info[1]}')
            print(f'출판일: {auth_info[2]}')
            print(f'가격: {price.split(", ")[0] }')
            '''
            
            
            data_write = csv.writer(f, delimiter=',')
            data_write.writerow([
                rank,
                title,
                auth_info[0],
                auth_info[1],
                auth_info[2],
                price.split(", ")[0]
            ])

            rank+=1 # 랭크 누적


        # 바깥 반복문의 범위    
        # 순위탭의 xpath 규칙성
        # //*[@id="newbg_body"]/div[3]/ul/li[3]/a
        # //*[@id="newbg_body"]/div[3]/ul/li[4]/a
        # //*[@id="newbg_body"]/div[3]/ul/li[5]/a
        # ...
        # //*[@id="newbg_body"]/div[3]/ul/li[11]/a

        # 11까지 클릭이 되어야 하고 12일떄 까지 반복해서 코드가 실행되어야 하기 때문에
        # range(3, 13)
        # 전체 페이지 소스를 구해오는 부분부터 반복
        try :
            driver.find_element_by_xpath(f'//*[@id="newbg_body"]/div[3]/ul/li[{x}]/a').click()
            time.sleep(1)
        except :
            print("-" * 100)
            break


