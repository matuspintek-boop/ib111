def heapsort(to_sort: list[int]) -> None:
    heapify(to_sort)

    for i in range(len(to_sort) - 1, 0, -1):
        to_sort[i], to_sort[0] = to_sort[0], to_sort[i]
        sift_down(to_sort, 0, i)


def heapify(to_heap: list[int]) -> None:
    for i in range((len(to_heap) - 1) // 2, -1, -1):
        sift_down(to_heap, i, len(to_heap))


def sift_down(heap: list[int], idx: int, heap_end: int) -> None:
    while idx < heap_end:
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        largest = idx

        if left_idx < heap_end and heap[left_idx] > heap[largest]:
            largest = left_idx
        if right_idx < heap_end and heap[right_idx] > heap[largest]:
            largest = right_idx

        if largest == idx:
            break
        else:
            heap[largest], heap[idx] = heap[idx], heap[largest]
            idx = largest
