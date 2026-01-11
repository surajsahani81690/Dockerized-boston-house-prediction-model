#  Machine Learning Model API (Dockerized)

This project demonstrates a **production-ready ML model** deployed using **FastAPI and Docker**.

# Take the dataset from
- run on browser :- https://www.kaggle.com/datasets/altavish/boston-housing-dataset

##  Tech Stack
- Python
- FastAPI
- Scikit-learn
- Docker

##  Features
- REST API for predictions
- Fully Dockerized
- Easy to deploy anywhere

##  Run with Docker

```bash
docker build -t ml-model-api .
docker run -p 8000:8000 ml-model-api
