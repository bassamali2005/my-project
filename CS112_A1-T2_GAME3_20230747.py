# file name : CS_A1_T2_GAME3_20230747.PY
# descripiton of your game: The players remove a number of coins alternately , and the number is always square number and non-zero ( whoever get the last coins wins")
# my name : bassam wagdi ali
# ID : 20230747

#welcome message and display stauts
print("The Game Is Played By Two Pepole")
print(" The way of the game : The players remove a number of coins alternately , and the number is always square number and non-zero ( whoever get the last coins wins")

#the function
import random   # this function is used when the user choose the number to be random
import math     # this function is requsted when we want to use math functions

choise = str(input(" Do you want the number of bank a)random b)manually"))   #make the user choose whether he wants the number to be random or to enter it manually
while True:
    if choise == "a" :
        THE_BANK = random.randint(10,1000)
        print("THE BANK : " , THE_BANK)
        break
    elif choise == "b" :
        THE_BANK = int(input(" Please enter the number of bank"))
        while not math.sqrt(THE_BANK) % 1 == (THE_BANK):   # to make the user unable to enter a sqaure number because then whoever plays first will win
            if math.sqrt(THE_BANK) % 1 == 0:
                print(" the bank number cannot be sqaure  , enter a non-sqaure number for the bank ")
                THE_BANK = int(input("please enter the number of bank"))
            break
        break
    else:
        print(" Return your choice")    # when you enter a selection that does not exist,it will make you reselect it
        choise = str(input(" Do you want the number of bank a)random b)manually"))
        continue
while THE_BANK != 0 :
    player_one = int(input(" player 1 , enter your sqaure number ")) # First player turn
    while player_one <= THE_BANK:
        if math.sqrt(player_one) % 1 == 0 :
            THE_BANK -= player_one
            print(" THE BANK :" , THE_BANK)
            break
        else:
            while not math.sqrt(player_one) %1 ==0 :  # if the number is not sqaure. have him re-enter a sqaure number
                print(" invalid number , enter sqaure number")
                player_one = int(input(" player 1 , enter your sqaure number"))
                break
    else:
        print("the number > the bank , enter correct number ")  # if the number is lager than the bank. make him re-enter smaller than the bank
        continue
    if THE_BANK == 0 :   # when the first player takes the last coins
        print(" player 1 is winner")   # he wins
        break
    player_two = int(input(" player 2 , enter your sqaure number"))   # the second player turn
    while player_two <= THE_BANK :
        if math.sqrt(player_two) % 1 == 0 :
            THE_BANK -= player_two
            print(" THE BANK :" , THE_BANK)
            break
        else:
            while not math.sqrt(player_two) % 1 ==0:   # if the number is not sqaure. have him re-enter a sqaure number
                print(" invalid number , enter sqaure number")
                player_two = int(input(" player 2 , enter your sqaure number"))
                continue
    else:
        print(" the number > the bank")
        player_two = int(input(" player 2 , enter your sqaure number"))
        THE_BANK -= player_two
        print(" The bank :" , THE_BANK)
        while not math.sqrt(player_two) % 1 == 0 :
            print("invalid number , enter your sqaure number")
            player_two = int(input(" player 2 , enter your sqaure number"))
            break
        continue
    if THE_BANK == 0 : # when the second player takes the last coins
        print(" player 2 is winner")  # he wins