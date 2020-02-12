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
    print(raw[:2000])
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
    mean_SM = round(statistics.mean(numVolLst), 2)
    return mean_SM

def readAndComputeSD_SM():
    """Computes sample standard deviation of selected variable in avocado.csv"""
    numVolLst = intLst()
    sd_SM = round(statistics.stdev(numVolLst), 2)
    return sd_SM

def readAndComputeMedian_SM():
    """Computes median of selected variable in avocado.csv"""
    numVolLst = intLst()
    median_SM = round(statistics.median(numVolLst), 2)
    return median_SM

def readAndComputeMean_HG():
    """Returns mean without using statistics module"""
    lst = intLst()
    total = sum(lst)
    n = len(lst)
    mean_HG = round((total / n), 2)
    return lst, mean_HG

def readAndComputeSD_HG():
    """Returns sample standard deviation without using statistics module"""
    lst, mean_HG = readAndComputeMean_HG()
    n = len(lst) - 1
    tempSum = 0
    for i in lst:
        tempSum += (i - mean_HG)**2
    sd_HG = round(((tempSum / n)**0.5), 2)
    return sd_HG

def readAndComputeMedian_HG():
    """Returns median without using statistics module"""
    lst = sorted(intLst())
    # if len(lst) is even
    if len(lst) % 2 == 0:
        cut = int(len(lst) / 2)
        midValues = lst[cut-1:-(cut-1)]
        median_HG = sum(midValues)/2
        return median_HG
    # if len(lst) is odd
    else:
        midValue = int((len(lst) - 1) / 2)
        median_HG = lst[midValue]
        print(median_HG)
        return median_HG

def readAndComputeMean_MML():
    folder = Path('data/')
    file = folder / 'avocados.csv'
    infile = open(file, 'r')
    for i in infile:
        print(i)

readAndComputeMean_MML()
