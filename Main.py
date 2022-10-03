import csv
from operator import itemgetter

with open('Opgaven.csv', 'r', newline='') as inputfile:
    reader = csv.reader(inputfile, delimiter=';')
    
    strings = []
    for row in reader:
        strings.append(row)
    
    # create highscores list
    highscores = [0]
    for index in range(1,6):
        highscores.append(int(strings[1][index]))
    # 1 abstract, 2 decomp, 3 pattern, 4 algo, 5 total
    
    # create number table
    numbers = []
    for row in range(2, len(strings)):
        numbers.append(list(map(int, strings[row])))
    
    mode = input('Herhalen (h) of Verdiepen (v)?')
    subject = int(input('Abstractie (1), Decompositie (2), Patroonherkenning (3), Algoritme (4) of Alles (5)?'))
    if mode != 'h' and mode != 'v' or subject not in range(1,6):
        print('Verkeerde invoer, start het programma opnieuw')
        quit()
        
    herhalen = []
    verdiepen = []
    for row in numbers:
        repeatcount = 0
        for index in range(1,6):
            if highscores[index] >= row[index]:
                repeatcount += 1
        if repeatcount == 5:
            herhalen.append(row)
        else:
            verdiepen.append(row)

    endresult = []
    if mode == 'h':
        herhalen.sort(key=itemgetter(subject))
        endresult = herhalen
    else:
        for row in verdiepen:
            totalraise = 0
            for index in range(1,5):
                row[index] -= highscores[index]
                if row[index] > 0:
                    totalraise += row[index]
            row[5] = totalraise
        if subject == 5:
            verdiepen.sort(key=itemgetter(5))
            endresult = verdiepen
        else:
            verdiepen.sort(key=itemgetter(subject))
            for row in verdiepen:
                highestraiseinrow = 0
                for index in range(1,5):
                    if row[index] > highestraiseinrow:
                        highestraiseinrow = row[index]
                if highestraiseinrow == row[subject]:
                    endresult.append(row)
        
        for row in endresult:
            originaltotal = 0
            for index in range(1,5):
                row[index] += highscores[index]
                originaltotal += row[index]
            row[5] = originaltotal

    print(endresult)
    
    with open('Result.csv', 'w', newline='') as outputfile:
        writer = csv.writer(outputfile, delimiter=';')
        for index in range(2):
            writer.writerow(strings[index])
        for row in endresult:
            writer.writerow(row)

