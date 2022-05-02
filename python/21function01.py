#!/usr/bin/env python
# coding: utf-8

# ## 함수
# > def 이름() :
# 
# 1. 선언하고, 호출하는 과정이 있다.
# 2. 함수의 선언은 호출 구문보다 "항상 위에" 있어야 한다.

# In[6]:


# 함수의 호출 구문이 선언 구문보다 위에 올 수 없다.
# cal_sum()

def cal_sum() :
    
    sum = 0
    
    for i in range(1, 11) :
        sum += i
        
    print(sum)

# 전달받고자 하는 매개 변수가 있는 경우
def cal_sum2(x) :
    sum = 0
    for i in range(1, x + 1) :
        sum += i
        
    print(sum)

# 전달받고자 하는 매개 변수가 두 개 이상인 경우
def get_info(name, age) :
    print(f'이름은 {name}이고 나이는 {age}살 입니다.')
    
# 함수의 호출 구문은 선언 구문 다음에 와야 한다.    
cal_sum()
cal_sum2(20)
get_info('홍길동', 25)


# In[15]:


# 돌려줄 값이 있다면 return키워드에 값을 담아준다.
def add(n1, n2) :
    result = n1 + n2
    return result

# 원래는 아무것도 나오지 않는다.
# print(add(5, 10))

# 이렇게 쓰는게 정석임
result1 = add(5,10)
print(result1)

# 함수의 리턴값은 하나여야 한다.
# 소괄호를 생략하고 콤마로 붙이면 콤마로 붙인 값 전체가 하나의 튜플로 인식된다.
def oper(n1, n2) :
    return n1 + n2, n1 - n2, n1 * n2, n1 // n2

result2 = oper(10, 2)
print(type(result2))


# In[19]:


# 리턴 없이 함수를 선언하면????
def say_nick(name) :
    if name != '홍길동' :
        
        print('홍길동을 입력하세요')
        
        return # return을 선언하고 뒤에 아무 값도 넣지 않으면?
        
    print(f'당신은 {name}입니다')
    
# 함수 호출    
say_nick('빡빡이') # 홍길동을 입력받지 않으면 그 즉시 함수가 종료가 된다.


# In[21]:


# 리턴 없이 함수를 선언하면 출력문으로 불러왔을 때 리턴 결과가 none이다.
print( cal_sum() )
print( cal_sum2(20) )


# #### 연습문제
# 함수 연습  
# 1. 자연수 n을 인수로 받아서 n의 약수를 더한 결과를 return하는 sum함수를 완성하면 됩니다  
# hint : 반복문으로 회전하면서 해당값의 나머지가 == 0인 경우 값 누적  
# 
# 
# 2. 인수를 2개를 입력받아서 (start, end)  
# 반복문으로 start~end누적 합을 구하는 sumNum함수를 완성하면 됩니다  
# 단, 두 수의 크기는 지정되지 않았습니다  
# sumNum(1, 3) -> 6  
# sumNum(3, 1) -> 6  
# hint :  if n1 > n2 :  
#     start, end = n2, n1  
# 
# 
# 3. 정수 n을 받아서 n의 약수를 모두 가로로 출력하고, 약수의 개수와, 약수의 합을 튜플로 리턴하는  
# 한번에 리턴하는 함수 calc_divisor를 완성합니다  
# - 약수의 출력은 함수 내부에서 이루어 집니다.

# In[56]:


# 1
def sum(n) :
    sum = 0;
    for i in range(1, n + 1) :
        if n % i == 0 :
            sum += i
        
    return sum

# 2
def sumNum(start, end) :
    sum = 0;
    if(start > end) :
        start, end = end, start
        for i in range(start, end+1) :
            sum += i
    else :
        for i in range(start, end+1) :
            sum += i
    
    return sum

# 3
def calc_divisor(n) :
    count = 0
    sum = 0
    for i in range(1, n+1) :
        if n % i == 0 :
            print(i, end=" ")
            count += 1
            sum += i
    
    return count, sum


# In[57]:


print( sum(10) )
print( sumNum(10, 5) )
print( calc_divisor(9) )

