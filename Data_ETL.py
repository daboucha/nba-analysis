#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import dependencies
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[2]:


def createPlayerDF(stat, year):
    # Set url for given year
    url = f'https://www.basketball-reference.com/leagues/NBA_{year}_{stat}.html'
    page = requests.get(url)
    
    # Convert the page html to a soup object
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Find the sought after table of data
    table = soup.find_all(class_="full_table")

    # Store the headers/column names
    head = soup.find(class_="thead")
    column_names_raw = [head.text for item in head][0]

    # Clean the column_names_raw list
    column_names = column_names_raw.replace("\n",",").split(",")[2:-1]
    
    # Create the dataframe
    players = []

    for i in range(len(table)):
        player_ = []

        for td in table[i].find_all("td"):
            player_.append(td.text)

        players.append(player_)

    df = pd.DataFrame(players, columns=column_names).set_index("Player")

    # Cleaning the player's name from occasional special characters
    df.index = df.index.str.replace('*', "", regex=True)
    
    return df


# In[4]:


def createRosters(team):
    roster = []

    # Set url for given team
    url = f"https://www.basketball-reference.com/teams/{team}/{datetime.now().year}.html"
    page = requests.get(url)

    # Convert the page html to a soup object
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find the sought after table of data
    table = soup.find(id="roster")
    player_table = table.find_all(attrs={"data-stat" : "player"})

    # Create a list of all players in the player table
    for p in player_table[1:]:
        roster.append(p.text)

    # Remove "TW" suffix
    for i in range(len(roster)):
        if "\xa0\xa0(TW)" in roster[i]:
            roster[i] = roster[i].replace("\xa0\xa0(TW)", "")

    return roster


# In[5]:


def createPlayerTotals(df):
    # Drop categorical and unnecessary columns
    columns_to_drop=["Pos", "Age", "Tm", "GS", "FG", "FG%", "3P", "3P%", "2P", "2PA", "2P%", "eFG%", "FT", "FT%", "TRB", "PTS"]
    df = df.drop(columns=columns_to_drop)

    # Convert data to numeric instead of object
    df = df.astype(float)
    
    return df


# In[6]:


def createTeamAverages(roster, player_totals):
    # Initilizing
    team_averages = [0,0,0,0,0,0,0,0,0,0]
    
    # Normalize team stats to 240 minutes per game
    team_minutes = calculateTeamMinutes(roster, player_totals)
    if team_minutes != 240:
        factor = 240/team_minutes
    
    # Loop through roster to store team average stats        
    for player in roster:
        totals = player_totals[player]
        
        # Store the number of games played before dropping column
        g = totals["G"]

        # Drop the now unnecessary columns
        totals = totals.drop(labels=["MP", "G"])
                 
        # Adjust player totals columns to show stats per game
        for col in totals.index:
            totals[col] = totals[col] / g * factor
        
        team_averages += totals
                             
    return team_averages


# In[7]:


def calculateTeamMinutes(roster, player_totals):
    # Initilizing
    team_minutes = 0
    
    for player in roster:
        totals = player_totals[player]
        team_minutes += totals["MP"] / totals["G"]
    
    return team_minutes


# In[8]:


# Get nba players data into dataframes from the year 2016 - present
currentYear = datetime.now().year
startYear = 2016
year_totals = {}

for year in range(startYear, currentYear+1):
    year_totals[year] = createPlayerDF('totals', str(year))


# In[9]:


# Get nba team rosters into dataframes
nba_teams = teams.get_teams()
nba_team_abr = [team['abbreviation'] for team in nba_teams]
team_rosters = {}

# Convert abreviation for Brooklyn, Pheonix, & Charlotte for basketball-reference.com
nba_team_abr[14] = "BRK"
nba_team_abr[19] = "PHO"
nba_team_abr[29] = "CHO"

for team in nba_team_abr:
    team_rosters[team] = createRosters(team)


# In[10]:


# Create dataframe for each player's stats over the last 5 years
currentYear = datetime.now().year
num_years = 5
player_totals = {}

