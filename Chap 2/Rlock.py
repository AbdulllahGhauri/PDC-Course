import threading
import time

rlock = threading.RLock()

def bake_step():
    with rlock:
        print("Step 1: Mixing ingredients")
        time.sleep(1)
        with rlock:
            print("Step 2: Baking the bread")
            time.sleep(1)
    print("Bread ready!")

threading.Thread(target=bake_step).start()
