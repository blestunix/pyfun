# Name: It is so called because it selects the smallest/largest element in the list and swaps it with the element at the first position, 
# then selects the next smallest/largest element in the list and swaps it with the element at the second position and so on until it is 
# done with the number at last position in the list.

def find_next_min(lst, i):
    mini = min(lst[i:])
    return lst.index(mini)

def selection_sort(lst):
    for i in range(len(lst)):
        j = find_next_min(lst, i)
        lst[i], lst[j] = lst[j], lst[i]   # swap        

        
lst = [45, 20, 34, 21, 81, 42]
selection_sort(lst)
print(lst)
