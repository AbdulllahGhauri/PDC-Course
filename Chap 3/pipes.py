from multiprocessing import Process, Pipe

def sender(conn):
    conn.send("Message from child process")
    conn.close()

def receiver(conn):
    print("Received:", conn.recv())

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=sender, args=(child_conn,))
    p.start()
    receiver(parent_conn)
    p.join()
