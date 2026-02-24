# COMP472 — Malaria Parasite Image Classification using CNNs

## Project Overview

This repository contains the implementation of the COMP472 Applied Artificial Intelligence course project (Winter 2026). The goal of the project is to study image classification performance using multiple Convolutional Neural Network (CNN) architectures across three different malaria parasite microscopy image datasets.

The project focuses on understanding how model complexity, dataset variability, preprocessing strategies, and optimization techniques affect classification performance.

This repository is currently under active development. At this stage, the team is focusing on **Phase 2 (Data Preparation & Pipeline Setup)** and **Phase 3 (Training Models from Scratch)** according to the approved project Gantt chart.

---

## Team Members

This project is completed collaboratively by a team of five members. Work responsibilities are divided equally across dataset preparation, pipeline development, experimentation, debugging, and documentation.

Each team member is expected to contribute regular commits throughout development as part of project evaluation.

---

## Current Project Status

### Phase 2 — Data Preparation & Pipeline Setup (In Progress)

The following work has been completed or is currently underway:

#### Dataset Preparation

* Three malaria parasite classification datasets selected from different sources to satisfy project requirements.
* Datasets downloaded from publicly available sources (primarily Kaggle).
* Dataset filtering performed to ensure total image count remains below project limits.
* Class mapping and filtering completed to remove irrelevant or inconsistent labels.
* Conversion of annotation-based datasets into classification-ready folder structures.

#### Dataset Splitting

* Train, validation, and test splits implemented.
* Balanced dataset distributions ensured across splits where applicable.

#### Data Pipeline Development

* Initial dataset loading pipeline being implemented using PyTorch Dataset and DataLoader classes.
* Debugging ongoing to ensure compatibility across datasets.

#### Preprocessing and Augmentation (Ongoing)

Planned preprocessing includes:

* Image resizing and normalization.
* Basic augmentation techniques to improve model robustness.

#### Training Framework Setup (In Progress)

The team is developing a reusable training framework including:

* Logging mechanisms.
* Model checkpoint saving.
* Debugging and monitoring utilities.

#### Model Selection

The following CNN architectures have been selected for experimentation:

* ResNet-18
* VGG-16
* MobileNet-V2

Initial small-scale validation tests are planned before large training runs.

#### Evaluation Preparation

Evaluation metrics under implementation include:

* Accuracy
* Precision
* Recall
* F1 Score

Validation testing workflows are being prepared.

---

## Phase 3 — Training Models From Scratch (Upcoming / Early Development)

The next stage of development includes:

* Training ResNet-18 on all three datasets.
* Training VGG-16 on all three datasets.
* Training MobileNet-V2 on all three datasets.

This results in nine baseline models trained from scratch.

Additional work will include:

* Debugging failed training runs.
* Organizing saved checkpoints.
* Generating comparison plots across datasets and architectures.

---

## Repository Structure (Planned)

```
COMP-472/
│
├── notebooks/          # Experiments and exploratory analysis
├── scripts/            # Dataset preparation and training scripts
├── models/             # Model checkpoints (local use)
├── data/               # Local datasets (not tracked in GitHub)
├── results/            # Metrics and generated plots
└── README.md
```

Note:
The `data/` directory is intentionally excluded from version control due to dataset size limitations.

---

## Dataset Access Instructions

Datasets used in this project are publicly available and must be downloaded locally.

Team members should download datasets from their official sources and place them inside:

```
COMP-472/data/raw/
```

Dataset links will be maintained and updated here as preprocessing stabilizes.

---

## Environment Setup (Preliminary)

Python virtual environments are recommended.

Example setup:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Final dependency requirements will be provided once pipeline development stabilizes.

---

## Running the Project (Work in Progress)

Detailed instructions for:

* training models,
* validating performance,
* running pretrained models,

will be finalized as development progresses toward Phase 4.

---

## Contribution Workflow

All team members are expected to:

* commit regularly,
* document major changes,
* maintain readable commit messages.

GitHub commit activity will be used as part of individual contribution evaluation.

---

## License

This repository is created strictly for academic use as part of COMP472 at Concordia University (Winter 2026).
