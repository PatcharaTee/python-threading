import threading


class Counter:

    def __init__(self):
        self.value = 0

    def increment(self):
        temp = self.value
        temp += 1
        self.value = temp


def worker(counter):
    for _ in range(100000):
        counter.increment()


for _ in range(100000000):
    counter = Counter()
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=worker, args=(counter,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Final counter value:", counter.value)
