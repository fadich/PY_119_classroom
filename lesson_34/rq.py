import requests
import time
import threading

# from concurrent.futures import ThreadPoolExecutor

urls = [
    "https://youtube.com",
    "https://google.com.ua",
    "https://beetroot.academy",
    "https://pravda.com.ua",
    "https://github.com",
    "https://python.org",
]


def make_request(url):
    result = requests.get(url)
    print(url, result)
    return result


start_at = time.time()
# for u in urls:
#     make_request(url=u)
end_at = time.time()

total_time = end_at - start_at
print(total_time)


start_at = time.time()

thrs = []

for u in urls:
    thr = threading.Thread(target=make_request, args=(u, ))
    thrs.append(thr)
    thr.start()

time.sleep(10)

for thr in thrs:
    thr.join()
    print(thr.name)

end_at = time.time()

total_time = end_at - start_at
print(total_time)
