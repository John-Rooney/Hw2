
def stemandleaf():
    '''Prints stem and leaf plot from .txt file'''
    print('Hello!')
    num = str(input('Select 1, 2, or 3: '))
    while num != '':
        dict = {'1': 'stemAndLeaf1.txt', '2': 'stemAndLeaf2.txt', '3': 'stemAndLeaf3.txt'}

        infile = open('../data/' + dict[num], 'r')
        raw = infile.read()
        infile.close()
        rawSplit = raw.split()

        lstNums = []
        for i in rawSplit:
            lstNums.append(int(i))
        sortNums = sorted(lstNums)

        stringNums = []
        for i in sortNums:
            stringNums.append(str(i))

        '''creates dictionary; key = everything up to last digit, value = last digit'''
        nums = {}
        for i in stringNums:
            if i[:-1] not in nums.keys():
                nums[i[:-1]] = i[-1] + ' '
            else:
                nums[i[:-1]] += i[-1] + ' '

        print()
        print('Stem and Leaf Plot ' + num)
        for i in nums:
            print('{:3}| {}'.format(i, nums[i]))
        print()
        num = input('Select 1, 2, or 3: ')
    else:
        print('Thanks, Come Again')
    return


stemandleaf()
