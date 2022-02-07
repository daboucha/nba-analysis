## Machine Learning Model
Q. Description of Data Preprocessing.

A. We web scraped the data from the website and getting data from NBA.com api. Luckily, we did not have to deal with missing data although we had to watch out for players that had zero for all stats or players with the same name. We stored the data into dictionaries and dataframes. We dropped the columns not necessary for the prediction model. Creating new dataframes like average of each players for individual year and a new dataframes for their last 5years average.


Q. Description of feature engineering and the feature selection, including decision making process

A. The training data was gathered from an nba.com api and the data had every NBA game's total statistics for each team. Since older data was likely to be less accurate at predicting current NBA games, we took only the last 10 years data of each and every game individually. We were fortunate to have complete data, so there were no null values which needed to be predicted during the feature engineering process. With the complete data set ready, we continued the feature engineering process by dropping all categorical values. After that we had to drop certain numerical value columns which displayed the Field Goals Made during the game, as this number directly translates to the Points column and would overtrain our model. Lastly we dropped any redundant columns, which displayed duplicate information with another column, leaving us with our target column and features required for our machine learning model.


Q. Description of how data was split into training and testing sets 

A. For the training data we used scikit learn model (train test split), so we used that to test the model. We got the training data from nba.com api and the testing data which is actual live data has been collected by scrapping the website. To evaluate the model of testing and training data we used scikit learn train test split library. 


Q. Explanation of model choice, including limitation and benefit.

A. We tried a few prediction models such as random forest regression and multiple linear regression model. We knew based on data and what we are trying to predict we were looking for linear correlation. We are not classifying data and we knew it was supervised learning, so we started testing some of the model and got similar results. But the one which was most efficient for our prediction was multiple linear regression model.


Q. Description of current accuracy score

A. We have got an accuracy of 65% on the multiple linear regression model. 
