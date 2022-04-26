#!/usr/bin/env python
# coding: utf-8

# #### 표준 입력함수 input()
# 
# * input의 결과는 항상 문자열입니다.

# In[5]:


nick = input('너 별명이 뭐냥?:')


print('입력된 별명은:' + nick)
print(type(nick))


# In[8]:


print('두 수를 입력하세요>')
n1 = int(input('첫번째 수:'))
n2 = int(input('두번째 수:'))

print(n1 + n2)

