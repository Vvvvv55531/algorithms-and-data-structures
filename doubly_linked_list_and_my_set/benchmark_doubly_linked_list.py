import timeit
from doubly_linked_list import DoubleLinkedList, Cat


doubly_linked_list = DoubleLinkedList[Cat]()
for i in range(1000):
    doubly_linked_list.push_tail(Cat("M", i))


def reverse_benchmark():
    doubly_linked_list.reverse()


time_taken = timeit.timeit(reverse_benchmark, number=1000)
print(f"Test 1.1 - average execution time: {time_taken / 1000:.6f} seconds")


def getitem_benchmark():
    result = doubly_linked_list[500]


time_taken = timeit.timeit(getitem_benchmark, number=1000)
print(f"Test 1.2 - average execution time: {time_taken / 1000:.6f} seconds")


def delitem_benchmark():
    del doubly_linked_list[500]


time_taken = timeit.timeit(delitem_benchmark, number=1000)
print(f"Test 1.3 - average execution time: {time_taken / 1000:.6f} seconds")
