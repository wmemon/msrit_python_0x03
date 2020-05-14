def special_in_sorted(li, key):
    # IN CASE li IS NOT SORTED
    li = sorted(li)
    print(li)
    mid = int(len(li) / 2)
    start = 0
    stop = len(li)
    while start < stop:
        if key < li[mid]:
            stop = mid - 1
            mid = int((start + mid) / 2)

        if key > li[mid]:
            start = mid + 1
            mid = int((stop + mid) / 2)

        if key == li[mid]:
            return True

    return False


print(special_in_sorted([99, 298, 397, 486, 355, 2], key= 2))
