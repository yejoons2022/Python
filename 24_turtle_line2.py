import turtle as t

t.bgcolor("black")
t.shape("turtle")     
t.speed(0)           

for x in range(200): 
    if x % 3 == 0:  
        t.color("red")
    if x % 3 == 1:
        t.color("yellow")
    if x % 3 == 2:
        t.color("blue")
    t.forward(x * 2)                  # x*2 만큼 앞으로 이동합니다(반복하면서 선이 점점 길어집니다).
    t.left(119)                          # 거북이를 119도 왼쪽으로 회전합니다.
