import random
import numpy as np
from datetime import datetime

ARRAY_SIZE = 1_000_000
ARRAY_SIZE_NUMPY = 1_000_000_000
ITERATION = 10


def start_test():
    print('start test')
    start_time = datetime.now()
    print(start_time)
    for iter in range(ITERATION):
        start_time_fill = datetime.now()
        print(f'ITERATION-{iter+1}')
        print('.................................')
        print(f'fill array size {ARRAY_SIZE}')
        random_array = [random.randint(1, 1_000_000) for i in range(ARRAY_SIZE)]
        array_fill_time = datetime.now() - start_time_fill
        print(f'fill time array {array_fill_time}')
        print('.................................')
        print(f'sort array size {ARRAY_SIZE}')
        start_time_sort = datetime.now()
        random_array.sort()
        array_sort_time = datetime.now() - start_time_sort
        print(f'sort time array {array_sort_time}')
        print('.................................')
        print(f'iteration time {array_sort_time+array_fill_time}')
        print('*********************************')
        print()
    print('.................................')
    print(f'All time test {datetime.now() - start_time}')


def start_test_numpy():
    print('start test')
    start_time = datetime.now()
    print(start_time)
    print('.................................')
    print(f'fill array size {ARRAY_SIZE_NUMPY}')
    random_array = np.random.rand(ARRAY_SIZE_NUMPY)
    array_fill_time = datetime.now() - start_time
    print(f'fill time array {array_fill_time}')
    print('.................................')
    print(f'sort array size {ARRAY_SIZE_NUMPY}')
    start_time_sort = datetime.now()
    np.sort(random_array, kind='stable')
    array_sort_time = datetime.now() - start_time_sort
    print(f'sort time array {array_sort_time}')
    print('.................................')
    print(f'iteration time {array_sort_time+array_fill_time}')
    print('*********************************')
    print()


if __name__ == '__main__':
    run = True
    while run:
        print(
            'for test with numpy enter: 1\n'
            'for test without numpy enter: 2\n'
            'for exit type stop1'
        )
        val = input()
        if val == '1':
            start_test_numpy()
        elif val == '2':
            start_test()
        elif val == 'stop':
            run = False
        else:
            print('invalid input, try again')
