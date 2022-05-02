#!/usr/bin/env python
# coding: utf-8

# #### default 매개변수 (가변인수)
# - 파이썬에서는 매개변수(인수)의 기본값을 설정해서 자주 쓰지 않는 매개값을 기본값으로 선언할 수 있다.

# In[6]:


def calc(begin, end, step=1) :
    sum = 0
    for i in range(begin, end+1, step) :
        sum += i
        
    return sum


# In[7]:


# 기본 값을 가지고 있더라도 매개변수의 개수를 맞추어 호출할 수 있다.
print( calc(1, 10, 2) ) # 1 + 3 + 5 + 7 + 9 = 25

# 매개변수의 개수를 맞추지 않으면 기본 값이 적용된다.
print( calc(1, 10) ) # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55


# #### 기본 매개변수가 없으므로, default 매개변수는 뒤로

# In[13]:


# 기본값을 주려면 일반 매개변수보다 뒤에 위치시켜야 한다.
def calc2(end, begin=0, step=1) :
    sum = 0
    for i in range(begin, end+1, step) :
        sum += i
        
    return sum


# In[15]:


print( calc2(10) )
print( calc2(10, 1) )
print( calc2(10, 1, 1) )


# #### 키워드 변수
# - 인수의 개수가 많아지면, 파악이 어렵기 때문에, 순서와 무관하게 인수를 전달하는 방법을 제공합니다.
# - 직접 지정해서 꽂아줌
# 
# > print('출력문', sep=',', end='\n')

# In[17]:


def calc3(begin, end, step) : 
    sum = 0
    for i in range(begin, end+1, step) :
        sum += i
        
    return sum


# In[19]:


calc3(1, 10, 1)
calc3(begin=1, end=10, step=1) 
calc3(end=10, step=1, begin=1) # 순서는 바뀌어도 상관없다.

# 키워드와 위치인수를 혼용으로 사용할 수 있다.
calc3(1, step=1, end=10)

# 단, 혼용 사용할 경우 위치 변수가 가장 앞에 위치해야 한다. default값이 항상 위치변수보다 뒤에 위치
# 잘 모르겠으면 print() 문의 구조를 잘 생각해보면 된다.
# print('출력문1', '출력문2', sep=' ', end=' ')
# calc3(begin=1, 10, step=1) : 오류 발생

