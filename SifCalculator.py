print("|-----------------------------------------------|")
print("   _____ _  __                                   ")
print("  / ____(_)/ _|                                  ")
print(" | (___  _| |_                                   ")
print("  \___ \| |  _|                                  ")g
print("  ____) | | |                                    ")
print(" |_____/|_|_| _            _       _             ")
print("  / ____|    | |          | |     | |            ")
print(" | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ ")
print(" | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|")
print(" | |___| (_| | | (__| |_| | | (_| | || (_) | |   ")
print("  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   ")
print("|-----------------------------------------------|")
categoria = int(input("\n escolha a area que deseja calcular: \n 1.Pleno \n 2.Tecnico \n >>> "))
if (categoria == 1):
    poNum = int(input("digite o numero de provas \n >> "))
    acNum = int(input("digite o numero de ac's \n >> "))
    if(poNum == 1):
        po1 = float(input("digite a nota da po1 \n >> ", ))
        poTotal = po1 * 0.5
        print("valor da prova na media: ", poTotal)
    if(poNum == 2):
        po1 = float(input("digite a nota da po1 \n >> ", ))
        po2 = float(input("digite a nota da po2 \n >> ", ))
        poTotal = (po1 + po2)
        poTotal = (poTotal / 2 )
        poTotal = (poTotal * 0.5)
        print("valor da prova na media: ", poTotal)
    if(acNum == 1):
        ac1 = int(input("digite a nota da ac1 \n >> "))
        acTotal = (ac1 * 0.3)
        print("valor da ac na media: ", acTotal)
    if(acNum == 2):
        ac1 = int(input("digite a nota da ac1 \n >> "))
        ac2 = int(input("digite a nota da ac2 \n >> "))
        acTotal = (ac1 + ac2)
        acTotal = (acTotal / 2)
        acTotal = (acTotal * 0.3)
        print("valor da ac na media: ", acTotal)
    if(acNum == 3):
        ac1 = int(input("digite a nota da ac1 \n >> "))
        ac2 = int(input("digite a nota da ac2 \n >> "))
        ac3 = int(input("digite a nota da ac3 \n >> "))
        acTotal = (ac1 + ac2 + ac3)
        acTotal = (acTotal / 3)
        acTotal = (acTotal * 0.3)
        print("valor da ac na media: ", acTotal)
    if(acNum == 4):
        ac1 = int(input("digite a nota da ac1 \n >> "))
        ac2 = int(input("digite a nota da ac2 \n >> "))
        ac3 = int(input("digite a nota da ac3 \n >> "))
        ac4 = int(input("digite a nota da ac4 \n >> "))
        acTotal = (ac1 + ac2 + ac3 + ac4)
        acTotal = (acTotal / 4)
        acTotal = (acTotal * 0.3)
        print("valor da ac na media: ", acTotal)
    agh = float(input("digite a nota da AGH \n >> "))
    aghTotal = (agh * 0.2)
    bonus = float(input("digite sue bonus: "))
    Total = (aghTotal + poTotal + acTotal + bonus)
    print("sua media sera de ", Total, "\n \n \n \n")
    print("\n criado por mim")
if(categoria == 2):
    print("ops! parece que o programador ainda não passou por aqui")
