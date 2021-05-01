import turtle

doidaruga = turtle.Turtle()

ladoEstrela = float(input("Informe o tamanho dos lados da estrela de cinco pontas (em píxeis): "))

for x in range(10):
    doidaruga.forward(ladoEstrela)
    if (x % 2 == 0):
        doidaruga.left(72)
    else:
        doidaruga.right(144)

doidaruga.hideturtle()
turtle.done()
