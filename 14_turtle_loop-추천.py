import turtle as t

t.color ("blue")         
t.shape("turtle")      

# 삼각형 그리기
for x in range(3):          #0 ~ n-1,    3-1 == 2
    t.forward(100)     
    t.left(120)          

# 사각형 그리기
for x in range(4):      
    t.forward(100)     
    t.left(90)           

# 원 그리기
for x in range(360):      # t.circle을 사용하지 않음 
    t.forward(1)     
    t.left(1)           
