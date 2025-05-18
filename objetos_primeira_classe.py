def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a*b


def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O valor da operação é {resultado}")

exibir_resultado(10,30,somar)
exibir_resultado(10,30,subtrair)
exibir_resultado(5,12,multiplicar)