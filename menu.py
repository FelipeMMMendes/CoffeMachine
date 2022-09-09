MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#funcao que associa cada numero ao respectivo drink
def associateIDWithDrink(drinkId):
    if drinkId==1:
        return MENU["espresso"]

#funcao que checa se há ingredientes o suficiente para fazer tal bebida
def checkResources(drink,resources):
    for item in drink["ingredients"]:
        if item[""] > resources[item]:
            print("There's not enough ingredients! Maybe try another drink? ")

#funcao que checa se as moedas que o cliente inseriu sao o suficiente
def checkCoins(quarter,dimes,nickles,pennie,drink):
    total = (quarter * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennie * 0.01)
    if total >= drink["cost"]:
        return total
    else:
        return print("Not enough money! Coins refunded")       



    



art = """

                                    .
                                            `:.
                                            `:.
                                    .:'     ,::
                                    .:'      ;:'
                                    ::      ;:'
                                    :    .:'
                                    `.  :.
                            _________________________
                            : _ _ _ _ _ _ _ _ _ _ _ _ :
                        ,---:".".".".".".".".".".".".":
                        : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
                        `.`.  `:-===-===-===-===-===-:'
                        `.`-._:                   :
                            `-.__`.               ,' 
                        ,--------`"`-------------'--------.
                        `"--.__                   __.--"'
                                `""-------------""'

 _______ _______ _______ _______ _______    _______ _______ _______ _     _ _ _______ _______ 
(_______|_______|_______|_______|_______)  (_______|_______|_______|_)   (_) (_______|_______)
 _       _     _ _____   _____   _____      _  _  _ _______ _       _______| |_     _ _____   
| |     | |   | |  ___) |  ___) |  ___)    | ||_|| |  ___  | |     |  ___  | | |   | |  ___)  
| |_____| |___| | |     | |     | |_____   | |   | | |   | | |_____| |   | | | |   | | |_____ 
 \______)\_____/|_|     |_|     |_______)  |_|   |_|_|   |_|\______)_|   |_|_|_|   |_|_______)



"""