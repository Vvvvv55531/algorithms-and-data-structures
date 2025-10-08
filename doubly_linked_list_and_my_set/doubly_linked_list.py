from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable

T = TypeVar("T")


class IndexOutRangeException(Exception):
    pass


@dataclass
class Cat:
    name: str
    age: int

    def __str__(self) -> str:
        return f"Cat({self.name},{self.age})"


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
