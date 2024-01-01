# Biomedical classification

## Technology

- CellProfiler
- Python 3.10.4
- pandas==1.4.3
- seaborn
- torch==2.1.1 : Neural Network
- Scikit-learn: Logistic Regression, Multilayer Perceptron

## Reason

- Obtaining better results than traditional CNN which achive only 62% accuracy because of:
  - difficult nature of the data
  - various data distributions
  - small number of individuals

## Data

- The original data are microscopic images of the brains of mice aged 4, 8 and 15 months taken with an Opera Phenix confocal microscope
- These data were transformed with cellprofiler software using two pipelines:
  - the first pipeline performed projections and illumination corrections of 30 images in TIFF format containing a stack of piece of image to single image
  - the second pipeline enhanced the image, measured a number of features and extracted primary and secondary objects like cells and dendrites
- Data of this project:
  - 3243 files (summary-image data) contains 102 measures of image e.g. [img_2-summary ](example_data/Tab_Image.csv)
  - 3243 files (secondary-dendrities) contains each containing on average 150 dendrities describing with 116 features [img-2-secondary-dendrities](example_data/Tab_secondary_dendrities.csv)

## Tasks

- loading data, cleaning data, join summary image data with secondary dendrites
- preprocessing data with Standard Scaler
- feature engineering
  - calculate average area of dendrities in summary image data
- random under sample
- own cross validation

## Classifiaction based on summary image data

Classification of 3256 pieces into healthy and sick classes based summary-image data

|           | LogisticRegression | MLPClassifier | Net   |
| --------- | ------------------ | ------------- | ----- |
| accuracy  | 0.747              | 0.704         | 0.748 |
| recall    | 0.783              | 0.735         | 0.767 |
| precision | 0.757              | 0.700         | 0.775 |
| f1_score  | 0.748              | 0.697         | 0.743 |
