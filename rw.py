
import threading
import random
import time
import copy
TIME_DIVISOR=1000

class RWLock:
	
	def __init__(self):
		self.__read_switch = _LightSwitch()
		self.__write_switch = _LightSwitch()
		self.__no_readers = threading.Lock()
		self.__no_writers = threading.Lock()
		self.__readers_queue = threading.Lock()
		"""A lock giving an even higher priority to the writer in certain
		cases """
	
	def reader_acquire(self):
		self.__readers_queue.acquire()
		self.__no_readers.acquire()
		self.__read_switch.acquire(self.__no_writers)
		self.__no_readers.release()
		self.__readers_queue.release()
	
	def reader_release(self):
		self.__read_switch.release(self.__no_writers)
	
	def writer_acquire(self):
		self.__write_switch.acquire(self.__no_readers)
		self.__no_writers.acquire()
	
	def writer_release(self):
		self.__no_writers.release()
		self.__write_switch.release(self.__no_readers)
	

class _LightSwitch:
	"""The first thread turns on the switch, the last one turns it off ."""
	def __init__(self):
		self.__counter = 0
		self.__mutex = threading.Lock()
	
	def acquire(self, lock):
		self.__mutex.acquire()
		self.__counter += 1
		if self.__counter == 1:
			lock.acquire()
		self.__mutex.release()

	def release(self, lock):
		self.__mutex.acquire()
		self.__counter -= 1
		if self.__counter == 0:
			lock.release()
		self.__mutex.release()


class Writer(threading.Thread):

	def __init__(self, rw_lock,sleeptime,exctime,id):
		threading.Thread.__init__(self)
		#self.__buffer = buffer_
		self.__rw_lock = rw_lock
		self.__init_sleep_time = float(sleeptime)/TIME_DIVISOR
		self.__excution_time = float(exctime)/TIME_DIVISOR
		self.id=id

		#self.__to_write = to_write
		self.entry_time = None
		"""Time of entry to the critical section"""
		self.exit_time = None
		"""Time of exit from the critical section"""

		print('Writer:', self.id, 'is created',self.__init_sleep_time,self.__excution_time)

		
	def run(self):
		time.sleep(self.__init_sleep_time)
		self.__rw_lock.writer_acquire()
		self.entry_time = time.time()
		time.sleep(self.__excution_time)
		#self.__buffer.append(self.__to_write)
		self.exit_time = time.time()
		self.__rw_lock.writer_release()

class Reader(threading.Thread):


	def __init__(self,rw_lock,sleeptime,exctime,id)
  threading.Thread.__init__(self)
		#self.__buffer = buffer_
		self.__rw_lock = rw_lock
		self.__init_sleep_time = float(sleeptime)/TIME_DIVISOR
		self.__excution_time= float(exctime)/TIME_DIVISOR
		self.id=id
		self.buffer_read = None
		"""a copy of a the buffer read while in critical section"""	
		self.entry_time = None
		"""Time of entry to the critical section"""
		self.exit_time = None
		"""Time of exit from the critical section"""
		print('Reader:', self.id, 'is created', self.__init_sleep_time, self.__excution_time)


	def run(self):
		time.sleep(self.__init_sleep_time)
		self.__rw_lock.reader_acquire()
		self.entry_time = time.time()
    #print"reader"
		time.sleep(self.__excution_time)
		#self.buffer_read = copy.deepcopy(self.__buffer)
		self.exit_time = time.time()
		self.__rw_lock.reader_release()

