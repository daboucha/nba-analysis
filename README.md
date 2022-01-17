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

- Broken down by year starting in 2008-2009 through to 2021-2022
- Important columns that we will be examining throughout our analysis: 
    - Player Full Name
    - Position 
    - Team (Tm)
    - Games Played (GP)
    - Turnover Rate (TO%)
    - Offensive Rating (ORTG)
    - Defensive Rating (DRTG)
    - Effective Shooting Percentage (eFG%)
    - PPG (Points per Game)

Note: Players who are were drafted throughout the season will appear twice in the dataset on two different teams stats. 

![This is an image](https://github.com/daboucha/to-be-determined/blob/aefe6217b418ac2973c442410fb975d74abb8f4b/Data_Screenshot.png)

**Questions we hope to answer by analyzing the data** 

1. Will we be able to predict the outcome of a game based on a team's roster and player statistics?

## Group Communication Protocols

- Communication with Team Members via Slack App in our 'Group 4' Channel
- Colaboration at organized weekly meetings

**Group Members & Roles**
- Danny Abouchakra
- Danielle Di Gioacchino
- Shantanu Vaidya
- Keshav Gupta

## Provisional Machine Learning Model 
Our goal is to use a logistic regression model to predict the outcome of game based on roster, and player statistical history. We will train the model with past game data. We may have to train and test multiple models to try and find what gives us higher accuracy with this type of data.

Inputs into our Model: 
- Home Team PER (Player Efficiency Rating)
- Home Team Win Shares
- Away Team PER (Player Efficiency Rating)
- Away Team Win Shares

## Provisional Database

We used SQL to import our data into 6 tables, since we had multiple csv files we are working with.

![This is an image](https://github.com/daboucha/to-be-determined/blob/40ba51eedde106726031031336923a3146e1bd90/Image_Database/database.png)

