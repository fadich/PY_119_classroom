import tracemalloc

tracemalloc.start()
print(tracemalloc.get_traced_memory())  # << memory used: 0

a = [x for x in range(1_000_000)]

print(tracemalloc.get_traced_memory())  # << memory used: 40Mb

b = [x for x in range(1_000_000)]
print(tracemalloc.get_traced_memory())  # << memory used: 80Mb

g = (x for x in range(1_000_000))   # << GENERATOR
print(tracemalloc.get_traced_memory())  # << memory used: 80Mb - almost the same (200b for generator object)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

tracemalloc.stop()
