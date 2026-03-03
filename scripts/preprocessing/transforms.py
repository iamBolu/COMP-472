import torch
from torchvision import transforms

# Member 3: Preprocessing & Augmentation Lead
# Shared configuration for all 11 models
IMG_SIZE = 128

# Official Training Pipeline (includes Augmentation)
train_transforms = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(90),
    transforms.ToTensor(),
    # Standard ImageNet normalization for Transfer Learning compatibility
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Official Validation/Testing Pipeline (Standardized)
val_test_transforms = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
