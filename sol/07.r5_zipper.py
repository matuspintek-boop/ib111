from typing import Annotated


class Node:
    def __init__(self, value: int) -> None:
        self.next: Node | None = None
        self.value = value


class Zipper:
    def __init__(self, value: int) -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self._cursor = value

    def cursor(self) -> int:
        return self._cursor

    def insert_left(self, num: int) -> None:
        node = Node(num)
        node.next = self.left
        self.left = node

    def delete_left(self) -> int | None:
        value: int | None = None
        if self.left:
            value = self.left.value
            self.left = self.left.next
        return value

    def shift_left(self) -> None:
        if self.left is None:
            return

        node = Node(self._cursor)
        node.next = self.right
        self.right = node
        self._cursor = self.left.value
        self.left = self.left.next

    def shift_right(self) -> None:
        if self.right is None:
            return

        node = Node(self._cursor)
        node.next = self.left
        self.left = node
        self._cursor = self.right.value
        self.right = self.right.next


def ops_enum(index: int) -> list[str]:
    ops: list[str] = []
    while index:
        index, kind = divmod(index, 4)
        if kind == 0:
            ops.append('shift_left')
        elif kind == 1:
            ops.append('shift_right')
        elif kind == 2:
            ops.append('delete_left')
        elif kind == 3:
            index, value = divmod(index, 7)
            ops.append('insert_left ' + str(value + 1))
    ops.extend(['shift_left' for _ in range(5)])
    ops.extend(['shift_right' for _ in range(5)])
    return ops


Ops = Annotated[list[str], ops_enum]


def run(Z: to_test) -> to_test:
    def cursor_after_each_op(ops: Ops) -> list[int]:
        zipper = Z(0)
        out: list[int] = []
        for op in ops:
            parts = op.split(' ')
            if parts == ['shift_left']:
                zipper.shift_left()
            elif parts == ['shift_right']:
                zipper.shift_right()
            elif parts == ['delete_left']:
                zipper.delete_left()
            else:
                cmd, value = parts
                assert cmd == 'insert_left'
                zipper.insert_left(int(value))
            out.append(zipper.cursor())
        return out

    return cursor_after_each_op
