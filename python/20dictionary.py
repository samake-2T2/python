#!/usr/bin/env python
# coding: utf-8

# #### dictionary : 사전
# - {키 : 값}
# - dict() : 빈 사전 만들기

# In[19]:


stu = dict()
print(stu)

students = {"1" : "김철수", "2" : "김영희", "3" : "홍길동"}

print(type(students))

print(len(students)) # 자료형의 길이


# In[14]:


# 딕셔너리를 사용하는 방법
# 사전이름[키]
students["1"]

# 키가 있는지 없는지 확인 : in
print("1" in students )
print("고구마" in students )
print("고구마" not in students )


# #### 데이터 관리(추가, 변경, 삭제)

# In[8]:


eng = {"apple" : "사과", "peach" : "복숭아"}
eng


# In[9]:


eng["melon"] = "멜론"
eng["banana"] = "바나나"
print(eng)


# In[10]:


# 값의 변경
# 사전에 이미 존재하는 key를 사용하여 변경할 수 있습니다.
eng["banana"] = "버내너"
print(eng)


# In[11]:


# 값의 삭제
del eng["banana"] # del(eng["book"])과 같음
print(eng)


# #### 딕셔너리 함수의 반복문 keys, values

# In[16]:


for i in eng :
    print(i) # 키를 뽑는다.
    print(eng[i]) # 값을 뽑는다.


# In[18]:


print( eng.keys() )

for i in eng.keys() :
    print(i)


# #### 연습문제
# '''
# dictionary를 이용한 사전만들기
# 
# 1. eng_kor이라는 이름으로 빈 사전을 하나 생성합니다
# 
# 2. 사용자가 '그만'을 입력할 때 까지 영단어를 입력받습니다.
# 
# 3. 총 2번을 입력받는데, 영단어를 key로, 한글 뜻은 value값으로 지정해서 사전에 등록하세요.
# 
# 4. '그만'을 입력하여 단어장 만들기를 종료하면
# 그동안 입력받았던 사전의 내부 데이터를 반복문으로 전부 출력해주세요.
# 
# '''

# In[25]:


eng_kor = dict()
print(eng_kor)

while True :
    eng = input("단어를 입력하세요.")
    
    if eng == '그만' :
        
        break
    elif eng in eng_kor :
        
        print('그 단어는 이미 존재합니다.')
        
    else :
        kor = input("한글 뜻을 입력하세요.")
        eng_kor[eng] = kor
        print('영단어를 추가했습니다.')
        
for i in eng_kor :
    print(f'{i} = {eng_kor[i]}')


# In[ ]:





# In[ ]:




