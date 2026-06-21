import sys
from unique_element import find_unique

if __name__ == "__main__":
    arr = [int(x) for x in sys.argv[1:]]
    print(find_unique(arr))
