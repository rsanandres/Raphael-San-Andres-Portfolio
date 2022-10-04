<a href="https://www.linkedin.com/in/raphael-san-andres/">
  <img align="left" alt="Raphael's LinkedIN" width="22px" src="https://raw.githubusercontent.com/peterthehan/peterthehan/master/assets/linkedin.svg" />
</a>

<br />

About
=============================

My name is Raphael San Andres and I am a recent UCLA graduate where I got a B.S. in Statistics. At UCLA, I have had the opportunity to use statistical models to identify trends in data in Python and R as well as present my findings in various visual forms such as PowerPoints, Tableau, and RShiny applets. I have also worked on creating Neural Networks, Natural Language Processing, and Machine Learning models which includes my completion of a Deep Learning Specialization from Coursera.

I am passionate about data and the applications of data in the world. I love learning about different data techniques which include Deep Learning, Neural Networks, Machine Learning, Visualizations, and Application Creations. I believe that there is an extreme amount of data in the world and that can be utilized for a variety of tasks. I am most interested in the application and advancement of unsupervised learning in simulating more and more complex problems. I love working with data and believe that there is unlimited potential for human advancement that is still to be discovered in data. I hope that one day that the following creations can be made out of the advancement of data techniques:

- Clothing Design recommendation based on needs, materials, and stylistic preferences
- Suits/clothing with full body sensors that can simulate touch and feeling alongside VR/AR simulations
- Advanced body prosthetics for natural human motion
- (Not an application but) Acessibility to data models and techniques for the masses

My ultimate goal is the advancement of unsupervised/supervised learning techniques that can provide supplements to everyday human life.

This is my portfolio for side projects that I have completed since graduating from UCLA.


----------------------------------

Contents
=============================


- [In-Progress](#in-progress)
- [Completed](#completed)
  
----------------------------------
# In-Progress

## 💻 Twitch Recommendation System
### Progress: ![10%](https://progress-bar.dev/30)

[UCSD Twitch Dataset](https://cseweb.ucsd.edu/~jmcauley/datasets.html#twitch)

- Python
- Recommendation Systems, Collaborative Filtering
- Numpy, K-Means Clustering

Current Progress: Working through an EDA of the Twitch dataset provided by UCSD. The data only has a few columns so I am making my own columns to further understand the data and the relationships between the viewers and streamers are. Planning to implement KNN as my model of choice. I am currently looking for other options but my options are limited due there only being three main features of the dataset: Streamer, User watching, and time period the User was watching the streamer. Data can be derived from these few things, but I cannot see past using KNN for time being.

----------------------------------
# Completed


## 🧠 Neural Network for Celebrity Face Classifier (LFW)

[Labeled Faces in the Wild Dataset](http://vis-www.cs.umass.edu/lfw/)

- Python
- Neural Networks, HyperParameter Tuning (GridSearchCV)
- Labeled Faces in the Wild Dataset (LFW)
- Keras, SKlearn, Numpy, Pandas, Tensorflow, SciKeras, glob
- Computer Vision

Created and modeled a Neural Network in order to create a celebrity classifier using the Labeled Faces in the Wild Dataset. Conducted an EDA of the dataset to find the distribution of the pictures as well as examples of the photos. Parsed the dataset to only look up people with 20+ photos of themselves (which resulted in 57 total people and 2923 images). Created Convolutional Neural Networks to classify the photos of the 57 people. Initial Models included Conv2D, MaxPooling, Flatten, and Dense layers. Used GridSearchCV to find number pf Neurons, Batch Sizes, Activation Functions, Optimizers, Learning Rates, Momentum, Epochs, and Dropout Rate. Final model implemented the tuned hyperparameteres with some adjustments based on results. 

**Results:** \
Using sparse categorical crossentropy for loss, the final model produced a ~0.45 validation accuracy and 2.47 validation loss. The model seems to have reach a valley as both validation accuracy and validation loss plateaued. 

**Comments for next time:** 
- George Bush dominated the dataset with 500+ images and Collin Powell had 200+. Normalizing the amounts of pictures per person would provide a more accurate model as well as a less biased result. 
- The model seemed a little bit too complex and found itself overfitting towards the end. Optimizations by chaning some of the layers may have resulted in a better learning curve.


## 💬 Rbiot Discord Bot with Cohere.ai
- Python
- Discord Bot API, Cohere.ai API, Cohere.ai Finetuning Modeling
- Embeddings, Classifications
- Discord Bot Messaging and Commands

Created a Discord Bot in Python that scraped messages from users, sends a message to a channel whenever a user gets online, and provides a command that takes in a message and outputs the user most likely to type that message. Data was cleaned inside of a Jupyter Notebook and the Discord Bot is hosted via local Python Scripts. Cohere.ai provided a finetuning modeling service that the Discord Bot calls to find the user most likely to type that message. 



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
