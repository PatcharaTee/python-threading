import time
from concurrent.futures import ThreadPoolExecutor


def sum(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError

    return num1+num2


# Context manager
with ThreadPoolExecutor(max_workers=2) as ex:
    f1 = ex.submit(sum, 1, 2)
    f2 = ex.submit(sum, 2, "10")

    # Check future object for any raised exception before access result.
    f1_ex = f1.exception()
    if f1_ex is None:
        print(f1.result())

    f2_ex = f2.exception()
    if f2_ex is None:
        print(f2.result())

    # Map list of parameter to one function
    fs = ex.map(sum, [1, 5], [1, 4])
    for f in fs:
        print(f)

# Thread pool object
ex = ThreadPoolExecutor(max_workers=2)
f = ex.submit(sum, 10, 5)
f.result()
ex.shutdown()


def task(task_number, sleep_time):
    print(f"Start task number: {task_number}")
    time.sleep(sleep_time)
    print(f"Finish task number: {task_number}")


# Context manager, Example of worker count
with ThreadPoolExecutor(max_workers=2) as ex:
    f1 = ex.submit(task, 1, 2)
    f2 = ex.submit(task, 2, 10)
    f3 = ex.submit(task, 3, 4)
