import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.pensize(3)



caonha = 50
ngangnha = 100
ngangcua = 20
caocua = 30
canhtraimai = 50
gocnocnha = 90
ngangmai = 1
maunha = 91/255,155/255,213/255
canhthannho = 15
canhthanto = 30
canhtanla1 = 60
canhtanla2 = 50
canhtanla3 = 40

# Thân nhà
t.pencolor(maunha)
t.fillcolor("pink")
t.begin_fill()
t.fd(ngangnha)
t.left(90)
t.fd(caonha)
t.left(90)
t.fd(ngangnha)
t.left(90)
t.fd(caonha)
t.end_fill()


# Cửa
t.left(90)
t.goto((ngangnha/2 - ngangcua/2),0)
t.fd(ngangcua)
t.left(90)
t.fd(caocua)
t.left(90)
t.fd(ngangcua)
t.left(90)
t.fd(caocua)



# Mái nhà
t.penup()
t.goto(0,caonha)
t.left(90 + (180-gocnocnha)/2)
t.fillcolor("purple")
t.begin_fill()
t.pendown()
t.fd(canhtraimai)
t.right(180-gocnocnha)
t.fd(math.sqrt((ngangmai**2) + (canhtraimai**2) - 2*ngangmai*canhtraimai*math.cos((180-gocnocnha)/2)))
t.left(180-(180-gocnocnha)/2-gocnocnha)
t.end_fill()


# Ống khói
t.penup()
t.right(gocnocnha/2)
t.backward(canhtraimai*2/3)
t.right(gocnocnha/2)
t.pendown()
t.backward(10)
t.left(90)
t.forward(5)
t.right(90)
t.forward(20)


# khói
t.penup()
t.backward(25)
t.pensize(2)
t.pendown()
t.backward(15)
t.right(90)
t.penup()
t.forward(3)
t.left(90)
t.pendown()
t.forward(10)

t.left(gocnocnha)
t.pensize(3)

t.pencolor("green")
# Thân cây: màu nâu
t.penup()
t.goto(200,0)
t.left(90)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.forward(canhthanto)
t.right(90)
t.forward(canhthannho)
t.right(90)
t.forward(canhthanto)
t.right(90)
t.forward(canhthannho)
t.end_fill()


# Tán lá: màu xanh lá (1/3)
t.penup()
t.right(90)
t.forward(30)
t.left(90)
t.forward((canhtanla1-canhthannho)//2)
t.pendown()
t.fillcolor("light green")
t.begin_fill()
t.left(45)
t.backward(canhtanla1/math.sqrt(2))
t.left(90)
t.forward(canhtanla1/math.sqrt(2))
t.left(45)
t.backward(canhtanla1)



# Tán lá: màu xanh lá (2/3)
t.penup()
t.left(90)
t.forward(canhtanla1/2)
t.left(90)
t.pendown()
t.left(45)
t.backward(canhtanla1/math.sqrt(2))
t.left(90)
t.forward(canhtanla1/math.sqrt(2))
t.left(45)
t.backward(canhtanla1)


# Tán lá: màu xanh lá (3/3)
t.penup()
t.left(90)
t.forward(canhtanla1/2)
t.left(90)
t.pendown()
t.left(45)
t.backward(canhtanla1/math.sqrt(2))
t.left(90)
t.forward(canhtanla1/math.sqrt(2))
t.left(45)
t.backward(canhtanla1)
t.end_fill()


# Cây bên trái:
t.penup()
t.goto(-100,-50)
t.left(90)

# Thân cây: màu nâu
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.forward(canhthanto)
t.right(90)
t.forward(canhthannho)
t.right(90)
t.forward(canhthanto)
t.right(90)
t.forward(canhthannho)
t.end_fill()


# Tán lá: màu xanh lá (1/3)
t.penup()
t.right(90)
t.forward(30)
t.left(90)
t.forward((canhtanla2-canhthannho)//2)
t.pendown()
t.fillcolor("light green")
t.begin_fill()
t.left(45)
t.backward(canhtanla2/math.sqrt(2))
t.left(90)
t.forward(canhtanla2/math.sqrt(2))
t.left(45)
t.backward(canhtanla2)



# Tán lá: màu xanh lá (2/3)
t.penup()
t.left(90)
t.forward(canhtanla2/2)
t.left(90)
t.pendown()
t.left(45)
t.backward(canhtanla2/math.sqrt(2))
t.left(90)
t.forward(canhtanla2/math.sqrt(2))
t.left(45)
t.backward(canhtanla2)


# Tán lá: màu xanh lá (3/3)
t.penup()
t.left(90)
t.forward(canhtanla2/2)
t.left(90)
t.pendown()
t.left(45)
t.backward(canhtanla2/math.sqrt(2))
t.left(90)
t.forward(canhtanla2/math.sqrt(2))
t.left(45)
t.backward(canhtanla2)
t.end_fill()


turtle.done()