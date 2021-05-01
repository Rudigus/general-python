palavra = input("Informe uma palavra: ")
palavra = palavra.lower()
letras = list(palavra)
numeroVogais = 0
for i in letras:
    if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or
       i == "á" or i == "é" or i == "í" or i == "ó" or i == "ú" or
       i == "â" or i == "ê" or i == "ô" or
       i == "ã" or i == "õ" or
       i == "à"):
        numeroVogais += 1
print(numeroVogais)
       
