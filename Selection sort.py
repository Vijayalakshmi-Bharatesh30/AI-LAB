

arr = [64, 25, 12, 22, 11]

n = len(arr)

for i in range(n):
    mini= i

    for j in range(i + 1, n):
        if arr[j] < arr[mini]:
            mini = j

    arr[i], arr[mini] = arr[mini], arr[i]

print("Sorted array:", arr)