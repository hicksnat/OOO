# The script of the game goes in this file.


#variables
default money = 200.0
default numOfWorkers = 20

default inventory = []
default nameOfRestaurant = "tempname"

#costs
default costFries = 10
default costBoiledBurger = 15
default costSoda = 5
default costGrilledChicken = 19

#items on menu for each turn
default itemsTurn = {
    1: ["Fries.", "Boiled burger."],
    2: ["Soda.", "Grilled chicken.","Fries.", "Boiled burger."],
    #TODO: add turns. change maxTurnNumber to increase as you add more turns
}
default maxTurnNumber = 2

default turnNumber = 1

#Fastfood worker character
define w = Character("Worker", color = "#FF0000")


# The game starts here.

label start:

    
   
    scene bg car




    #begin dialog

    "Insert what main character is thinking at the start here."

    "Insert goal here."

    scene bg window1
    



    w "Welcome to [nameOfRestaurant]. We have a variety of foods to choose from!"

    w "What would you like to order?"

    label order:
        $ reciept = 0;
        jump menuPrompt
        

    label menuPrompt:
        scene bg window1
        #TODO: Add lose condition (if money <= 0 then lose) add the check right here in the code
        $ turnNumber = maxTurnNumber if turnNumber >= maxTurnNumber else turnNumber
        $ currentItems = itemsTurn[turnNumber] 

        $ friesInMenu = "Fries." in currentItems
        $ boiledBurgerInMenu = "Boiled burger." in currentItems
        $ sodaInMenu = "Soda." in currentItems
        $ grilledChickenInMenu = "Grilled chicken." in currentItems

        menu:
            "Fries. ($[costFries])" if (money >= costFries) and (friesInMenu):
                $ money -= costFries
                $ reciept += costFries
                $ inventory.append("Fries")
                jump continueOrder
            "You don't have enough money for fries." if money < costFries:
                "You need at least [costFries] to buy fries."
                jump menuPrompt
            
            "Boiled burger. ($[costBoiledBurger])" if (money >= costBoiledBurger) and (boiledBurgerInMenu):
                $ money -= costBoiledBurger
                $ reciept += costBoiledBurger
                $ inventory.append("Boiled burger")
                jump continueOrder
            "You don't have enough money for a boiled burger." if money < costBoiledBurger:
                "You need at least [costBoiledBurger] to buy a boiled burger."
                jump menuPrompt

            "Soda. ($[costSoda])" if (money >= costSoda) and (sodaInMenu):
                $ money -= costSoda
                $ reciept += costSoda
                $ inventory.append("Soda")
                jump continueOrder
            "You don't have enough money for soda." if money < costFries:
                "You need at least [costSoda] to buy soda."
                jump menuPrompt

            "Grilled chicken. ($[costGrilledChicken])" if (money >= costGrilledChicken) and (grilledChickenInMenu):
                $ money -= costGrilledChicken
                $ reciept += costGrilledChicken
                $ inventory.append("Grilled chicken")
                jump continueOrder
            "You don't have enough money for grilled chicken." if money < costGrilledChicken:
                "You need at least [costGrilledChicken] to buy soda."
                jump menuPrompt

    

    label continueOrder:
        "Sure, anything else?"
        menu: 
            "Yes.":
                jump menuPrompt
            "No, that's it.":
                jump finishOrder
    
    label finishOrder:
        $ turnNumber +=1
        "Okay, that will be $[reciept]. Please continue to the checkout window to recieve your food."
        scene bg window2
        "bla bla bla here"
        "please pull back around"
   


    #TODO: do checkout window INSERT THAT HERE IN THIS SPACE
    # they will have to pull back around and order again:
    jump order






    #TODO: Make it so that when they run out of money they fail
    #TODO: death of workers stuff and its loss condition
    #done
    return
