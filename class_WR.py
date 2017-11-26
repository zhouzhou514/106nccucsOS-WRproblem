#writer and reader
import random

class events:
    counter=0
    def __init__(self,type,delay,time):
        self.id=events.counter
        self.type=type      #reader=0 writer=1
        self.delay=random.randint(1,delay)
        self.time=random.randint(1,delay)
        events.counter+=1

    def showid(self):
        return self.id

    def showtype(self):
        return self.type

    def showdelay(self):
        return self.delay

    def showtime(self):
        return self.time

