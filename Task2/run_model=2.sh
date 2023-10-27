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
echo starting_5_2
cd ..
dir="./fold=5_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=5_model=2
cd ./fold=5_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_6_2
cd ..
dir="./fold=6_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=6_model=2
cd ./fold=6_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_7_2
cd ..
dir="./fold=7_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=7_model=2
cd ./fold=7_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_8_2
cd ..
dir="./fold=8_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=8_model=2
cd ./fold=8_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_9_2
cd ..
dir="./fold=9_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=9_model=2
cd ./fold=9_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_10_2
cd ..
dir="./fold=10_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=10_model=2
cd ./fold=10_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_11_2
cd ..
dir="./fold=11_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=11_model=2
cd ./fold=11_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_12_2
cd ..
dir="./fold=12_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=12_model=2
cd ./fold=12_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_13_2
cd ..
dir="./fold=13_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=13_model=2
cd ./fold=13_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_14_2
cd ..
dir="./fold=14_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=14_model=2
cd ./fold=14_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_15_2
cd ..
dir="./fold=15_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=15_model=2
cd ./fold=15_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_16_2
cd ..
dir="./fold=16_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=16_model=2
cd ./fold=16_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_17_2
cd ..
dir="./fold=17_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=17_model=2
cd ./fold=17_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_18_2
cd ..
dir="./fold=18_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=18_model=2
cd ./fold=18_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_19_2
cd ..
dir="./fold=19_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=19_model=2
cd ./fold=19_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_20_2
cd ..
dir="./fold=20_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=20_model=2
cd ./fold=20_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_21_2
cd ..
dir="./fold=21_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=21_model=2
cd ./fold=21_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_22_2
cd ..
dir="./fold=22_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=22_model=2
cd ./fold=22_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_23_2
cd ..
dir="./fold=23_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=23_model=2
cd ./fold=23_model=2
dir="./result"
mkdir $dir
python -m Train
echo starting_24_2
cd ..
dir="./fold=24_model=2"
mkdir $dir
cp ./fold=0_model=2/*.py ./fold=24_model=2
cd ./fold=24_model=2
dir="./result"
mkdir $dir
python -m Train
exit
