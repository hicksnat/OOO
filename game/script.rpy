# The script of the game goes in this file.


#Fastfood worker character
define w = Character("Worker", color = "#FF0000")


# The game starts here.

label start:

    
    #Show car
    scene bg car




    # Begining dialog

    "Insert what main character is thinking at the start here."

    "Insert goal here."

    scene bg window1
    



    w "Welcome to {name}"

    w "Once you add a story, pictures, and music, you can release it to the world!"




    menu:

        "Yes, I do.":
            jump choice1_yes

        "No, I don't.":
            jump choice1_no

    label choice1_yes:

        $ menu_flag = True

        w "While creating a multi-path visual novel can be a bit more work, it can yield a unique experience."

        jump choice1_done

    label choice1_no:

        $ menu_flag = False

        w "Games without menus are called kinetic novels, and there are dozens of them available to play."

        jump choice1_done

    label choice1_done:

        # ... the game continues here.
 
    # This ends the game.
    #test
    return
