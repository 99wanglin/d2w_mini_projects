def merge(array, p, q, r):
    nleft = q - p + 1
    nright = r - q
    left_array = array[p:q+1]
    right_array = array[(q+1):r+1]
    left = 0
    right = 0
    dest = p
    while left < nleft and right < nright:
        if left_array[left] <= right_array[right]:
            array[dest] = left_array[left]
            left += 1
        else:
            array[dest] = right_array[right]
            right += 1
        dest += 1
    while left < nleft:
        array[dest] = left_array[left]
        left += 1
        dest += 1
    while right < nright:
        array[dest] = right_array[right]
        right += 1
        dest += 1

def mergesort_recursive(array, p, r):
    q = (r+p)//2
    if r-p == 1:
        merge(array, p, q, r)
    else:
        mergesort_recursive(array, p, q)
        mergesort_recursive(array, q+1, r)
        merge(array, p, q, r)

def mergesort(array):
    mergesort_recursive(array, 0, len(array)-1)

input_array = [5, 2, 4, 7, 1, 3, 2, 6]
mergesort(input_array)
print(input_array)