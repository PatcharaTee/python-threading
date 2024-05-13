import queue
import threading
import time

values = [
    [10, 10, 1],
    [5, 100, 2],
    [40, 2, 3],
    [70, "30", 4],
    [3, 6, 5]
]


def main():
    q = queue.Queue()
    for value in values:
        q.put(value)

    threads: list[threading.Thread] = []
    for _ in range(2):
        t = threading.Thread(target=sum_task, args=(q, ))
        t.start()
        threads.append(t)

    # t = threading.Thread(target=sum_task_finish, args=(q, ))
    # t.start()
    # threads.append(t)

    # q.not_empty.acquire()
    # q.not_empty.notify_all()
    # q.not_empty.release()

    for t in threads:
        t.join()

    # q.all_tasks_done.acquire()
    # q.all_tasks_done.notify_all()
    # q.all_tasks_done.release()


def sum_task(q: queue.Queue):
    t = threading.current_thread()

    while not q.empty():
        if q.empty():
            return

        values = q.get()
        if not isinstance(values, list):
            raise TypeError

        if len(values) < 3:
            raise ValueError

        time.sleep(values[2])
        try:
            print(
                f"Thread: {t.name}, Sum of {values[0]} and "
                f"{values[1]} is {sum(values[0], values[1])}"
            )
        except:
            return

        q.task_done()


def sum_task_finish(q: queue.Queue):
    q.all_tasks_done.acquire()
    if q.all_tasks_done.wait():
        print(f"All task finish, Unfinished tasks: {q.unfinished_tasks}")
    q.all_tasks_done.release()


def sum(num1: int, num2: int):
    return num1 + num2


if __name__ == '__main__':
    main()
