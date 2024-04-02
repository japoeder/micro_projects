import time
import sys
from fork import Fork
from philosopher import Philosopher


def DiningPhilosophers():
    # create array of 5 names: Plato, Aristotle, Buddha, Marx, and Nietzsche
    names = ['Plato', 'Aristotle', 'Buddha', 'Marx', 'Nietzsche']

    # use a list comprehension to create 5 Fork’s
    forks_left = [Fork() for f in range(5)]
    forks_right = [forks_left[ind + 1] if ind < 4 else forks_left[0] for ind, x in enumerate(forks_left)]

    # use a list comprehension to create 5 Philosopher’s and correctly
    # assign each pair of forks to each philosopher
    p_list = [Philosopher(n,l,r) for n,l,r in zip(names, forks_left, forks_right)]

    # start all 5 Philosopher threads (should be non-blocking)
    for p in p_list:
        p.start()

    # sleep for 10 seconds
    time.sleep(10)
    # set ‘running’ to False
    running = False
    # exit all threads
    sys.exit()
    return


if __name__ == "__main__":
    DiningPhilosophers()
