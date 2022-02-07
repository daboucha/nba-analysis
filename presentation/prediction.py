# Import dependencies
import os
import pandas as pd
import joblib

def predictScore(roster):
    # Import linear regression model
    file_dir = os.path.join("static", "model", "mlr_model.sav")
    mlr_model = joblib.load(file_dir)

    # Import player_totals dataframe
    file_dir = os.path.join("static", "data", "player_totals.csv")
    player_totals_df = pd.read_csv(file_dir).set_index('Player')

    X = createTeamAverages(roster, player_totals_df)
    y_pred = mlr_model.predict(X)

    return int(round(y_pred[0]))

def createTeamAverages(roster, player_totals_df):
    # Normalize team stats to 240 minutes per game
    factor = calculatePerMinuteFactor(roster, player_totals_df)

    totals = player_totals_df.loc[roster].reset_index(drop=True)
    g = totals["G"]

    totals = totals.drop(columns=["MP", "G"])

    for col in totals:
        totals[col] = totals[col]/g*factor

    team_averages = pd.DataFrame([totals.sum()])
                             
    return team_averages 

def calculatePerMinuteFactor(roster, player_totals_df):
    team_totals = player_totals_df.loc[roster].reset_index(drop=True)
    player_games = team_totals["G"]
    player_minutes = team_totals["MP"]

    team_minutes = player_minutes/player_games
    team_minutes = team_minutes.sum()
    
    if (team_minutes != 240) & (team_minutes != 0):
        factor = 240/team_minutes
    else:
        factor = 1
    
    return factor