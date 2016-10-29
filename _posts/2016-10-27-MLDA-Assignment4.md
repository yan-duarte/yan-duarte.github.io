---
title: 'Assignment 4: Running a k-means Cluster Analysis'
date: '2016-10-27 20:00:00 -0300'
categories:
  - Machine Learning for Data Analysis
tags:
  - Machine Learning for Data Analysis
published: true
---

This is the last assignment for the machine learning for data analysis course, fourth from a series of five courses from Data Analysis and Interpretation ministered by Wesleyan University.
The previous content you can see [here](https://yan-duarte.github.io/tags/).

In this assignment, we have to run a k-means Cluster Analysis.

My response variable is the number of new cases of breast cancer in 100,000 female residents during the year 2002 (breastCancer100th).
My first explanatory variable is the mean of sugar consumption quantity (grams per person and day) between the years 1961 and 2002.
My second explanatory variable is the mean of the total supply of food (kilocalories / person & day) available in a country, divided by the population and 365 between the years 1961 and 2002.
My third explanatory variable is the average of the mean TC (Total Cholesterol) of the female population, counted in mmol per L; (calculated as if each country has the same age composition as the world population) between the years 1980 and 2002.

All variables used in this assignment are quantitative.

All of the images posted in the blog can be better view by clicking the right button of the mouse and opening the image in a new tab.

The complete program for this assignment can be download [here](https://yan-duarte.github.io/archives/mlda-assignment4.py) and the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv).

You also can run the code using jupyter notebook by clicking [here](https://github.com/yan-duarte/yan-duarte.github.io/blob/master/archives/mlda-ass4.ipynb){:target="_blank"}.

## **Running a k-means Cluster Analysis**

The first thing to do is to import the libraries and prepare the data to be used.

```python
import pandas
import statistics
import numpy as np
import matplotlib.pylab as plt
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
from sklearn.cluster import KMeans

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x)

#load the data
data = pandas.read_csv('separatedData.csv')

# convert to numeric format
data["breastCancer100th"] = pandas.to_numeric(data["breastCancer100th"], errors='coerce')
data["meanSugarPerson"]   = pandas.to_numeric(data["meanSugarPerson"], errors='coerce')
data["meanFoodPerson"]   = pandas.to_numeric(data["meanFoodPerson"], errors='coerce')
data["meanCholesterol"]   = pandas.to_numeric(data["meanCholesterol"], errors='coerce')

# listwise deletion of missing values
sub1 = data[['breastCancer100th', 'meanFoodPerson', 'meanCholesterol', 'meanSugarPerson']].dropna()

#Split into training and testing sets
cluster = sub1[[ 'meanSugarPerson', 'meanFoodPerson', 'meanCholesterol', 'breastCancer100th']]

# standardize predictors to have mean=0 and sd=1
clustervar = cluster.copy()
clustervar['meanSugarPerson']=preprocessing.scale(clustervar['meanSugarPerson'].astype('float64'))
clustervar['meanFoodPerson']=preprocessing.scale(clustervar['meanFoodPerson'].astype('float64'))
clustervar['meanCholesterol']=preprocessing.scale(clustervar['meanCholesterol'].astype('float64'))
clustervar['breastCancer100th']=preprocessing.scale(clustervar['breastCancer100th'].astype('float64'))

# split data into train and test sets - Train = 70%, Test = 30%
clus_train, clus_test = train_test_split(clustervar, test_size=.3, random_state=123)
```

To run the k-means Cluster Analysis we must standardize the predictors to have mean = 0 and standard deviation = 1. After that, we make 9 analysis with the data, the first one with one cluster increasing a cluster per experiment.

```python
# k-means cluster analysis for 1-9 clusters
from scipy.spatial.distance import cdist
clusters=range(1,10)
meandist=[]

for k in clusters:
    model=KMeans(n_clusters=k)
    model.fit(clus_train)
    clusassign=model.predict(clus_train)
    meandist.append(sum(np.min(cdist(clus_train, model.cluster_centers_, 'euclidean'), axis=1))
    / clus_train.shape[0])

"""
Plot average distance from observations from the cluster centroid
to use the Elbow Method to identify number of clusters to choose
"""

plt.plot(clusters, meandist)
plt.xlabel('Number of clusters')
plt.ylabel('Average distance')
plt.title('Selecting k with the Elbow Method')
```

![#fig_1]({{site.baseurl}}/yan-duarte.github.io/images/mlda-assignments/mlda-ass4-fig1.png)

*This plot shows the decrease in the average minimum distance of the observations from the cluster centroids for each of the cluster solutions. We can see that the average distance decreases as the number of clusters increases. Since the goal of cluster analysis is to minimize the distance between observations and their assigned clusters we want to chose the fewest numbers of clusters that provides a low average distance. What we're looking for in this plot is a bend in the elbow that kind of shows where the average distance value might be leveling off such that adding more clusters doesn't decrease the average distance as much.*

In our case, the bend in the elbow appears to be at two clusters and at three clusters.

To help us figure out which of the solutions is best we should we are going to use the canonical discriminate analysis.

