import pandas as pd   

input_data = pd.read_csv("input.csv", sep=",")

data = pd.read_csv("output.csv", sep=",")

print(data.keys())