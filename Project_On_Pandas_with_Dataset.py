#!/usr/bin/env python
# coding: utf-8

# ## Pandas - Analysing DataFrames

# In[3]:


# to view the data ".head()" is used

import pandas as pd 
df = pd.read_csv('data.csv')
print(df.head(10))


# In[5]:


# to view the data from the last we can use 'tail()'
print(df.tail(10))


# In[6]:


print(df.info())


# The 'info()' method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "calories" column.

# #### data cleaning

# Data cleaning means fixing bad data in your data set.
# Bad data can be-1)emty cell, 2) data in wrong format, 3) wrong data, 4) duplicates
# 

# In[8]:


import pandas as pd 
df = pd.read_csv('dirtydata.csv') # importing different data set
print(df.info())


# In[10]:


print(df.to_string())  # .to_string() is used to show all data


# In[11]:




df.dropna(inplace = True)    # dropna(inplace = True) will not return new DataFrame, but it will remove all the rows containing NULL values from the original DataFrame.
print(df.to_string())


# #### Replace the Empty Values

# Another way of dealing with empty cell is to insert a new value instead.
# 
# The fillna() method allows us to replace empty cell with a value:
# 

# In[13]:


df = pd.read_csv('dirtydata.csv')
df.fillna(130, inplace = True)
print(df)


# #### replacing Only For Specified Columns

# In[15]:


import pandas as pd 
df = pd.read_csv('dirtydata.csv')
df["Calories"].fillna(130, inplace = True)
print(df)


# #### Replace Using Mean, Median, or Mode

# In[19]:


import pandas as pd 
df = pd.read_csv('dirtydata.csv')
x = df['Calories'].mean() # here .mean() is used to calculate mean of all values of Calories column
df["Calories"].fillna(x, inplace = True)
print(x)
print(df)


# In[23]:


# replacing by median
import pandas as pd 
df = pd.read_csv('dirtydata.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
print(f"median of Calories is {x}.")
print(df)


# In[28]:


# now inplacing with Mode

df = pd.read_csv('dirtydata.csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
print(x)
print(df.tail())


# In our raw dataframe there two cell of row of date having wrong format so we have to change it correctly or replace.
# 

# In[31]:


# to_datetime():  it is used to farmate the date and time
import pandas as pd
df = pd.read_csv("dirtydata.csv")
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())


#  Here in above result in row 22 still there is NaT(Not a Time) this can to be changed because it was not number
#  
#  So clean this data we have to remove this row 22

# In[32]:


df.dropna(subset = ['Date'], inplace = True)
print(df.to_string)


# In[33]:


x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
print(df.to_string)


# ### Replacing Values

# One way to fix wrong values is to replace with something else. Wrong values doesn't mean that it should be of wrong formate or wrong type, it can also be like unexpexted value like in our data set in duration column and at 7 row there is 450 which is looking like very big as comparision to other values in the duration column.
# 

# In[34]:


# by setting 450 to 45 only
df.loc[7,"Duration"] = 45
print(df)


# In[36]:


# in large dataset we can not go through above method because it will take very much time to search it

# by looping it will be easy

for x in df.index:
    if df.loc[x,"Duration"] > 100:
        df.loc[x, "Duration"] = 100
        
print(df.head(15))


# ### Removing rows

# In[37]:


# To handle wrong data we can also remove that wrong row
# delete the row in which duration is less than 30

for x in df.index:
    if df.loc[x, "Duration"] == 30: # here you can use any condition according to your convenience
        df.drop(x, inplace = True)
        
print(df)


# ### Discovering and Removing The Duplicates

# In Our Data set there is one duplicate of data in the row 11 and 12 which repeat itself

# In[38]:


# duplicated() method is used to find out the dupicate
print(df.duplicated())


# In[39]:


# Now We have find the duplicate which at 12th row
# now we have remove the duplicate
#  which can be done by drop_duplicates()

df.drop_duplicates(inplace = True)
print(df)


# ### Finding Relationships between the data

# In[41]:


# to find out the relation we have to use .corr()

df.corr()  # Note: The corr() method ignores "Not numeric" values


# In[ ]:





# In[ ]:





# In[ ]:





# ### Data Ploting

# In[44]:


import pandas as pd
import matplotlib.pyplot as plt   # to import matplot library

df = pd.read_csv("dataset.csv")
print(df)
df.plot()
plt.show()


# ### Scatter plot

# For Scatter plot we have define the x and y axis, so i am taking x = Duration and y = Calories.

# In[46]:


df.plot(kind = 'scatter', x = "Duration", y = "Calories") # here kind is used to for which type of plot do you want.
plt.show()


# In[47]:


df.plot(kind = 'scatter', x = 'Pulse', y = 'Maxpulse')
plt.show()


# ### Histogram plot

# Histogram plot takes only one column to plot and tell how data is varied
# 
# to plot a histogram we have tell that kind = 'hist'

# In[48]:


df["Calories"].plot(kind = 'hist')
plt.show()


# In[49]:


df["Duration"].plot(kind = 'hist')


# In[ ]:




