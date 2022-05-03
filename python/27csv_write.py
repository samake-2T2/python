#!/usr/bin/env python
# coding: utf-8

# #### csv파일 읽고 쓰기
# - 임포트
# - writer( open객체, 구분자)
# - reader( open객체, 구분자)

# In[6]:


import csv

path = 'dataset/hello.csv'


# In[9]:


# newline='' 윈도우에서 파일을 쓰는 경우 다음행이 자동으로 줄바꿈이 나타나는 경우에 쓴다. 

with open(path, 'w', encoding='utf-8-sig', newline='') as f:
        data_write = csv.writer(f, delimiter=',')
        
        data_write.writerow(['a', 'b', 'c', 'd', 'e']) # 행별로 쓰기
        data_write.writerow(['a', 'b', 'c', 'd', 'e'])


# In[11]:


data_list = [['a', 'b','c'], ['1', '2','3'], ['hong', 'park','lee']]

with open(path, 'w', encoding='utf-8-sig', newline='') as f:
        data_write = csv.writer(f, delimiter=',')
        
        data_write.writerows(data_list)


# In[12]:


# csv파일 읽기

with open(path, 'r', encoding='utf-8-sig', newline='') as f:
    data_read = csv.reader(f, delimiter=',')
    
    for i in data_read :
        print(i)

