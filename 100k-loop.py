import os
def main():
    a = 100000000
    while a > 0:
        a = a - 1
    print(a)
    with open('/proc/self/statm') as f:
    print(f.readline().split()[0])
main()
    
