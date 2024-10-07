
# Put any import statements here
import random as r

# while loop 
def game_function():
    # variable
    done = False
    low = 1
    high = 100
    guesses = 5
    valid_ans = False
    wins = 0
    losses = 0
    while not done:

        # Example menu - feel free to change this
        print( "{:^40}".format( "GUESS MY NUMBER") )
        print( "----------------------------------------" )
        print( "Game stats: \033[1;32m{}\033[0m won and \033[1;31m{}\033[0m lost".format(wins, losses) )
        print( "----------------------------------------" )
        print( " 1. Play game" )
        print( " 2. Change low number ({})".format( low ) )
        print( " 3. Change high number ({})".format( high ) )
        print( " 4. Change number of guesses ({})".format( guesses ) )
        print( "----------------------------------------" )
        print( " X. Exit" )
        print( "----------------------------------------" )
        
        menu = input( "Selection: " )
        menu = menu.lower()
        valid_ans = False
        # Check for valid input
        
        
        while not valid_ans:
            # Check for x
            if str(menu) == "x":
                print("\nThanks for playing")
                valid_ans = True
                done = True
            
            # Check for numbers
            elif menu.isdigit():
            
                # Check for numbers 1-4
                if int(menu) == 1 or int(menu) == 2 or int(menu) == 3 or int(menu) == 4:
                    valid_ans = True
            
                # New Attempt
                else:
                    menu = input( "Invalid Option. Try Again: " )
                    menu = menu.lower()
                
            # New Attempt
            else:
                menu = input( "Invalid Option. Try Again: " )
                menu = menu.lower()
    
        if menu.isdigit():
            # Change Low Number
            if int(menu) == 2:
                low = input("Enter new low num: ")
            
                # Digit Check
                while not low.isdigit(): # check if string contains a number
                    low = input("Not a number. Try again: ")
                
                # Lower than high
                while int(low) >= int(high):
                    low = input("must be smaller than {}. Try again: ".format(high))
                
                # Digit Check
                while not low.isdigit(): # check if string contains a number
                        low = input("Not a number. Try again: ")
                
            low = int(low)
        
            # Change High Number
            if int(menu) == 3:
                high = input("Enter new high num: ")
            
                # Digit Check
                while not high.isdigit(): # check if string contains a number
                    high = input("Not a number. Try again: ")
            
                # Higher than low
                while int(low) >= int(high):
                    high = input("must be larger than {}. Try again: ".format(low))
                
                    # Digit Check
                    while not high.isdigit(): # check if string contains a number
                        high = input("Not a number. Try again: ")
                
                high = int(high)
            
            # Change Number of Guesses
            if int(menu) == 4:
                guesses = input("Enter new guesses num: ")
            
                # Digit Check
                while not guesses.isdigit(): # check if string contains a number
                    guesses = input("Not a number. Try again: ")
                
                guesses = int(guesses)
        
            # Play Game
            if int(menu) == 1:
                print("\nGuess a number between", low ,"and", high)
                print("You have", guesses, "guesses left")
       
                #Create random int
                answer = r.randint( low, high)
            
                # Ask for guess
                gnum= input("\nEnter guess:")
            
                #Digit Check
                while not gnum.isdigit(): # check if string contains a number
                    gnum = input("Not a number. Try again: ")
                
                # Convert gnum to int
                gnum = int(gnum)
            
                # Attempt tracker
                attempts=1
       
                while int(gnum) != answer and attempts <guesses:
                
                    #Check for lower
                    if gnum > answer:
                        print("Wrong answer. Try lower\nYou have", (guesses-attempts), "guesses left\n")
                    
                    #Check for higher
                    if gnum < answer:
                        print("Wrong answer. Try higher\nYou have", (guesses-attempts), "guesses left\n")
                
                    # Ask for answer
                    gnum = input ("Enter guess:")
    
                    #Digit Check
                    while not gnum.isdigit(): # check if string contains a number
                        gnum = input("Not a number. Try again: ")
                    gnum = int(gnum)
                
                    #Attempts tracker
                    attempts+=1
            
                #Check for lower
                if gnum > answer:
                    print("Wrong answer. Try lower\nSorry you lost. The number was",answer,".\n")
                    losses+=1
                
                #Check for higher
                if gnum < answer:
                    print("Wrong answer. Try higher\nSorry you lost. The number was",answer,".\n")
                    losses+=1
                
                #Check to see if won
                if gnum==answer:
                    print("Yes, the number was",answer, "you won in",attempts,"guesses.\n")
                    wins+=1
                
                    #Celebration
                    for i in range(0,3):
                        print("\033[1;32mWinner!!\033[0m")
                
        print(" ")
        
if __name__ == "__main__":
    game_function()