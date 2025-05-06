import sys

#!/usr/bin/python3
if __name__ == "__main__":

    # Sum all arguments converted to integers
    total = sum(int(arg) for arg in sys.argv[1:])
    print(total)
