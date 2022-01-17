<h1 align="center">NBA Analysis - Module 20 First Segment Project Deliverable</h1>

![This is an image](https://github.com/daboucha/to-be-determined/blob/a6d32efad004fe892e9dc237b41719ccbfcfdbec/NBA_Image.jpeg)

<p align="center">Our goal with Module 20 First Segment Project Deliverable is to build a foundation for our NBA Analysis. We have defined a purpose, found our data source, outlined our topic and determined our group communication protocols. We have started to prepare our data for our analysis, and included our provisional machine learning model and database.</p>

## Purpose
Using NBA data sets, our team will run supervised machine learning to answer whether or not the outcome of a game can be predicted with high accuracy.

## Resources
- Data Source: https://www.basketball-reference.com/

## Technologies
To transform our data, build our machine learning model (including importing different libraries) and store our data we will be using the following:
- Conda 4.10.3
- Python 3.9.6
- Jupyter-Notebook 6.3.0
- Pandas 1.2.4 
- Leaflet 1.7.1, D3.js v5
- PostgreSQL 14.0
- pgAdmin 4 5.7, 
- Imbalanced-learn 0.8.1
- Scikit-learn 1.0.1
- Tensorflow 2.9.0, Keras-tuner 1.1.0

To prepare our presentation of our final results we will be building a website to display our findings. This will require the use of:
- Javascript 1.7
- CSS/Bootstrap 4.0.0
- HTML 5

## Topic Overview

**Reasons we selected topic:**
- Large dataset available
- Hobby or interest in the sport 
- Famous sport across North America
- If we predict game outcomes with high accuracy we could profit from gambling

**Description of the Data**

There exists an abundance of data collected on players and teams in the NBA. 

Currenty we collected data in the following format: 

![This is an image](https://github.com/daboucha/nba-analysis/blob/746bfa4cc6afd819601d72c40916d1176a737153/Data_Screenshot.png)

Our plan is to reduce the data to the columns that are important to our analysis and give the columns more meaninful names. 
The features we are going to highlight are: 
- Home Team PER (Player Efficiency Rating)
- Home Team Win Shares
- Away Team PER (Player Efficiency Rating)
- Away Team Win Shares

As we build and create our model we may plan to add other features to our data that may have an impact at increasing accuracy at predicting a winner. Such as age, total points, or 3-point percentage. 

**Questions we hope to answer by analyzing the data** 

1. Will we be able to predict the outcome of a game based on a team's roster and player statistics?
2. As we add more features to our data (for example: age or total points) will we be more successful at predicting the winner?
3. Will certain player statistics be less or more important towards the accuracy of our prediction?
4. Does including more years worth of player statistics help to better predict our outcome, versus just looking at the last season?

## Group Communication Protocols

- Communication with Team Members via Slack App in our 'Group 4' Channel
- Colaboration at organized weekly meetings

**Group Members & Roles**
- Danny Abouchakra
- Danielle Di Gioacchino
- Shantanu Vaidya
- Keshav Gupta

## Provisional Machine Learning Model 
Our framework for the data:

Game Statistics 
![This is an image](https://github.com/daboucha/nba-analysis/blob/c3af2167b048c92b632af7f2c017dba51a46393a/Game_Stat_Framework.png)

Player Statistics 
![This is an image](https://github.com/daboucha/nba-analysis/blob/3ec253da2ae13437484ec22780ba998b42ddb944/Player_Stat_Framework.png)

Our goal is to use a logistic regression model to predict the outcome of game based on roster, and player statistical history. We will train the model with past game data. We may have to train and test multiple models to try and find what gives us higher accuracy with this type of data.

Inputs into our Model: 
- Home Team PER (Player Efficiency Rating)
- Home Team Win Shares
- Away Team PER (Player Efficiency Rating)
- Away Team Win Shares

Output: 
- Winning Team

## Provisional Database

We used SQL to import our data into tables, since we had multiple csv files we are working with.

<img width="408" alt="two_tables" src="https://user-images.githubusercontent.com/86980240/149687246-9e1e7365-aa51-488a-b38e-75b2825a564f.png">


