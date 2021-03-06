#!python
from sorting_iterative import selection_sort, insertion_sort


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n) Why and under what conditions?
        because regardless of items1 or items2 we would need to traverse through the length of one.
    TODO: Memory usage: O(n) Why and under what conditions?
        because it creates a new list of a sorted list of two n inputs   
    """
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    sorted_list = []
    while len(items1) > 0 and len(items2) > 0:
        if items1[0] > items2[0]:
            sorted_list.append(items2.pop(0))
        else:
            sorted_list.append(items1.pop(0))
    sorted_list.extend(items1)
    del items1
    sorted_list.extend(items2)
    del items2
    return sorted_list

    # front = 0
    # back = (len(items1) - 1)
    # while len(items2) > 0:
    #     value = items2.pop()
    #     while front <= back:
    #         pivot = ((front + back) // 2)
    #         # if p f and b all equal the same index
    #         if front == back:
    #             # if the value is greater append at the back
    #             if value > items1[back]:
    #                 items1.insert(back + 1, value)
    #                 break
    #             # if the value is less than insert at index 0
    #             if items1[back] < value:
    #                 items1.insert(0, value)
    #                 break
    #             # if the value is equal to the value insert at index 0
    #         # if f, p, and b are greater than the value
    #         if items1[front] > value:
    #             # insert the value before f and p
    #             items1.insert(front, value)
    #             break
    #         # if b, p, and f are less than the value
    #         if items1[back] < value:
    #             # insert the value after b and p
    #             items1.insert(back + 1, value)
    #             break
    #         if items1[pivot] > value:
    #             back = pivot - 1
    #         elif items1[pivot] < value:
    #             front = pivot + 1
    #         elif items1[pivot] == value:
    #             items1.insert(pivot + 1, value)
    #             break
    #     front = 0
    #     back = (len(items1) - 1)
    # return items1


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: O(n^2) Why and under what conditions?
        because it uses an iterative sorting algorithm; insertion sort. 
    TODO: Memory usage: O(n) Why and under what conditions?
        because it creates a new list of sorted items and does not do this in-place
    """
    # TODO: Split items list into approximately equal halves
    pivot = len(items) // 2
    # TODO: Sort each half using any other sorting algorithm
    # sort first half in-place (insertion sort)
    left = insertion_sort(items[:pivot])

    right = insertion_sort(items[pivot:])
    # TODO: Merge sorted halves into one list in sorted order
    # merge the two half list (merge function but this does this in-place)
    sorted_list = merge(left, right)
    # change the input items
    items[:] = sorted_list
    return items


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(n log n) Why and under what conditions?
    TODO: Memory usage: O(n) Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) > 1:
        pivot = len(items) // 2
        right = merge_sort(items[pivot:])
        left = merge_sort(items[:pivot])
        sorted_list = merge(left, right)
    else:
        sorted_list = items
    # change the input items 
    items[:] = sorted_list
    return items


def get_pivot(items, low, high):
    """
        Returns the pivot index; medium of three values.
    """
    mid = low + (high - low) // 2
    pivot = high
    if items[low] < items[mid]:
        if items[mid] < items[high]:
            pivot = mid
    elif items[low] < items[high]:
        pivot = low
    return pivot


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot;
    (TODO: the method for selecting a pivot, I used a three medium selection) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: O(n/2) Why and under what conditions?
    TODO: Memory usage: O(1) Why and under what conditions?"""
    pivot = get_pivot(items, low, high)
    pivot_value = items[pivot]

    items[pivot], items[low] = items[low], items[pivot]
    border = low

    for i in range(low, high + 1):
        if items[i] < pivot_value:
            border += 1
            items[i], items[border] = items[border], items[i]
    
    items[low], items[border] = items[border], items[low]
    return border
 

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: O(n log n) Why and under what conditions?
    TODO: Worst case running time: O(n^2) Why and under what conditions?
    TODO: Memory usage: O(1) Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    if low == None and high == None:
        low = 0
        high = len(items) - 1

    # TODO: Check if list or range is so small it's already sorted (base case)
    if low < high:
        # TODO: Partition items in-place around a pivot and get index of pivot
        pivot = partition(items, low, high)
        # TODO: Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, pivot - 1)
        quick_sort(items, pivot + 1, high)
    

