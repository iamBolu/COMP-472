# COMP472 - Malaria Parasite Image Classification using CNNs

## Project Overview

This repository contains the implementation of the **COMP472 Applied Artificial Intelligence course project (Winter 2026)** at Concordia University.

The objective of this project is to evaluate the performance of multiple **Convolutional Neural Network (CNN)** architectures on microscopy images of malaria parasites. The study compares how different neural network models perform across multiple datasets representing various parasite stages.

The project investigates how the following factors influence image classification performance:

- CNN architecture complexity
- Dataset variability
- Image preprocessing techniques
- Training optimization strategies

The final outcome of the project will be a comparative analysis of model performance across multiple datasets.

---

# Project Phases

The project is divided into several development phases.

## Phase 1 - Project Planning

During this phase the team:

- Defined the research problem
- Selected candidate datasets
- Proposed CNN architectures for experimentation
- Developed a project timeline and Gantt chart

This phase resulted in the **project proposal and experimental plan**.

---

## Phase 2 - Data Preparation and Pipeline Setup

This phase focuses on preparing datasets and building the machine learning pipeline required for training models.

Key objectives include:

- Selecting appropriate malaria microscopy datasets
- Organizing datasets into a classification-ready structure
- Preparing training, validation, and test splits
- Implementing dataset loading pipelines
- Designing preprocessing and augmentation strategies

The data pipeline will be implemented using **PyTorch Dataset and DataLoader utilities**.

---

## Phase 3 - Training CNN Models

In this phase, multiple CNN architectures will be trained on the prepared datasets.

The following models have been selected for experimentation:

- **ResNet-18**
- **VGG-16**
- **MobileNet-V2**

Each architecture will be trained on all datasets, resulting in multiple baseline models.

Training experiments will involve:

- hyperparameter tuning
- monitoring training metrics
- saving model checkpoints
- comparing model convergence behavior

---

## Phase 4 - Model Evaluation and Comparison

After training is completed, models will be evaluated using standard classification metrics.

Evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1-score

Additional analysis may include:

- confusion matrices
- per-class performance analysis
- comparison across datasets and architectures

The goal is to identify how different CNN architectures perform when trained on microscopy parasite datasets.

---

# Datasets

This project uses three malaria microscopy image datasets sourced from publicly available repositories.

The datasets represent different parasite stages and infection conditions.

Datasets are organized locally in the following structure:

```
data/raw/

miracle9to9/
  train/
  val/
  test/

iml_malaria/
  train/
  val/
  test/

malaria/
  train/
  val/
  test/
```

Each dataset contains class folders that correspond to parasite categories.

Datasets are stored locally and **are not tracked in GitHub due to size constraints**.

---

# Machine Learning Pipeline

The project training pipeline will include the following components:

1. Dataset loading
2. Image preprocessing
3. Data augmentation
4. CNN model training
5. Validation during training
6. Final evaluation on test datasets

The implementation will primarily use **PyTorch**.

---

# Repository Structure

```
COMP-472/
│
├── notebooks/            # Experiments and exploratory analysis
├── scripts/              # Data preprocessing and training utilities
├── models/               # Saved model checkpoints (local)
├── results/              # Experiment outputs and plots
├── data/                 # Local datasets (excluded from GitHub)
└── README.md
```

Note:

The `data/` directory is excluded from version control because the datasets exceed GitHub size limits.

---

# Environment Setup

It is recommended to run the project inside a Python virtual environment.

Example setup:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Dependencies will be listed in `requirements.txt`.

---

# Running Experiments

Training and evaluation scripts will be provided in the `scripts/` directory.

These scripts will support:

- model training
- validation monitoring
- evaluation on test datasets

Detailed instructions will be added as the training pipeline is finalized.

---

# Collaboration Workflow

This project is developed collaboratively by a team of five members.

Team members contribute by:

- implementing project components
- documenting experiments
- maintaining clear commit histories
- participating in debugging and evaluation

GitHub activity is used to track project contributions.

---

# License

This repository is created strictly for **academic use** as part of the **COMP472 Applied Artificial Intelligence course at Concordia University (Winter 2026)**.
