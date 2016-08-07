---
published: true
date: '2016-08-07 17:20:00 -0300'
Name:
  - Assignment: Generating a Correlation Coefficient
categories:
  - Data Analysis Tools
tags:
  - Data Analysis Tools
title: 'Assignment 3: Generating a Correlation Coefficient'
---
This is the third assignment for the data analysis tool course, second of a series of five courses from Data Analysis and Interpretation ministered from Wesleyan University.
The previous content you can see [here](https://yan-duarte.github.io/tags/#Data Management and Visualization).

For this assignment, we have to generate a correlation coefficient test in our data.
The data that I am using is adapted from gapminder and both of my variables (response and explanatory) are already quantitative.
The response variable is the incidence of new breast cancer in 100,000 female residents during the 2002 year while the explanatory variable is the mean of the sugar consumption (grams per person and day) between 1961 and 2002.
 
The hypothesis that is being approached is that the higher quantity of sugar consumption in countries increases the incidence of new breast cancer cases.

The complete program for this assignment can be download [here](https://yan-duarte.github.io/archives/dat-assignment3.py) and the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv).


## **Correlation Coefficient**

Below is the code to make the Correlation Coefficient technique:

First I have imported the libraries, management the data and created the scatterplot graph of my variables.

```python
import pandas
import numpy
import statistics
import seaborn
import matplotlib.pyplot as plt
import scipy

# Import the data set to memory
data = pandas.read_csv("separatedData.csv", low_memory = False)

# Change data type among variables to numeric
data["breastCancer100th"] = data["breastCancer100th"].convert_objects(convert_numeric=True)
data["meanSugarPerson"]   = data["meanSugarPerson"].convert_objects(convert_numeric=True)

# Create a subData with only the variables breastCancer100th, meanSugarPerson, meanFoodPerson, meanCholesterol
sub1 = data[['breastCancer100th','meanSugarPerson']]

# Bivariate Scatterplot Q->Q -  Incidence of breast cancer versus sugar consumption
scat1 = seaborn.regplot(x="meanSugarPerson", y="breastCancer100th", fit_reg=True, data=sub1)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
plt.title('Scatterplot for the association between the incidence of breast cancer and the sugar consumption.')
plt.show()
```

![Figure 1]({{site.baseurl}}/yan-duarte.github.io/images/dat-assignment3/dat-ass3-fig1.png)

After that, I made the correlation coefficient.

```python 
print ('association between meanSugarPerson and breastCancer100th')
print (scipy.stats.pearsonr(sub1['meanSugarPerson'], sub1['breastCancer100th']))
```

```
association between meanSugarPerson and breastCancer100th
(0.64050235531179356, 2.9900485245592816e-16)
```



