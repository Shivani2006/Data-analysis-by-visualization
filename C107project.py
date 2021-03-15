import pandas as pd 
import csv
import plotly.express as px

df = pd.read_csv("data.csv")

sections = df.groupby("level")["attempt"].mean()
#print(sections)

group_id = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
print(group_id)

student_df = df.loc[df["student_id"]=="TRL_987"]
student_level = student_df.groupby("level")["attempt"].mean()
#print(student_level)


chart=px.scatter(group_id,x="student_id", y="level", size="attempt", color="attempt")
chart.show()