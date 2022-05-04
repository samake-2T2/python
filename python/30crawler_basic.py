#!/usr/bin/env python
# coding: utf-8

# #### 뷰리풀숩
# 1. find() - 단일 선택자로 태그를 취득
# 2. find_all() - 모든태그를 리스트 형태로 취득
# 3. select() - 선택자를 이용해서 태그를 취득

# In[2]:


from selenium import webdriver
import time
from bs4 import BeautifulSoup


# In[3]:


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.aladin.co.kr')

time.sleep(1)

# 베스트셀러 탭 클릭
driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()

# selenium으로 전체 페이지 소스코드를 문자열로 가져오기
src = driver.page_source

# src 문자열 데이터를 html형태로 파싱
soup = BeautifulSoup(src, 'html')

# div를 가져오는데, class속성이 ss_book_box인것만 선택하여 리스트로 가져옴
div_list = soup.find_all('div', {'class': 'ss_book_box'})

# print(div_list)
# print('-' * 50)
# print(div_list[0]) # 리스트중 첫번째

first_book = div_list[0].find_all('li') # 첫번째 중 제목 - 작성자 부분

#for i in first_book :
#   print(i) # li
#  print(i.text) # li태그안에 텍스트만 표시

print( first_book[0].text)
print( first_book[1].text)
print( first_book[2].text)
print( first_book[3].text)
print( first_book[4].text)

