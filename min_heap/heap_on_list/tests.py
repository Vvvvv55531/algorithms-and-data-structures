from min_heap_on_list import Car, Heap
from single_linked_list import SingleLinkedList
import unittest


class TestHeap(unittest.TestCase):

    def test_init(self):
        single_linked_list = SingleLinkedList[Car]()
        single_linked_list.push_head(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        self.assertEqual(heap.is_empty(), False)

    def test_contains(self):
        single_linked_list = SingleLinkedList[Car]()
        single_linked_list.push_head(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        self.assertEqual(heap.contains(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55)), False)
        self.assertEqual(heap.contains(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60)), True)

    def test_create_heap_from_list(self):
        single_linked_list = SingleLinkedList[Car]()
        single_linked_list.push_head(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        self.assertEqual(heap.is_empty(), False)
        self.assertEqual(heap._check_range(1), False)
        self.assertEqual(heap.get_size(), 1)

    def test_check_range(self):
        single_linked_list = SingleLinkedList[Car]()
        single_linked_list.push_head(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        self.assertEqual(heap._check_range(1), False)
        self.assertEqual(heap._check_range(0), True)

    def test_resize(self):
        single_linked_list = SingleLinkedList[Car]()
        single_linked_list.push_head(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55))
        single_linked_list.push_head(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        heap._resize(3)
        heap.insert(Car("Honda", "JHMGE8H50DC072263", 1.8, 18000, 58))
        self.assertEqual(heap.get_size(), 3)

    def test_is_empty(self):
        single_linked_list = SingleLinkedList[Car]()
        single_linked_list.push_head(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        self.assertEqual(heap.is_empty(), False)

    def test_get_size(self):
        single_linked_list = SingleLinkedList[Car]()
        single_linked_list.push_head(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        self.assertEqual(heap.get_size(), 1)

    def test_trickle_up(self):
        single_linked_list = SingleLinkedList[Car]()
        single_linked_list.push_head(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55))
        single_linked_list.push_head(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        heap._resize(3)
        heap.insert(Car("Honda", "JHMGE8H50DC072263", 1.8, 28000, 58))
        self.assertEqual(heap.contains(Car("Honda", "JHMGE8H50DC072263", 1.8, 28000, 58)), True)
        heap.remove()
        self.assertEqual(heap.contains(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55)), False)

    def test_trickle_down(self):
        single_linked_list = SingleLinkedList[Car]()
        single_linked_list.push_head(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55))
        single_linked_list.push_head(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        heap.change(1, Car("Honda", "JHMGE8H50DC072263", 1.8, 28000, 58))
        self.assertEqual(heap.contains(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55)), True)
        heap.remove()
        self.assertEqual(heap.contains(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55)), False)

    def test_change(self):
        single_linked_list = SingleLinkedList[Car]()
        single_linked_list.push_head(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55))
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        heap.change(0, Car("Honda", "JHMGE8H50DC072263", 1.8, 28000, 58))
        self.assertEqual(heap.contains(Car("Honda", "JHMGE8H50DC072263", 1.8, 28000, 58)), True)
        self.assertEqual(heap.get_size(), 1)

    def test_insert(self):
        single_linked_list = SingleLinkedList[Car]()
        single_linked_list.push_head(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55))
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        heap._resize(2)
        heap.insert(Car("Honda", "JHMGE8H50DC072263", 1.8, 28000, 58))
        self.assertEqual(heap.contains(Car("Honda", "JHMGE8H50DC072263", 1.8, 28000, 58)), True)
        self.assertEqual(heap.get_size(), 2)

    def test_remove(self):
        single_linked_list = SingleLinkedList[Car]()
        single_linked_list.push_head(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55))
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        heap.remove()
        self.assertEqual(heap.is_empty(), True)

    def test_save(self):
        single_linked_list = SingleLinkedList[Car]()
        single_linked_list.push_head(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55))
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        heap.save()
        students: list[Car] = heap.load()
        single_linked_list = SingleLinkedList[Car]()
        for student in range(0, len(students)):
            single_linked_list.push_head(students[student])
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        self.assertEqual(heap.contains(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55)), True)
        self.assertEqual(heap.get_size(), 1)

    def test_load(self):
        single_linked_list = SingleLinkedList[Car]()
        single_linked_list.push_head(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55))
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        heap.save()
        students: list[Car] = heap.load()
        single_linked_list = SingleLinkedList[Car]()
        for student in range(0, len(students)):
            single_linked_list.push_head(students[student])
        heap: Heap[Car] = Heap[Car].create_heap_from_list(single_linked_list)
        self.assertEqual(heap.contains(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55)), True)
        self.assertEqual(heap.get_size(), 1)


if __name__ == '__main__':
    unittest.main()
