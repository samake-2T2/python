#!/usr/bin/env python
# coding: utf-8

# #### 예외처리
# > try :
#   ~ except :

# In[8]:


while True :    
    try :
        a = int(input('양의 정수를 입력하세요>'))
        b = int(input('양의 정수를 입력하세요>'))

        print(a + b)
        break # 정상적을 입력받으면 탈출
    except :
        print('반드시 숫자로 입력하세요.')


# In[19]:


try :
    
    a = int(input('양의 정수를 입력하세요.'))
    
    print(100 // a) # zeroDivision에러 가능성
    
    print('햄버거' [a]) # index에러 가능성
    
except ValueError : # 해당 예외만 처리함(생략하면 모든 예외를 처리하게 됩니다.
    print('반드시 숫자로 입력하세요')
except ZeroDivisionError :
    print('0으로 나눌 수 없습니다.')
except IndexError :
    print('인덱스 범위를 벗어났네용~')


# #### finally문장 (예외여부랑 상관없이 실행)

# In[21]:


pets = ['강아지', '고양이', '망아지', '송아지']

for i in range(5) :
    try :
        print(pets[i])        
    except :
        print("애완동물 정보가 없습니다.")
    
    finally :
        print('아무튼 출력되는 문장입니다.')
        print('-' * 20)


# #### 예외 강제로 만들기

# In[25]:


def calc_sum(n) :
    
    if n <= 0 :
        raise ValueError 
    
    sum = 0
    for i in range(1, n+1) :
        sum += i
        
    return sum


# In[27]:


try :
    a = calc_sum(10)
    print(a)
    b = calc_sum(-10)
    print(b)
except :
    print('매개값은 양수로 전달하세요') # 예외처리를 대신 진행

