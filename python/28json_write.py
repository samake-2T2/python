#!/usr/bin/env python
# coding: utf-8

# #### json파일 읽고 쓰기
# - dump: 딕셔너리를 제이슨형식으로 쓴다
# - load: 제이슨형식의 문자열을 딕셔너리로 변경

# In[3]:


import json # !pip install 모듈명

path = 'dataset/hello.json'


# In[13]:


json_data = {"id": "kkk123", "pw": "abc123"}
type(json_data)

with open(path, 'w', encoding='utf-8-sig') as f:
    json.dump(json_data, f, indent=True)


# In[25]:


# json형식의 파일 읽기

with open(path, 'r', encoding='utf-8-sig') as f:
    data_dict = json.load(f)
    print(data_dict)
    print(type(data_dict))
    
    # 데이터 다루기
    print(data_dict['id'])
    print(data_dict['pw'])
    
    print(data_dict.keys()) # 반복문 회전
    print(data_dict.items()) # 반복문 회전


# #### json데이터의 형변환

# In[26]:


dict_data = {"a": "abcde"}


type(dict_data)
str_data = json.dumps(dict_data)
type(str_data)

dict_data2 = json.loads(str_data)
type(dict_data2)

