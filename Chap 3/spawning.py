from multiprocessing import Process

def task(name):
    print(f"Process {name} is running")

if __name__ == "__main__":
    processes = []
    for i in range(3):
        p = Process(target=task, args=(f"P{i+1}",))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
