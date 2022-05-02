#!/usr/bin/env python
# coding: utf-8

# #### 파이썬의 문자열 다루기 함수들
# 1. len
# 2. replace
# 3. split
# 4. find
# 5. count
# 
# > shift + tab으로 함수의 정보를 확인할 수 있다.

# In[2]:


s = 'python'

print('문자열의 길이: ', len(s))


# In[3]:


len(range(1, 1001)) # 길이 1000
len([1,2,3,4]) # 길이 4


# In[5]:


s = 'python programming'

s = s.replace('python', '파이썬')

s


# In[6]:


s = '010-1234-5678'
list_ = s.split('-')
list_


# In[12]:


s = '''
생각이라는 생각은 생각할수록 자꾸 생각이 나기때문에 
생각이라는 것은 아예 생각하지 않는 것이 좋다고 생각합니다.
'''

print('생각이라는 단어가 처음 발견된 위치:', s.find('생각'))
print('생각이라는 단어가 발견된 횟수:', s.count('생각'))

