import turtle

doidaruga = turtle.Turtle()

ladoEstrela = float(input("Informe o tamanho dos lados da estrela de Davi (em píxeis): "))

for x in range(6):
    for z in range(3):
        doidaruga.forward(ladoEstrela)
        doidaruga.right(120)
    doidaruga.forward(ladoEstrela)
    doidaruga.left(60)

doidaruga.hideturtle()
turtle.done()
