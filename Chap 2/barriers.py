import threading
import time
import random

barrier = threading.Barrier(3)

def baker(name):
    print(f"{name} is preparing ingredients...")
    time.sleep(random.randint(1, 3))
    print(f"{name} is ready and waiting...")
    barrier.wait()
    print(f"{name} starts baking together!")

threads = [threading.Thread(target=baker, args=(f"Baker {i+1}",)) for i in range(3)]

for t in threads:
    t.start()
for t in threads:
    t.join()
