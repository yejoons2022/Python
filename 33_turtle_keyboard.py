import turtle as t

def turn_right():                
    t.setheading(0)            
    t.forward(10)               

def turn_up():                  
    t.setheading(90)
    t.forward(10)

def turn_left():                 
    t.setheading(180)
    t.forward(10)

def turn_down():              
    t.setheading(270)
    t.forward(10)

def blank():                     
    t.clear()

t.shape("turtle")               
t.speed(0)                       
t.onkeypress(turn_right, "Right")           # 방향키 사용 , [→]를 누르면 turn_right 함수를 실행합니다.
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape")              # [Esc]키 사용 
t.listen()                                             # 거북이 그래픽 창이 키보드 입력에 대한 응답
