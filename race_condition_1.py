import threading

x = 0


def main():
    global x
    x = 0

    # Example 1 (Race condition)
    t1 = threading.Thread(target=task)
    t2 = threading.Thread(target=task)

    # Example 2
    # lock = threading.Lock()
    # t1 = threading.Thread(target=task_safe, args=(lock, ))
    # t2 = threading.Thread(target=task_safe, args=(lock, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def increase():
    global x
    x += 1


def task():
    """Not implement lock and unlock logic before access global variable,
    Sum of variable 'x' will be invalid (Race condition).
    """
    for _ in range(500000):
        increase()


def task_safe(lock: threading.Lock):
    """Implement lock and unlock logic before access global variable.
    """
    for _ in range(500000):
        lock.acquire()
        increase()
        lock.release()


if __name__ == '__main__':
    for i in range(5):
        main()
        print(f"Loop number {i + 1}, X = {x}")
