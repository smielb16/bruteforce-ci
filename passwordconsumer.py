import queue
import random
import string
import threading
import sys


class PasswordConsumer(threading.Thread):

    def __init__(self, queue, condition):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = condition

    def run(self):
        password = None
        while(True):
            self.condition.acquire()
            try:
                password = self.queue.get(block=False)
                self.condition.notify()
            except queue.Empty:
                self.condition.wait()

            self.condition.release()

            #todo brute force algorithm implementation
            if not password is None:
                maxLength = 3
                tries = 0
                while(True):
                    length = random.randint(1, maxLength)
                    randPassword = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase+
                                                         string.digits) for i in range(length))
                    print("Checking " + randPassword)
                    tries = tries+1
                    if password.check(randPassword):
                        print("Password " + randPassword + " found in " + str(tries) + " tries")
                        break