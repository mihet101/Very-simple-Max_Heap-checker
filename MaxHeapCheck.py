"""
__updated__ = "2021-03-11"
Author:  Timothy Mihet
ID:      180963200
Email:   mihe3200@mylaurier.ca
"""

def isMaxHeap(A, heap_size):
    
    for i in range(heap_size):
        if i*2 < heap_size and A[i] < A[i*2]:
            return False
        if i*2+1 < heap_size and A[i] < A[i*2+1]:
            return False
    return True

A = list(map(int,input("\nEnter the array to test: ").strip().split()))
heap_size = int(input("Enter heap size: "))
print("\nstarting array: ", A)
result = isMaxHeap(A, heap_size)
print()
if result == True:
    print("This is a max heap")
else:
    print("This is not a max heap")


    