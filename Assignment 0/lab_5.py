def minimum_swaps(arr):
    swaps = 0
    n = len(arr)
    visited = [False] * n
    for i in range(n):
        if visited[i] or arr[i] == i + 1:
            continue
        cycle_size = 0
        x = 1
        while not visited[x]:
            visited[x] = True
            x = arr[x] - 1
            cycle_size += 1
        swaps += cycle_size - 1
    return swaps
n = int(input("Enter the number of elements: "))
arr = []
print("Enter the array elements one by one:")
for _ in range(n):
    arr.append(int(input()))
print("Minimum swaps needed:", minimum_swaps(arr))


