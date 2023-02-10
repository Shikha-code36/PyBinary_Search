# __init__.py
from binary_search import binary_search

def initialize():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = binary_search(arr, target)
    print(result) 
    print("binary_search package initialized")

initialize()
