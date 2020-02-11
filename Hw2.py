
def stemandleaf():
    print('Hello!')
    num = eval(input('Select 1, 2, or 3: '))
    while num not in [1, 2, 3]:
        num = eval(input('Select 1, 2, or 3: '))

    dict = {1: 'stemAndLeaf1.txt', 2: 'stemAndLeaf2.txt', 3: 'stemAndLeaf3.txt'}

    infile = open('../data/' + dict[num], 'r')
    raw = infile.read()
    infile.close()
    rawSplit = raw.split()
    rawLst = []
    for i in rawSplit:
        rawLst.append(int(i))

    lst = sorted(rawLst)


stemandleaf()
