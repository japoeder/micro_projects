from threading import Thread, Lock


class Fork:
    # add a lock as an instance variable
    def __init__(self):
        self.lock = Lock()

    # return True if you can acquire self.lock, False otherwise
    def acquire_fork(self):
        if self.lock.acquire():
            return True
        else:
            return False

    # release lock
    def release_fork(self):
        self.lock.release()

