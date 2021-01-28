import turtle as t

t.bgcolor("black")     
t.color("green")
t.shape("turtle")   

n = 50                 
t.speed(0)                  # 거북이 속도(0이 가장 빠름, 1이 가장 느림)
for x in range(n):           # n번 반복합니다.
    t.circle(80)               # 현재 위치에서 반지름이 80인 원을 그립니다.
    t.left(360/n)              # 360/n 만큼 거북이를 왼쪽으로 회전합니다.
