import random

startingMoney = 100
highscore = startingMoney
money = startingMoney
print("\nWelcome to Dice Betting! Play as long as you have money!\n")



#plays as long as you have money
while money > 0:
    dice = random.randint(1, 6)
    # print("dice: ", dice)
    print("\nmoney:", money)
    deposit = 0
    
    # validate deposit
    while (deposit <= 0):
        try:
            deposit = int(input("deposit: "))
            
            #checks for overdraft
            if (deposit > money):
                    print("Insufficient funds! You have:", money, "to spend\n")
                    deposit = 0

        except:
            print("amount entered was not an integer bigger than 0")
  
    # validate guess
    guess = 0
    while (guess <= 0):
        try:    
            guess = int(input("guess: "))
            if (guess < 1 or guess > 6):
                print("Can only guess an integer between 1-6")
                guess = 0
        except:           
                print("amount entered was not an integer bigger than 0")


    # high score calculation
    if money > highscore:
        highscore = money


    # win/lose calculation
    if (guess == dice):
        winnings = deposit*2
        money += winnings
        print("Dice rolled a", dice)
        print("You earned:", winnings)
    else:
        money -= deposit
        print("Dice rolled a", dice)
        print("You lost:", deposit)

print("You lose :(")
print("Your highest money was:", highscore)
