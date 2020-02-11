import statistics

def mean():
    cat = input('Pick a category: ')
    infile = open('../data/'avocado.csv', 'r')
    raw = infile.readlines(20)
    infile.close()
    print(raw)

mean()