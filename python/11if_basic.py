#!/usr/bin/env python
# coding: utf-8

# #### 실습
# 
# 1. 국어, 영어, 수학점수를 받아서 평균이 60점 이상이면
# "시험에 통과했습니다" 를 출력하세요
# 평균점수를 소수점 2자리까지 출력하세요. hint: round()
# 
# 2. 평균이 60점 미만이라면 "재수강 대상입니다" 를 출력하세요
# 
# 3. 통과/재수강 여부에 상관없이 "열공합시다" 를 출력하세요

# In[2]:


kor = int(input('국어점수: '))
eng = int(input('영어점수: '))
math = int(input('수학점수: '))

avg = round((math + eng + kor) / 3, 2)

if avg >= 60 :
    print('합격입니다')
else :
    print('재수강 대상입니다.')
    
print(avg)
    
print('열공 합시다~!')


# #### elif

# In[4]:


age = int(input('나이를 입력하세요>'))

if age >= 20 :
    print('성인')

elif age >= 17 :
    print('고등학생~')

elif age >= 14 :
    print('중학생~')
    
elif age >= 8 :
    print('초등학생~')
    
else :
    print('미취학 아동입니다~')


# #### 중첩if

# In[5]:


cm = int(input('키>'))
age = int(input('나이>'))

if cm >= 140 : 
    
    if age  >= 8 :
        print('놀이기구 탑승이 가능합니다.')
    else :
        print('나이가 8세 미만입니다.')
    print('-' * 50)
        
else :
    print('키가 140미만 입니다.')


# #### 실습2
# 
# 1. 점수(point)를 입력받아 90점 이상이면
# 다시 한번 조건을 검사하여 
# 100점을 초과한 경우 "점수를 잘못 입력했습니다" 를 출력.
# 95~100일 때는 "학점은 A+입니다" 
# 위 두 조건을 만족하지 못하면 "학점은 A입니다"
# 
# 2. 다중 분기 조건문을 사용하여 
# 80점대는 B학점
# 70점대는 C학점
# 60점대는 F학점으로 처리하세요

# In[8]:


point = int(input('점수: '))

if point >= 90 :
    if point > 100 :
        print('점수를 잘못입력했습니다.')
    elif point >= 95 :
        print('학점은 A+입니다.')
    else :
        print('학점은 A입니다.')
elif point >= 80 :
    print('학점은 B입니다.')
elif point >= 70 :
    print('학점은 C입니다.')
else :
    print('학점은 F입니다.')

