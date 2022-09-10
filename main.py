from menu import *
import os

#imprime a logo da maquina de cafe
print(art)

#estabelece os recursos iniciais da maquina
machineResources = resources
#variavel flag para manter a maquina funcionando em loop
machineStillActive = True

#variavel flag para armazenar a quantidade de dinheiro na maquina
currentMoney = 0.0

#loop que vai manter a maquina ativa
while machineStillActive:
    choice = input("""
    Enter with your choice:

    (1) - ESPRESSO
    (2) - LATTE
    (3) - CAPPUCCINO

    """)

    if choice == 'report':
        print(f"\n\tCurrent Money: $ {currentMoney}")
        print(f"""\tCurrent Ingredients: 
        
        Water - {machineResources['water']}
        Milk - {machineResources['milk']}
        Coffe - {machineResources['coffee']}
        
        """)
        continue
    if choice == 'turn off':
        machineStillActive = False

    #funcao que, a partir do ID que o usuario entrou, identifica o drink que ele queria
    drink = associateIDWithDrink(choice)

    #tratamento de excecao caso o numero inserido seja invalido
    if drink == False:
        print("Invalid number, try again: ")
        os.system("cls")
        continue
    
    if checkResources(drink,machineResources) == True:
        print("\tPlease insert coins: ")
    else:
        continue   
    
    quarter = int(input("\tHow many quarters? "))
    dimes = int(input("\tHow many dimes? "))
    nickles = int(input("\tHow many nickles? "))
    pennie = int(input("\tHow many pennies? "))
    
    total = checkCoins(quarter,dimes,nickles,pennie,drink)

    if total == False:
        print("Not enough money! Coins refunded! ")
        continue
    else:
        print(f"You inserted $ {total}")
        print(f"Your drink costs $",str(drink["cost"]))
        print(f"Here's $ {(total - (drink['cost'])):.2f} in change ")
        currentMoney += drink['cost']
        machineResources = useIngredients(drink,machineResources)
        continue

    





