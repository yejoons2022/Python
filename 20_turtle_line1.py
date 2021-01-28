import turtle as t

t.bgcolor("black")  
t.color("yellow")
t.shape("turtle")

angle = 89

t.speed(1)             #speed : 0, 1, 10, 100??

for x in range(200):   
    t.forward(x)        # x의 길이는 ???
    t.left(angle)        # 거북이 89도 왼쪽으로 회전합니다.
