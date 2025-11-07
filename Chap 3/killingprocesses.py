import multiprocessing
import time
import os

def worker():
    print(f"Worker process started with PID: {os.getpid()}")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker)
    p.start()
    time.sleep(3)
    print("Terminating process...")
    p.terminate()     # kills the process
    p.join()
    print("Process terminated.")
