#!/usr/bin/env python
# coding: utf-8

# In[4]:


# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


#Load Dataset
filename = 'supermarket_sales data.csv'
df = pd.read_csv(filename)

#Checking for Null Values
null_value_count = df.isnull().sum()
print(f"\nNull value count in {filename}:")
print(null_value_count)


# In[6]:


#Checking for duplicates
duplicate_count = df[df.duplicated()].count()
print(f"\nDuplicate rows count in {filename}:")
print(duplicate_count)


# In[67]:


df['Product line'].unique()


# In[28]:


df.shape


# In[29]:


#Which branch has the most sales?
#Which product line sells the most? 
#How do sales vary across different cities? 
#What is the gross income per month?


# In[78]:


#Subset
Salesperbranch_df = df[['Branch', 'Total']]
Productline_df = df[['Product line', 'Quantity']]
Cities_df = df[['City', 'Total']]

# Sort the DataFrame by Quantity in descending order
quantity_per_product_sorted = quantity_per_product.sort_values(by='Quantity', ascending=False)


# In[84]:


# Extract month from the 'Date' column and calculate gross income per month
df['Month_Name'] = df['Date'].dt.strftime('%B')
monthly_gross_income = df.groupby('Month_Name')['gross income'].sum() # Calculate sum of gross income for each month

# Filter data for each month (January, February, March) and aggregate sales per day
january_sales = df[df['Month_Name'] == 'January'].groupby('Date')['Total'].sum()
february_sales = df[df['Month_Name'] == 'February'].groupby('Date')['Total'].sum()
march_sales = df[df['Month_Name'] == 'March'].groupby('Date')['Total'].sum()

print(march_sales)


# In[37]:


#Problem 1 - Which branch has the most sales?
# Set seaborn style
sns.set(style="whitegrid")

# Order of the branches
branch_order = ['A', 'B', 'C']

# Bar plot using Seaborn with specified branch order
plt.figure(figsize=(8, 7))
ax = sns.barplot(x='Branch', y='Total', data=Salesperbranch_df, estimator=sum, order=branch_order, errorbar=None)

# Annotate total sales value for each branch with dollar sign and digit separator
for p in ax.patches:
    ax.annotate(f"${p.get_height():,.2f}", 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 10), 
                textcoords='offset points')

plt.title('Total Sales per Branch')
plt.xlabel('Branch')
plt.ylabel('Total Sales')
plt.show()


# In[49]:


# Create a vertical bar plot using Seaborn with custom color palette and without error bars
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='City', y='Total', data=Cities_df, estimator=sum, errorbar=None)

#Annotate values
for p in ax.patches:
    ax.annotate(f"${p.get_height():,.2f}", 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 10), 
                textcoords='offset points')
plt.title('Total Sales per City')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()


# In[81]:


# Create a horizontal bar plot using Seaborn after sorting the data
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Quantity', y='Product line', data=quantity_per_product_sorted, orient='h', estimator=sum, errorbar= None)
plt.title('Total Quantity Sales per Product Line (Highest to Lowest)')
plt.xlabel('Quantity')
plt.ylabel('Product Line')

# Annotate total quantity per product line
for p in ax.patches:
    ax.annotate(f"{p.get_width():.0f}",
                (p.get_width(), p.get_y() + p.get_height() / 2.),
                ha='left', va='center',
                xytext=(5, 0),
                textcoords='offset points')

plt.show()


# In[75]:


# Define the order of months
month_order = ['January', 'February', 'March']

# Sort the monthly_gross_income Series based on the custom order of months
monthly_gross_income = monthly_gross_income.reindex(month_order)

# Plotting the bar plot with sorted months
plt.figure(figsize=(10, 6))
ax = sns.barplot(x=monthly_gross_income.index, y=monthly_gross_income.values)

# Annotate the values with dollar sign
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f"${height:,.2f}", 
                (p.get_x() + p.get_width() / 2., height), 
                ha='center', va='center', 
                xytext=(0, 5), 
                textcoords='offset points', 
                fontsize=10)

plt.title('Monthly Gross Income')
plt.xlabel('Month')
plt.ylabel('Total Gross Income')

plt.grid(True)
plt.show()


# In[65]:


# Plot for January
plt.figure(figsize=(10, 6))
january_sales.plot(kind='line', color='blue', marker='o')
plt.title('Overall Daily Sales Trend - January')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# Plot for February
plt.figure(figsize=(10, 6))
february_sales.plot(kind='line', color='red', marker='o')
plt.title('Overall Daily Sales Trend - February')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# Plot for March
plt.figure(figsize=(10, 6))
march_sales.plot(kind='line', color='green', marker='o')
plt.title('Overall Daily Sales Trend - March')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:




