## Machine Learning Model
Q. Description of Data Preprocessing.

A. We web scraped the data from the website and getting data from NBA.com api. Luckily, we did not have to deal with missing data although we had to watch out for players that had zero of all stats or with the same name. We stored the data into dictionaries and dataframes. We dropped the columns not necessary for the prediction model. Creating new dataframes like average of each players for individual year and a new dataframes for their last 5years average.


Q. Description of feature engineering and the feature selection, including decision making process

A. How we ended up getting training data and testing data helped the in the decision process. The training data was taken from nba.com api and the data had each individual game stats total. Since older data was irrelevant we took only the last 10 years data of each and every game individually and dropped the unnecessary columns from there and ran the machine learning algorithm with that data. The model we used was multiple linear model. 
The feature selection and engineering when came to the players statistics was based on the data we got from each game. We used the same statistic as game data and negated the advance statistic for each player.


Q. Description of how data was split into training and testing sets 

A. For the training data we used scikit learn model (train test split), so we used that to test the model. We got the training data from nba.com api and the testing data which is actual live data has been collected by scrapping the website. To evaluate the model of testing and training data we used scikit learn train test split library. 


Q. Explanation of model choice, including limitation and benefit.

A. We tried a few prediction models such as random forest regression and multiple linear regression model. We knew based on data and what we are trying to predict we were looking for linear correlation. We are not classifying data and we knew it was supervised learning, so we started testing some of the model and got similar results. But the one which was most efficient for our prediction was multiple linear regression model.


Q. Description of current accuracy score

A. We have got an accuracy of 65% on the multiple linear regression model. 
