
# pandas for data processing library
import pandas as pd

# Display library - for displaying results
from IPython.display import display

data = pd.read_csv('Season_2018_2019.csv')

# Season 2018 - 2019 : Win rate 43.33%
# Season 2017 - 2018 : Win rate 45.53%
# Season 2016 - 2017 : Win rate 49.21%

# head - the first few columns of that data-set - prove that the data is coming in
# display(data.head())
#####################

# Total number of matches.
number_matches = data.shape[0]

# Total number of matches per team
number_matches_per_team = number_matches / 20

# Calculate matches won by home team - at FTR.
number_home_wins = len(data[data.FTR == 'H'])  # FTR - full time result

# Number of away wins
number_away_wins = len(data[data.FTR == 'A'])

# Number of draws
number_draws = len(data[data.FTR == 'D'])

# Calculate matches won by home team - at HTR.
number_home_wins_half_time = len(data[data.HTR == 'H'])  # HTR - full time result

# Calculate win rate for home team.
# Half time
win_rate_half_time = (float(number_home_wins_half_time) / number_matches) * 100

# Full time
win_rate = (float(number_home_wins) / number_matches) * 100

# Print the results
print("Total number of matches: {}".format(number_matches))

print("Total number of matches per team so far in season: {}".format(number_matches_per_team))

print("Number of matches won by Home team: {}".format(number_home_wins))

print("Number of matches won by Away team: {}".format(number_away_wins))

print("Number of Draws: {}".format(number_draws))

print("Win rate of home team - Half Time: {:.2f}%".format(win_rate_half_time))

print("Win rate of home team - Full Time: {:.2f}%".format(win_rate))