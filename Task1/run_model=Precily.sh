#!bin/sh
cd ./fold=0_model=Precily
echo starting_0_Precily
python -m Train
echo starting_1_Precily
cd ..
dir="./fold=1_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=1_model=Precily
cd ./fold=1_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_2_Precily
cd ..
dir="./fold=2_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=2_model=Precily
cd ./fold=2_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_3_Precily
cd ..
dir="./fold=3_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=3_model=Precily
cd ./fold=3_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_4_Precily
cd ..
dir="./fold=4_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=4_model=Precily
cd ./fold=4_model=Precily
dir="./result"
mkdir $dir
python -m Train
exit
