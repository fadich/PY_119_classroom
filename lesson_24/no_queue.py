import time


def process(val):
    time.sleep(2)
    print(f"{val} processed")


started_at = time.time()
for i in range(10):
    val = input(f"User #{i + 1}: ")
    process(val)

print(f"Took {time.time() - started_at:.2f} seconds")

