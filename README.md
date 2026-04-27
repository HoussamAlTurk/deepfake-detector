# Deepfake Detection using CNN-LSTM

## 1. Overview

This project implements a deepfake detection system using a CNN-LSTM architecture on the FaceForensics++ dataset. The goal is to classify videos as real or manipulated.

---

## 2. Dataset

* Dataset: FaceForensics++ (C23 compression)

* Classes:

  * Real videos (`original`)
  * Fake videos:

    * Deepfakes
    * Face2Face
    * FaceSwap
    * NeuralTextures
    * FaceShifter

* Total used:

  * 200 real videos
  * 200 fake videos

---

## 3. Methodology

### Frame Extraction

* 10 frames sampled uniformly from each video

### Preprocessing

* Resize to 224×224
* Normalization using MobileNetV2 preprocessing

### Face Cropping

* MTCNN used for face detection
* Largest detected face selected

### Data Augmentation

* Horizontal flip
* Brightness & contrast adjustment
* Rotation

### Model Architecture

* CNN backbone: MobileNetV2 (pretrained on ImageNet)
* Temporal modeling: LSTM (64 units)
* Fully connected layers with dropout
* Output layer: Sigmoid (binary classification)

---

## 4. Experiments

### Experiment 1: Baseline

* No face cropping
* No augmentation

### Experiment 2: Face Cropping

* Uses MTCNN for face extraction

### Experiment 3: Face Cropping + Augmentation

* Combines face detection with data augmentation

---

## 5. Results

| Experiment | Accuracy | F1 Score |
| ---------- | -------- | -------- |
| Baseline   | 0.70     | 0.71     |
| Face Crop  | 0.58     | 0.55     |
| Face + Aug | 0.65     | 0.65     |

Face cropping alone reduced performance due to detection errors and loss of contextual information. However, combining face cropping with augmentation improved generalization and resulted in better performance.

---

## 6. How to Run

1.	Open the notebook in Google Colab.
2.	Make sure the dataset folder is already placed in Google Drive inside your project folder Like this below.
MyDrive
└── Deepfake_Project
  └── datasets
    └── FaceForensics++_C23
      ├── original
      ├── Deepfakes
      ├── Face2Face
      ├── FaceSwap
      ├── FaceShifter
      └── NeuralTextures
3.	Start from the top of the notebook and run the cells in order, one by one.
4.	First, allow Colab to connect to your Google Drive when prompted.
5.	Let the notebook load the dataset paths and confirm that the real and fake video folders are detected correctly.
6.	Run the preprocessing part to:
o	load the videos
o	extract frames
o	detect/crop faces
o	prepare the data for training
7.	Run the dataset split section so the notebook creates:
o	training set
o	validation set
o	test set
8.	Run the baseline experiment first.
9.	After the baseline finishes, run the face-cropping experiment.
10.	Then run the face-cropping + augmentation experiment.
11.	After each experiment finishes:
•	check the training curves
•	check the confusion matrix
•	note the accuracy, precision, recall, and F1-score
12.	At the end, run the comparison/results section to generate the final performance table.
13.	Check the project folders in Google Drive to confirm that:
•	trained model files were saved
•	result files were saved
•	the final comparison table was saved
Important notes
•	Always run the notebook from top to bottom.
•	If the runtime restarts, you must rerun the notebook from the beginning.
•	The preprocessing and dataset-building stages take time, so wait until each section fully finishes before moving on.
•	If Colab runs out of memory or time, reduce the dataset size or number of frames and rerun.
•	Do not skip directly to training before the preprocessing and dataset preparation sections are completed.
Output of the project
When the notebook finishes, you should have:
•	trained model files
•	training and validation curves
•	confusion matrices
•	accuracy, precision, recall, and F1-score
•	a final experiment comparison table

---

## 7. Requirements

See `requirements.txt`

---

## 8. Notes

* Training performed on Google Colab with GPU
* Dataset is not included due to large size
