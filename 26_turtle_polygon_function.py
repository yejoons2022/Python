import turtle as t

t.color ("violet") 
t.shape("turtle") 

def polygon(n):
    for x in range(n):    
        t.forward(50)     
        t.left(360/n)   

def polygon2(n, a):
    for x in range(n):
        t.forward(a)   
        t.left(360/n)   

polygon(3)                              # 삼각형을 그립니다.
polygon(4)                              # 오각형을 그립니다.

# 그림을 그리지 않고 거북이를 100만큼 이동합니다.
t.up()                                     #pen을 올립니다. 
t.forward(100)
t.down()                                 #pen을 내립니다. 

polygon2(3, 100)                    # 한 변이 75인 삼각형을 그립니다.
polygon2(5, 100)                    # 한 변이 100인 오각형을 그립니다.
