
import turtle as t

def tri(tri_len):
    if tri_len <= 5:
        for i in range(0, 3):
            t.forward(tri_len)
            t.left(120)
        return
    new_len = tri_len / 2
    tri(new_len)
    t.forward(new_len)
    tri(new_len)
    t.backward(new_len)
    t.left(60)
    t.forward(new_len)
    t.right(60)
    tri(new_len)
    t.left(60)
    t.backward(new_len)
    t.right(60)

t.shape("turtle")
t.speed(0)

num = int(input("숫자를 입력하세요 >>> "))
tri(num)
t.hideturtle()
t.done()
