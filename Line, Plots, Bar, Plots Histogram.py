
# Packages / libraries
import os #provides functions for interacting with the operating system
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns #data visualisation libary based on matplotlib

#Load the raw data
url = 'https://raw.githubusercontent.com/Pitsillides91/Python-Tutorials/master/Seaborn%20Tutorial/Marketing%20Raw%20Data.csv'
raw_data=pd.read_csv(url,index_col=0,parse_dates=[0])

#run all the data
raw_data
#run the first 5 rows
(raw_data.head())
#shape
raw_data.shape


##LINE GRAPHS

#Investigte the revenue by Date

#ax = sns.lineplot(x = 'Date', y = 'Revenue', data=raw_data)
# Notes: error bands show the confidence interval
#ax = sns.lineplot(x = 'Week_ID', y = 'Revenue', data=raw_data)

# Example 2 - Adding Categories

# By Promo
#ax = sns.lineplot(x = 'Week_ID', y = 'Revenue', data = raw_data, hue = 'promo')

# Example 3 - By Promo with style
ax = sns.lineplot(x = 'Week_ID', y = 'Revenue', data = raw_data, hue = 'promo', style='promo')

# Example 4 - By Promo with style & Increase the size & Remove error bars
sns.set(rc=('figure.figsize':(12,10))
ax = sns.lineplot(x = 'Week_ID', y = 'Revenue', data = raw_data, hue = 'promo', style='promo', ci = False)

# increase the size
sns.set(rc=('figure.figsize':(12,10))
ax = sns.lineplot(x = 'Week_ID', y = 'Revenue', data = raw_data, hue = 'promo', style='promo')

# Example 5 - By Promo with style & Increase the size & Remove error bars & adding markers & by month
ax = sns.lineplot(x = 'Week_ID', y = 'Revenue', data = raw_data, hue = 'promo', style='promo', ci = False, markers = true)

# Example 6 - By Day_Name with style & Increase the size & Remove error bars & adding markers & by month
ax = sns.lineplot(x = 'month_ID', y = 'Revenue', data = raw_data, hue = 'Day_Name', style='promo', ci = False, markers = true)

# Example 7 - By Year with style & Increase the size & Remove error bars & adding markers & by month
ax = sns.lineplot(x = 'Year', y = 'Revenue', data = raw_data, hue = 'Day_Name', style='promo', ci = False, markers = true)

### BAR PLOTS
#
# Example 1 - Total Revenue by Month
ax= sns.barplot((x = 'Month_ID', y = 'Revenue', data = raw_data)

#cal the mean
raw_data[['revenue,'month_id]].groupby('month_id').agg(('revenue;mean'))

# Notes:
# 1 - the lines signify the confidence interval
# 2 - Takes mean by default

# create a df with the mean values

# Example 2 - Total Revenue by Month - Remove the Confidence Interval
ax= sns.barplot((x = 'Month_ID', y = 'Revenue', data = raw_data, ci=none)

# Example 3 - Total Revenue by Month - Remove the Confidence Interval - By Promo
ax= sns.barplot((x = 'Month_ID', y = 'Revenue', data = raw_data, ci=none, hue='promo')

# Example 4 - Total Revenue by Month - Remove the Confidence Interval - By Promo - Changing direction
ax= sns.barplot((x = 'Revenue', y = 'Month_ID', data = raw_data, ci=none, hue='promo', orient= 'h')

# Example 5 - Total Revenue by Month - Remove the Confidence Interval - By Promo - Changing direction - Changing Colour
ax= sns.barplot((x = 'Revenue', y = 'Month_ID', data = raw_data, ci=none, hue='promo', orient= 'h', colour = 'green')

# Cool Way to pick colours
# https://htmlcolorcodes.com/color-picker/

####Histograms
x = raw_data['Revenue'].values

# Example 1 - Investigating the distribution of Revenue
sns.distplot(x, color = blue)


# As you can see, it's a bit imbalance. Right skewd distribution as the mean is to the right
# Example 2 - Investigating the distribution of Revenue, adding the mean

# Calculating the mean
mean = raw_data['Revenue'].mean
sns.distplot(x, color = blue)
#ploting the mean
plt.axline(mean,0,1, color = red)

# Example 3 - Investigating the distribution of Visitors, adding the mean
x = raw_data['Visitors'].values

#ploting the mean


# Calculating the mean
mean= raw_data['Visitors'].mean
sns.distplot(x, color = red)
#ploting the mean
plt.axline(mean,0,1, color = black)


###Box Plots - Distributions
sns
# Example 1 - Investigating the distribution of Revenue
x = raw_data['Revenue'].values #create an array
sns.boxplot(x, color = blue)

#Increase the size
sns.set(rc=('figure.figsize':(12,10))
#Median
Median = raw_data['Revenue'].Median()
# Notes:
# The line signifies the median


PATH = "F:\\Github\\Python tutorials\\Introduction to Seaborn\\"
Image(filename = PATH + "Seaborn boxplot.png", width=900, height=900)

# More details here: https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51
# Credits: Michael Galarnyk

