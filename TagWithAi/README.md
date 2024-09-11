
# Web Scraper and NLP Classifier with PySpark

This project is designed to scrape data from Hacker News and perform Natural Language Processing (NLP) tasks using PySpark. The goal is to build and evaluate machine learning models that classify text data, leveraging the distributed computing capabilities of PySpark.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Processing](#data-processing)
- [Machine Learning Models](#machine-learning-models)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project involves:
- Scraping data from Hacker News.
- Cleaning and preprocessing text data.
- Building machine learning pipelines using PySpark's MLlib to classify the text data.
- Evaluating the performance of different classification models.

## Features

- **Data Collection**: Scrapes data from Hacker News using the `requests` library.
- **Data Processing**: Uses PySpark for data cleaning, preprocessing, and feature extraction.
- **Machine Learning**: Implements classification models such as Random Forest and Naive Bayes using PySpark's MLlib.
- **Model Evaluation**: Evaluates models using various metrics like accuracy, precision, recall, and F1-score.

## Installation

To get started with this project, ensure you have the necessary dependencies installed. This project uses PySpark, which requires Java and a compatible Python environment.

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install dependencies:
   ```bash
   pip install pyspark
   ```
3. If you are using Google Colab, you may need additional setup for PySpark:
   ```python
   !pip install pyspark
   ```

## Usage

1. **Initialize the Spark Session**: The project initializes a Spark session for processing data from Hacker News.
   ```python
   hackerNews = SparkSession.builder.appName("HackerNewsData").getOrCreate()
   ```
2. **Run the Notebook**: Execute the cells in the notebook sequentially. The notebook is structured to first scrape data, then clean and process it, and finally build and evaluate the models.

## Project Structure

- `WebScrapper For NLP.ipynb`: Main notebook containing all the code for data collection, processing, and modeling.
- `data/`: Directory where scraped data is stored (ensure paths are correctly set in the notebook).
- `models/`: Directory for saving trained machine learning models.

## Data Processing

- The notebook includes steps to clean and preprocess the text data from Hacker News.
- Uses PySpark's DataFrame operations to handle large datasets efficiently.
- Text preprocessing includes:
  - Removing unwanted characters and punctuation.
  - Converting text to lowercase.
  - Splitting text into words and removing stopwords.

## Machine Learning Models

The project implements the following models using PySpark's MLlib:

- **Random Forest Classifier**: A robust ensemble method that is used for classification tasks.
- **Naive Bayes Classifier**: A probabilistic classifier based on applying Bayes' theorem with strong independence assumptions between features.

### Model Pipeline

1. **Feature Extraction**: Uses `CountVectorizer` to convert text into numerical features.
2. **Model Training**: Models are trained using the extracted features.
3. **Prediction and Evaluation**: Evaluates the performance of the models using test data.

## Evaluation

The project evaluates models using PySpark's `MulticlassClassificationEvaluator`, focusing on metrics such as:
- Accuracy
- Precision
- Recall
- F1-score
