def criar_carro(modelo,ano,placa,/, marca, motor, combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

criar_carro("Palio", 2006, "EUC6782", "Fiat", 1.0, "Gasolina")   #itens antes da barra "/" são nomeados por posição, itens após o asterisco "*" são nomeados por keyword ou seja marca=fiat

def criar_marcas(Nome, porte, funcionarios, / , ramo,):
    print(Nome,porte,funcionarios,ramo)

criar_marcas("Mc'Donalds", "Grande porte", 10000, "Alimentício")
    