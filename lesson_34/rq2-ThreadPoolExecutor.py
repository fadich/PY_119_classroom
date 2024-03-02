import requests
import time

from concurrent.futures import ThreadPoolExecutor

from requests import Response

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

with ThreadPoolExecutor() as executor:
    results = executor.map(make_request, urls)

# res_dict = {url: next(results) for url in urls}
res_dict = {}
for url in urls:
    result: Response = next(results)
    # print(url, result.request.url)
    res_dict[url] = result

print(res_dict)
end_at = time.time()

total_time = end_at - start_at
print(total_time)
