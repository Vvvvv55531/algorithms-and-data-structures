import timeit
from my_set import MySet

my_set1 = MySet()
for i in range(500):
    my_set1.add(i)

my_set2 = MySet()
for i in range(500):
    my_set2.add(i)


def union_benchmark():
    result = my_set1.union(my_set2)


time_taken = timeit.timeit(union_benchmark, number=1000)
print(f"Test 2.1 - average execution time: {time_taken / 1000:.6f} seconds")


def intersect_benchmark():
    result = my_set1.intersect(my_set2)


time_taken = timeit.timeit(intersect_benchmark, number=1000)
print(f"Test 2.2 - average execution time: {time_taken / 1000:.6f} seconds")


def difference_benchmark():
    result = my_set1.difference(my_set2)


time_taken = timeit.timeit(difference_benchmark, number=10000)
print(f"Test 2.3 - average execution time: {time_taken / 10000:.6f} seconds")
