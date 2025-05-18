texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print (letra, end=",")
#FOR SERVE PARA LISTAR CADA ITEM DA STRING OU VARIAVEL TANGIVEL
print()

for numero in range(0,51,7): #sempre inicia no 0 e sempre termina um numero a menos do stop
 
 
 print(numero, end=",")
 #start,stop e step (onde inicia, onde termina, a diferença que será contada entre numeros)

