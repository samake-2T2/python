#!/usr/bin/env python
# coding: utf-8

# #### 리스트 함수 insert, append

# In[6]:


list_ =[1,2,3,4,5]

list_.append(6) # 마지막에 추가
list_.append(7)
 
list_


# In[8]:


list_.insert(3, 10)
list_


# #### 리스트의 값 삭제, remove, 내장함수 del, clear

# In[13]:


list1 = [34, 23, 65, 23, 73, 347]
list1

list1.remove(65) # 값을 이용해서 지움
list1


# In[15]:


del list1[0] # del 지우고싶은 인덱스
list1


# In[17]:


list1.clear() # 리스트를 비움
list1


# #### 실습

# In[17]:


# 사용자에게 값을 입력받아 입력받은 값이 있다면 삭제
# 반복문으로 회전
kakao = ['무지', '네오', '어피치', '라이언', '제이지']

kinput = input('값을 입력하세요> ')
    
for i in range(0, len(kakao)) :
    
    if kakao[i] == kinput :
        del kakao[i]
            
        break
    
print(kakao)


# #### 리스트의 탐색과 정렬
# - index, count, sort, reverse
# - 공용함수 max, min, len

# In[26]:


point = [65, 54, 86, 45, 100, 76, 99, 98, 65]


# In[24]:


max(point) # 리스트의 가장 높은값
min(point) # 리스트의 가장 낮은값
len(point) # 리스트의 길이


# In[27]:


x = point.index(100)
print('100이 존재하는 인덱스:', x)

y = point.count(65)
print('65의 개수:', y)


# In[29]:


point.sort() # 데이터의 오름차순 정렬
print(point)

point.reverse()
print(point)

