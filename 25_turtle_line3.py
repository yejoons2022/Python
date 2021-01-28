import turtle

colors = ["red", "purple", "blue", "green", "yellow", "orange" ]

t = turtle.Turtle()                      # import turtle as t 와 같은 객체 생성 동일

turtle.bgcolor("black")              # background color는 객체가 아니므로 turtle로 선언 
t.speed(0)
t.width(3)
length = 10	

while length < 500:	
    t.forward(length)			
    t.pencolor(colors[length%6])	
    t.right (89)			
    length += 5
