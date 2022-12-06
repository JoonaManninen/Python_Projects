########################################
#BM40A1500 Data Structures and Algorithms
# Made by: Joona Manninen
# 4.11.2022
# Quicksort algorithm 

# Quicksort function
def qsort(list, low, high):
  
    # Low value is pointer to first element on the list and high value pointer to last element on the list
    if low < high:
      
      # finding pivot element so that elements smaller than pivot are on the left and bigger on the right
      pivot = partition(list, low, high)

      # recursively make left side of the pivot in order
      qsort(list, low, pivot - 1)
      # recursively make right side of the pivot in order
      qsort(list, pivot + 1, high)

# Partition function
def partition(list, low, high):

  # Choosing pivot value as last value of the split
  pivot = list[high]
  # pointer to greater element 
  i = low - 1


  # compararing every element with pivot
  for k in range(low, high):
    if list[k] <= pivot:
        # When element is smaller than pivot, it's changed with element at position i
        i = i + 1
        # swapping element at i with element at k to get them in order
        (list[i], list[k]) = (list[k], list[i])
      
  # Placing pivot element last in the list
  (list[i + 1], list[high]) = (list[high], list[i + 1])
  # Returning partition position
  return i + 1

if __name__ == "__main__":
    A = [20, 22, 61, 57, 32, 64, 73, 83, 37, 12, 36, 87, 29, 75, 56, 40, 90, 91, 99, 7, 33, 70, 78, 18, 80]
    print(A)    # [9, 7, 1, 8, 5, 3, 6, 2, 4]
    qsort(A, 0, len(A)-1)
    print(A)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#eof