import requests
import time
import threading

urls = [
    "https://youtube.com",
    "https://google.com.ua",
    "https://beetroot.academy",
    "https://pravda.com.ua",
    "https://github.com",
    "https://python.org",
]

results = ""  # [(url1, 200), (url2, code2), ...]
# {url1: code1, url2: code2, ...}


def make_request(url):
    global results
    result = requests.get(url)
    print(url, result)
    results += str(result)
    # results[url] = result
    print(results)
    return result


start_at = time.time()

thrs = []

for u in urls:
    thr = threading.Thread(target=make_request, args=(u, ))
    thrs.append(thr)
    thr.start()


for thr in thrs:
    thr.join()
    print(thr.name)

end_at = time.time()
print(repr(results))
total_time = end_at - start_at
print(total_time)
