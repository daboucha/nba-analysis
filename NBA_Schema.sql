-- Creating tables for NBA Stats

CREATE TABLE game_statistics(
	game_index INT NOT NULL,
	date DATE NOT NULL,
	away_team VARCHAR NOT NULL,
	home_team VARCHAR NOT NULL,
	home_team_roster VARCHAR NOT NULL,
	away_team_roster VARCHAR NOT NULL,
	outcome VARCHAR NOT NULL
	
);

CREATE TABLE player_statistics(
	home_team_PER FLOAT NOT NULL,
	home_team_win FLOAT NOT NULL,
	away_team_PER FLOAT NOT NULL,
	away_team_win FLOAT NOT NULL,
	home_team_roster VARCHAR NOT NULL,
	away_team_roster VARCHAR NOT NULL
);