for team in team_rosters.values():
    for player in team:
        # Initializing
        player_totals[player] = [0,0,0,0,0,0,0,0,0,0,0,0]

        for i in range(0, num_years+1):
            if player in year_totals[currentYear-i].index:
                player_totals[player] += createPlayerTotals(year_totals[currentYear-i]).loc[player]            


# In[11]:


# Create a dataframe for each teams per minute average based on current roster
team_averages = {}

for team in team_rosters:
    print(team)
    team_averages[team] = createTeamAverages(team_rosters[team], player_totals)


# In[140]:


player_totals["Chris Paul"]


# In[131]:


for team in team_rosters:
    print(team)


# In[130]:


team_rosters["LAL"]


# In[150]:


for player in team_rosters["LAL"]:
    print(player_totals[player]["G"])


# In[132]:


team = "LAL"
team_averages[team] = createTeamAverages(team_rosters[team], player_totals)


# In[120]:


for team in team_rosters:
    print(team)
len(team_rosters)


# In[112]:


team = "TOR"

# Initilizing
team_averages = [0,0,0,0,0,0,0,0,0,0]

# Normalize team stats to 240 minutes per game
team_minutes = calculateTeamMinutes(team_rosters[team], player_totals)
if team_minutes != 240:
    factor = 240/team_minutes

# Loop through roster to store team average stats        
for player in team_rosters[team]:
    totals = player_totals[player]

    # Store the number of games played before dropping column
    g = totals["G"]

    # Drop the now unnecessary columns
    totals = totals.drop(labels=["MP", "G"])

    # Adjust player totals columns to show stats per game
    for col in totals.index:
        totals[col] = totals[col] / g * factor

    team_averages += totals


# In[113]:


team_averages


# In[215]:


player_totals[2020]


# In[203]:


team_rosters["TOR"]


# In[213]:


player_totals["Precious Achiuwa"]


# In[200]:


team_averages["TOR"]


# In[202]:


team_averages["ATL"]


# In[137]:


test    


# In[ ]:





# In[142]:


player_totals[2021]


# In[5]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


player_df = players_combined[2021]


# In[9]:


month = "january"
year = "2021"

url = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{year}_games-{month}.html&div=div_schedule'
html = requests.get(url).content
df_list = pd.read_html(html)
games_df = df_list[-1]


# In[10]:


games_df.head()


# In[31]:


roster_home = ["Devonte' Graham", "Terry Rozier", "Gordon Hayward", "P.J. Washington", "Bismack Biyombo", "Miles Bridges", "LaMelo Ball", "Cody Martin", "Caleb Martin", "Jalen McDaniels", "Malik Monk", "Nick Richards", "Vernon Carey Jr.", "Nate Darling"]
roster_away = ["Tyus Jones", "Dillon Brooks", "Kyle Anderson", "Brandon Clarke", "Jonas Valančiūnas", "Desmond Bane", "John Konchar", "Gorgui Dieng", "Sean McDermott"]


# In[64]:


team_home = player_df.loc[roster_home]
team_away = player_df.loc[roster_away]


# In[28]:


team_home


# In[34]:


team_away


# In[90]:


team_home_fin = team_home.reset_index(drop=True)


# In[91]:


drop_columns = ["Pos", "Age", "Tm", "G", "GS", "FG%", "3P%", "2P", "2PA", "2P%", "eFG%", "FT%", "ORB", "DRB", "TS%", "3PAr", "FTr", "ORB%", "DRB%", "TRB%", "AST%", "STL%", "BLK%", "TOV%", "USG%", "WS/48", "OBPM", "DBPM", "BPM", "VORP"]
team_home_fin = team_home_fin.drop(columns=drop_columns)
team_home_fin = team_home_fin.dropna(axis=1, how="all")


# In[92]:


team_home_fin = team_home_fin.drop(team_home_fin.columns[19], axis=1)


# In[101]:


team_home_fin


# In[94]:


for col in team_home_fin:
    team_home_fin[col] = team_home_fin[col].astype(float)


# In[98]:


for col in team_home_fin.columns[1:]:
    team_home_fin[col] = team_home_fin[col]/team_home_fin["MP"]
