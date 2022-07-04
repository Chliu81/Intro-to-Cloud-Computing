import os

path = "/Users/charl/OneDrive/Documents/Intro to Cloud Computing/Assignment 3/DynamoDB/data.CSV"
assert os.path.isfile(path)
with open(path, "r") as f:
    pass