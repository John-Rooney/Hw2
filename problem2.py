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

def strLst():
    """Creates list of str numbers for given variable"""
    cat = input('Pick a category: ')
    dict = {'Average Price': 2, 'Total Volume': 3, 'Total Bags': 7, 'Small Bags': 8, 'Large Bags': 9, 'XLarge Bags': 10}
    rawLst = makeLst()
    strVolLst = []
    offset = dict[cat]
    while offset < len(rawLst):
        strVolLst.append(rawLst[offset])
        offset += 13
    return strVolLst

def intLst():
    """Creates list of int numbers for given variable"""
    strVolLst = strLst()
    numVolLst = []
    for i in range(1, len(strVolLst)):
        numVolLst.append(float(strVolLst[i]))
    return numVolLst

def readAndComputeMean_SM():
    """Computes mean of selected variable in avocado.csv"""
    numVolLst = intLst()
    return round(statistics.mean(numVolLst), 2)

def readAndComputeSD_SM():
    """Computes standard deviation of selected variable in avocado.csv"""
    numVolLst = intLst()
    return round(statistics.stdev(numVolLst), 2)


def readAndComputeMedian_SM():
    """Computes median of selected variable in avocado.csv"""
    numVolLst = intLst()
    return round(statistics.median(numVolLst), 2)