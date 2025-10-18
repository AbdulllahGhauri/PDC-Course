import multiprocessing

# Function to calculate partial sum
def calculate_partial_sum(start, end, results, index):
    total = sum(range(start, end + 1))
    results[index] = total

def run_processes(num_processes, N):
    print(f"\nRunning with {num_processes} Processes...")
    manager = multiprocessing.Manager()
    results = manager.list([0] * num_processes)
    processes = []
    step = N // num_processes

    # Create processes
    for i in range(num_processes):
        start = i * step + 1
        end = (i + 1) * step if i != num_processes - 1 else N
        p = multiprocessing.Process(target=calculate_partial_sum, args=(start, end, results, i))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print(f"Total sum using {num_processes} processes: {sum(results)}")

if __name__ == "__main__":
    N = 1000000  # range of numbers to sum
    run_processes(5, N)
    run_processes(10, N)
    run_processes(15, N)
