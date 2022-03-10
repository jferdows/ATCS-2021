import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pd.set_option("display.max_columns", None)
df= pd.read_csv("FinalProjectData.csv")

# # bar graph for Total Fatalities in 2018
# df1 = df.sort_values(by="2018 Tot. Fatal.", ascending=False)
# topFiveB1 = df1.head(5)
# x1 = topFiveB1["State"]
# y1= topFiveB1["2018 Tot. Fatal."]
# plt.bar(x1, y1, color ='orange')
# plt.title("States with the Highest Number of Vehicular Fatalities in 2018")
# plt.xlabel("States")
# plt.ylabel("Number of Fatalities Per 100,000")
# def addlabels(x,y):
#     for i in range(len(x)):
#         plt.text(i,y.iloc[i],y.iloc[i], ha = 'center')
# addlabels(x1,y1)
# plt.show()

# # bar graph for Total Fatalities in 2019
# df2 = df.sort_values(by="2019 Tot. Fatal.", ascending=False)
# topFiveB2 = df2.head(5)
#
# x2 = topFiveB2["State"]
# y2= topFiveB2["2019 Tot. Fatal."]
# plt.bar(x2, y2, color ='orange')
#
# plt.title("States with the Highest Number of Vehicular Fatalities in 2019")
# plt.xlabel("State")
# plt.ylabel("Number of Fatalities")
#
# def addlabels(x,y):
#     for i in range(len(x)):
#         plt.text(i,y.iloc[i],y.iloc[i], ha = 'center')
# addlabels(x2,y2)
# plt.show()

# #Creating a Scatterplot
# colormap=np.array(["r","g","b"])
# df.plot.scatter(x="State", y="2018 Urban Fatal.", fontsize=5)
# plt.xticks(rotation=90)
# plt.show()

# #Creating a Scatterplot
# colormap=np.array(["r","g","b"])
# df.plot.scatter(x="State", y="2018 Rural Fatal.", fontsize=5)
# plt.xticks(rotation=90)
# plt.show()

# #Creating a Scatterplot
# colormap=np.array(["r","g","b"])
# df.plot.scatter(x="State", y="2019 Urban Fatal. Num.", fontsize=5)
# plt.xticks(rotation=90)
# plt.show()

# # bar graph for Rural Fatalities in 2018
# df = df.sort_values(by="2019 Rural Fatal. Num.", ascending=False)
# x3 = df["State"]
# y3= df["2019 Rural Fatal. Num."]
# plt.barh(x3, y3, color ='green')
# plt.title("2019 Rural Fatalities per State ")
# plt.xlabel("Number of Fatalities Per 100,000")
# plt.ylabel("States")
# plt.show()

# # bar graph for Urban Fatalities in 2018
# df = df.sort_values(by="2019 Urban Fatal. Num.", ascending=False)
# x4 = df["State"]
# y4= df["2019 Urban Fatal. Num."]
# plt.barh(x4, y4, color ='grey')
# plt.title("2019 Urban Fatalities per State ")
# plt.xlabel("Number of Fatalities Per 100,000")
# plt.ylabel("States")
# plt.show()

# # bar graph for Rural Fatalities in 2019
# df = df.sort_values(by="2018 Rural Fatal.", ascending=False)
# x5 = df["State"]
# y5= df["2018 Rural Fatal."]
# plt.barh(x5, y5, color ='green')
# plt.title("2018 Rural Fatalities per State ")
# plt.xlabel("Number of Fatalities Per 100,000")
# plt.ylabel("States")
# plt.show()

# # bar graph for Urban Fatalities in 2019
# df = df.sort_values(by="2018 Urban Fatal.", ascending=False)
# x6 = df["State"]
# y6= df["2018 Urban Fatal."]
# plt.barh(x6, y6, color ='grey')
# plt.title("2018 Urban Fatalities per State ")
# plt.xlabel("Number of Fatalities Per 100,000")
# plt.ylabel("States")
# plt.show()

# # bar graph for Rural Fatalities in 2019
# df = df.sort_values(by="2019 AID Fatal. Num.", ascending=False)
# x7 = df["State"]
# y7= df["2019 AID Fatal. Num."]
# plt.barh(x7, y7, color ='red')
# plt.title("2019 Alcohol-Induced-Driving Fatalities per State ")
# plt.xlabel("Number of Fatalities Per 100,000")
# plt.ylabel("States")
# plt.show()

# # bar graph for Total Fatalities in 2018
# df5 = df.sort_values(by="2019 Population", ascending=False)
# topFiveC1 = df5.head(5)
# print(topFiveC1)
# x8 = topFiveC1["State"]
# y8= topFiveC1["2019 Population"]
# plt.bar(x8, y8, color ='blue')
# plt.title("2019 State Population")
# plt.xlabel("States")
# plt.ylabel("Population")
# # def addlabels(x,y):
# #     for i in range(len(x1)):
# #         plt.text(i,y.iloc[i],y.iloc[i], ha = 'center')
# # addlabels(x1,y1)
# plt.show()