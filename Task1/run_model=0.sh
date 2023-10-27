#!bin/sh
cd ./fold=0_model=0
echo starting_0_0
python -m Train
echo starting_1_0
cd ..
dir="./fold=1_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=1_model=0
cd ./fold=1_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_2_0
cd ..
dir="./fold=2_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=2_model=0
cd ./fold=2_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_3_0
cd ..
dir="./fold=3_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=3_model=0
cd ./fold=3_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_4_0
cd ..
dir="./fold=4_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=4_model=0
cd ./fold=4_model=0
dir="./result"
mkdir $dir
python -m Train
exit
