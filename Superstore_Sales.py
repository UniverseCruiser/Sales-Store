## Sales Data Analysis

import pandas as pd
import os
import numpy as np


## Read in updated dataframe
  
  
all_data = pd.read_csv("Global Superstore.csv")
## all_data.head()

## Remove NaNs
nan_df = all_data[all_data.isna().any(axis=1)]
nan_df.head()

all_data = all_data.dropna(how='all')
all_data.head()


## Add Month Column
all_data['Month'] = all_data['Order Date'].str[3:5]
all_data['Month'] = all_data['Month'].astype('int32')
 
## Add a Sales column

 
all_data['Sales_Total'] = pd.to_numeric(all_data['Quantity']) * pd.to_numeric(all_data['Sales'])
all_data.head()

 

 
## Highest Sales Month
results = all_data.groupby('Month').sum()

import matplotlib.pyplot as plt

months = range(1,13)
plt.bar(months, results['Sales_Total'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month nunber')
plt.show()


## City by highest sales

results = all_data.groupby('City').sum()
results
 

import matplotlib.pyplot as plt

cities =  [city for city, df in all_data.groupby('City')]
plt.bar(cities, results['Sales_Total'])
plt.xticks(cities, rotation= 'vertical', size=8)
plt.ylabel('Sales in USD ($)')
plt.xlabel('City name')
plt.show()
 

# ## What time should we display advertisement to maximise likelihood of customer's buying product?

# all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
 
# all_data['Hour'] = all_data['Order Date'].dt.hour
# all_data['Minute'] = all_data['Order Date'].dt.minute

# hours = [hours for hours, df in all_data.groupby('Hour')]
# plt.plot(hours, all_data.groupby(['Hour']).count())
    
# plt.xticks(hours)
# plt.xlabel('Hour')
# plt.ylabel('Number of orders')   
# plt.grid()
# plt.show()

all_data = all_data.drop(columns='Hour')
all_data = all_data.drop(columns='Minute')
    
## What products are most often sold together?
from itertools import combinations
from collections import Counter
test_df = all_data
counts_df = test_df.groupby('Order ID')['Product Name'].agg(lambda x: list(combinations(x, 2)))\
    .apply(pd.Series).stack().value_counts().to_frame()\
    .reset_index().rename(columns={'index': 'Combination', 0:'Count'})
print(counts_df)

 


 





## What products sold the most and why do you think so?









