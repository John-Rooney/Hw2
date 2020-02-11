import statistics
print('hello')
def mean():
    cat = input('Pick a category: ')
    infile = open('../data/avacado.csv', 'r')
    raw = infile.readlines(20)
    infile.close()
    print(raw)
