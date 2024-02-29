#ESte es un comentario en el shellsort

def shell_sort(arr):
    l = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, l):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr
