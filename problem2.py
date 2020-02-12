import statistics
from pathlib import Path

def makeLst():
    """Makes list of values out of avocado.csv"""
    folder = Path('data/')
    file = folder / 'avocado.csv'
    infile = open(file, 'r')
    raw = infile.read()
    infile.close()
    rawLst = raw.split(',')
    return rawLst

def readAndComputeMean_SM():
    """Computes mean of selected variable in avocado.csv"""
    rawLst = makeLst()
    cat = input('Pick a category: ')

    dict = {'Average Price': 2, 'Total Volume': 3, 'Total Bags': 7, 'Small Bags': 8, 'Large Bags': 9, 'XLarge Bags': 10}

    # Creates list of str numbers for given variable
    strVolLst = []
    count = dict[cat]
    while count < len(rawLst):
        strVolLst.append(rawLst[count])
        count += 13

    # Creates list of int numbers for given variable
    numVolLst = []
    for i in range(1, len(strVolLst)):
        numVolLst.append(float(strVolLst[i]))

    return round(statistics.mean(numVolLst), 2)

def readAndComputeSD_SM():
    """Computes standard deviation of selected variable in avocado.csv"""
    rawLst = makeLst()
    cat = input('Pick a category: ')

    dict = {'Average Price': 2, 'Total Volume': 3, 'Total Bags': 7, 'Small Bags': 8, 'Large Bags': 9, 'XLarge Bags': 10}

    # Creates list of str numbers for given variable
    strVolLst = []
    count = dict[cat]
    while count < len(rawLst):
        strVolLst.append(rawLst[count])
        count += 13

    # Creates list of int numbers for given variable
    numVolLst = []
    for i in range(1, len(strVolLst)):
        numVolLst.append(float(strVolLst[i]))

    return round(statistics.stdev(numVolLst), 2)

def readAndComputeMedian_SM():
    """Computes median of selected variable in avocado.csv"""
    rawLst = makeLst()
    cat = input('Pick a category: ')

    dict = {'Average Price': 2, 'Total Volume': 3, 'Total Bags': 7, 'Small Bags': 8, 'Large Bags': 9, 'XLarge Bags': 10}

    # Creates list of str numbers for given variable
    strVolLst = []
    count = dict[cat]
    while count < len(rawLst):
        strVolLst.append(rawLst[count])
        count += 13

    # Creates list of int numbers for given variable
    numVolLst = []
    for i in range(1, len(strVolLst)):
        numVolLst.append(float(strVolLst[i]))

    return round(statistics.median(numVolLst), 2)
