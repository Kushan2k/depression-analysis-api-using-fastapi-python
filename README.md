# 🧠 Depression Analysis API

A FastAPI-based web service that leverages Machine Learning and Deep Learning models to analyze and detect depression levels from user inputs.

## 🚀 Overview

This project implements a RESTful API using FastAPI to assess depression levels based on user-provided text. It integrates various ML/DL models to classify and predict depression severity.

## 🧩 Key Features

- **FastAPI Backend**: High-performance web framework for building APIs.
- **Machine Learning Integration**: Utilizes models trained to detect depression indicators.
- **Deep Learning Models**: Incorporates advanced neural networks for accurate predictions.
- **Scalability**: Designed to handle multiple requests efficiently.

## 🧠 Technologies Used

- **FastAPI**: Modern, fast (high-performance) web framework for building APIs with Python 3.6+.
- **TensorFlow / PyTorch**: Deep learning frameworks for model development.
- **Scikit-learn**: Machine learning library for model training and evaluation.
- **Pandas / NumPy**: Data manipulation and analysis tools.
- **Uvicorn**: ASGI server for serving FastAPI applications.

## 🛠️ Setup & Installation

### Clone the Repository

```bash
git clone https://github.com/Kushan2k/depression-analysis-api-using-fastapi-python.git
cd depression-analysis-api-using-fastapi-python

```

## Install Dependancies
```bash
pip install -r requirements.txt
```

## Run the Application
```bash
uvicorn main:app --reload
```
The API will be accessible at http://127.0.0.1:8000

## Project Structure
```bash
depression-analysis-api-using-fastapi-python/
├── data/                   # Dataset and preprocessing scripts
├── models/                 # Trained model files
├── routers/                # API route definitions
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Git ignore file

```

## Model Details

- Model Type: Support Vector Classifier (SVC)
- Training Data: Custom dataset of text samples labeled with depression levels.
- Performance: Achieves high accuracy in classifying depression severity.


## Contributing
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your proposed changes.
