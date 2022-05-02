#!/usr/bin/env python
# coding: utf-8

# #### 문자열 다루기
# 1. 문자열을 다루는 다양한 방법으로 indexing, slicing 방법을 제공합니다.
# 2. 다양한 내장함수(기능)도 존재합니다.

# In[3]:


s = 'python'
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])

# print( s[6]) # 초과한 인덱스 값을 사용하면 에러


# In[4]:


#음수 -1은 문자의 마지막 번째를 의미함
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])


# #### 문자열이나, 순차적 구조를 가진 list는 for문에 사용이 가능합니다.

# In[8]:


for i in s : # python
    print(i, end='')
    
print()
    
for i in '월화수목금토일' :
    print(i, end='')


# #### 문자열 슬라이싱

# In[9]:


s = 'python'

s[0:6] # 0~6민만
s[0:5]
s[1:5]

s[:] # 생략시에는 자동으로 시작~끝 값을 나타냄
s[:4] # 0~4미만
s[0:] # 0~끝까지


# In[10]:


# 시작: 끝미만: step
s[2:5:1]

s[::2] # python
s[::3] 


# #### 실습
# 
# 주민번호를 051105-3124567형식으로 입력받습니다.  
# 최종 출력구문은: 2005년 11월 05일 16세 남자  
# 
# 힌트
# 생년월일 부분을 슬라이싱으로 추출해서 변수로 저장  
# 연도같은 경우는 int() 함수를 이용해서 정수로 변환해야 연도 나이를 구할수 있습니다.  
# 7번째자리가 "3" or "4"라면 2000년대 생  

# In[16]:


str = input('주민번호를 입력하세요> ')

year = str[0:2]
month = str[2:4]
day = str[4:6]
gender = str[7]

if gender == '3' or gender == '4' :
    year = '20' + year
    
    if gender == '3' :
        gender = '남자'
    else :
        gender = '여자'
else :
    year = '19' + year
    
    if gender == '1' :
        gender = '남자'
    else :
        gender = '여자'

    
age = (2022 - int(year))+1

print(f'{year}년 {month}월 {day}일 {age}세 {gender}')

