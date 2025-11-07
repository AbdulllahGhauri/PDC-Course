import threading
import time

def add(a, b):
    print(f"Adding {a} + {b}")
    time.sleep(2)  # simulate delay
    print(f"Result: {a + b}")

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    time.sleep(2)
    print(f"Result: {a - b}")

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    time.sleep(2)
    print(f"Result: {a * b}")

def divide(a, b):
    print(f"Dividing {a} / {b}")
    time.sleep(2)
    print(f"Result: {a / b if b != 0 else 'Error'}")

def power(a, b):
    print(f"Power {a} ^ {b}")
    time.sleep(2)
    print(f"Result: {a ** b}")

if __name__ == "__main__":
    start_time = time.time()
    print("=== THREADING CALCULATOR ===")

    t1 = threading.Thread(target=add, args=(5, 3))
    t2 = threading.Thread(target=subtract, args=(10, 4))
    t3 = threading.Thread(target=multiply, args=(2, 8))
    t4 = threading.Thread(target=divide, args=(9, 3))
    t5 = threading.Thread(target=power, args=(2, 5))

    for t in [t1, t2, t3, t4, t5]:
        t.start()

    for t in [t1, t2, t3, t4, t5]:
        t.join()

    print(f"Total Time Taken: {time.time() - start_time:.2f} seconds")
