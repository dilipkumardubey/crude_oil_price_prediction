# crude_oil_price_prediction
This repository contains the code of price prediction of Crude Oil Price (West Teaxs Intermediate) using Machine Learning

## Workflow

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

'''bash
https://github.com/Swati-Dilip-Dubey/crude_oil_price_prediction.git
'''
### STEP 01- Create a conda environment after opening the repository

'''bash
conda create -n mlproj python=3.8 -v
'''

'''bash
conda activate mlproj
'''


### STEP 02- install the requirements
'''bash
pip install -r requirements.txt
'''


'''bash
# Finally run the following command
python app.py
'''

Now,
'''bash
open up your local host and post
'''



## MLFlow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://gagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/dilipkumardubey/crude_oil_price_prediction.mlflow \
MLFLOW_TRACKING_USERNAME=dilipkumardubey \
MLFLOW_TRACKING_PASSWORD=cf8ece7bc6cee01c3cc542f6cbd79e242230c771 \
python script.py

Run this to export as env variables:

'''bash

export MLFLOW_TRACKING_URI=https://dagshub.com/dilipkumardubey/crude_oil_price_prediction.mlflow

export MLFLOW_TRACKING_USERNAME=dilipkumardubey

export MLFLOW_TRACKING_PASSWORD=cf8ece7bc6cee01c3cc542f6cbd79e242230c771

'''