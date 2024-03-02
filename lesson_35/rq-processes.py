import requests
import time
import multiprocessing

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


if __name__ == "__main__":
    start_at = time.time()
    for u in urls:
        make_request(url=u)
    end_at = time.time()

    total_time = end_at - start_at
    print(total_time)

    start_at = time.time()

    procs = []

    for u in urls:
        print(u)
        proc = multiprocessing.Process(target=make_request, args=(u, ))
        procs.append(proc)

    # proc[0].start()
    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()
        print(proc.name)

    end_at = time.time()

    total_time = end_at - start_at
    print(total_time)
