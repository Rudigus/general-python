import turtle

doidaruga = turtle.Turtle()

linhaPentagrama = float(input("Informe o tamanho das linhas do pentagrama (em píxeis): "))

for x in range(5):
    doidaruga.forward(linhaPentagrama)
    doidaruga.right(144)

doidaruga.hideturtle()
turtle.done()
