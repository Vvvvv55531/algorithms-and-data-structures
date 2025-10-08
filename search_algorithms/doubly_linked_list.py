from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, Callable, Any


class IKey(ABC):

    @abstractmethod
    def key(self) -> Any:
        ...


T = TypeVar("T", bound=IKey)


class IndexOutRangeException(Exception):
    pass


@dataclass
class Student(IKey):
    fio: str
    group_number: int
    age: int
    course: int
    average_mark: float

    def key(self) -> str:
        return self.fio

    def __str__(self) -> str:
        return f"Student({self.fio}, {self.group_number}, {self.age}, {self.course}, {self.average_mark})"


@dataclass
class Car(IKey):
    stamp: str
    vin: str
    engine_capacity: float
    cost: int
    average_speed: int

    def key(self) -> int:
        return self.cost

    def __str__(self) -> str:
        return f"Car({self.stamp}, {self.vin}, {self.engine_capacity}, {self.cost}, {self.average_speed})"


@dataclass
class DoublyNode(Generic[T]):
    data: T
    next_ptr: Optional['DoublyNode[T]'] = None
    prev_ptr: Optional['DoublyNode[T]'] = None


class DoubleLinkedList(Generic[T]):

    def __init__(self) -> None:
        self._length: int = 0
        self._head: Optional[DoublyNode[T]] = None
        self._tail: Optional[DoublyNode[T]] = None

    def __str__(self) -> str:
        my_str: str = ""
        node = self._head
        while node is not None:
            my_str += str(node.data) + " "
            node = node.next_ptr
        return f"Current state: [{my_str}]"

    def __getitem__(self, index: int) -> T:
        ok: bool = self._check_range(index)
        if not ok:
            raise IndexOutRangeException("-_-")

        if index == 0:
            return self._head.data
        if index == self._length - 1:
            return self._tail.data

        node = self._head
        for i in range(0, index):
            node = node.next_ptr
        return node.data

    def __delitem__(self, index: int) -> bool:
        ok: bool = self._check_range(index)
        if not ok:
            return False

        if index == 0:
            node = self._head
            self._head = node.next_ptr
            self._head.prev_ptr = None
            del node
            self._length -= 1
            return True

        node = self._head
        for i in range(0, index - 1):
            node = node.next_ptr

        if index == self._length - 1:
            self._tail.prev_ptr = None
            self._tail = node
            self._tail.next_ptr = None
            self._length -= 1
            return True

        delete_node = node.next_ptr
        node.next_ptr = delete_node.next_ptr
        node.next_ptr.prev_ptr = delete_node.prev_ptr
        self._length -= 1
        return True

    def __contains__(self, item: T) -> bool:
        node = self._head
        while node is not None:
            if node.data == item:
                return True
            node = node.next_ptr
        return False

    def contains(self, item: T) -> bool:
        node = self._head
        while node is not None:
            if node.data == item:
                return True
            node = node.next_ptr
        return False

    def get_size(self) -> int:
        return self._length

    def _check_range(self, index: int) -> bool:
        if index >= self._length or index < 0:
            return False
        return True

    def is_empty(self) -> bool:
        return self._length == 0

    def push_tail(self, data: T) -> None:
        node = DoublyNode[T](data, None)
        if self._length <= 0:
            self._head = node
            self._tail = node
            self._length += 1
            return

        self._tail.next_ptr = node
        node.prev_ptr = self._tail
        self._tail = node
        self._length += 1

    def push_head(self, data: T) -> None:
        node = DoublyNode[T](data)
        if self._length <= 0:
            self._head = node
            self._tail = node
            self._length += 1
            return

        node.next_ptr = self._head
        self._head.prev_ptr = node
        self._head = node
        self._length += 1

    def insert(self, index: int, data: T) -> None:
        ok: bool = self._check_range(index)
        if not ok:
            raise IndexOutRangeException("-_-")

        if index == 0:
            self.push_head(data)
            return
        elif index == self._length - 1:
            self.push_tail(data)
            return

        node = self._head
        for i in range(0, index):
            node = node.next_ptr

        insert_node = DoublyNode[T](data)
        insert_node.next_ptr = node
        node.prev_ptr.next_ptr = insert_node
        insert_node.prev_ptr = node.prev_ptr
        node.prev_ptr = insert_node
        self._length += 1

    def for_each(self, func: Callable[[T], None]):
        node = self._head
        func(node.data)
        while node.next_ptr is not None:
            node = node.next_ptr
            func(node.data)

    def reverse_for_each(self, func: Callable[[T], None]):
        node = self._tail
        func(node.data)
        while node.prev_ptr is not None:
            node = node.prev_ptr
            func(node.data)

    def reverse(self) -> None:
        if self._length <= 1:
            return

        self._head, self._tail = self._tail, self._head
        current_node = self._head
        while current_node is not None:
            current_node.next_ptr, current_node.prev_ptr = (
                current_node.prev_ptr,
                current_node.next_ptr,
            )
            current_node = current_node.next_ptr

    def get_pointer(self, data: T) -> Optional['DoublyNode[T]']:
        current_node = self._head

        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next_ptr

    def sort(self) -> None:
        if self._length == 0:
            raise ValueError("array is empty")

        for i in range(self._length):
            for j in range(self._length - i - 1):
                if self.__getitem__(j).key() > self.__getitem__(j + 1).key():
                    node = self.get_pointer(self.__getitem__(j))
                    memory_node = node.data
                    node_min = self.get_pointer(self.__getitem__(j + 1))
                    node.data = node_min.data
                    node_min.data = memory_node

    def is_sorted(self) -> bool:
        if self._length == 0:
            raise ValueError("array is empty")

        for i in range(1, self._length):
            if self.__getitem__(i - 1).key() > self.__getitem__(i).key():
                raise AttributeError("array is not sorted")
        return True

    def linear_search_by_fio(self, fio: str) -> int:
        if self.is_sorted():
            for i in range(self._length):
                if fio == self.__getitem__(i).key():
                    return i
                if fio < self.__getitem__(i).key():
                    break
            raise ValueError("Not Found")

    @staticmethod
    def get_min(a: int, b: int) -> int:
        if a <= b:
            return a
        else:
            return b

    def fibonacci_search_by_cost(self, cost: int) -> int:
        if self.is_sorted():
            if cost < self.__getitem__(0).key() or cost > self.__getitem__(self._length - 1).key():
                raise ValueError("Not Found")

            fm2 = 0
            fm1 = 1
            fm = fm1 + fm2
            offset = -1

            while fm < self._length:
                fm2 = fm1
                fm1 = fm
                fm = fm1 + fm2

            while fm > 1:
                i = self.get_min(offset + fm2, self._length - 1)
                if self.__getitem__(i).key() < cost:
                    fm = fm1
                    fm1 = fm2
                    fm2 = fm - fm1
                    offset = i
                elif self.__getitem__(i).key() > cost:
                    fm = fm2
                    fm1 = fm1 - fm2
                    fm2 = fm - fm1
                else:
                    return i

            if fm1 == 1:
                if self.__getitem__(offset + 1).key():
                    return offset + 1

            raise ValueError("Not Found")
