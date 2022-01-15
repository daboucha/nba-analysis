# NBA Analysis

## Purpose
Using NBA data sets, our team will run supervised machine learning to answer whether or not the outcome of a game can be predicted with high accuracy

## Topic Overview

**Reasons we selected topic:**
- Large dataset available
- Hobby or interest in the sport 
- Famous sport across North America
- If we predict game outcomes with high accuracy we could profit from gambling

**Description of the Data**

## Resources
- Data Source: https://www.basketball-reference.com/
- Software: Conda 4.10.3, Python 3.9.6, Jupyter-Notebook 6.3.0, Pandas 1.2.4, JavaScript 1.7, HTML 5, CSS/Bootstrap 4.0.0, Leaflet 1.7.1, D3.js v5, PostgreSQL 14.0, pgAdmin 4 5.7, Imbalanced-learn 0.8.1, Scikit-learn 1.0.1, Tensorflow 2.9.0, Keras-tuner 1.1.0

- Broken down by year starting in 2008-2009 through to 2021-2022
- Important columns that we will be examining throughout our analysis: 
    - Player Full Name
    - Team 
    - Games Played (GP)
    - Turnover Rate (TO%)
    - Offensive Rating (ORTG)
    - Defensive Rating (DRTG)
    - Effective Shooting Percentage (eFG%)
    - PPG (Points per Game)

Note: Players who are were drafted throughout the season will appear twice in the dataset on two different teams stats. 

**Questions we hope to answer by analyzing the data** 
1. Which players had the highest Offensive Rating 
2. Which players had the highest Defensive Rating 
3. Top 5 players with most potential 
4. Which team has the youngest average age of players 
5. Which team could potential winners 
6. Which teams had the highest number of new players added to their team (trading)

## Group Communication Protocols

- Communication with Team Members via Slack App in our 'Group 4' Channel
- Colaboration at organized weekly meetings

**Group Members & Roles**
- Danny Abouchakra
- Danielle Di Gioacchino
- Shantanu Vaidya
- Keshav Gupta

## Provisional Machine Learning Model 
**Example 1**

Input: Players, Team, Versatility Index (VI) 

Output: Average Versatility Index per Team

**Example 2**

Input: USG% (Usage Rate), TS% (Total Shooting Percentage), Versatility Index (VI)

Output: Top 5 players with most potential 

## Provisional Database

<< INSERT MOCK DATABASE >> 

Use SQL to mimic expected final database structure 
