from collections import deque

# 1. Array (list): data berurutan, akses indeks O(1)
array = ["Ahmad", "Siti", "Budi"]
print("Array :", array, "| indeks 1 =", array[1])

# 2. Stack: LIFO, push/pop O(1)
stack = []
stack.append("A1")
stack.append("A2")
print("Stack :", stack, "| pop =", stack.pop())

# 3. Queue: FIFO, enqueue/dequeue O(1)
queue = deque()
queue.append("Ahmad")
queue.append("Siti")
print("Queue :", list(queue), "| dequeue =", queue.popleft())

# 4. Hash table (dict): cari berdasarkan key, rata-rata O(1)
mahasiswa = {"001": "Ahmad", "002": "Siti"}
print("Dict  :", mahasiswa, "| cari 002 =", mahasiswa["002"])
