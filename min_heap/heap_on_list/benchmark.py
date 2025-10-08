from min_heap_on_list import Car, Heap
from single_linked_list import SingleLinkedList
import timeit

single_linked_list = SingleLinkedList[Car]()
single_linked_list.push_head(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))
single_linked_list.push_head(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55))
single_linked_list.push_head(Car("Honda", "JHMGE8H50DC072263", 1.8, 18000, 58))
single_linked_list.push_head(Car("Chevrolet", "1G1JA5SH1E4175145", 1.6, 20000, 50))
single_linked_list.push_head(Car("Volkswagen", "3VWFA7AT4EM636650", 1.9, 21000, 52))
single_linked_list.push_head(Car("BMW", "WBA3A9G59DNP18865", 3.0, 35000, 70))
single_linked_list.push_head(Car("Mercedes-Benz", "WDDHF5KB3EB016724", 2.5, 40000, 65))

heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)


def change_benchmark():
    heap.change(2, Car("Nissan", "JN8AS5MT3CW253168", 2.0, 23000, 55))


time_taken = timeit.timeit(change_benchmark, number=10000)
print(f"Test 2.1 - average execution time: {time_taken / 10000:.6f} seconds")


def contains_benchmark():
    heap.contains((Car("Nissan", "JN8AS5MT3CW253168", 2.0, 23000, 55)))


time_taken = timeit.timeit(contains_benchmark, number=1000)
print(f"Test 2.2 - average execution time: {time_taken / 1000:.6f} seconds")


def save_benchmark():
    heap.save()


time_taken = timeit.timeit(save_benchmark, number=1000)
print(f"Test 2.3 - average execution time: {time_taken / 1000:.6f} seconds")
