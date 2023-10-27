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
echo starting_5_Precily
cd ..
dir="./fold=5_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=5_model=Precily
cd ./fold=5_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_6_Precily
cd ..
dir="./fold=6_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=6_model=Precily
cd ./fold=6_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_7_Precily
cd ..
dir="./fold=7_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=7_model=Precily
cd ./fold=7_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_8_Precily
cd ..
dir="./fold=8_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=8_model=Precily
cd ./fold=8_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_9_Precily
cd ..
dir="./fold=9_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=9_model=Precily
cd ./fold=9_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_10_Precily
cd ..
dir="./fold=10_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=10_model=Precily
cd ./fold=10_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_11_Precily
cd ..
dir="./fold=11_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=11_model=Precily
cd ./fold=11_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_12_Precily
cd ..
dir="./fold=12_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=12_model=Precily
cd ./fold=12_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_13_Precily
cd ..
dir="./fold=13_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=13_model=Precily
cd ./fold=13_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_14_Precily
cd ..
dir="./fold=14_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=14_model=Precily
cd ./fold=14_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_15_Precily
cd ..
dir="./fold=15_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=15_model=Precily
cd ./fold=15_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_16_Precily
cd ..
dir="./fold=16_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=16_model=Precily
cd ./fold=16_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_17_Precily
cd ..
dir="./fold=17_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=17_model=Precily
cd ./fold=17_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_18_Precily
cd ..
dir="./fold=18_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=18_model=Precily
cd ./fold=18_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_19_Precily
cd ..
dir="./fold=19_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=19_model=Precily
cd ./fold=19_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_20_Precily
cd ..
dir="./fold=20_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=20_model=Precily
cd ./fold=20_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_21_Precily
cd ..
dir="./fold=21_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=21_model=Precily
cd ./fold=21_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_22_Precily
cd ..
dir="./fold=22_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=22_model=Precily
cd ./fold=22_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_23_Precily
cd ..
dir="./fold=23_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=23_model=Precily
cd ./fold=23_model=Precily
dir="./result"
mkdir $dir
python -m Train
echo starting_24_Precily
cd ..
dir="./fold=24_model=Precily"
mkdir $dir
cp ./fold=0_model=Precily/*.py ./fold=24_model=Precily
cd ./fold=24_model=Precily
dir="./result"
mkdir $dir
python -m Train
exit
