import threading
import time

condition = threading.Condition()
bread_ready = False

def baker():
    global bread_ready
    print("Baker is preparing bread...")
    time.sleep(3)
    with condition:
        bread_ready = True
        print("Baker: Bread is ready! Notifying customer...")
        condition.notify()

def customer():
    with condition:
        print("Customer: Waiting for bread...")
        condition.wait()
        print("Customer: Got the fresh bread!")

threading.Thread(target=baker).start()
threading.Thread(target=customer).start()
