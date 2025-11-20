def partition(data, idx):
    pivot = data[idx]
    low, high = 0, len(data) - 1
    while True:
        while data[low] < pivot:
            low += 1

        while data[high] > pivot:
            high -= 1

        if low >= high:
            return
        data[low], data[high] = data[high], data[low]
