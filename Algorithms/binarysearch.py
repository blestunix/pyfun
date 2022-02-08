def binary_search(lst, target):
  lo, hi = 0, len(lst)
  while hi > lo:
    mid = lo + (hi - lo) // 2
    if lst[mid] < target:
      lo = mid + 1
    else:
      hi = mid
  return -1 if lo > len(lst) else lo

# lst is a sorted list
lst = [1, 7, 8, 90, 920, 1560]
binarysearch(lst, 8)
