#!/usr/bin/env python
# coding: utf-8

# #### 파일 출력

# In[2]:


path = 'dataset/test.txt'

f = open(path, mode='w', encoding='utf-8-sig') # utf8, CP949(EUC-KR)
f.write('w모드는 글을 씁니당~~')
f.close()


# In[17]:


try :
    f = open(path, mode='a', encoding='utf-8-sig') # utf8, CP949(EUC-KR)
    f.write('\na모드는 글을 추가합니당~~') # \n 줄바꿈 \r 캐리지리턴
    f.close()
except :
    print('파일 저장 실패!!')
finally :
    f.close()


# #### 파일 입력
# 1. read() - 통째로 읽는다.
# 2. readline() - 한줄씩 읽는다.
# 3. readlines() - 한줄씩 읽어서 리스트로 반환

# In[27]:


try :
    f = open(path, mode = 'r', encoding='utf-8-sig')
    
    # a = f.read()
    
    # print(f.readline())
    
    '''
    while True :
        a = f.readline()
        
        if len(a) == 0 : # 더이상 읽을게 없다는 의미
            break
        print(a)
    '''
    
    a = f.readlines()
    
    for i in a :
        print(i)
    
except :
    print('파일 찾기 실패')
finally :
    f.close


# #### with open() as 변수명
# - close작업을 자동으로 처리

# In[1]:


path = 'dataset/test.txt'


# In[5]:


with open(path, 'r', encoding='utf-8-sig') as f :
    data = f.readlines() # 반환 리스트
    print(data)


# #### 실습
# 
# '''
# 사용자의 입력을 파일(xxx.txt)에 저장하는 프로그램을 작성하세요.  
# 
# (단, 프로그램을 다시 실행하더라도 파일명이 동일하다면  
# 기존 작성한 내용을 그대로 유지하고,
# 새로 입력된 내용이 추가되어야 합니다.  
# 파일명도 마지막에 입력받아서 생성하세요.)  
# '''

# In[13]:


fname = input('저장할 파일의 이름을 입력하세요: ')

path = 'dataset/' + fname + '.txt'

with open(path, 'a', encoding='utf-8-sig') as f :
    while True :
        data = input('파일에 넣을 내용을 입력하세요: ')
        if data == '그만' :
            break
        else :
            f.write(data + '\n')# 한줄씩 쓰기
            # writeline() # 데이터를 한번에 쓰기
        

