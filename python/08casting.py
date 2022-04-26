#!/usr/bin/env python
# coding: utf-8

# #### 형변환(type casting)
# 1. str()
# 2. int()
# 3. float()
# 4. bool()
# 
# * 단, 변환할 수 없는 값이라면 에러가 발생합니다.

# In[4]:


name ='홍길동'
score = 90

type(name)
type(score)

# 문자열에 숫자를 더할 수 없지만, 정수형을 문자형으로 형변화하여 덧셈이 가능해졌다.
# print(name + str(score))
print(name + '의 점수는:' + str(score) + '입니다.')


# In[5]:


n1 = 10
n2 = "34"

# 문자열을 정수로 형변환하여 정수와 정수의 덧셈으로 만듬
print(n1 + int(n2))


# In[6]:


# 타입변환 함수들은 일시적으로 값을 변환해줄뿐, 실제값을 변경해주지는 않는다.

# 변환된 값을 변수에 다시 저장해주어 변환값을 유지시켜준다.
n2 = int(n2)

print (n1 + n2)


# In[10]:


f1 = "3.14"
print(float(f1))
print(type(float(f1)))


# In[ ]:


# 변환이 안되는 경우

s1 = '10입니다.'
s2 = "3.14~"

#에러
int(s1)
float(s2)


# In[12]:


# 정수 3으로 형변환
s3 = "3.141592"

print(int(float(s3)))

