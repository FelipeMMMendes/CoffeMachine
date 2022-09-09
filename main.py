from menu import *

#imprime a logo da maquina de cafe
print(art)

#variavel flag para manter a maquina funcionando em loop
machineStillActive = True

#def totalCurrency()



#loop que vai manter a maquina ativa
while machineStillActive:
    choice = int(input("""
    Enter with your choice:

    (1) - ESPRESSO
    (2) - LATTE
    (3) - CAPPUCCINO

    """))

    drink = associateIDWithDrink(choice)
    
    checkResources(drink,resources)

    print("----COINS----")
    quarter = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennie = int(input("How many pennies? "))

    total = checkCoins(quarter,dimes,nickles,pennie,drink)

    print(total)


    machineStillActive=False





