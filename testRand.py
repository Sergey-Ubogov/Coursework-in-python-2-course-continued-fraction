import random
from concurrent import futures
import matplotlib.pyplot as plt

def counter (size):
    group=[]
    for i in range(size + 1):
        rnd = random.randint(1,size)
        group.append(rnd)
    return group

def tester(size):
    executor = futures.ThreadPoolExecutor(max_workers=50000)
    future = executor.submit(counter, size)
    executor.shutdown(wait=True)
    return future.result()

if __name__ == '__main__':
    res = tester(99)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    for i in range(len(res[::2])):
        plt.scatter(res[::2][i], res[1::2][i])
    plt.savefig('ExAmPlE.png', fmt='png')
