import statistics
from pathlib import Path

def mean():
    cat = input('Pick a category: ')
    folder = Path('data/')
    file = folder / 'avocado.csv'
    infile = open(file, 'r')
    raw = infile.read(5000)
    infile.close()
    rawLst = raw.split(',')

    strVolLst = []
    count = 3
    while count < 100:
        strVolLst.append(rawLst[count])
        count += 13

    numVolLst = []
    count2 = 1
    while count2 < len(strVolLst):
        numVolLst.append(float(strVolLst[count2]))
        count += 1
    print(numVolLst)

mean()