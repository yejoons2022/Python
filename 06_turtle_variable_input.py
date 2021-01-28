import turtle as t

t.color ("red")      
t.shape("turtle")
t.pensize(3)

d = int(input("변의 값을 입력하세요 >>> "))
angle = int(input("각도의 값을 입력하세요 >>> "))

# 삼각형 그리기

t.forward(d)     
t.left(angle)      
t.forward(d)
t.left(angle)
t.forward(d)
t.left(angle)
