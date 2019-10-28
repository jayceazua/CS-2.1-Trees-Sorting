#!python
def is_sorted(items):
  """Return a boolean indicating whether given items are in sorted order.
  TODO: Running time: O(n) Why and under what conditions?
    Because if the list is sorted already we would need to go through the entire input list.
  TODO: Memory usage: O(1) Why and under what conditions?
    Because we are not storing anything into memory just simply returning true or false.
  """
  # TODO: Check that all adjacent items are in order, return early if so
  for index in range(len(items)-1):
    if items[index] > items[index + 1]:
      return False
  return True



def bubble_sort(items, order=True):
  """Sort given items by swapping adjacent items that are out of order, and
  repeating until all items are in sorted order.
  TODO: Running time: O(n^2) Why and under what conditions?
    Because each iteration we subtract 1 from the input size.
  TODO: 
  Memory usage: O(1) 
  Why and under what conditions?
    Because it changes the input array in-place and does not create a new copy
  """
  # TODO: Repeat until all items are in sorted order
  # TODO: Swap adjacent items that are out of order
  # instructions - algorithm
  # start at the first number from the items array
  last_sorted = len(items)
  swapped = True

  while last_sorted > 0:
    if swapped:
        swapped = False
        for index in range(last_sorted - 1):
          if order:
            # ascending order
            if items[index] > items[index + 1]:
              items[index], items[index + 1] = items[index + 1], items[index]
              swapped = True
          else:
            # decending order
            if items[index] < items[index + 1]:
              items[index], items[index + 1] = items[index + 1], items[index]
              swapped = True
    else:
        # we do not need to return the items value it changes the state of the input array
        return items

    last_sorted -= 1
      
      
def selection_sort(items):
  """Sort given items by finding minimum item, swapping it with first
  unsorted item, and repeating until all items are in sorted order.
  TODO: Running time: O(n^2) Why and under what conditions?
    Because we save the first index then loop through the array multiple times.
  TODO: Memory usage: O(1) Why and under what conditions?
    Because we are doing the swaps in place.
  """
  # TODO: Repeat until all items are in sorted order
  # TODO: Find minimum item in unsorted items
  # TODO: Swap it with first unsorted item
  
  first = 0
  smallest = None
  # swapped = True
  while first < (len(items) - 1):

    for i in range(first+1, len(items)):

      if smallest == None:
        smallest = items[first]

      if items[i] < smallest:
        smallest = items[i]
        items[first], items[i] = items[i], items[first]

    first += 1
    smallest = None

  return items





def insertion_sort(items):
  """Sort given items by taking first unsorted item, inserting it in sorted
  order in front of items, and repeating until all items are in order.
  TODO: Running time: ??? Why and under what conditions?
  TODO: Memory usage: ??? Why and under what conditions?"""
  # TODO: Repeat until all items are in sorted order
  # TODO: Take first unsorted item
  # TODO: Insert it in sorted order in front of items
  pass

