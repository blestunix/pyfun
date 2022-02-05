def find_next_min(lst, i):
    mini = min(lst[i:])
    return lst.index(mini)

def selection_sort(lst):
    for i in range(len(lst)):
        j = find_next_min(lst, i)
        lst[i], lst[j] = lst[j], lst[i]   # swap        
