import threading

# Function to calculate partial sum
def calculate_partial_sum(start, end, results, index):
    total = sum(range(start, end + 1))
    results[index] = total

def run_threads(num_threads, N):
    print(f"\nRunning with {num_threads} Threads...")
    threads = []
    results = [0] * num_threads
    step = N // num_threads

    # Create threads
    for i in range(num_threads):
        start = i * step + 1
        end = (i + 1) * step if i != num_threads - 1 else N
        t = threading.Thread(target=calculate_partial_sum, args=(start, end, results, i))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print(f"Total sum using {num_threads} threads: {sum(results)}")

if __name__ == "__main__":
    N = 1000000  # range of numbers to sum
    run_threads(5, N)
    run_threads(10, N)
    run_threads(15, N)
