#!/usr/bin/env python
# coding: utf-8

# #### 셀레니움 - 웹 자동화를 위한 모듈
# - 브라우저를 키거나, 이동하거나, 클릭하는(이벤트)를 실행할 수 있음

# In[1]:


get_ipython().system('pip install selenium')


# In[3]:


from selenium import webdriver
import time


# In[13]:


# 다운로드 받은 크롬 물리드라이버 가동명령(경로)
driver = webdriver.Chrome('chromedriver.exe')

time.sleep(3)
# 웹페이지 이동명령
driver.get('http://www.naver.com')
time.sleep(1)

# xpath란 화면에서 고유하게 표기하는 id입니다.
login_btn = driver.find_element_by_xpath('//*[@id="account"]/a')
login_btn.click()
time.sleep(1)

# 자동으로 텍스트 입력하기
id_input = driver.find_element_by_xpath('//*[@id="id"]')
id_input.send_keys('jithub')
time.sleep(1)

pw_input = driver.find_element_by_xpath('//*[@id="pw"]')
pw_input.send_keys('ddiddu8741!')
time.sleep(1)

# 로그인 버튼 클릭
login_btn2 = driver.find_element_by_xpath('//*[@id="log.login"]')
login_btn2.click()

# 뒤로가기
driver.back()



# #### 실습
# 1. 네이버에 접속해서 검색창에 '오늘 날씨'를 입력하세요.
# 2. 검색 후 첫번째로 나오는 네이버 뉴스기사를 띄워주세요.

# In[14]:


# 다운로드 받은 크롬 물리드라이버 가동명령(경로)
driver = webdriver.Chrome('chromedriver.exe')

time.sleep(3)
# 웹페이지 이동명령
driver.get('http://www.naver.com')
time.sleep(1)

search_input = driver.find_element_by_xpath('//*[@id="query"]')
search_input.send_keys('오늘 날씨')
time.sleep(1)

search_btn = driver.find_element_by_xpath('//*[@id="search_btn"]')
search_btn.click()
time.sleep(1)

news = driver.find_element_by_xpath('//*[@id="sp_nws_all1"]/div[1]/div/a')
news.click()

