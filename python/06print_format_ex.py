#!/usr/bin/env python
# coding: utf-8

# #### format() 함수로 출력
# - 서식문자
# 1. %s (:s) 문자열을 출력
# 2. %f (:f) 실수를 출력
# 3. %d (:d) 정수를 출력
# 4. %% - % 특수문자를 출력

# In[2]:


apple = 3
print('사과가 ', apple, '개 있습니다.', sep='')
print('사과가 {}개 있습니다.'.format(apple))


# In[4]:


month = 4
day = 26
ani = '화'

print('오늘은 {}월 {}일 {}요일 입니다.'.format(month, day, ani))
# 순서를 지정할 수 있습니다. (0이 첫번째)
print('오늘은 {1}월 {2}일 {0}요일 입니다.'.format(ani, month, day))


# In[13]:


# 서식문자를 이용해서 출력형식을 지정하는 방법
pi = 3.141592
print('원주율의 값은{}입니다.'.format(pi))
print('원주율의 값은{:f}입니다.'.format(pi))
print('원주율의 값은{:.2f}입니다.'.format(pi)) # 소수점 이하 2자리까지 출력
print('원주율의 값은{:10f}입니다.'.format(pi)) # 10칸잡고 오른쪽에서부터 출력
print('원주율의 값은{:<10f}입니다.'.format(pi)) # 10칸잡고 왼쪽에서부터 출력
print('원주율의 값은{:10.2f}입니다.'.format(pi)) # 10칸잡고 소수점이하 2자리까지 출력

s = '안녕!'
print('나는 {:20s} 이라고 말했다.'.format(s))
print('나는 {:>20s} 이라고 말했다.'.format(s))


# In[16]:


# f 포맷 방법

hi = 'hi'
pi = 3.14
bool_ = True

print(f'안녕은 영어로 {"hi"}')
print(f'안녕은 영어로 {hi}')
print(f'안녕은 영어로 {hi}, 원주율은 {pi}, 진실은 영어로 {bool_}')

