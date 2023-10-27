#!bin/sh
cd ./fold=0_model=2
echo starting_0_2
python -m Train
echo starting_1_2
cd ..
dir="./fold=1_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=1_model=2
cd ./fold=1_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_2_2
cd ..
dir="./fold=2_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=2_model=2
cd ./fold=2_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_3_2
cd ..
dir="./fold=3_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=3_model=2
cd ./fold=3_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_4_2
cd ..
dir="./fold=4_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=4_model=2
cd ./fold=4_model=2
dir="./result"
mkdir $dir
python -m Train
exit