team_home_fin["PER"] = team_home_fin["PER"] * team_home_fin["MP"]


# In[100]:


team_home_fin = team_home_fin.drop(columns="MP")


# In[88]:


team_home_fin.dtypes


# In[102]:


team_home_fin = team_home_fin.sum()


# In[104]:


team_home_fin


# In[105]:


get_ipython().system('pip install nba_api')


# In[5]:


from nba_api.stats.static import teams

nba_teams = teams.get_teams()
# Select the dictionary for the Celtics, which contains their team ID
celtics = [team for team in nba_teams if team['abbreviation'] == 'BOS'][0]
celtics_id = celtics['id']


# In[6]:


from nba_api.stats.endpoints import leaguegamefinder

# Query for games where the Celtics were playing
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=celtics_id)
# The first DataFrame of those returned is what we want.
games = gamefinder.get_data_frames()[0]
games.head()


# In[7]:


games


# In[20]:


test = games.drop(columns=["SEASON_ID", "TEAM_ID", "TEAM_ABBREVIATION", "TEAM_NAME", "GAME_ID", "GAME_DATE", "MATCHUP", "WL", "MIN", "FG_PCT", "FG3_PCT", "FT_PCT", "REB", "PLUS_MINUS", "FGM", "FG3M", "FTM"])


# In[21]:


test


# In[64]:


# Split our preprocessed data into our features and target arrays
X = test.drop("PTS", 1)
y = test["PTS"]

# Split the preprocessed data into a training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)


# In[65]:


model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_train)
y_pred


# In[66]:


print(f'Training Score: {model.score(X_train, y_train)}')
print(f'Testing Score: {model.score(X_test, y_test)}')


# In[ ]:





# In[ ]:





# In[61]:





# In[ ]:





# In[ ]:





# In[113]:


# Create a StandardScaler instances
scaler = StandardScaler()

# Fit the StandardScaler
X_scaler = scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)


# In[121]:


# Define the model - deep neural net
number_input_features = len(X_train_scaled[0])
hidden_nodes_layer1 = 40
hidden_nodes_layer2 = 10

nn = tf.keras.models.Sequential()

# First hidden layer
nn.add(tf.keras.layers.Dense(units=hidden_nodes_layer1, input_dim=number_input_features, activation="relu"))

# Second hidden layer
nn.add(tf.keras.layers.Dense(units=hidden_nodes_layer2, activation="relu"))

# Output layer
nn.add(tf.keras.layers.Dense(units=1, activation="relu"))

# Check the structure of the model
nn.summary()


# In[122]:


# Compile the model
nn.compile(loss="mean_squared_error", optimizer="adam", metrics=["accuracy"])


# In[123]:


# Train the model
fit_model = nn.fit(X_train_scaled, y_train, epochs=100, validation_data=(X_test_scaled, y_test))


# In[124]:


# Evaluate the model using the test data
model_loss, model_accuracy = nn.evaluate(X_test_scaled,y_test,verbose=2)
print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")


# In[25]:





# In[26]:


model = LinearRegression()


# In[27]:


model.fit(X, y)


# In[28]:


y_pred = model.predict(X)


# In[29]:


y_pred


# In[133]:


y


# In[135]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)


# In[136]:


# Resample the training data with the BalancedRandomForestClassifier
from imblearn.ensemble import BalancedRandomForestClassifier

clf = BalancedRandomForestClassifier(random_state=1, n_estimators=100).fit(X_train, y_train)


# In[141]:


from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import confusion_matrix
from imblearn.metrics import classification_report_imbalanced


# In[139]:


# Calculated the balanced accuracy score
y_pred = clf.predict(X_test)
balanced_accuracy_score(y_test, y_pred)


# In[142]:


# Display the confusion matrix
confusion_matrix(y_test, y_pred)


# In[143]:


model.fit(X_train, y_train)
training_score = model.score(X_train, y_train)
testing_score = model.score(X_test, y_test)


# In[144]:


print(f"Training Score: {training_score}")
print(f"Testing Score: {testing_score}")


# In[ ]:




