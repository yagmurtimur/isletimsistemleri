import threading
from multiprocessing import Process
import os
import time

def thread_fonk():
    print("Thread çalışıyor")
    time.sleep(1)

def process_fonk():
    print("Process ID:", os.getpid())
    time.sleep(1)

t1 = threading.Thread(target=thread_fonk)
t2 = threading.Thread(target=thread_fonk)

t1.start()
t2.start()

t1.join()
t2.join()

p1 = Process(target=process_fonk)
p2 = Process(target=process_fonk)

p1.start()
p2.start()

p1.join()
p2.join()
