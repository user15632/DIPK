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
echo starting_5_1
cd ..
dir="./fold=5_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=5_model=1
cd ./fold=5_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_6_1
cd ..
dir="./fold=6_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=6_model=1
cd ./fold=6_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_7_1
cd ..
dir="./fold=7_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=7_model=1
cd ./fold=7_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_8_1
cd ..
dir="./fold=8_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=8_model=1
cd ./fold=8_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_9_1
cd ..
dir="./fold=9_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=9_model=1
cd ./fold=9_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_10_1
cd ..
dir="./fold=10_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=10_model=1
cd ./fold=10_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_11_1
cd ..
dir="./fold=11_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=11_model=1
cd ./fold=11_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_12_1
cd ..
dir="./fold=12_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=12_model=1
cd ./fold=12_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_13_1
cd ..
dir="./fold=13_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=13_model=1
cd ./fold=13_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_14_1
cd ..
dir="./fold=14_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=14_model=1
cd ./fold=14_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_15_1
cd ..
dir="./fold=15_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=15_model=1
cd ./fold=15_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_16_1
cd ..
dir="./fold=16_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=16_model=1
cd ./fold=16_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_17_1
cd ..
dir="./fold=17_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=17_model=1
cd ./fold=17_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_18_1
cd ..
dir="./fold=18_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=18_model=1
cd ./fold=18_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_19_1
cd ..
dir="./fold=19_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=19_model=1
cd ./fold=19_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_20_1
cd ..
dir="./fold=20_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=20_model=1
cd ./fold=20_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_21_1
cd ..
dir="./fold=21_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=21_model=1
cd ./fold=21_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_22_1
cd ..
dir="./fold=22_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=22_model=1
cd ./fold=22_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_23_1
cd ..
dir="./fold=23_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=23_model=1
cd ./fold=23_model=1
dir="./result"
mkdir $dir
python -m Train
echo starting_24_1
cd ..
dir="./fold=24_model=1"
mkdir $dir
cp ./fold=0_model=1/*.py ./fold=24_model=1
cd ./fold=24_model=1
dir="./result"
mkdir $dir
python -m Train
exit
