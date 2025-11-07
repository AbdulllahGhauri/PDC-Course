import threading
import queue
import time
import random

bread_queue = queue.Queue()

def baker(name):
    for i in range(3):
        bread = f"Bread {i+1} from {name}"
        time.sleep(random.uniform(0.5, 1))
        bread_queue.put(bread)
        print(f"{name} baked and added {bread} to the queue.")

def packager():
    while True:
        try:
            bread = bread_queue.get(timeout=3)
            print(f"📦 Packager packed: {bread}")
            time.sleep(0.8)
            bread_queue.task_done()
        except queue.Empty:
            break

if __name__ == "__main__":
    bakers = [threading.Thread(target=baker, args=(f"Baker {i+1}",)) for i in range(2)]
    for b in bakers:
        b.start()

    pack_thread = threading.Thread(target=packager)
    pack_thread.start()

    for b in bakers:
        b.join()
    bread_queue.join()
    print("✅ All bread has been baked and packed!")
