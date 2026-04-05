# COMP-472 Malaria Parasite Classification

GitHub Repository: https://github.com/iamBolu/COMP-472

Video Presentation: [ADD VIDEO LINK HERE]

---

## Project Description

This project trains convolutional neural networks (CNNs) to classify malaria parasite images taken from microscopy slides. We compare two CNN architectures (ResNet-18 and MobileNet-V2) trained from scratch and with transfer learning across three publicly available datasets.

The datasets cover different parasite stages: ring, trophozoite, schizont, and gametocyte, as well as a binary parasitized vs uninfected classification task.

---

## Requirements

This project runs in Google Colab with GPU. All experiments are in the notebook `notebooks/cnn_malaria.ipynb`.

Install required libraries with:

```
pip install -r requirements.txt
```

The requirements.txt includes:

- torch
- torchvision
- pandas
- Pillow
- matplotlib
- thop

---

## How to Get the Dataset

The datasets are stored in a shared Google Drive folder.

Download link: https://drive.google.com/drive/folders/1cimbdxEGg51H_wNYZlnBtCZkhFMgrQ_n?usp=drive_link

The folder contains three datasets:

- malaria (4 classes)
- iml_malaria (4 classes)
- miracle9to9 (2 classes: Parasitized, Uninfected)

Each dataset is already split into train, val, and test folders.

**Important step for collaborators before running the notebook:**

Each person must do the following so that the file paths in the code work correctly:

1. Open the shared Google Drive folder using the link above
2. Right-click the folder and select "Add shortcut to Drive"
3. Place the shortcut in "My Drive" (not in "Shared with me")
4. The notebook will then find data at `/content/drive/MyDrive/COMP472/Project/data/raw`

If you skip this step, the notebook will print `Data: ... (exists: False)` and no dataset will load.

---

## Repository Structure

```
COMP-472/
    notebooks/         main experiment notebook (cnn_malaria.ipynb)
    data/              local dataset folder (not tracked in GitHub)
    requirements.txt   Python dependencies
    README.md          this file
```

---

## How to Train the Models

1. Open Google Colab and upload or open `notebooks/cnn_malaria.ipynb` from this repository
2. Connect to a GPU runtime: Runtime > Change runtime type > GPU
3. Run cell 3 to mount Google Drive and set up paths
4. Run cell 4 to confirm the drive is mounted (skip if already mounted)
5. Run cell 5 to verify that all three dataset folders are found
6. Run the remaining cells in order to train ResNet-18 and MobileNet-V2

Cells 3, 4, and 5 will only work if you have completed the Google Drive shortcut step described above. Cell 3 automatically tries several possible path formats for the data folder. If data is not found, check that the shortcut is placed in "My Drive" and not "Shared with me".

Model checkpoints are saved to `/content/drive/MyDrive/COMP472/Project/checkpoints/` during training.

---

## How to Run the Pre-Trained Model on the Sample Test Dataset

1. Open `notebooks/cnn_malaria.ipynb` in Google Colab
2. Mount Google Drive and complete the drive shortcut step described above
3. Run cell 3 to set up paths
4. Skip the training cells and go to the evaluation section
5. Load a saved checkpoint by pointing the model to the checkpoint file:

```python
model.load_state_dict(torch.load("/content/drive/MyDrive/COMP472/Project/checkpoints/your_checkpoint.pth"))
model.eval()
```

6. Run the evaluation cells to generate predictions, confusion matrices, and classification reports on the test split

The test split is already included in each dataset folder under the `test/` subdirectory.

---

## Source Code

All training, evaluation, and visualization code is contained in:

`notebooks/cnn_malaria.ipynb`

The notebook is written in PyTorch and covers:

- data loading and augmentation
- model definitions (ResNet-18, MobileNet-V2)
- training loops with validation
- evaluation with F1 score, accuracy, confusion matrix
- transfer learning runs
- T-SNE visualizations
- final comparison table of all models

---

## Team Contribution Table

| Member Name | GitHub Username | Assigned Tasks | Details |
| ----------- | --------------- | -------------- | ------- |
| [Member 1]  | [username1]     | Data Exploration & Visualization | Verified datasets, counted images, created plots, and provided shared visualization/reporting functions for all members. |
| [Member 2]  | [username2]     | Pipeline & Utilities | Built shared data/model pipeline, implemented dataset/dataloader/transform/class weights, and provided model/training utilities for all members. |
| [Member 3]  | [username3]     | ResNet-18 Training | Trained ResNet-18 from scratch on all datasets, saved results, and generated training/evaluation outputs. |
| [Member 4]  | [username4]     | (Planned: VGG-16 + Optimization) | (Planned: Would train VGG-16 and run LR sweep, but not completed in final results.) |
| [Member 5]  | [username5]     | MobileNet-V2 & Transfer Learning | Trained MobileNet-V2 from scratch and with transfer learning, performed T-SNE visualizations, and created final comparison tables. |

---

## Contributors

To add the professor and Lead-TA as contributors:

1. Go to the repository on GitHub
2. Click Settings > Collaborators
3. Add them using their GitHub usernames or email addresses

---

## Note on Data

The `data/` folder is not tracked in this repository because the datasets are too large for GitHub. Use the Google Drive link above to download them.
