lista_abre = ["[", "{", "("]
lista_fecha = ["]", "}", ")"]

def verificar(string):
    pilha = []
    for i in string:
        if i in lista_abre:
            pilha.append(i)
        elif i in lista_fecha:
            aux = lista_fecha.index(i)
            if ((len(pilha) > 0) and (lista_abre[aux] == pilha[len(pilha) - 1])):
                pilha.pop()
            else:
                return "Validação --> Falso"
    if len(pilha) == 0:
        return "Validação --> Verdadeiro"
    else:
        return "Validação --> Falso"


while(True):
    a = True

    while(a):
        print("Digite uma string para validação: ")

        string = input()

        if string != "":
            a = False

    print(string, "-", verificar(string))

    print("Deseja continuar? S/N")

    resp = input().upper()

    if resp == "N":
        break