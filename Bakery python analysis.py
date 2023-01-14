#v.1.1.1
#%%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import os
from tqdm import tqdm
# %%
#Output File
check = 0
for i in tqdm(range(len(os.listdir())),desc = "Checking for 'Output Folder'"):
    if os.listdir()[i] == "Output":
        check = check + 1
if check != 1:
    os.mkdir("Output")    
# %%
#Load backery file as a Dataframe & change df columns names
df = pd.read_csv("./Bakerysales.csv",usecols=["date","time","article","Quantity","unit_price","ticket_number"])
df = df.rename(columns={"article":"product","Quantity":"quantity", "unit_price":"unit_price_EUR"})

df[["unit_price_EUR","unit_price_EUR2"]] = df["unit_price_EUR"].str.split(pat= " ",expand = True)

df[["unit_price_EUR","unit_price_EUR2"]] = df["unit_price_EUR"].str.split(pat= "," ,expand = True) 

#combine data
df["unit_price_EUR"] = df["unit_price_EUR"] + "." + df["unit_price_EUR2"]

#change data type
df['date'] = pd.to_datetime(df['date'])
df['time'] = pd.to_datetime(df['time'])
df["unit_price_EUR"] = df["unit_price_EUR"].astype(float)
df = df.astype({"product":"string"})

#remove exsess column 
df = df.drop(["unit_price_EUR2"], axis=1)

print(df.dtypes)
df.head()


#%% 
#Slicing to make a siries from the product colomn
slicingProductColumn = df["product"]
print(slicingProductColumn.head())
# %%
#Slicing to make an new data frame of Product
newDf = df[["product"]]
print(newDf.head())
# %%
#Slicing df for "BAGUETTE" 
three = df[df["product"] == "BAGUETTE"]
three.to_excel(".\Output\SlicingArticleForBaguette.xlsx")
print(three.head())
# %%
#Bar Charts 
groupByDfProductQuantity = df.groupby(df['product'])["quantity"].sum()

data = groupByDfProductQuantity.to_frame()
data = groupByDfProductQuantity.reset_index()

plt.style.use("classic")

fig, barChart = plt.subplots(figsize=(20,30))

barChart.set_title('Products in Stock', fontweight='bold')
barChart.set_ylabel("Product Name", fontweight="bold")
barChart.set_xlabel("Number of Products in Stock",fontweight="bold")
barChart.grid()
barChart.xaxis.set_major_locator(ticker.MultipleLocator(5000))
barChart = barChart.barh(data["product"],data["quantity"], color="red",align="center")

plt.show()

os.chdir("Output")
fig.savefig("Bar_Chart_No._Products_in_Stock.pdf")
os.chdir("../")
# %%
#Pie Chart 
fig, pieChart = plt.subplots()
#figsize=(20,30)

pieChart.set_title("Pie Chart",fontweight="bold")
pieChart.pie(data["quantity"],labels= data["product"],labeldistance= 1.05,wedgeprops=dict(width=.60))

plt.show()

os.chdir("Output")
fig.savefig("Pie_Chart_No._Products_in_Stock.pdf")
os.chdir("../")


# %%
# Time V Amount Scatter Plot

data_Lables_of_Products = df[["product"]]
data_x = df[["date"]]
data_y = df[["unit_price_EUR"]]

fig, scatterPlot = plt.subplots(figsize=(14,4))
scatterPlot.set_title("Time V Amount Scatter Plot",fontweight="bold")
scatterPlot.scatter(data_x, data_y)

plt.show()

os.chdir("Output")
fig.savefig("Scatter_Chart_No._Products_in_Stock.pdf")
os.chdir("../")

# %%
