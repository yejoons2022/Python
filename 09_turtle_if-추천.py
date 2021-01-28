import turtle as t

t.shape("turtle")

select = int(input("그리고 싶은 도형을 선택하세요 (1~3) >>> "))


if select == 1 :
    # 삼각형 그리기
    t.forward(100)      
    t.left(120)         
    t.forward(100)  
    t.left(120)
    t.forward(100)
    t.left(120)

elif select == 2 :
    # 사각형 그리기
    t.forward(100)    
    t.left(90)         
    t.forward(100) 
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)

elif select == 3 :
    # 원 그리기
    t.circle(50)        # 반지름이 50인 원을 그립니다.
