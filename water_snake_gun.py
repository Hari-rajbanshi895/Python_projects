import random

user_wins = 0
computer_wins = 0

options = ['gun','water','snake']



while True:
    user_input = input('Enter gun/water/snake or Q to quit: ').lower()
    if user_input == "q":
            break
    
    if user_input not in options:
          continue
    
    random_number = random.randint(0,2)
    # gun:0, water:1, snake:2
    computer_pick = options[random_number]
    print('computer picked', computer_pick +'.')

    if user_input == "gun" and computer_pick == "snake":
          print('You won!')
          user_wins += 1
          
        
    elif user_input == "snake" and computer_pick == "water":
          print('You won!')
          user_wins += 1
          
    
    elif user_input == "water" and computer_pick == "gun":
          print('You won!')
          user_wins += 1
          
    else:
          print('You lose!')
          computer_wins += 1

print('You scored',user_wins,'times.')
print('computer scored',computer_wins,'times.')  
print('Goodbye!')    

    
    
