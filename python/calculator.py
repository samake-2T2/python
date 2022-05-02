#!/usr/bin/env python
# coding: utf-8

# In[2]:


def calc_sum(end) :
    sum = 0
    for i in range(0, end+1) :
        sum += i
        
    return sum

def add(n1, n2) :
    return n1 + n2

def info() :
    print('모듈 임포트 연습시간')

    
inch = 2.5
PI = 3.14

'''
1. 모듈로 만든 파일을 테스트 코드로 확인하는 방법



__name__에는 실행중인 모듈의 이름이 저장됩니다.

현재파일에서 모듈을 실행할 때는 __name__에 "__main__"이 저장됩니다.
다른파일에서 모듈을 실행할 때는 __name__에 파일명이 저장되게됩니다.

'''
print('다른 파일에서 사용할 때 모듈명:', __name__)

if __name__ == "__main__" :
    print('음 잘된다~')

