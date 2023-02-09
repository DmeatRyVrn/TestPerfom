import random
from datetime import datetime

ARRAY_SIZE = 1_000_000
ITERATION = 10


def start_test():
    print('start test')
    start_time = datetime.now()
    print(start_time)
    for iter in range(ITERATION):
        start_time_fill = datetime.now()
        #print('.................................')
        print(f'ITERATION-{iter+1}')
        print('.................................')
        print(f'fill array size {ARRAY_SIZE}')
        random_array = [random.randint(1, 1_000_000) for i in range(ARRAY_SIZE)]
        #print(random_array)
        array_fill_time = datetime.now() - start_time_fill
        print(f'fill time array {array_fill_time}')
        print('.................................')
        print(f'sort array size {ARRAY_SIZE}')
        start_time_sort = datetime.now()
        random_array.sort()
        #print(random_array)
        array_sort_time = datetime.now() - start_time_sort
        print(f'sort time array {array_sort_time}')
        print('.................................')
        print(f'iteration time {array_sort_time+array_fill_time}')
        print('*********************************')
        print()

    print('.................................')
    print(f'All time test {datetime.now() - start_time}')


if __name__ == '__main__':
    start_test()
