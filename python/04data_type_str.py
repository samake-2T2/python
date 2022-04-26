#!/usr/bin/env python
# coding: utf-8

# # 문자열 타입 string

# - 문자열을 표기할때는 "", ''로 표기합니다.

# In[6]:


s1 = "안녕"
s2 = '안녕'

s2

# 문자열 안에서 홀따옴표를 사용하고 싶다면 앞에 \을 붙여준다.
s3 = 'Let\'s go!!!!';
print(s3)


# In[12]:


s4 = '안녕~ \n낼봥~'
print(s4)

# 탈출문자 경로를 표현할때는 \\을 붙여서 표현해줍니다.
path = "C:\\temp\\user";
path = "C:/temp/user";
print(path)

