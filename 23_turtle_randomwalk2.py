import turtle as t
import random as R                #랜덤 변수 라이브러리 오픈,  r 객체 생성

t.shape("turtle")                 
t.speed(0)

for x in range(500):           
    a = R.randint(1, 360)    
    t.setheading(a)            
    b = R.randint(1,20)       
    t.forward(b)                 
