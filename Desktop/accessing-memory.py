import os
import random
def main():
    a = random.sample(range(1,1000),100)
    print(a)
    b = random.randint(1,100)
    print (a[b])
main()
