from doubly_linked_list import DoubleLinkedList, Cat
from my_set import MySet

if __name__ == "__main__":

    print("----- set list -----")
    doubly_linked_list = DoubleLinkedList[Cat]()
    print(doubly_linked_list)

    doubly_linked_list.push_head(Cat("Max", 4))
    doubly_linked_list.push_head(Cat("Alex", 5))
    doubly_linked_list.push_tail(Cat("Tom", 7))
    doubly_linked_list.push_tail(Cat("Tom1", 7))
    doubly_linked_list.push_tail(Cat("Tom2", 7))
    doubly_linked_list.push_tail(Cat("Tom3", 7))

    doubly_linked_list.insert(1, Cat("Tommy", 1))
    print(f"List size: {doubly_linked_list.get_size()}")

    age = 0

    def print_list(data: Cat) -> None:
        global age
        age += data.age
        print(data)

    doubly_linked_list.for_each(print_list)
    print(f'Sum age = {age}')
    print(f"Get data with index {1}: {doubly_linked_list[1]}")

    print("--Checking--")
    print(doubly_linked_list[1])
    if doubly_linked_list.contains(Cat("Tommy", 1)):
        print(f"1 - data with index {1} located in doubly_linked_list")
    if (Cat("Tommy", 1)) in doubly_linked_list:
        print(f"2 - data with index {1} located in doubly_linked_list")

    print("--Remove data--")
    del doubly_linked_list[1]
    print(doubly_linked_list)

    print("--Reversing--")
    doubly_linked_list.reverse()
    print(doubly_linked_list)

    print(" ")
    set_a = MySet(1, 2, 3, 4, 5, 6, 3, 3, 3, 2, 1, 4, 7, 8, 5)
    print("----- set A -----")
    set_a.print_set()

    set_b = MySet(10, 22, 1, 4, 21, 4, 5, 21, 11, 10)
    print("----- set B -----")
    set_b.print_set()

    print("----- Contains -----")
    val = 10
    print(f"SetA is contains '{val}'? {set_a.contains(val)}")
    print(f"SetB is contains '{val}'? {val in set_b}")

    print("----- A - B -----")
    set_a.difference(set_b).print_set()
    print("----- B - A -----")
    set_b.difference(set_a).print_set()
    print("----- Symmetric Difference -----")
    set_a.symmetric_difference(set_b).print_set()
    print("----- Union -----")
    set_a.union(set_b).print_set()
    print("----- Intersect -----")
    set_a.intersect(set_b).print_set()

    set_c = MySet[int](3, 5, 6)
    print(set_c.is_subset(set_a))
    print(set_c.is_subset(set_b))
