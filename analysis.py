import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas


cnames =['sl', 'title', 'questionHTML', 'date', 'month', 'year', 'solved_by','difficulty_rating']
data = pandas.read_csv('database.csv',names=cnames)

sl = data.sl.tolist()
date = data.date.tolist()
month = data.month.tolist()
year = data.year.tolist()
solvedby = data.solved_by.tolist()
dr = data.difficulty_rating.tolist()


plt.plot(sl[100:200],solvedby[100:200])
plt.show()
plt.plot(sl[200:300],solvedby[200:300])
plt.show()