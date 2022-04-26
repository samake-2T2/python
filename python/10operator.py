#!/usr/bin/env python
# coding: utf-8

# #### 연산자
# 1. +, -, /(실수몫), //(정수몫), %(나머지)

# In[2]:


print(10 / 4) # 실수 몫
print(10 // 4) # 정수 몫
print(10 % 4) # 나머지
print(4 % 7) # 나머지

print(2 ** 3) # 제곱 2의 3승
print(3 ** 5) # 제곱 3의 5승


# #### 복합대입연산자 +=, -=, /=, //=,.....

# In[7]:


a = 5
b = 3

# a = a + 3
a += 3

# a = a // 2
a //= 2

# a = a % 3
a %= 3

# a = a ** 2
a **= 2

a


# In[8]:


a = 1
# a++ # 전치, 후치 연산 없음
a += 1
a


# #### 논리연산자
# - & | and or not

# In[10]:


print(True & True)
print(True and True)
print(True | False)
print(True or False)
print(not True) # 부정 - !부호는 없음


# In[15]:


a = 5

b = 10

if a > 1 and a < 10 :
    print('a는 1보다 크고 10보다 작습니다.')

if b == 2 or b == 10 :
    print('b는 2 또는 10 입니다.')

if a > 1 & a < 10 :
    print('a는 1보다 크고 10보다 작습니다.')

if b == 2 | b == 10 :
    print('b는 2 또는 10 입니다.')

# not은 부정의 의미 T -> F, F -> T
if not b < 10 :
    print('b는 10 미만입니다.')


# In[19]:


# 단축평가 연산
# 논리 연산에서 좌할에서 전체결과가 나오는 경우, 우측의 항에 대한 연산을 진행하지 않는다.

c = 0
# print(c / 0) # 0으로 나눌 수 없기 때문에 에러가 발생

# 첫번째 행의 연산만 실행함(단축연산)
if c == 0 or c / 0 == 0 :
    print('통과함?')

# 결과에 상관없이모든 항의 연산을 진행하기 때문에 에러 발생    
#if c == 0 | c / 0 == 0 :
#    print('통과함?')

