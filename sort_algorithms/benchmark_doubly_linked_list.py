import timeit
from doubly_linked_list import DoubleLinkedList, Student, Car


double_linked_list = DoubleLinkedList[Student]()
for i in range(50):
    double_linked_list.push_tail(Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5))


def getitem_benchmark():
    result: Student = double_linked_list[49]


time_taken = timeit.timeit(getitem_benchmark, number=1000)
print(f"Test 1.1 - average execution time: {time_taken / 1000:.6f} seconds")


def sort_fio_benchmark():
    double_linked_list.sort_fio()


time_taken = timeit.timeit(sort_fio_benchmark, number=1000)
print(f"Test 1.2 - average execution time: {time_taken / 1000:.6f} seconds")


def sort_course_benchmark():
    double_linked_list.sort_course()


time_taken = timeit.timeit(sort_course_benchmark, number=1000)
print(f"Test 1.3 - average execution time: {time_taken / 1000:.6f} seconds")


double_linked_list = DoubleLinkedList[Car]()
for i in range(50):
    double_linked_list.push_tail(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))


def sort_engine_capacity_benchmark():
    double_linked_list.sort_engine_capacity()


time_taken = timeit.timeit(sort_engine_capacity_benchmark, number=1000)
print(f"Test 2.1 - average execution time: {time_taken / 1000:.6f} seconds")


def sort_average_speed_benchmark():
    double_linked_list.sort_average_speed()


time_taken = timeit.timeit(sort_average_speed_benchmark, number=1000)
print(f"Test 2.2 - average execution time: {time_taken / 1000:.6f} seconds")
