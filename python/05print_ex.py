#!/usr/bin/env python
# coding: utf-8

# # 표준출력 함수 print()

# In[4]:


value = 1234
name = '홍길동'

print(value)
print(name)
# print(value + name) # 그냥 쓰면 에러 발생

# 출력할 데이터가 여러개라면 ,로 연결합니다.
print(name, '님의 나이는' , value, '입니다.')


# # 구분자 sep

# In[17]:


dog = '갱얼쥐'
cat = '킹냥이'
pig = '도야지'

# sep을 지정하지 않으면 디폴트값이 '공백' 이다.
print(dog, cat, pig)
print(dog, cat, pig, sep=' ')
print('----------------------')

# sep을 지정하면 구분자의 기능을 합니다.
print(dog, cat, pig, sep=', ')
print(dog, cat, pig, sep=' => ')
print(dog, cat, pig, sep=' > ')
print(dog, cat, pig, sep='')


# # 마지막에 기입될 값 end

# In[20]:


# end를 지정하지 않으면 디폴트 값이 \n(줄바꿈) 이다.
print(dog, cat, pig)
print(dog, cat, pig, end='\n') 
print('결과')

print('오늘', '오전에', '안나온 사람', '오후에 나올꺼죠?', end='^^?')
print('다음 출력 구문은?') # end속성을 따로 지정했기 때문에 다음 출력 구문은 붙어서 나온다.


# # end과 sep의 혼용

# In[26]:


# end과 sep은 순서를 바꿔서 배치해도 되지만 출력구문보다 먼저 넣으면 오류가 발생한다.
# print(end=' 저 먼저 퇴근할게요', sep='...', '안녕?', '집에 가고 싶다')
print('안녕?', '집에 가고 싶다.', end=' 저 먼저 퇴근할게요', sep='...')

