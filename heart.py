import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.csv')
graphCategories = ["scatter", "bar", "line", "pie", "box", "hist"]
columnCategories = ["Duration", "Pulse", "Maxpulse", "Calories"]

df.drop_duplicates(inplace=True)
plt.ion()

meanCalories = int(df.loc[:,"Calories"].mean())
missingCalories = df.loc[:,"Calories"].isna()
df.loc[missingCalories, "Calories"] = meanCalories

df.dropna(inplace=True)

while True:
    kind=""
    x=""
    y=""
    while kind not in graphCategories:
        kind = input("What kind of graph would you like to see? (scatter, bar, line, pie, box, hist):")
    while x not in columnCategories:
        x= input("What would you like the x axis to be? (Duration,Pulse,Maxpulse,Calories):")
    while y not in columnCategories:
        y=input("What would you like the y axis to be? (Duration,Pulse,Maxpulse,Calories):")
    print(df.loc[:,x].corr(df.loc[:,y]))
    df.plot(kind=kind, x=x, y=y)
