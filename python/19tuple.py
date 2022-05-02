#!/usr/bin/env python
# coding: utf-8

# #### 튜플
# 1. 튜플은 집합이라는 의미에서 리스트와 유사합니다.
# 2. 하지만 값을 바꿀 수 없습니다.(불변 리스트)

# In[3]:


point = (1, 2, 3, 4, 5)
type(point)

point = 1, 2, 3, 4, 5 # 소괄호 생략 가능
type(point)

x = 1
y = 2

x, y = y, x # 변수 = 튜플 (튜플의 언패킹)
print(x, y)


# #### 튜플도 인덱싱과 슬라이싱이 됩니다.

# In[4]:


print(point)

point[0]
point[1]

point[:] # 슬라이싱
point[1:]
point[:3]
point[::2] # 처음~끝. 2번째 마다


# In[ ]:


# 튜플에서 불가능한 문법
# 값을 변경하는 행위는 모두 안된다.                                                                                                                                                       

# point[0] = 100
# point.append(100)
# del point[0]


# #### max, min, len, index, count함수들은 사용이 가능.

# In[5]:


point.index(5) # 5의 위치


# In[6]:


point.count(5) # 5의 개수


# In[7]:


len(point) # 튜플의 길이


# In[8]:


max(point) # 가장 큰 값


# In[9]:


min(point) # 가장 작은 값


# #### 튜플과 리스트는 상호 형변환이 가능합니다.
#     1. list()
#     2. tuple()

# In[11]:


arr = [1,2,3,4,5,6,7,8,9,10]

arr = tuple(arr) # 리스트 => 튜플

arr = list(arr) # 튜플 => 리스트

arr


# In[12]:


tuple(range(0, 10))

