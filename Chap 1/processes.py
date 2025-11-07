import multiprocessing
import time

def add(a, b):
    print(f"Adding {a} + {b}")
    time.sleep(2)
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
    print("=== MULTIPROCESSING CALCULATOR ===")

    p1 = multiprocessing.Process(target=add, args=(5, 3))
    p2 = multiprocessing.Process(target=subtract, args=(10, 4))
    p3 = multiprocessing.Process(target=multiply, args=(2, 8))
    p4 = multiprocessing.Process(target=divide, args=(9, 3))
    p5 = multiprocessing.Process(target=power, args=(2, 5))

    for p in [p1, p2, p3, p4, p5]:
        p.start()

    for p in [p1, p2, p3, p4, p5]:
        p.join()

    print(f"Total Time Taken: {time.time() - start_time:.2f} seconds")
