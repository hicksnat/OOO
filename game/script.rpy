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
define u = Character("???", color = "#c9315ecf")


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

    #Boolean values that tell if certain negative statuses are active
    default fireActive = False                        #Kills one worker every turn                                      
    default customerRevoltActive = False              #Kills two workers every turn
    default strangePersonActive = False               #In three turns, will kill 5 workers
    default curseActive = False                       #All workers will die in 6 turns
    default hydraActive = False                       #Kills 1 worker the first turn, then 1 + n workers for n turns
    default firstRound = True




    

    label order:
        $ reciept = 0;

        scene bg window1

        w "Welcome to [nameOfRestaurant]. We have a variety of foods to choose from!"

        w "What would you like to order?"

        if firstRound:
            jump menuPrompt

        #Generates one of the statuses (or a chance to have none) randomly
        #Checks if status is already active, if so jumps to menuprompt, if not, jumps to prompt activation
        $ status = renpy.random.randint(1, 6)
        if status == 1:
            if fireActive:
                jump menuPrompt
            $ fireActive = True
            jump fireTalkbox
        elif status == 2:
            if customerRevoltActive:
                jump menuPrompt
            $ customerRevoltActive = True
            jump customerRevoltTalkbox
        elif status == 3:
            if strangePersonActive:
                jump menuPrompt
            $ strangePersonActive = True
            jump strangePersonTalkbox
        elif status == 4:
            if curseActive:
                jump menuPrompt
            $ curseActive = True
            jump curseTalkbox
        elif status == 5:
            if hydraActive:
                jump menuPrompt
            $ hydraActive = True
            jump hydraTalkbox
        #If 6 is generated no status occurs

        jump menuPrompt

    label fireTalkbox:
        "In between bursts of static, you hear calls of distress"
        u  "TH-- --- FI-- FIRE --S-"
        w "Welcome to [nameOfRestaurant]. Please ignore the screaming." 
        w "Service is our priority! Even if it costs {b}a worker per order!{/b}"

        jump menuPrompt

    label customerRevoltTalkbox:
        u "Next up for execution by firing squad…!"

        w "Welcome to [nameOfRestaurant]. Please excuse the wait, there is currently a customer revolt going on."
        w "They like to {b}kill two people for every order{/b}, but no go ahead I'm sure you're really hungry."
        w "I'm sure we can find someone who can settle this down."
        w "Atleast we get some extra ingredients from this."
        w "I’m rambling. What would you like to order?"

        jump menuPrompt

    label strangePersonTalkbox:
        "You feel… unsettled. Like you, and everyone in the restaurant, is being watched."
        w "Welcome to [nameOfRestaurant]. Do you see that strange person over there?"
        w "I’m sure they won’t murder {b}5 of us in 3 turns.{/b}"
        w "But if they did… A Restraining Order adds 1 turn. Metal detectors stop it."
        w "Would you like anything?"

        jump menuPrompt

    label curseTalkbox:
        "Sunday School suddenly feels a little nostalgic…"
        w "Welcome to [nameOfRestaurant]. Have you ever heard of…"
        w "…the “lingering death” curse? You can call it by saying 'Death, oh restore your sting.'"
        w "So whatever you do, don't..."
        w "..."
        w "Oh shit, um."
        w "Yo, Um, no way, some dumbass just cursed us so, uh, we can get about {b}6 orders done before we all croak.{/b}"
        w "Daily Christian Bible Quote is now on the menu."
        w "Would you like anything?"

        jump menuPrompt

    label hydraTalkbox:
        u "RRRAA-------AA-H-----HHHHHH---RRRRGGHH"
        w "Welcome to [nameOfRestaurant]! We are doomed."
        w "There’s a hydra in the kitchen. It just {b}kills more and more people for every order.{/b}"
        w "Did we tell you about our premium sword and under-boiled burger options?"
        w "If only there was some way to poison it… Your order?"

        jump menuPrompt

    
    
        

    label menuPrompt:
        scene bg window1
        
                 
        $ turnNumber = maxTurnNumber if turnNumber >= maxTurnNumber else turnNumber
        $ currentItems = itemsTurn[turnNumber] 

     
        #Boolean values that tell if the item is currently a menu option
        $ friesInMenu = "Fries." in currentItems                    
        $ boiledBurgerInMenu = "Boiled burger." in currentItems
        $ sodaInMenu = "Soda." in currentItems
        $ grilledChickenInMenu = "Grilled chicken." in currentItems

        

        #Test function lowest price
        python: 
            def lowest_price():
                lowestPrice = money
                
                if (friesInMenu and costFries < lowestPrice):
                    lowestPrice = costFries
                if (boiledBurgerInMenu and costBoiledBurger < lowestPrice):
                    lowestPrice = costBoiledBurger
                if (sodaInMenu and costSoda < lowestPrice):
                    lowestPrice = costSoda
                if (grilledChickenInMenu and costGrilledChicken < lowestPrice):
                    lowestPrice = costGrilledChicken
                return lowestPrice

        if money < lowest_price():
            jump starve          ### Added condition, lowest_price function is under the menu                    ### 

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
        if firstRound:
            "The barred window is dark when you pull up."
            "At first you think it’s just tinted enough to make an obnoxious car guy blush."
            "But you realize that’s not the case when the window slides open."
            "You can barely see a thing inside there. Is anyone even in there?"
            "Between the darkness and the abysmal sanitation rating hanging in the window, you’re tempted to drive off and give up on this altogether."
            "But then a hand juts out from the darkness." 

        w "Ahem. Your payment please."
        "You push down your unease and fish in your pocket for the proper change."
        y "...Here."
        "The worker quickly snatches the money from your outstretched hand, and before you can retract it, they hand you your order in a crumpled bag."
        w "Enjoy your grub. We hope to see you again soon for some more burger bliss."

        if firstRound:
            "You ignore the fact that their lack of enthusiasm makes the statement sound more like a threat than a well-wish, preparing to pull out."


 #TODO: make it say what foods they ordered
        
   


    # they will have to pull back around and order again:
    label checkOrder:
        if fireActive:
            w "Man, that fire is still going on... well, we're too busy with orders to put it out."
        if customerRevoltActive:
            w "These customer revolts are getting old. I don't really know how to stop it though."
        if strangePersonActive:
            w "Why is that guy still here? he's gotta be up to no good."
        if curseActive:
            w "I feel a strange sense of impending doom. Strange."
        if hydraActive:
            w "God the hydra is still in here. We're gonna need a bigger broom."
        $ firstRound = False
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
