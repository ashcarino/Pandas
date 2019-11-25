import pandas as pd

data = pd.read_csv('cars.csv')
cars = data.loc[[0,1,2,3,4,27,28,29,30,31]]
