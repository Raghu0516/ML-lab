#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd 
df=pd.read_csv('studata.csv')
print("\n first five records:")
print(df.head())
print("\n last five records:")
print(df.tail())
print("\n total no.of rows and columns:",df.shape)
print("column names:",df.columns.tolist())
print("datatypes:",df.dtypes)
print(df.info())


# In[3]:


mean_attendance = df["Attendance"].mean()
print(mean_attendance)


# In[4]:


avg_internal = df["InternalMarks"].mean()
print(avg_internal)


# In[5]:


avg_external = df["ExternalMarks"].mean()
print(avg_external)


# In[7]:


max_internal = df["InternalMarks"].max()
print(max_internal)


# In[8]:


min_internal = df["InternalMarks"].min()
print(min_internal)


# In[10]:


max_external = df["ExternalMarks"].max()
print(max_external)


# In[11]:


min_external = df["ExternalMarks"].min()
print(min_external)


# In[12]:


std_internal = df["InternalMarks"].std()
print(std_internal)


# In[13]:


summary = df.describe()
print(summary)


# In[14]:


df["TotalMarks"] = df["InternalMarks"] + df["ExternalMarks"]



# In[16]:


df["Percentage"] = df["TotalMarks"]/100*100


# In[17]:


print(df.head())


# In[20]:


Nty_above = df[df["Percentage"] > 90]
print(Nty_above)


# In[21]:


print(df.loc[df["Percentage"] > 90, "Name"])


# In[25]:


print(df.loc[df["Gender"] =="F","Name"])


# In[26]:


print(df.loc[df["Gender"] =="M","Name"])


# In[27]:


df[df["ExternalMarks"] < 50]


# In[32]:


df.loc[df["TotalMarks"].idxmax(),"Name"]


# In[33]:


df.loc[df["TotalMarks"].idxmin(),"Name"]


# In[34]:


print(df.nlargest(3,"TotalMarks")["Name"])


# In[37]:


print(df.nsmallest(3,"TotalMarks")["Name"])


# In[39]:


avg_total = df["TotalMarks"].mean()
above_avg_students = df[df["TotalMarks"] > avg_total]
print(above_avg_students )


# In[44]:


avg_total_male = df.loc[df["Gender"] == "M", "TotalMarks"].mean()
print("Average TotalMarks (Male):", avg_total_male)


# In[45]:


avg_total_female= df.loc[df["Gender"] == "F", "TotalMarks"].mean()
print("Average TotalMarks (Female):", avg_total_female)


# In[46]:


avg_attendance = df.groupby("Gender")["Attendance"].mean()
print(avg_attendance)


# In[ ]:




