import turtle

def figura(tamanio,lados):
    for i in range(lados):
        t.forward(tamanio)
        t.rt(360/lados)

t = turtle.Turtle()

figura(100,5)#Graficar pentagono de 100 px por lado
#figura(200,6)#Graficar hexagono de 100 px por lado
#figura(50,15)
#figura(150,10)#Graficar hexagono de 100 px por lado
#t.backward(300)
#t.home
#t.forward(500)
t.circle(60)
t.goto(80,-90)
t.dot(30)
turtle.done()
