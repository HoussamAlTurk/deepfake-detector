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

```bash
git clone https://github.com/HoussamAlTurk/deepfake-detector.git
cd deepfake-detector
pip install -r requirements.txt
```

Place the dataset inside:

```
data/FaceForensics++_C23/
```

Run the project:

```bash
python main.py
```

---

## 7. Requirements

See `requirements.txt`

---

## 8. Notes

* Training performed on Google Colab with GPU
* Dataset is not included due to large size
