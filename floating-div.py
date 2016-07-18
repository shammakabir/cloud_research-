import os
import random
def main():   
    d = 1000000
    while d > 0:
        a = random.uniform(0.0,100.0)
        print(a)
        b = random.uniform(0.0,100.0)
        print(b)
        c = a/b
        print(c)
        d = d - 1
    with open('/proc/self/statm') as f:
    print f.readline().split()[0]
main()
