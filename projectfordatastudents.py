import csv
import pandas as pd
import plotly.express as px

with open('class2.csv',newline='') as fuperMan:
    reader = csv.reader(fuperMan)
    datafromfuperman = list(reader)

datafromfuperman.pop(0)

total_marks = 0
total_entries = len(datafromfuperman)

for marks in datafromfuperman:
    total_marks += float(marks[1])

mean = total_marks/total_entries
print("THE MEAN OF THE STUDENT MARKS DATA IS AS FOLLOWS:\n",mean,"\n")

dataframe = pd.read_csv('class2.csv')
plot = px.scatter(dataframe,x="Student Number",y="Marks")

plot.update_layout(shapes=[
    dict(
        type='line',
        y0=mean, y1=mean,
        x0=0, x1=total_entries
    )
])

plot.update_yaxes(rangemode="tozero")

plot.show()