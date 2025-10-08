from single_linked_list import SingleLinkedList
from min_heap_on_list import Car, Heap

if __name__ == '__main__':
    print("----- Cars ------")
    single_linked_list = SingleLinkedList[Car]()
    print(single_linked_list)
    single_linked_list.push_head(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))
    single_linked_list.push_head(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55))
    single_linked_list.push_head(Car("Honda", "JHMGE8H50DC072263", 1.8, 18000, 58))
    single_linked_list.push_head(Car("Chevrolet", "1G1JA5SH1E4175145", 1.6, 20000, 50))
    single_linked_list.push_head(Car("Volkswagen", "3VWFA7AT4EM636650", 1.9, 21000, 52))
    single_linked_list.push_head(Car("BMW", "WBA3A9G59DNP18865", 3.0, 35000, 70))
    single_linked_list.push_head(Car("Mercedes-Benz", "WDDHF5KB3EB016724", 2.5, 40000, 65))
    single_linked_list.push_head(Car("Nissan", "JN8AS5MT3CW253168", 2.0, 23000, 55))
    single_linked_list.push_head(Car("Subaru", "JF2GPACC7F9234425", 2.5, 27000, 62))
    single_linked_list.push_head(Car("Hyundai", "5NPD84LF5JH246034", 1.6, 19000, 53))
    single_linked_list.insert(2, Car("Audi", "WAUMFAFR0EA087729", 2.0, 32000, 68))
    print(single_linked_list)

    print("----- Create ------")
    heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
    heap.print_heap()

    print("----- Remove ------")
    print(f"Remove root: {heap.remove()}")
    heap.print_heap()

    print("----- Change ------")
    heap.change(3, Car("Lexus", "JTHBK1GG3E2123456", 3.5, 45000, 75))
    heap.print_heap()

    print("----- Check ------")
    if heap.contains(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55)):
        print(f"data with average_mark = {22000} located in heap")
    if (Car("Subaru", "JF2GPACC7F9234425", 2.5, 27000, 62)) in heap:
        print(f"data with average_mark = {27000} located in heap")

    print("\n----- Save and Load ------")
    heap.save()
    single_linked_list = SingleLinkedList[Car]()
    students: list[Car] = heap.load()
    for student in range(0, len(students)):
        single_linked_list.push_head(students[student])
    heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
    heap.print_heap()
