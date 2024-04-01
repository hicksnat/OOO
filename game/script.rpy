# The script of the game goes in this file.


#variables
default money = 100.0
default numOfWorkers = 10

default inventory = []
default nameOfRestaurant = "The Boiled Burger"

#costs
default costFries = 10
default costBoiledBurger = 15
default costSoda = 5
default costGrilledChicken = 19

#goal list (list of things you want to get)
default goalsList = ["Fries","Soda"]

#items on menu for each turn
default itemsTurn = {
    1: ["Fries.", "Boiled burger."],
    2: ["Soda.", "Grilled chicken.","Fries.", "Boiled burger."],
    #TODO: add more turns. change maxTurnNumber to increase as you add more turns
}
default maxTurnNumber = 2

default turnNumber = 1

#Characters
define y = Character("You", color = "#8fd567")
define w = Character("Worker", color = "#FF0000")


# The game starts here.

label start:

    
   
    scene bg car




    #begin dialog

    y "Hells, I thought that shift would never end. I can’t wait to climb into bed and rot."

    "It’s completely dark outside by the time you finish work and finally regain your freedom."
    "Your bed is calling to you, but unfortunately, it has to wait. First, you have to go to [nameOfRestaurant]."
    "That’s right. You promised your partner you’d go get them something at that dreaded place."
    "You’ve never liked any of their food – that is, their singular option: the boiled burger."
    "You’re not sure how anyone does."
    "Just the name itself sounds unappetizing. Boiled Burgers?"
    "But alas, your partner requested their squishy, soggy-bread burger, and YOU have to buy it for them."
    "That’s what love’s all about."
    "You have $[money] on you, more than enough to get a boiled burger, even with the inflation these days. God willing, this will be a quick, painless experience. It was fast food, after all."
    "And now, you pull into the decrepit, empty drive thru of this forsaken restaurant." 

    
    "[goalsList]" #TODO: make this look better in the game

    
    



    

    label order:
        $ reciept = 0;

        scene bg window1

        w "Welcome to [nameOfRestaurant]. We have a variety of foods to choose from!"

        w "What would you like to order?"

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

            #TODO: Add choice for no money

    

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
        jump recieveItemsAtWindow
        
        
    label recieveItemsAtWindow:
        scene bg window2
        "Here's your food." #TODO: make it say what foods they ordered
        
   


    # they will have to pull back around and order again:
    label checkOrder:
        $ hasNotCompletedOrder = True
        python:
            for item in goalsList:
                if item not in inventory:
                    hasNotCompletedOrder = False
            hasNotCompletedOrder = not hasNotCompletedOrder
        
        if money <= 5: #minimum cost of item
            jump starve
        if numOfWorkers <= 0:
            jump becomeWorker
        if hasNotCompletedOrder:
            w "Sorry, please pull back around. No refunds."
            jump order


    label win:
        scene bg car
        "You have completed your order and drive off."
        return

    label starve:
        scene bg window1
        w "No money no food."
        "NOOOOOOO!"
        return

    label becomeWorker:
        w "WE ARE HIRING"
        return


    #done
    return
