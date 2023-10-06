#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    surmation = 0
    for i in range(1, len(sys.argv)):
        sumation = surmation + int(sys.argv[i])
    print(surmation)
