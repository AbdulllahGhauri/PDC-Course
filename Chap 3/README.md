# ⚙️ Chapter 3 — Process-Based Parallelism in Python

## 📘 Summary
This chapter investigates the core principles of **process-based parallelism** using Python’s `multiprocessing` module.  
It demonstrates how multiple independent processes can execute simultaneously, each with its own memory space, enabling true parallelism on multi-core CPUs.  

The exercises in this chapter focus on the following process management techniques:
- **Killing Processes**
- **Using Queues**
- **Pipes for Communication**
- **Parallel Backups**
- **Spawning Processes**

Each example illustrates a fundamental aspect of multiprocessing, emphasizing inter-process communication, resource sharing, and synchronization in a distributed environment.

---

## 🧱 Concepts and Implementations

### 1️⃣ Killing Processes
Demonstrates how to create, monitor, and terminate processes programmatically.  
This mechanism is essential for maintaining control over long-running or malfunctioning parallel tasks.  

**Module:** `multiprocessing.Process`

---

### 2️⃣ Queue — Inter-Process Communication (IPC)
Explains how `multiprocessing.Queue` allows safe message passing between processes.  
It ensures that concurrent read and write operations do not interfere with one another.  

**Example Use Case:** A producer process generates data, and multiple consumers retrieve and process it concurrently.

---

### 3️⃣ Pipe — Direct Communication Channel
Uses `multiprocessing.Pipe` to establish a **bidirectional communication link** between two processes.  
This is a lightweight alternative to queues when only two processes are involved.  

**Example Use Case:** A parent process sends commands, and a child process responds with computed results.

---

### 4️⃣ Parallel Backups — Real-World Implementation
Implements parallel file backups using a **process pool**.  
Each process copies one file, showcasing true parallelism and efficient I/O handling.  
If files are missing, they are automatically generated before the backup process begins.

**Example File:** `parallelbackups.py`

**Key Features:**
- Uses `multiprocessing.Pool` for task distribution.  
- Automatically creates source files.  
- Handles file operations concurrently for improved speed.

---

### 5️⃣ Spawning Processes
Illustrates how new processes are **spawned dynamically** using Python’s process creation model.  
This is especially relevant for Windows systems, which rely on the spawn method rather than fork semantics.

**Example Use Case:** Creating multiple worker processes that execute computational tasks concurrently.

---

## 🧠 Conclusion
Process-based parallelism offers **true concurrency**, leveraging multiple CPU cores to improve performance for compute-intensive workloads.  
Unlike threading, where the **Global Interpreter Lock (GIL)** restricts parallel execution, multiprocessing creates **isolated memory spaces** that enable simultaneous execution of tasks.  

By mastering concepts such as **Queues**, **Pipes**, and **Process Pools**, developers can design robust, scalable systems capable of executing complex operations efficiently across multiple processors.
