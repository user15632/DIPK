import random

with open('Random.txt', 'a') as file0:
    print('seed={}'.format(random.randint(0, 10000000)), file=file0)
    for i in range(5):
        print(random.randint(1, 100), file=file0)
