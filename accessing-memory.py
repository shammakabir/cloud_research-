import os
import random
def main():
    a = random.sample(range(1,1000),100)
    print(a)
    c = 1000000
    while c > 0:
        b = random.randint(0,99)
        print (a[b])
        c = c - 1
    with open('/proc/self/statm') as f:
    print f.readline().split()[0]
main()
