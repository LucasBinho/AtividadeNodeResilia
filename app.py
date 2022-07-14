# exemplo de como seria com python

resposta = input("DIGITE ALGO: ")
lista_respostas = []

while resposta != "sair":
    lista_respostas.append(resposta.lower())
    resposta = input("DIGITE ALGO: ")

lista_respostas.sort()
print(lista_respostas)