import turtle as t
import random as R                #랜덤 변수 라이브러리 오픈,  r 객체 생성

t.shape("turtle")    
t.speed(0)

for x in range(500):                # 거북이를 500번 움직입니다.
    a = R.randint(1, 360)           # 1~360 사이의 아무 수나 골라 a에 저장합니다. 객체 r 사용 
    t.setheading(a)                  # a 각도로 거북이의 머리방향을 돌립니다.
    t.forward(10)                     # 거북이를 10만큼 앞으로 이동합니다.
