#!/usr/bin/env python
# coding: utf-8

# #### 전역변수 vs 지역변수
# - lexical특성 : 함수가 전역변수와 동일한 지역변수를 가질 때, 함수 안에서 전역변수를 참조하지 못하는 특징

# In[4]:


a = "홍길동" # 전역변수

def func1() :
    print(a)

def func2() :
    print(a)
    
def func3() :
    b = 10 # 지역변수
    print(b)


# In[7]:


func1()
func2()
func3()
# b는 지역변수이기 때문에 그냥은 사용할 수 없다.


# In[20]:


# lexical특성
c = 10
def func4() :
    c = 100
    print(c) # 100

# global을 사용해서 lexical특성 해결하기
d = 10
def func5() :
    global d # global을 사용했기 때문에 오류가 x
    print(d) # 전역변수 d : 10
    d = 100
    print(d) # 지역변수 d : 100


# In[21]:


func4() # 지역변수부터 찾기 때문에 100이 나온 모습
print('-' * 50)
func5() # global을 사용했기 때문에 오류 x


# #### 함수를 변수에 저장하기

# In[22]:


def func6() :
    sum = 0
    for i in range(1, 11) :
        sum += i
        
    print('1부터 10까지의 합:', sum) 


# In[24]:


a = func6 # a라는 변수에 func6을 저장
type(a) # function

a() # 함수를 대신 호출 ( =func6() )

