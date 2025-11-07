import threading
import time

oven_ready = threading.Event()

def oven():
    print("Oven: Heating up...")
    time.sleep(3)
    oven_ready.set()
    print("Oven: Ready for baking!")

def baker(name):
    print(f"{name} waiting for oven...")
    oven_ready.wait()
    print(f"{name} starts baking now!")

threading.Thread(target=oven).start()
for i in range(3):
    threading.Thread(target=baker, args=(f"Baker {i+1}",)).start()
