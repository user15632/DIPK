# Improving Drug Response Prediction via Integrating Gene Relationships with Deep Learning

This repository is the official implementation.

> 📋 We provide the implementation code for a series of experiments on DIPK. Due to the limitation of file size, please get the missing data from [DIPK - GoogleDrive](https://drive.google.com/drive/folders/16hP48-noHi3-c_LP9TcZxkwAzqxgR0VB?usp=sharing).

## Requirements

To install requirements:

```setup
pip install -r pre-requirements.txt
pip install -r requirements.txt
```

## Evaluation on learned cell lines and drugs

Run the following command to pre-train the Denoising AutoEncoder:

```train
python Task1/PreTrain/PreTrain.py
```

Then, run the following commands to train and test the model:

```train
dos2unix Task1/run_model\=0.sh Task1/run_model\=1.sh Task1/run_model\=2.sh Task1/run_model\=Precily.sh
source Task1/run_model\=0.sh Task1/run_model\=1.sh Task1/run_model\=2.sh Task1/run_model\=Precily.sh
```

Finally, run the following command to collate the test results:

```
python Task1/test_result.py
```

## Evaluation on unlearned cell lines and drugs

Run the following command to pre-train the Denoising AutoEncoder:

```train
python Task1/PreTrain/PreTrain.py
cp Task1/PreTrain/PreTrain.pkl Task2/PreTrain
```

Then, run the following commands to train and test the model:

```train
dos2unix Task2/run_model\=0.sh Task2/run_model\=1.sh Task2/run_model\=2.sh Task2/run_model\=Precily.sh
source Task2/run_model\=0.sh Task2/run_model\=1.sh Task2/run_model\=2.sh Task2/run_model\=Precily.sh
```

Finally, run the following command to collate the test results:

```
python Task2/test_result.py
python Task2/test_loss.py
```

## Evaluation on bulk RNA-seq data

Run the following command to pre-train the Denoising AutoEncoder:

```train
python Task3/PreTrain/PreTrain.py
```

Then, run the following commands to train and test the model:

```train
dos2unix Task3/run_model\=2.sh
source Task3/run_model\=2.sh
```

Finally, run the following command to collate the test results:

```
python Task3/test_result.py
```

## Validation on single-cell RNA-seq data

Run the following command to pre-train the Denoising AutoEncoder:

```train
python Task3/PreTrain/PreTrain.py
cp Task3/PreTrain/PreTrain.pkl Task4/PreTrain
```

Then, run the following commands to train and test the model:

```train
dos2unix Task4/run_model\=2.sh
source Task4/run_model\=2.sh
```

Finally, run the following command to collate the test results:

```
python Task4/test_result.py
```

## Validation on clinical patient data

Run the following command to pre-train the Denoising AutoEncoder:

```train
python Task5/PreTrain/PreTrain.py
```

Then, run the following commands to train and test the model:

```train
dos2unix Task5/run_model\=2.sh
source Task5/run_model\=2.sh
```

Finally, run the following command to collate the test results:

```
python Task5/test_geo01/Test.py
python Task5/test_geo02/Test.py
python Task5/test_geo03/Test.py
```
