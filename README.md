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

| Experiment       | Accuracy | Precision | Recall | F1 Score |
|------------------|----------|-----------|--------|----------|
| Baseline         | 0.700    | 0.688     | 0.733  | 0.710    |
| Face Crop        | 0.583    | 0.600     | 0.500  | 0.546    |
| Face Crop + Aug  | 0.650    | 0.645     | 0.667  | 0.656    |

Face cropping alone reduced performance due to detection errors and loss of contextual information. However, combining face cropping with augmentation improved generalization and resulted in better performance.

---

## 6. How to Run

## Dataset Structure

Place the dataset in Google Drive using the following structure:

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

## How to Run the Project

1. Open the notebook in Google Colab.

2. Make sure the dataset is already placed in Google Drive in the folder structure shown above.

3. Run the notebook from the top to the bottom in order.

4. When prompted, allow Colab to connect to Google Drive.

5. Let the notebook verify the dataset folders and load the real and fake video files.

6. Run the preprocessing stage to prepare the videos for training. This includes frame extraction, resizing, face cropping, and input preparation.

7. Run the dataset split stage to generate the training, validation, and testing sets.

8. Run the baseline experiment first.

9. After that, run the face-cropping experiment.

10. Then run the face-cropping plus augmentation experiment.

11. After each experiment finishes, review:

* training and validation curves
* confusion matrix
* accuracy
* precision
* recall
* F1-score

12. At the end, run the comparison section to generate the final performance table.

13. Check Google Drive to confirm that:

* trained model files were saved
* results were saved
* the final comparison table was saved

## Output

After the notebook finishes, the project should generate:

* trained model files
* training and validation curves
* confusion matrices
* accuracy, precision, recall, and F1-score
* final experiment comparison table

## Important Notes

* Always run the notebook in order from top to bottom.
* If the runtime restarts, rerun the notebook from the beginning.
* Preprocessing and dataset preparation may take time, so wait for each stage to finish before moving on.
* If Colab runs out of memory or session time, reduce the dataset size or frame count and rerun.
* Do not skip directly to training before preprocessing and dataset preparation are completed.

## Project Experiments

The project includes three main experiments:

1. Baseline CNN-LSTM
2. CNN-LSTM with face cropping
3. CNN-LSTM with face cropping and augmentation

These experiments are compared using standard evaluation metrics to analyze the effect of preprocessing and augmentation on deepfake detection performance.

## Evaluation Metrics

The project evaluates performance using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrix

---

## 7. Requirements

See `requirements.txt`

---

## 8. Notes

* Training performed on Google Colab with GPU
* Dataset is not included due to large size
* The project is designed to run in Google Colab with Google Drive integration.
