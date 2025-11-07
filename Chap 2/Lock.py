import threading
import time
import random

oven_lock = threading.Lock()

def bake(baker_name):
    print(f"{baker_name} is waiting to use the oven...")
    with oven_lock:
        print(f"{baker_name} is now baking 🍞...")
        time.sleep(random.uniform(1, 2))
        print(f"{baker_name} has finished baking ✅")
    print(f"{baker_name} left the oven.\n")

if __name__ == "__main__":
    bakers = [threading.Thread(target=bake, args=(f"Baker {i+1}",)) for i in range(3)]
    for baker in bakers:
        baker.start()
    for baker in bakers:
        baker.join()
    print("👨‍🍳 All bakers are done baking!")
