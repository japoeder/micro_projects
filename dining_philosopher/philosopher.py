import random
import threading
import time
from fork import Fork


class Philosopher(threading.Thread):
    running = True

    # initialize a Philosophers name, left fork, and right fork
    def __init__(self, name: str, left_fork: Fork, right_fork: Fork):
        # call ‘threading’ superclass constructor
        super().__init__()
        # initialize ‘name’ instance variable
        self.name = name
        # initialize ‘left_fork’ instance variable
        self.left_fork = left_fork
        # initialize ‘right_fork’ instance variable
        self.right_fork = right_fork
        return

    # run() is called by thread’s start() method; starts the thread running
    def run(self):
        while self.running:
            # call think()
            Philosopher.think(self)
            # call eat()
            Philosopher.eat(self)
            # print <Philosopher name> is cleaning up.
            print(f"{self.name} is cleaning up")
        return

    # make philosopher think for a random number of seconds until hungry
    def think(self):
        # ‘thinking’ = random number of seconds between 3 and 5 using random.uniform()
        thinking = random.uniform(3, 5)
        # print <Philosopher name> is thinking for ‘thinking’ seconds.
        print(f"{self.name} is thinking for {thinking} seconds")
        # sleep for ‘thinking’ seconds
        time.sleep(thinking)
        # print <Philosopher name> is now hungry.
        print(f"{self.name} is now hungry")
        return

    # make philosopher eat for a random number of seconds until thinking again
    def eat(self):
        # try to acquire left fork
        if self.left_fork.acquire_fork():
            # if successful, try to acquire right fork
            if self.right_fork.acquire_fork():
                # if successful ‘eating’ = random num of seconds between 3 and 5 using random.uniform()
                eating = random.uniform(3, 5)

                # print <Philosopher name> is eating for ‘eating’ seconds.
                print(f"{self.name} is eating for {eating} seconds")

                # sleep for ‘eating’ seconds
                time.sleep(eating)

                # release right fork
                self.right_fork.release_fork()

                # print <Philosopher name> has put down his right fork.
                print(f"{self.name} has put down his right fork")

                # release left fork
                self.left_fork.release_fork()

                # print <Philosopher name> has put down his left fork.
                print(f"{self.name} has put down his left fork")

            else:

                return

        else:

            return
