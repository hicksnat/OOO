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
default costStirfries = 11

default costIceWater = 3
default costPolitician = 20
default costRestrainingOrder = 30
default costDailyChristianBibleQuote = 15
default costSword = 12

#goal list (list of things you want to get)
default goalsList = ["Fries","Soda"]

#items on menu for each turn
default itemsTurn = {
    1: ["Fries.", "Boiled burger."],
    2: ["Soda.", "Grilled chicken.","Fries.", "Boiled burger.","Stir-fries."],
    #TODO: add more turns. change maxTurnNumber to increase as you add more turns
}
default maxTurnNumber = 2

default turnNumber = 1

#Characters
define y = Character("You", color = "#8fd567")
define w = Character("Worker", color = "#FF0000")
define u = Character("???", color = "#c9315ecf")
define p = Character("Partner", color = "#90bdcc")


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

    
    "Your partner wants [goalsList]" #TODO: make this look better in the game

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

        $ StrangePersonCountdown = 3

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
        $ curseCountdown = 6

        jump menuPrompt

    label hydraTalkbox:
        u "RRRAA-------AA-H-----HHHHHH---RRRRGGHH"
        w "Welcome to [nameOfRestaurant]! We are doomed."
        w "There’s a hydra in the kitchen. It just {b}kills more and more people for every order.{/b}"
        w "Did we tell you about our premium sword option? Your burger will never be cut cleaner!"
        w "If only there was some way to kill it… Your order?"

        $ hydraNumber = 1

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
        $ stirFriesInMenu = "Stir-fries." in currentItems


        

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
            
            "Stir-fries. ($[costStirfries])" if (money >= costStirfries) and (stirFriesInMenu):
                $ money -= costStirfries
                $ reciept += costStirfries
                $ inventory.append("Stir-fries")
                jump continueOrder
            "You don't have enough money for Stir-fries" if money < costStirfries:
                "You need at least [costStirfries] to buy stir-fries."
                jump menuPrompt

            #Status items
        
            "Ice water. ($[costIceWater])" if (money >= costIceWater) and (fireActive):
                $ money -= costIceWater
                $ reciept += costIceWater
                $ fireActive = False
                #Do not append to inventory because the workers use it
                jump continueOrder
            "You don't have enough money for Ice water." if (money < costIceWater) and (fireActive):
                "You need at least [costIceWater] to buy ice water."
                jump menuprompt

            "Politician. ($[costPolitician])" if (money >= costPolitician) and (customerRevoltActive):
                $ money -= costPolitician
                $ reciept += costPolitician
                $ customerRevoltActive = False
                #Do not append to inventory because the workers use it
                jump continueOrder
            "You don't have enough money for a politician." if (money < costPolitician) and (customerRevoltActive):
                "You need at least [costPolitician] to buy a politician."
                jump menuprompt
            
            "Restraining Order. ($[costRestrainingOrder])" if (money >= costRestrainingOrder) and (strangePersonActive):
                $ money -= costRestrainingOrder
                $ reciept += costRestrainingOrder
                $ strangePersonActive = False
                #Do not append to inventory because the workers use it
                jump continueOrder
            "You don't have enough money for a restraining order." if (money < costRestrainingOrder) and (strangePersonActive):
                "You need at least [costRestrainingOrder] to buy a restraining order."
                jump menuprompt

            "Daily Christian Bible Quote. ($[costDailyChristianBibleQuote])" if (money >= costDailyChristianBibleQuote) and (curseActive):
                $ money -= costDailyChristianBibleQuote
                $ reciept += costDailyChristianBibleQuote
                $ curseActive = False
                #Do not append to inventory because the workers use it
                jump continueOrder
            "You don't have enough money for a Daily Christian Bible Quote." if (money < costDailyChristianBibleQuote) and (curseActive):
                "You need at least [costDailyChristianBibleQuote] to buy ice water."
                jump menuprompt

            "Sword. ($[costSword])" if (money >= costSword) and (hydraActive):
                $ money -= costSword
                $ reciept += costSword
                $ hydraActive = False
                #Do not append to inventory because the workers use it
                jump continueOrder
            "You don't have enough money for a sword." if (money < costSword) and (hydraActive):
                "You need at least [costSword] to buy a sword."
                jump menuprompt

            "You don't have money... order something anyway?" if (money < 3) and (fireActive):
                "You helped them out, surely they'll return your good will."
                jump starve
            "You don't have money... order something anyway?" if (money < 5) and (fireActive == False):
                "You helped them out, surely they'll return your good will."
                jump starve




    


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
    label checkOrder:         #Status effects and their consequences

        if numOfWorkers <= 0:
            jump becomeWorker

        if fireActive:
            w "Man, that fire is still going on... well, we're too busy with orders to put it out."
            $ numOfWorkers -= 1
        if customerRevoltActive:
            w "These customer revolts are getting old. I don't really know how to stop it though."
            $ numOfWorkers -= 2
        if strangePersonActive:
            w "Why is that guy still here? he's gotta be up to no good."
            $ StrangePersonCountdown -= 1
            if (StrangePersonCountdown == 0):
                $ numOfWorkers -= 5
                $ strangePersonActive = False    
        if curseActive:
            w "I feel a strange sense of impending doom. Strange."
            $ curseCountdown -= 1
            if (curseCountdown == 0):
                $ numOfWorkers = 0
        if hydraActive:
            w "God the hydra is still in here. We're gonna need a bigger broom."
            $ numOfWorkers -= hydraNumber
            $ hydraNumber += 1
        "You have $[money] left."
        "Judging by the carnage, there are probably about [numOfWorkers] employees left."
        if curseActive:
            "About [curseCountdown] more orders until everyone in there is doomed!"
        if strangePersonActive:
            "That strange man is up to no good. About [StrangePersonCountdown] orders until he strikes...."

        

        if firstRound:
            "Just as you flip on your turn signal, your phone rings, causing you to jump in your seat. You answer."
            y "Hello?"
            p "Ah, hey, have you left [nameOfRestaurant] yet?"
            y "…no?"
            p "Awesome! I realized I’m a bit hungrier than expected and their website says they added new stir-fries to the menu. I was hoping you’d get me some of those, too. Pretty please?"
            y "…yeah, I can do that."
            p "Thank you, thank you, thank you! See you soon! Love ya!"
            "They hang up, leaving you in silence."
            y "Gods above, I have to go back around."
            $ goalsList.append("Stir-fries")
            #Write the things left that you need
            
            
            if fireActive:
                if money < 3:
                    jump starve
            elif money < 5:
                jump starve
            
            $ currentGoalsList = []
            python:
                for item in goalsList:
                    if item not in inventory:
                        currentGoalsList.append(item)
            #You could add here if the currentGoalsList is empty at this point then jump to the win label
            "You still need [currentGoalsList]."
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
        "You pull away from the window, expecting your phone to ring. But a moment passes, and another, with nothing. No call. Could it be? Can you finally… leave?"
        "You pull out of the parking lot, unable to wipe the stupid grin off your face as that awful place grows smaller and smaller in your rearview mirror."
        y "Thank Oderus, I thought I was never getting out of that hellhole. I think I got everything that was requested of me. At least I hope so."
        "As you drive down the empty, moonlit road towards home, you let your thoughts shift from that experience to much, much more pleasant thoughts."
        y "I can’t wait to hit the sack."

        return

    label starve:
        scene bg window2
        "You reach into your pocket to grab your payment, but are met by nothingness. Somehow in this whole shebang, you’d managed to spend $200. At Boiled Burgers, of all places."
        "You think about how many Robux you could’ve bought with that kind of money, or Dairy Queen Blizzards. A lot, that’s for damn sure. But now you’re here, $200 in and still unable to get everything that was requested of you."
        "A sharp cough breaks you from your thoughts, and you realize the worker—or at least their phantom hand in the darkness—is still awaiting your payment." 
        "You frantically search your car, checking under the seats and in every nook and cranny for a bit of cash, but it’s all in vain. You have nothing, and the worker is starting to notice, if the gradual closing of their fist is any indication."
        y "I… uh… I don’t have any money. Can I just cancel my order?"
        w "But… we already made it. It’s already done. You can’t just… we can’t take the loss. You have to give us something. Something worth the same as your order."
        y "I don’t have anything! What do you want me to do? I even spent money trying to help you guys. Can’t you just give me this one thing?"
        "The worker’s hands shake, moving faster and faster until they are vibrating at a speed that shouldn’t be humanly possible. You try to roll up your window, but it isn’t fast enough."
        "Their fingers cram into the remaining gap and grab you by the shirt, pulling you against your window. You feel your vision go black for a moment, and before you can fight back, your vision returns." 
        "You're driving. Boiled Burgers is nowhere in sight. You look to your left. All the food you’d accumulated… is gone? Were you ever at Boiled Burgers? Was this all a dream?"
        "There’s an emptiness in your chest. A tightness, that’s unfamiliar."
        "You check your pockets, and they are empty. Your money is gone. And maybe something else is too?"
        "You lose."

        return

    label becomeWorker:
        scene bg window2
        "You pull up to the window, your payment already in hand. But as you sit there, the window never opens. You wait, and wait, to no avail. Maybe you should knock?
        You lean out of your car and do just that. Still nothing.
        Maybe… it couldn’t be, right? There’s got to be someone in there still?
        You knock harder, more frantically."
        y "Hello? Can I please have my order?"
        "Silence."
        y "Please? Please! Is anyone there?"
        "You find yourself begging for the annoyingly absurd worker from earlier to return, or the spooky hand. Any sign of life."
        y "…please?"
        "It looks like you won’t be getting anything else from Boiled Burgers tonight. Your partner might be disappointed, but at the moment, all you can think about is:"
        menu:  
            "The terrible service.":
                "This is, quite frankly, unbelievable. When they made such a big deal about the protocol, the “customer is always right” nonsense. But they were unable to fulfill your requests."
                "You, a paying customer! Boiled Burgers corporate would definitely be hearing about this."
                "You pull away, frustrated and ready to leave a nasty Yelp review when you get home."
                

            "That this is your fault.":
                "Maybe if you had never shown up… never kept pushing for more things… maybe none of this would’ve happened. Maybe it was all preventable. Maybe their deaths were on your hands."
                "One thing’s for sure."
                "You Lose."

        return


    #done
    return
