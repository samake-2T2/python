#!/usr/bin/env python
# coding: utf-8

# #### 모듈
# - 파이썬 안에 미리 만들어진 스크립트 파일들
# - 모듈안에는 변수, 함수, 클래스 등이 있습니다
# - 파이썬 공식문서에서 document를 참조하면 모듈의 종류를 볼 수 있습니다
# - tap으로 확인하고, shift + tap으로 상세확인

# In[3]:


import math
import statistics as st
from math import pi, sqrt, ceil, log10 # math모듈에서 나열된 기능을 가져온다.


# In[17]:


math.pi
math.sqrt(3)
math.ceil(5.3)
math.log10(10)


# In[15]:


st.mean([1,2,3,4,5,6]) # 중간값
st.median([1,3,5,7]) # 중위값
st.variance([2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]) # 분산 (평균으로부터 얼마나 떨어져 있는가
st.stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]) # 표준편차


# In[4]:


# from math import ...,...
pi
sqrt(3)
ceil(3.14)
log10(10)


# In[10]:


# 시간 관련 기능 1
# 1970년 1월 1일 00시 기준 ~ 지금까지 경과한 시간을 초단위로 반환
import time as t

start = t.time()

sum = 0
for i in range(1, 5000000) :
    sum += i

end = t.time()

print(f'프로그램시간에 걸린시간{end - start}')

print('피카츄가 양파를 까면서 하는 말은?')
t.sleep(10)
print('언제언제 까지나~ㅋㅋㅋ')


# In[2]:


# 운영체제의 시간을 확인하는 모듈 datetime
import datetime as d
x = d.datetime.today()

print(f'{x.year}년 {x.month}월 {x.day}일 {x.hour}시 {x.minute}분 {x.second}초')


# #### 사용자 정의 모듈
# - py확장자 파일로 사용자 모듈을 직접 만들고 테스트코드를 작성후에 사용합니다.

# In[4]:


import calculator as c

c.add(1, 2)
c.calc_sum(10)
c.info()
c.PI
c.inch

