# Write your code here :-)
import random

def coinFlipStreaks(sample, streak):
    numberOfStreaks = 0
    for experimentNumber in range(sample):


        results = []
        count = 0

        # Code that creates a list of 'heads' or 'tails' values.
        for i in range (10):
            result = random.randint(0,1)
            if result == 0:
                results.append('H')
            else:
                results.append('T')

        # Code that checks is there is a streak of 6 'heads' or 'tails' values
        for i in results:
            if i == 'H':
                count += 1
                if count == streak:
                    numberOfStreaks += 1
                    count = 0
            else:
                count = 0

        for i in results:
            if i == 'T':
                count += 1
                if count == streak:
                    numberOfStreaks += 1
                    count = 0
            else:
                count = 0

    chance = numberOfStreaks / 100
    print ('Chance of streak: ' + str(chance))

print ('Enter sample to test: ')
inputSample = input()
print ('Enter streak: ')
inputStreak = input()
coinFlipStreaks(int(inputSample), int(inputStreak))
