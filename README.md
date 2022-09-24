<a href="https://www.linkedin.com/in/raphael-san-andres/">
  <img align="left" alt="Raphael's LinkedIN" width="22px" src="https://raw.githubusercontent.com/peterthehan/peterthehan/master/assets/linkedin.svg" />
</a>

<br />

About
=============================

My name is Raphael San Andres and I am a recent UCLA graduate where I got a B.S. in Statistics. At UCLA, I have had the opportunity to use statistical models to identify trends in data in Python and R as well as present my findings in various visual forms such as PowerPoints, Tableau, and RShiny applets. I have also worked on creating Neural Networks, Natural Language Processing, and Machine Learning models which includes my completion of a Deep Learning Specialization from Coursera. This is my portfolio for side projects that I have completed since graduating from UCLA.


----------------------------------

Contents
=============================


- [In-Progress](#in-progress)
- [Completed](#completed)
  
----------------------------------
# In-Progress

## 🧠 Neural Network for Celebrity Face Classifier (LFW)
### Progress: ![75%](https://progress-bar.dev/75)

[Labeled Faces in the Wild Dataset](http://vis-www.cs.umass.edu/lfw/)

- Python
- Neural Networks, HyperParameter Tuning (GridSearchCV)
- Labeled Faces in the Wild Dataset (LFW)
- Keras, SKlearn, Numpy, Pandas, Tensorflow, SciKeras, glob
- Computer Vision

Current Progress: Working on tuning the model with hyperparameter tuning using GridSearchCV. I am aware that GridSearchCV is not usually scalable to neural networks. I want to implement BayesianOptimization after GridSearch. Also looking to tune the layers. I have created some models to some degrees of success but want to continue tuning them. Am currently running the models while I do other things.

Creating and modeling a Neural Network in order to create a celebrity classifier using the Labeled Faces in the Wild Dataset. Currently programming the neural network and optimizing the parameters involved including the layers, activation functions, and weights. Implemented models using Keras, Tensorflow, and SKlearn. Attempting to optimize for the following parameters:
- Neurons
- Batch Sizes
- Activation Functions
-  Optimizer
- Learning Rate
- Momentum
- Epochs
- Dropout Rate

## 💻 Twitch Recommendation System
### Progress: ![10%](https://progress-bar.dev/10)

[UCSD Twitch Dataset](https://cseweb.ucsd.edu/~jmcauley/datasets.html#twitch)

- Python
- Recommendation Systems, Collaborative Filtering
- Numpy, K-Nearst Neighbors

Current Progress: Working through an EDA of the Twitch dataset provided by UCSD. The data only has a few columns so I am making my own columns to further understand the data and the relationships between the viewers and streamers are. Planning to implement KNN as my model of choice. I am currently looking for other options but my options are limited due there only being three main features of the dataset: Streamer, User watching, and time period the User was watching the streamer. Data can be derived from these few things, but I cannot see past using KNN for time being.

----------------------------------
# Completed
## 🏀 NBA MVP Statistical Analysis
- Python
- Data Cleaning
- Seaborn Visualizations
- Logistic Regression
-  Random Forest
- K-Nearest Neighbors
- Support Vector Machines (SVM)

Used NBA data from 1979 to 2022 to create Seaborn visualizations and MVP predictions models. Constructed a Logistic Regression model to determine most important statistical predictor of MVPs. Created KNN, Random Forest, and SVM models to create predictions for a season’s MVP.

## 🐦 Sentiment Analysis Twitter - Queen Elizabeth II's Death
- Python
- Twitter API
- Sentiment Analysis 
- Data Cleaning: Lemmetization, Stopwords, Vectorization
- Packages: Spacy, Tweepy, NLTK
- Seaborn Visualizations
- Wordclouds

Utilized the Twitter API to gather tweets regarding Queen Elizabeth II’s death. Cleaned and prepared tweets for sentiment analysis via Spacy lemmatization, NLTK’s stopwords, and sklearn vectorization. Visualized word counts of each sentiment with bar graphs and wordclouds


## 🕸️ Amazon Web Scraper Project
- Python
-  Web Scraping
-  BeautifulSoup
-  Automated Email

Created a guided-project to scrape a single Amazon URL for its price, append its data to a csv, and send an email if the prices reaches below a certain threshold.

## 🦠 Covid Portfolio Project
- SQL 
- CTE
- Temp Tables
- Views

Created basic SQL queries to conduct an EDA on Covid Vaccinations.

## 💸 CoinMarkeyCap API Pull 
- Python 
- CoinMarketCap API
- JSON
- Cryptocurrency
- Seaborn

Created a guided-project to collect the top 15 Cryptocurrency currencies from CoinMarketCap API over a period of 333 minutes and visualize the percent_change of the top 15 currencies over the last 90 days.
 


## 💾 Data Cleaning Portfolio Project
- SQL
- Data Cleaning
- CTE
- Joins
- Queries

A simple data cleaning project involving SQL queries, CTE, Joins, Text Separations, and Table Creation 
