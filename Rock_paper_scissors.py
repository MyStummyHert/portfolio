# a loop for the game to restart if the player wants.
game = True
while game:
    
    #to let the computer choose a random item.
    import random
    
    # a list of possible items.
    list = ["scissors","rock","paper"]
    #computer choice of an item(pc).
    pc  = random.choice(list)
    

    player = None

    #player chooses(player)  - from the LIST!
    while player not in list:    
        player = (input("Rock, Paper or Scissors?:")).lower()

        #what did yall choose?
    print("you: "+player)
    print("computer: "+pc)

    #who won tho?
    ##TIE option:
    if player == pc:
        print("that's a TIE!")

    #rock options:
    elif player == "rock":
        if pc == "paper":
            print("Computer WINS!")
        else:
            print("Player wins!")
            
    #paper options:
    elif player == "paper":
        if pc == "rock":
            print("Player WINS!")
        else:
            print("Computer wins!")

    #scissors options:
    elif player == "scissors":
        if pc == "rock":
            print("Computer WINS!")
        else:
            print("Player wins!")        
            
    #play again?
            
    loop = True    
    while loop:
        restart = input("play again?(Y/N): ").lower()
        if restart == "y":
            loop = False
        elif restart == "n":
            loop = False
            game = False
            
#farewell dear friend            
print( "goodbye:) ")    
    
       
        
    
