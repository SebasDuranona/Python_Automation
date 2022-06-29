# Rock, Paper, Scissors Game
from os import system
import random, sys, time

print ("ROCK, PAPER, SCISSORS")

#Variables to keep track of the number of wins, losses, and ties

wins = 0
losses = 0
ties = 0

while True: # Main game loop
    print ("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))

    while True: # Player input loop
        print ("Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit")
        playerMove = input()
        if playerMove == 'q':
            print ('Thank you for playing!')
            time.sleep(3)
            system('cls')
            sys.exit() # Quit the program.


        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.

        print ("Type one of (r)ock, (p)aper, (s)cissors, or (q)uit")

# Display player move

    if playerMove == 'r':
        print('ROCK versus...')
        time.sleep(1)
        print()
    elif playerMove == 'p':
        print ('PAPER versus...')
        time.sleep(1)
        print()
    elif playerMove == 's':
        print ('SCISSORS versus...')
        time.sleep(1)
        print()

# Display what the computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print ('ROCK')
        print()
        print('-'*25)
        print()
        time.sleep(0.5)
    elif randomNumber == 2:
        computerMove = 'p'
        print ('PAPER')
        print()
        print('-'*25)
        print()
        time.sleep(0.5)
    elif randomNumber == 3:
        computerMove = 's'
        print ('SCISSORS')
        print()
        print('-'*25)
        print()
        time.sleep(0.5)

# Display and record the win/loss/tie:

    if playerMove == computerMove:
        print ("It's a tie!")
        ties = ties + 1

    elif playerMove == 'r' and computerMove == 's':
        print ('You win!')
        print()
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print ('You win!')
        print()
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print ('You win!')
        print()
        wins = wins + 1

    elif playerMove == 's' and computerMove == 'r':
        print ('You lose!')
        print()
        losses = losses + 1
    elif playerMove == 'r' and computerMove == 'p':
        print ('You lose!')
        print()
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print ('You lose!')
        print()
        losses = losses + 1
