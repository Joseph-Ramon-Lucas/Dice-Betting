import random


money = 10

#plays as long as you have money
while money > 0:
    dice = random.randint(1, 6)
    # print("dice: ", dice)
    print("money:", money)
    deposit = int(input("deposit: "))

    #checks for negaitve
    if (deposit < 0):
        while deposit < 0:
            print("Negative money doesn't exist! You have:", money)
            deposit = int(input("deposit: "))
    #checks for wrong money
    if (deposit > money):
        while deposit > money:
            print("Insufficient funds! You have:", money)
            deposit = int(input("deposit: "))

    guess = int(input("guess: "))


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
