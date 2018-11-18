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
# readCSV = csv.reader(csvfile)
# for row in readCSV:
# print(row)

# pandas for data processing library
import pandas as pd
# Display library - for displaying results
from IPython.display import display

data = pd.read_csv('Season_2018_2019.csv')

# head - the first few columns of that data-set - prove that the data is coming in
display(data.head())
#####################
# Win rate for the home team

# Total number of matches.
n_matches = data.shape[0]

# Calculate number of features. -1 because we are saving one as the target variable (win/lose/draw)
n_features = data.shape[1] - 1

# Calculate matches won by home team.
n_homewins = len(data[data.FTR == 'H'])

# Calculate win rate for home team.
# As a percentage of all the wins
win_rate = (float(n_homewins) / n_matches) * 100

# Print the results
print("Total number of matches: {}".format(n_matches))
print("Number of features: {}".format(n_features))
print("Number of matches won by home team: {}".format(n_homewins))
print("Win rate of home team: {:.2f}%".format(win_rate))