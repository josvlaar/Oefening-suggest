import csv
from operator import itemgetter

# Open file
with open('Opgaven.csv', 'r', newline='') as inputfile:
    reader = csv.reader(inputfile, delimiter=';')
    
    # Create list of strings
    strings = []
    for row in reader:
        strings.append(row)
    
    # Create highscores list
    highscores = [0]
    for index in range(1,6):
        highscores.append(int(strings[1][index]))
    # 1 abstraction, 2 decomposition, 3 pattern recognition, 4 algorithm design, 5 total
    
    # Create table of numbers
    numbers = []
    for row in range(2, len(strings)):
        numbers.append(list(map(int, strings[row])))
    
    # Ask for user input
    mode = input('Herhalen (h) of Verdiepen (v)?')
    subject = int(input('Abstractie (1), Decompositie (2), Patroonherkenning (3), Algoritme (4) of Alles (5)?'))
    if mode != 'h' and mode != 'v' or subject not in range(1,6):
        print('Verkeerde invoer, start het programma opnieuw')
        quit()
    
    # Add all questions to either the repeat list of lists or the deepen list of lists
    repeat = []
    deepen = []
    for row in numbers:
        repeatcount = 0
        for index in range(1,6):
            if highscores[index] >= row[index]:
                repeatcount += 1
        if repeatcount == 5:
            repeat.append(row)
        else:
            deepen.append(row)

    endresult = []
    # Sort repeat list of lists by subject value and make it the end result
    if mode == 'h':
        repeat.sort(key=itemgetter(subject))
        endresult = repeat
    
    # Sort deepen list of lists by subject value and make it the end result
    else:
        # Calculate difference with highscores and calculate total raise
        for row in deepen:
            totalraise = 0
            for index in range(1,5):
                row[index] -= highscores[index]
                if row[index] > 0:
                    totalraise += row[index]
            row[5] = totalraise
        # If deepen on all subjects, sort by totalraise
        if subject == 5:
            deepen.sort(key=itemgetter(5))
            endresult = deepen
        # If deepen on a specific subject, see if it is the highest raise of all subjects and if so, append row to endresult
        else:
            deepen.sort(key=itemgetter(subject))
            for row in deepen:
                highestraiseinrow = 0
                for index in range(1,5):
                    if row[index] > highestraiseinrow:
                        highestraiseinrow = row[index]
                if highestraiseinrow == row[subject]:
                    endresult.append(row)
        
        # Recalculate original values in endresult table
        for row in endresult:
            originaltotal = 0
            for index in range(1,5):
                row[index] += highscores[index]
                originaltotal += row[index]
            row[5] = originaltotal

    print(endresult)
    
    # Write output to file
    with open('Result.csv', 'w', newline='') as outputfile:
        writer = csv.writer(outputfile, delimiter=';')
        for index in range(2):
            writer.writerow(strings[index])
        for row in endresult:
            writer.writerow(row)