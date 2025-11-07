import threading
import time
import random

semaphore = threading.Semaphore(2)

def baker(name):
    print(f"{name} waiting for oven...")
    with semaphore:
        print(f"{name} using oven...")
        time.sleep(random.randint(1, 3))
        print(f"{name} done baking.")

threads = [threading.Thread(target=baker, args=(f"Baker {i+1}",)) for i in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()
