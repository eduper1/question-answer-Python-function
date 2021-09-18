#abdullahi, 10, kenya

# This function is to ask the user wether to play or not?
def is_playing():
    # Know what the user want by asking
    will_play = input("Do you want to play? ")
    # store "yes" value in play variable
    play = "yes"
    
    # Compare the will_play variable to play
    # if True, show " let play!!!"
    if will_play == play:
        print("les tart to play!!!!!!.")
    else:
        print("you are done!!!!")
        quit()
