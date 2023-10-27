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
echo starting_5_0
cd ..
dir="./fold=5_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=5_model=0
cd ./fold=5_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_6_0
cd ..
dir="./fold=6_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=6_model=0
cd ./fold=6_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_7_0
cd ..
dir="./fold=7_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=7_model=0
cd ./fold=7_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_8_0
cd ..
dir="./fold=8_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=8_model=0
cd ./fold=8_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_9_0
cd ..
dir="./fold=9_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=9_model=0
cd ./fold=9_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_10_0
cd ..
dir="./fold=10_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=10_model=0
cd ./fold=10_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_11_0
cd ..
dir="./fold=11_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=11_model=0
cd ./fold=11_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_12_0
cd ..
dir="./fold=12_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=12_model=0
cd ./fold=12_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_13_0
cd ..
dir="./fold=13_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=13_model=0
cd ./fold=13_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_14_0
cd ..
dir="./fold=14_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=14_model=0
cd ./fold=14_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_15_0
cd ..
dir="./fold=15_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=15_model=0
cd ./fold=15_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_16_0
cd ..
dir="./fold=16_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=16_model=0
cd ./fold=16_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_17_0
cd ..
dir="./fold=17_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=17_model=0
cd ./fold=17_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_18_0
cd ..
dir="./fold=18_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=18_model=0
cd ./fold=18_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_19_0
cd ..
dir="./fold=19_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=19_model=0
cd ./fold=19_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_20_0
cd ..
dir="./fold=20_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=20_model=0
cd ./fold=20_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_21_0
cd ..
dir="./fold=21_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=21_model=0
cd ./fold=21_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_22_0
cd ..
dir="./fold=22_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=22_model=0
cd ./fold=22_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_23_0
cd ..
dir="./fold=23_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=23_model=0
cd ./fold=23_model=0
dir="./result"
mkdir $dir
python -m Train
echo starting_24_0
cd ..
dir="./fold=24_model=0"
mkdir $dir
cp ./fold=0_model=0/*.py ./fold=24_model=0
cd ./fold=24_model=0
dir="./result"
mkdir $dir
python -m Train
exit
