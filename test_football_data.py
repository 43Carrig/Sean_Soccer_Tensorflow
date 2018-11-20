# http://neuralnetworksanddeeplearning.com/chap1.html#perceptrons
# https://explained.ai/matrix-calculus/index.html # http://iamtrask.github.io/2015/07/12/basic-python-network/
# https://stevenmiller888.github.io/mind-how-to-build-a-neural-network/
# https://www.youtube.com/watch?v=gwitf7ABtK8 # https://www.youtube.com/watch?v=u_r_-z_qRsI
# https://www.youtube.com/watch?v=Py4xvZx-A1E
# https://www.youtube.com/watch?v=6sInH-pWi88&list=PLonlF40eS6nyYmALgj2sFMFMJF0nHwJ0M&index=8

# Beginner Intro to Neural Network - https://www.youtube.com/watch?v=ZzWaow1Rvho&list=PLxt59R_fWVzT9bDxA76AHm3ig0Gg9S3So
# Beginner Intro to Neural Networks 12: Neural Network in Python - https://www.youtube.com/watch?v=LSr96IZQknc&t=15s

# https://www.youtube.com/watch?v=CnCf1QGsjx8&list=PLjy4p-07OYzulelvJ5KVaT2pDlxivl_BN
# 5.2: Multiclass Classification for Deep Neural Networks - https://www.youtube.com/watch?v=GkKTWSInNvA
######################
# 5.3: Regression Neural Networks - https://www.youtube.com/watch?v=uLa-b3JxWAM

# How to Predict Stock Prices Easily - Intro to Deep Learning #7 - https://www.youtube.com/watch?v=ftMq5ps503w
# basketball neural network - https://www.youtube.com/results?search_query=basketball+neural+network

# https://www.poatek.com/2018/06/13/used-neural-networks-predict-2018-world-cup-champion/  # GOOD *

####################################################################
# Data-set from http://www.football-data.co.uk/englandm.php

# xgboast - a machine learning model - that is popular
# logistic regression - is another popular model used
# support vector machine  - model

# import csv

# with open('Season_2018_2019.csv') as csvfile:
# data = csv.reader(csvfile)

# for row in readCSV:
# print(row)

# pandas for data processing library
import pandas as pd

# Display library - for displaying results
from IPython.display import display

data = pd.read_csv('Season_2017_2018.csv')

# Season 2018 - 2019 : Win rate 43.33%
# Season 2017 - 2018 : Win rate 45.53%
# Season 2016 - 2017 : Win rate 49.21%


# head - the first few columns of that data-set - prove that the data is coming in
# display(data.head())
#####################
# Win rate for the home team

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

# LSTM networks are a type of RNN that uses special units in addition to standard units.
