# ⚙️ Chapter 2 — Understanding Synchronization Tools in Python

## 📘 Summary
This chapter explores key **thread synchronization mechanisms** in Python:  
**Lock**, **RLock**, **Semaphore**, **Condition**, **Event**, **Barrier**, and **Queue**.  

Each concept is demonstrated using a simple **“Bakery” example 🍞**, where multiple bakers (threads) must coordinate tasks like preparing, baking, packing, and sharing limited ovens.  
These examples highlight how synchronization prevents race conditions and ensures organized thread execution.

---

## 🧱 Concepts and Implementations

### 1️⃣ Lock — Exclusive Access
Ensures that only one thread accesses a shared resource at a time, preventing data corruption and race conditions.

**Example:** Only one baker can use the oven at a time.  
**Module:** `threading.Lock`

---

### 2️⃣ RLock — Reentrant Lock
Allows the same thread to acquire the same lock multiple times without blocking itself.

**Example:** A baker performs two baking steps under the same lock.  
**Module:** `threading.RLock`

---

### 3️⃣ Semaphore — Limiting Access
Restricts the number of threads that can access a shared resource simultaneously.

**Example:** Only two bakers can use the oven at once because there are only two ovens.  
**Module:** `threading.Semaphore`

---

### 4️⃣ Condition — Wait and Notify
One or more threads wait until a condition is met, and another thread signals it.

**Example:** A customer waits for bread until the baker notifies that it’s ready.  
**Module:** `threading.Condition`

---

### 5️⃣ Event — Signaling State Change
An event acts as a flag that can be set or cleared to signal all waiting threads.

**Example:** Bakers wait until the oven is heated before starting to bake.  
**Module:** `threading.Event`

---

### 6️⃣ Barrier — Coordinating Start
All threads wait until everyone is ready before proceeding.  
Used when multiple threads must synchronize at a common point.

**Example:** All bakers start baking together after preparation.  
**Module:** `threading.Barrier`

---

### 7️⃣ Queue — Thread-Safe Communication
Provides a safe way for threads to share data without explicit locks.  
The producer (baker) adds items, and the consumer (packager) removes them in FIFO order.

**Example:** Bakers place baked bread in a queue, and the packager takes it for packing.  
**Module:** `queue.Queue`

---

## 🧠 Conclusion
Thread synchronization is essential for managing **shared resources** and ensuring **orderly execution** in concurrent programs.  
Each synchronization primitive has a distinct use case:  
- **Lock** ensures exclusive access,  
- **RLock** allows safe reentrant locking,  
- **Semaphore** limits concurrent usage,  
- **Condition** and **Event** handle communication,  
- **Barrier** coordinates threads, and  
- **Queue** enables thread-safe data exchange.  

By mastering these tools, developers can create **safe**, **efficient**, and **real-world concurrent systems** that perform reliably even under heavy workloads.
