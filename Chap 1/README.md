# 🧩 Chapter 1 — Understanding Threads and Processes

## 📘 Summary
This chapter focuses on understanding the difference between **threads** and **processes** in Python.  
To visualize this, a simple **calculator program** was implemented twice:  
1. Once using **threads** (`threading` module).  
2. Once using **processes** (`multiprocessing` module).  

Each version performs five mathematical operations — addition, subtraction, multiplication, division, and power — running simultaneously to compare their execution behavior.

---

## ⚙️ Implementation Details

### 🔹 Thread-based Implementation
- Uses the `threading` module.
- Threads share the same memory space.
- Tasks appear to run simultaneously but are managed by the Python GIL (Global Interpreter Lock).
- More efficient for I/O-bound operations.

### 🔹 Process-based Implementation
- Uses the `multiprocessing` module.
- Each process runs independently with its own memory.
- True parallel execution on multiple CPU cores.
- Better suited for CPU-intensive tasks.

---

###  Mini Conclusion
Both implementations perform the same calculator tasks but differ in how they utilize system resources.

- The **thread-based version** runs faster to start and uses less memory, but due to the **Global Interpreter Lock (GIL)**, only one thread executes Python code at a time — so it’s more suited for I/O-bound tasks.  
- The **process-based version**, on the other hand, launches separate interpreters for each task, enabling **true parallelism** and better performance for CPU-heavy computations.

In summary:  
> 🧵 **Threads** = Shared memory, lower overhead, limited parallelism  
> ⚙️ **Processes** = Independent memory, higher overhead, true parallelism
