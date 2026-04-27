import os

def check_dataset():
    base_path = "data/FaceForensics++_C23"
    if not os.path.exists(base_path):
        raise ValueError("Dataset not found. Please place it inside data/ folder.")
    print("Dataset found.")

def main():
    print("Deepfake Detection Project")

    # Step 1: Check dataset
    check_dataset()

    # Step 2: Placeholder for pipeline
    print("Ready to run training pipeline...")

    # Later you can connect:
    # - data loading
    # - model training
    # - evaluation

if __name__ == "__main__":
    main()
