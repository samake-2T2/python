#!/usr/bin/env python
# coding: utf-8

# #### 탈출문 break, continue

# In[2]:


for i in range(1, 11) :
    print(i)
    if i == 5 :
        break


# In[4]:


# 무한루프
while True :
    name = input('먹고싶은 음식> ')
    if name == '그만' : # 탈출
        break
        
    print(name)


# #### continue

# In[5]:


for i in range(1, 11) :
    
    if i % 2 == 0 :
        continue
    
    print(i)


# #### 실습
# 
# 1. 사용자에게 38 x 12 = ? 문제를 내고 답을 입력받습니다.
# 
# 2. 정답을 맞춘 경우 "정답입니다", 
# 
#     "x번에 만에 맞추셨네요"
# 
#     를 출력하고 반복문을 종료합니다
# 
# 3. 오답일 경우 "틀렸습니다!" 를 출력하고,
#     
#     다시 정답을 입력받을 수 있도록 반복문을 구성하세요
# 
#     hint:횟수를 누적하는 count변수를 사용!

# In[2]:




a = 38 * 12

count = 1

while True :
    q = int(input('38 x 12 = ? >'))
    
    if q == a :
        print('입력한답: ', q)
        print('정답입니다!')
        print(f'{count}번 만에 맞추셨네요.')
        break
    else :
        print('입력한답: ', q)
        print('틀렸습니다!')
        
    
    count += 1


# In[ ]:




