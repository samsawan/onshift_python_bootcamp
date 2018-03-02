from random import randrange
# Sample iterators

x = iter([8, 6, 7, 5, 3, 0, 9])
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()


# Build your own iterator
class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            self.i += 1
            return self.i - 1
        else:
            raise StopIteration()

# Sample generator used by Ilya in a past bootcamp session


file_name = './sample_data.csv'

with open(file_name, 'w') as out_file:
    for i in range(0, 10000):
        out_list = [randrange(9999) for _ in range(0, 100)]
        out_file.write(','.join([str(i) for i in out_list]) + '\n')


def csv_file_generator ( fname ):
    with open(fname, 'r') as in_file:
        line = True
        while line:
            line = in_file.readline()
            if line:
                yield [int(i) for i in line.split(',')]


for ln_list in csv_file_generator(file_name):
    print(ln_list)
