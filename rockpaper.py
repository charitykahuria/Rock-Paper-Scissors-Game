import random 

rock = ('\U0001f44a') 
paper = ('\U0001faf3') 
scissors = ('\u2702\uFE0F') 
# print(rock,paper,scissors)

game_avatar = [rock,paper,scissors]
human_player = int(input("Please type: 0 for rock, 1 for  paper, 2 for scissors.\n"))

if  human_player >= 3 or human_player<0:
    print("Invalid Response, You lose '\U0001f644'")
else:
    print('You:',game_avatar[human_player])
    
    computer_response = random.randint(0,2)
    print('computer_response',game_avatar[computer_response])


    if human_player == 0 and computer_response == 2:
        print( "You won '\U0001f973'")
    elif computer_response ==0 and human_player ==2:
        print('you lose "\U0001f622"')
    elif human_player > computer_response:
        print( "You won '\U0001f973'")
    elif computer_response > human_player:
        print('you lose "\U0001f622"')
    elif human_player == computer_response:
        print ("Ops! it's a tie '\U0001f91d' ")



