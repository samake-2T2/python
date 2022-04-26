#!/usr/bin/env python
# coding: utf-8

# # 데이터 타입
# ## 정수형

# In[3]:


# 정수형 타입

num = 123
type(num)

# 2진수, 8진수, 16진수 형태로 표현
# 0b, 0o, 0x를 붙여서 표현 가능

a = 0b1011
a

b = 0o77
b

c = 0xAC00
c

bin(a) # 2진수 형태로 출력
oct(b) # 8진수 형태로 출력
hex(c) # 16진수 형태로 출력


# ## 실수형

# In[8]:


# float - 10진수 형태로 나타내거나, 지수표현법으로 표현가능

a = 3.14
type(a)

b = 3.141592e5
b

c = 3.141592e-3
c


# ## 논리형

# In[12]:


# true키워드는 파이썬에서는 True대문자로 작성해야한다.
b1 = True
b1

b2 = False
b2

type(b1)
type(b2)


# In[14]:


# >, <, <=, >=, ==. !=

a = 5

print(a < 10)
print(a > 5)
print(a == 5)
print(a != 5)
print("안녕" == "안녕")


# In[19]:


# 사전등재 순서대로 크기가 지정됨
print("apple" >  "grape")
print("감자" >  "고구마")
print("banana" < "버네이너")
print("Banana" < "banana")

