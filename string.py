nome="VinICius"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "OLÁ MUNDO"
print(texto.strip()) #tira o espaço dentro da string
print(texto.lstrip()) #tira o espaço left da string
print(texto.rstrip()) #tira o espaço right da string


menu= "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14,"#"))
print("P-y-t-h-o-n")
print("-".join(menu))