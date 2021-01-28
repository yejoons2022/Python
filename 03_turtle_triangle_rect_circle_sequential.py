import turtle as t

t.shape("turtle")

# 삼각형 그리기
t.color ("red")
t.pensize(1)

t.forward(100)      
t.left(120)         
t.forward(100)  
t.left(120)
t.forward(100)
t.left(120)

# 사각형 그리기
t.color ("green")
t.pensize(3)

t.forward(100)    
t.left(90)         
t.forward(100) 
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# 원 그리기
t.color ("blue")
t.pensize(5)

t.circle(50)        # 반지름이 50인 원을 그립니다.
