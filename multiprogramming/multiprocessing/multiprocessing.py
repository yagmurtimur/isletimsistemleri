from multiprocessing import Process
import os
import time

def calis():
    print("Process ID:", os.getpid())
    time.sleep(2)

if __name__ == "__main__":
    p1 = Process(target=calis)
    p2 = Process(target=calis)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
