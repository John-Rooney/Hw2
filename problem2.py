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
    infile.close()
    return rawLst

def strLst(cat):
    """Creates list of str numbers for given variable"""
    dict = {'Average Price': 2, 'Total Volume': 3, '4046': 4, '4225': 5, '4770': 6, 'Total Bags': 7, 'Small Bags': 8, 'Large Bags': 9, 'XLarge Bags': 10}
    rawLst = makeLst()
    strVolLst = []
    offset = dict[cat]
    while offset < len(rawLst):
        strVolLst.append(rawLst[offset])
        offset += 13
    return strVolLst

def intLst(cat):
    """Creates list of int numbers for given variable"""
    strVolLst = strLst(cat)
    numVolLst = []
    for i in range(1, len(strVolLst)):
        numVolLst.append(float(strVolLst[i]))
    return numVolLst

def readAndComputeMean_SM(cat):
    """Computes mean of selected variable in avocado.csv"""
    numVolLst = intLst(cat)
    mean_SM = round(statistics.mean(numVolLst), 2)
    return mean_SM

readAndComputeMean_SM('4046')

def readAndComputeSD_SM(cat):
    """Computes sample standard deviation of selected variable in avocado.csv"""
    numVolLst = intLst(cat)
    sd_SM = round(statistics.stdev(numVolLst), 2)
    return sd_SM

def readAndComputeMedian_SM(cat):
    """Computes median of selected variable in avocado.csv"""
    numVolLst = intLst(cat)
    median_SM = round(statistics.median(numVolLst), 2)
    return median_SM

def readAndComputeMean_HG(cat):
    """Returns mean without using statistics module"""
    lst = intLst(cat)
    total = sum(lst)
    n = len(lst)
    mean_HG = round((total / n), 2)
    return lst, mean_HG

def readAndComputeSD_HG(cat):
    """Returns sample standard deviation without using statistics module"""
    lst, mean_HG = readAndComputeMean_HG(cat)
    n = len(lst) - 1
    tempSum = 0
    for i in lst:
        tempSum += (i - mean_HG)**2
    sd_HG = round(((tempSum / n)**0.5), 2)
    return sd_HG

def readAndComputeMedian_HG(cat):
    """Returns median without using statistics module"""
    lst = sorted(intLst(cat))
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
        return median_HG

def readAndComputeMean_MML(cat):
    """Returns mean of given category only holding one value in memory at a time"""
    folder = Path('data/')
    file = folder / 'avocado.csv'
    offset = {'Average Price': 2, 'Total Volume': 3, '4046': 4, '4225': 5, '4770': 6, 'Total Bags': 7, 'Small Bags': 8, 'Large Bags': 9, 'XLarge Bags': 10}
    n = 0
    total = 0
    infile = open(file, 'r')
    for i in infile:
        raw = i.split(',')
        strNum = raw[offset[cat]]
        try:
            num = float(strNum)
            total += num
            n += 1
        except:
            continue
    infile.close()
    mean_MML = round(total/n, 2)
    return mean_MML

def readAndComputeSD_MML(cat):
    """Returns sample standard deviation of given category only holding one value in memory at a time"""
    folder = Path('data/')
    file = folder / 'avocado.csv'
    offset = {'Average Price': 2, 'Total Volume': 3, '4046': 4, '4225': 5, '4770': 6, 'Total Bags': 7, 'Small Bags': 8, 'Large Bags': 9, 'XLarge Bags': 10}
    mean = readAndComputeMean_MML(cat)
    n = 0
    total = 0
    infile = open(file, 'r')
    for i in infile:
        raw = i.split(',')
        strNum = raw[offset[cat]]
        try:
            num = float(strNum)
            total += (num - mean)**2
            n += 1
        except:
            continue
    infile.close()
    sd_MML = round((total / (n - 1)) ** 0.5, 2)
    return sd_MML

def readAndComputeMedian_MML(cat):
    """Returns median of given category only holding one value in memory at a time"""
    folder = Path('data/')
    file = folder / 'avocados.csv'
    offset = {'Average Price': 2, 'Total Volume': 3, '4046': 4, '4225': 5, '4770': 6, 'Total Bags': 7, 'Small Bags': 8, 'Large Bags': 9, 'XLarge Bags': 10}
    n = -1
    infile = open(file, 'r')
    srtLst = []
    for i in infile:
        n += 1

    infile.close()
    infile = open(file, 'r')
    midValue = int(n - 1) / 2
    count = -1
    for i in infile:
        if count == midValue:
            raw = i.split(',')
            strNum = raw[offset[cat]]
            median_MML = float(strNum)
            count += 1
        else:
            count += 1

    print(median_MML)
#readAndComputeMedian_MML('Total Volume')

