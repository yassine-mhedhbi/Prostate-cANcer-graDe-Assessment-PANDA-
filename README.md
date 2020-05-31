# Prostate-cANcer-graDe-PANDAS-

## Description

![Gleason Grading process->ISUP](static/img.png)
An illustration of the Gleason grading process for an example biopsy containing prostate cancer. The most common (blue outline, Gleason pattern 3) and second most common (red outline, Gleason pattern 4) cancer growth patterns present in the biopsy dictate the Gleason score (3+4 for this biopsy), which in turn is converted into an ISUP grade (2 for this biopsy) following guidelines of the International Society of Urological Pathology. Biopsies not containing cancer are represented by an ISUP grade of 0 in this challenge.


## Data

Radboud University Medical Center and Karolinska Institute are the data providers: `karolinska` and `radboud`.

`gleason_score`: (3, 4, or 5) based on the architectural growth patterns of the tumor.

`isup_grade`: The target variable, the severity of the cancer on a 0-5 scale, converted from `gleason_score`. 

Data has been processed by [Iafoss](https://www.kaggle.com/iafoss), [data](https://www.kaggle.com/iafoss/panda-16x128x128-tiles-data)

### Disclaimer:
This is a for a kaggle competition and should not be used for medical diagnosis.

for more [info](https://www.kaggle.com/c/prostate-cancer-grade-assessment/overview/description)

# Credits:
Thanks [Iafoss](https://www.kaggle.com/iafoss)] for [preprocessing](https://www.kaggle.com/iafoss/panda-16x128x128-tiles) the data and provide the dataset.
