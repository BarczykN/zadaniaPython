import multiprocessing as mp
import numpy as np
import time


a = np.random.randint(0, 10, size=[2000, 2000])


def count_histogram(data,arg):
    result = {}
    for i in data:
        result[i] = result.get(i, 0) + 1
    return result


def main():
    data = a.tolist()
    with mp.Pool(mp.cpu_count()) as pool:
        print(mp.cpu_count())
        t = time.time()
        result = [pool.apply_async(count_histogram, args=(row,1)) for row in data]
        print("Time multicore: "+str(time.time() - t))


    t = time.time()
    result = []
    for row in data:
        result.append(count_histogram(row, 1))
    print("Time single: " + str(time.time() - t))



    print(result)


if __name__ == '__main__':
    main()