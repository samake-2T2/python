#!/usr/bin/env python
# coding: utf-8

# #### for 변수 in 시퀀스자료형
# - 들여쓰기
# - 시퀀스자료형 : 집합형태로 만들어진 자료형( 대표적으로 리스트가 있습니다.)

# In[23]:


# [1, 2, 3]

for a in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] :
    print(a)
    


# In[24]:


for a in range(1, 101, 1) :
    print(a, end=' ')


# #### 내장함수 range()
# 
# - range(start, end, step)
# - end미만

# In[10]:


list1 = list(range(0, 10, 3))
list1

list2 = list(range(0, 10, 2))
list2

# 매개값이 두개인 경우 (start, end)
# step은 기본으로 1로 처리됩니다.
list3 = list(range(0, 10))
list3

# 매개값이 한개인 경우 (end)
# start=0, step=1로 처리
list4 = list(range(10))
list4

# 7~100까지 정수 중에서 7의 배수의 합
list5 = list(range(7, 101)) # 7~100

sum = 0

for a in list5 :
    if a % 7 == 0 :
       sum += a
    
print('7의 배수의 합: ', sum)


# In[15]:


# 1. 1~200까지 짝수만 출력
list1 = list(range(1, 201))

for a in list1 :
    if a % 2 == 0 :
        print(a, end=' ')
        
print()
print('-' * 50)

# 2. 1~2345까지 13의 배수의 개수
list2 = list(range(1, 2346))

count = 0

for a in list2 :
    if a % 13 == 0 :
        count += 1
print('1~2345까지 13의 배수의 개수: ', count)
print('-' * 50)

# 3. 1~300까지 정수중의 6의 배수이고, 12의 배수가 아닌 수의 합
list3 = list(range(1, 301))

sum = 0

for a in list3 :
    if(a % 6 == 0 and a % 12 != 0) :
        sum += a
        
print('1~300까지 정수중의 6의 배수이고, 12의 배수가 아닌 수의 합: ', sum)


# #### 반복문의 중첩

# In[17]:


for i in range(2, 10) : # 2~9
    
    print(f'구구단 {i}단')
    
    for j in range(1, 10) : # 1~9
        print(f'{i} x {j} = (i*j)')
        
    print('-' * 50)

