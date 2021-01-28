
import turtle as t

def spiral(sp_len):
    if sp_len <= 5:
        return
    t.forward(sp_len)
    t.right(90)
    spiral(sp_len - 5)

t.shape("turtle")
t.speed(1)
spiral(200)
t.hideturtle()
t.done()
