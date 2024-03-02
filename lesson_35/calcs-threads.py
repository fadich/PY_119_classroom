import requests
import time
import threading

# from concurrent.futures import ThreadPoolExecutor


def make_calculations():
    x = 0
    while x < 100_000_000:
        x += 1


start_at = time.time()
for u in range(10):
    print(u)
    make_calculations()
end_at = time.time()
total_time = end_at - start_at
print(total_time)


start_at = time.time()

thrs = []

for u in range(10):
    thr = threading.Thread(target=make_calculations)
    thrs.append(thr)
    thr.start()


for thr in thrs:
    thr.join()
    print(thr.name)

end_at = time.time()

total_time = end_at - start_at
print(total_time)
