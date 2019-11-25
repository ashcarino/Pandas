import pandas as pd
data = pd.read_csv('cars.csv')

a = data.iloc[[0,1,2,3,4],[0,1,3,5,7,9]]

b = data[:1]

c = data.loc[[23],['Model','cyl']]

d = data.loc[[1,28,18],['Model','cyl','gear']]