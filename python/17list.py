#!/usr/bin/env python
# coding: utf-8

# #### list
# 1. 리스트는 나열된 자료를 저장하는 자료형입니다.
# 2. 다른언어의 배열과 유사한 개념입니다.

# In[8]:


list1 = [1,2,3,4,5,6,7,8,9,10,'가']
list1

list2 = list(range(1,50))
list2

list3 = list(range(1,10, 2))
list3


# #### 리스트 인덱싱, 슬라이싱

# In[13]:


list_ = list(range(1,10))
print(list_)

list_[0]
list_[-1]

list_[len(list_)-1] #list_[8]
list_[2]


# In[15]:


list_[:]
list_[0:5]
list_[::2] # 0~끝번째 2번째 마다 슬라이싱
list_[5:]


# In[17]:


# 리스트의 값 변경
list_[0] = 10
list_[1] = 20
list_


# #### 리스트의 연산 +,-

# In[19]:


list1 = [1,2,3,4,5]
list2 = [6, 7, 8]

list1 + list2
list1 * 3


# #### 리스트 값을 변수에 한번에 저장하기

# In[ ]:



# 좌항의 변수와 우항의 리스트요소가 같으면 한번에 저장할 수 있다.
a, b, c, d, e = list1

print(a, b, ,c, d, e)


# #### 다차원 리스트

# In[22]:


list_ = [[1,2,3], [4,5,6], [10, 20, 30, 40, 50]]
   
list_[0]
list_[1]
list_[2]


list_[0][0]
list_[0][2]
list_[0][:2]
list_[2][::2]

list2 = ['소고기', '짜장면', '탕수육', '짬뽕']
list2[0][0]
list2[0][2]
list2[0][:2]

