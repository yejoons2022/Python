import turtle as t

t.color ("purple")
t.shape("turtle") 

n = 5                

t.begin_fill()                   # 색칠할 영역을 시작합니다.

for x in range(n) :
    t.forward(100)
    t.left(360/n)               # 거북이 360/n 만큼 왼쪽으로 회전합니다.

t.end_fill()                      # 색칠할 영역을 마무리합니다.
