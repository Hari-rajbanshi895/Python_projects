playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()
score = 0
answer = input("What CPU stands for? ")
if answer == 'central processing unit':
    print('correct!')
    score += 1
else:
    print('incorrect')

answer = input("What GPU stands for? ")
if answer == 'graphic processing unit':
    print('correct!')
    score += 1
else:
    print('incorrect')

answer = input("What HTML stands for? ")
if answer == 'hyper text markup language':
    print('correct!')
    score += 1
else:
    print('incorrect')

print('You have ' + str(score) + " correct ")
print('you have '+ str((score/3)*100) + '%')