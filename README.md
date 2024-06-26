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

```bash
https://github.com/dilipkumardubeyy/crude_oil_price_prediction.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -v
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up your local host and post
```



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

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/dilipkumardubey/crude_oil_price_prediction.mlflow

export MLFLOW_TRACKING_USERNAME=dilipkumardubey

export MLFLOW_TRACKING_PASSWORD=cf8ece7bc6cee01c3cc542f6cbd79e242230c771

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM USER for deployment

    # with specifiv access

    1. EC2 Access: It is virtual machine

    2. ECR: Elastic Container Registry to save your docker image in AWS.

    
    # Description: About the deployment

    1. Build Docker Image of the source code

    2. Push your Docker Image to ECR.

    3. Launch your EC2.

    4. Pull your Image from ECR in EC2.

    5. Launch your Docker Image in EC2.

    # Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess


## 3. Create ECR repo to store/save Docker Image
    - Save the URI: 645920365058.dkr.ecr.us-west-1.amazonaws.com/crude_oil_price_prediction


## 4. Create EC2 Machine (Ubuntu)

## 5. Open EC# and Install Docker in EC2 Machine:


    # Optional

    sudo apt-get update -y

    sudo apt-get upgrade

    # Required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

## 6. Configure EC2 as self-hosted runner:
    setting >> actions >> runner >>new self hosted runner >> choose os >>then run command one by one


## 7. Setup Github scerets:

    AWS_ACCESS_KEY_ID = 

    AWS_SECRET_ACCESS_KEY = 

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = 645920365058.dkr.ecr.us-west-1.amazonaws.com/crude_oil_price_prediction

    ECR_REPOSITORY_NAME = crude_oil_price_prediction




## About MLFlow:
MLFLOW

    - Its Prodcution Grade
    - Trace all of your experiments
    - Logginf & Tagging your model