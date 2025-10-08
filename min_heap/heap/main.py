from min_heap import Student, Heap

if __name__ == '__main__':
    print("----- Students ------")
    print("." * 64)
    students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5),
                               Student("Petrov Petr Petrovich", 4213, 21, 3, 4.2),
                               Student("Sidorova Anna Aleksandrovna", 4217, 20, 1, 4.8),
                               Student("Smirnov Sergey Viktorovich", 4214, 22, 4, 4.2),
                               Student("Kozlova Olga Alekseevna", 4218, 20, 2, 4.7),
                               Student("Gavrilov Mikhail Dmitrievich", 4206, 21, 3, 3.9),
                               Student("Novikova Ekaterina Pavlovna", 4216, 19, 1, 4.9),
                               Student("Zaitsev Andrey Anatolievich", 4210, 24, 4, 3.5),
                               Student("Lebedeva Mariya Igorevna", 4212, 19, 2, 4.3),
                               Student("Chernov Aleksey Aleksandrovich", 4211, 20, 3, 4.6),
                               Student("Goncharov Artem Valentinovich", 4219, 18, 1, 3.7)
                               ]
    for i in range(0, len(students)):
        print(students[i])
    print("." * 64)

    print("----- Create ------")
    heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
    heap.print_heap()

    print("----- Remove ------")
    print(f"Remove root: {heap.remove()}")
    heap.print_heap()

    print("----- Change ------")
    heap.change(3, Student("Loginov Georgiy Alekseevich", 4215, 18, 1, 4.1))
    heap.print_heap()

    print("----- Check ------")
    if heap.contains(Student("Loginov Georgiy Alekseevich", 4215, 18, 1, 4.1)):
        print(f"Average_mark = {4.1} located in heap")
    if (Student("Goncharov Artem Valentinovich", 4219, 18, 1, 3.7)) in heap:
        print(f"Average_mark = {3.7} located in heap")

    print("\n----- Save and Load ------")
    heap.save()
    students: list[Student] = heap.load()
    heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
    heap.print_heap()
