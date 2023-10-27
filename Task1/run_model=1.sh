#!bin/sh
cd ./fold=0_model=1
echo starting_0_1
python -m Train
echo starting_1_1
cd ..
dir="./fold=1_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=1_model=1
cd ./fold=1_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_2_1
cd ..
dir="./fold=2_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=2_model=1
cd ./fold=2_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_3_1
cd ..
dir="./fold=3_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=3_model=1
cd ./fold=3_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_4_1
cd ..
dir="./fold=4_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=4_model=1
cd ./fold=4_model=1
dir="./result"
mkdir $dir
python -m Train
exit
