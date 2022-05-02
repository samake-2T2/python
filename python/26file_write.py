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

