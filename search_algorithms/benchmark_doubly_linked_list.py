import timeit
from doubly_linked_list import DoubleLinkedList, Student, Car


double_linked_list = DoubleLinkedList[Student]()
for i in range(50):
    double_linked_list.push_tail(Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5))


def sort_benchmark():
    double_linked_list.sort()


time_taken = timeit.timeit(sort_benchmark, number=1000)
print(f"Test 1.1 - average execution time: {time_taken / 1000:.6f} seconds")


def search_by_fio_benchmark():
    full_name: str = "Ivanov Ivan Ivanovich"
    index: int = double_linked_list.linear_search_by_fio(full_name)


time_taken = timeit.timeit(search_by_fio_benchmark, number=1000)
print(f"Test 1.2 - average execution time: {time_taken / 1000:.6f} seconds")


double_linked_list = DoubleLinkedList[Car]()
for i in range(50):
    double_linked_list.push_tail(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))


def fibonacci_search_by_cost_benchmark():
    price: int = 25000
    index = double_linked_list.fibonacci_search_by_cost(price)


time_taken = timeit.timeit(fibonacci_search_by_cost_benchmark, number=1000)
print(f"Test 1.3 - average execution time: {time_taken / 1000:.6f} seconds")
