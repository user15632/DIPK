import os


def fun(model, start, end):
    with open('run_model={}.txt'.format(model), 'a') as file0:
        print('#!bin/sh', file=file0)
        print('cd ./fold=0_model={}'.format(model), file=file0)

        print('echo starting_{}_{}'.format(0, model), file=file0)
        print('python -m Train', file=file0)

        for i in range(start, end + 1):
            folder = 'fold={}_model={}'.format(i, model)

            print('echo starting_{}_{}'.format(i, model), file=file0)
            print('cd ..', file=file0)

            print('dir="./{}"'.format(folder), file=file0)
            print('mkdir $dir', file=file0)

            print('cp ./fold=0_model={}/*.py ./{}'.format(model, folder), file=file0)

            print('cd ./{}'.format(folder), file=file0)
            print('dir="./result"', file=file0)
            print('mkdir $dir', file=file0)
            print('python -m Train', file=file0)
        print('exit', file=file0)

    os.rename('run_model={}.txt'.format(model), 'run_model={}.sh'.format(model))


fun(0, 1, 24)
fun(1, 1, 24)
fun(2, 1, 24)
fun('Precily', 1, 24)
