#!/usr/bin/env python
# coding: utf-8

# #### while 조건
# 들여쓰기

# In[5]:


n = 1
sum = 0 # 누적할 변수

while n <= 10 :
    print(n)
    sum += n
    
    n += 1
    
print('1~10까지의 합: ', sum)


# In[7]:


# 50~100까지 합

a = 50
sum = 0

while a <= 100 :
    sum += a
    a += 1

print('50~100까지의 합: ', sum)


# In[8]:


b = 1

while b <= 100 :
    
    if b % 2 == 0 :
        print(b, ' ', end='')
    
    b += 1


# ####  실습1
# 
# * 구구단 n단 출력하기
# 1. 사용자에게 구구단 수를 입력받습니다.
# 2. while문을 사용해서 n단을 단순히 출력
# 
# ex)구구단 수> 4
# 
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# .
# .
# 4 x 9 = 36
# 

# In[11]:


n = int(input('몇단? > '))
i = 1

print('구구단 ', n, '단')
while i <= 9 :
    print(n, ' X ', i, ' = ', n*i)
    i += 1


# #### 실습2
# 
# while연습
# - 정수를 2개 입력받아서 x부터 y값 까지
# 누적합을 구하는 코드를 while문을 사용해서 작성.
# 
# - 우선 처음는 x값이 무조건 작은 값이 들어올 것이다
# 이렇게 가정하고 코드를 작성하면 됩니다.

# In[13]:


x = int(input('첫번째 정수>'))
y = int(input('두번째 정수>'))

if x > y :
    x, y = y, x

sum = 0

while x <= y :
    sum += x
    x += 1

print(sum)

