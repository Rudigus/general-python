import turtle

doidaruga = turtle.Turtle()

numeroRaio = int(input("Informe o número de raios do sol: "))
raioCircunferencia = float(input("Informe o raio da circunferência do sol: "))
tamanhoRaio = float(input("Informe o tamanho dos raios do sol: "))

doidaruga.pencolor("orange")
doidaruga.fillcolor("yellow")
doidaruga.begin_fill()
for x in range(numeroRaio):
    doidaruga.circle(raioCircunferencia, 360 / numeroRaio)
    doidaruga.right(90)
    doidaruga.forward(tamanhoRaio)
    doidaruga.backward(tamanhoRaio)
    doidaruga.left(90)
doidaruga.end_fill()

doidaruga.hideturtle()
turtle.done()
