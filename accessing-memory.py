import os
import random
def main():
    c = 1000000
    while c > 0:
    a = random.sample(range(1,1000),100)
    print(a)
    b = random.randint(1,99)
    print (a[b])
    c = c - 1
main()
