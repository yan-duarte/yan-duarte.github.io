---
published: true
date: '2016-08-19 10:30:00 -0300'
Name:
  - Assignment: Testing a Potential Moderator
categories:
  - Data Analysis Tools
tags:
  - Data Analysis Tools
title: 'Assignment 4: Testing a Potential Moderator'
---
This is the last assignment for the data analysis tool course, second of a series of five courses from Data Analysis and Interpretation ministered from Wesleyan University.
The previous content you can see [here](https://yan-duarte.github.io/tags/#Data Management and Visualization).

In this assignment, we can choose to run an ANOVA, Chi-Square test or correlation coefficient that includes a moderator. I have chosen to run the correlation coefficient with the moderator. 
The data that I am using is adapted from gapminder and both of my variables (response and explanatory) are already quantitative. 
The response variable is the incidence of new breast cancer in 100,000 female residents during the 2002 year while the explanatory variable is the mean of the sugar consumption (grams per person and day) between 1961 and 2002. 
To the moderator, I am using the mean of the total supply of food (kilocalories / person & day) available in a country divided by the population and 365 (the number of days in the year) between the years 1961 and 2002. This variable is subdivided in three categories:

  - 0: Low food consumption;
  - 1: Middle food consumption;
  - 2: High food consumption.

With this, we can create the question for the work: Does the food consumption moderate the relationship between the sugar consumption and the incidence of breast cancer?
So, the hypothesis for this assignment suggest that this relation is true.

The complete program for this assignment can be download [here](https://yan-duarte.github.io/archives/dat-assignment4.py) and the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv).


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

We get a correlation coefficient of 0.64050235531179356 and a p-value of 2.9900485245592816e-16.
This indicates to us that the relationship between the sugar consumption and the incidence of breast cancer is strong and it is also positive as the scatterplot has already shown us.

To help us to understand the correlation between the two variables we can square the correlation coefficient. This will result in the value 0.41024326716. This can be interpleted in the following way: If we know the sugar consumption grams per day of an woman we can predict 41% of the variability we will see in the incidence of breast cancer cases.