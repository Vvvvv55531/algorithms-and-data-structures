from min_heap import Student, Heap
import timeit

students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5),
                           Student("Petrov Petr Petrovich", 4213, 21, 3, 4.2),
                           Student("Sidorova Anna Aleksandrovna", 4217, 20, 1, 4.8),
                           Student("Smirnov Sergey Viktorovich", 4214, 22, 4, 4.1),
                           Student("Kozlova Olga Alekseevna", 4218, 20, 2, 4.7),
                           Student("Gavrilov Mikhail Dmitrievich", 4206, 21, 3, 3.9),
                           Student("Lebedeva Mariya Igorevna", 4212, 19, 2, 4.3)]

heap: Heap[Student] = Heap[Student].create_heap_from_list(students)


def change_benchmark():
    heap.change(2, Student("Goncharov Artem Valentinovich", 4219, 18, 1, 3.7))


time_taken = timeit.timeit(change_benchmark, number=10000)
print(f"Test 2.1 - average execution time: {time_taken / 10000:.6f} seconds")


def contains_benchmark():
    heap.contains(Student("Goncharov Artem Valentinovich", 4219, 18, 1, 3.7))


time_taken = timeit.timeit(contains_benchmark, number=1000)
print(f"Test 2.2 - average execution time: {time_taken / 1000:.6f} seconds")


def save_benchmark():
    heap.save()


time_taken = timeit.timeit(save_benchmark, number=1000)
print(f"Test 2.3 - average execution time: {time_taken / 1000:.6f} seconds")
