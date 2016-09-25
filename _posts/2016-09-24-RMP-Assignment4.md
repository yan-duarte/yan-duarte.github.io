---
title: 'Assignment 4: Test a Logistic Regression Model'
date: '2016-09-24 18:10:00 -0300'
categories:
  - Regression Modeling Practice
tags:
  - Regression Modeling Practice
published: true
---
This is the last assignment for the regression modeling practice course, third from a series of five courses from Data Analysis and Interpretation ministered from Wesleyan University.
The previous content you can see [here](https://yan-duarte.github.io/tags/).

In this assignment, we have to Test a Logistic Regression Model with our data.

My response variable is the number of new cases of breast cancer in 100,000 female residents during the year 2002 (breastCancer100th).
My explanatory variable is the mean of sugar consumption quantity (grams per person and day) between the years 1961 and 2002 (meanSugarPerson).

To make the assignment of this week I have added two other explanatory variables:  
  
  - Mean of the total supply of food (kilocalories / person & day) available in a country, divided by the population and 365 (the number of days in the year) between the years 1961 and 2002 (meanFoodPerson).
  - The average of the mean TC (Total Cholesterol) of the female population, counted in mmol per L; (calculated as if each country has the same age composition as the world population) between the years 1980 and 2002 (meanCholesterol).

Note that all off my variables are quantitative. Thus, I management they transforming it to qualitative.

All of the images posted in the blog can be better view by clicking the right button of the mouse and opening the image in a new tab.

The complete program for this assignment can be download [here](https://yan-duarte.github.io/archives/rmp-assignment4.py) and the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv).

## **Contents of variables**

Variable breastCancer100th:

  - (0) The incidence of breast cancer is below the average of the incidence of all countries.
  - (1) The incidence of breast cancer is above the average of the incidence of all countries.
    
Variable meanSugarPerson:
  
  - (0) Desirable 0 and 30 g.
  - (1) Raised with 30 and 60 g.
  - (2) Borderline high 60 and 90 g.
  - (3) High between 90 and 120 g.
  - (4) Very high under 120g.
  
Variable meanFoodPerson:
  
  - (0) The food consumption below the average of the food consumption of all countries.
  - (1) The food consumption above the average of the food consumption of all countries.
  
Variable meanCholesterol:
  
  - (0) Desirable below 5.2 mmol/L
  - (1) Borderline high between 5.2 and 6.2 mmol/L
  - (2) High above 6.2 mmol/L __*__
  
__*__ There is no data in the dataset that has a cholesterol in blood above 6.2, so I only used the two first categories.

## **Test a Logistic Regression Model**

The first thing to do is to import the libraries and prepare the data to be used.

```python
import numpy
import pandas
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn
import statistics

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
sub1 = data[['breastCancer100th', 'meanSugarPerson', 'meanFoodPerson', 'meanCholesterol']].dropna()

# Create the conditions to a new variable named sugar_consumption that will categorize the meanSugarPerson answers
meanIncidence = statistics.mean(sub1['breastCancer100th'])

def incidence_cancer (row):
    if row['breastCancer100th'] <= meanIncidence : return 0   # Incidence of breast cancer is below the average of the incidence of all countries.
    if row['breastCancer100th'] > meanIncidence  : return 1   # incidence of breast cancer is above the average of the incidence of all countries.

# Add the new variable sugar_consumption to subData
sub1['incidence_cancer'] = sub1.apply (lambda row: incidence_cancer (row),axis=1)

# Create the conditions to a new variable named sugar_consumption that will categorize the meanSugarPerson answers
def sugar_consumption (row):
   if 0 < row['meanSugarPerson'] <= 30 : return 0    # Desirable between 0 and 30 g.
   if 30 < row['meanSugarPerson'] <= 60 : return 1   # Raised between 30 and 60 g.
   if 60 < row['meanSugarPerson'] <= 90 : return 2   # Borderline high between 60 and 90 g.
   if 90 < row['meanSugarPerson'] <= 120 : return 3  # High between 90 and 120 g.
   if row['meanSugarPerson'] > 120 : return 4        # Very high under 120g.

# Add the new variable sugar_consumption to subData
sub1['sugar_consumption'] = sub1.apply (lambda row: sugar_consumption (row),axis=1)

# Create the conditions to a new variable named food_consumption that will categorize the meanFoodPerson answers
meanFood = statistics.mean(sub1['meanFoodPerson'])

def food_consumption (row):
    if row['meanFoodPerson'] <= meanIncidence : return 0   # food consumption below the average of the food consumption of all countries.
    if row['meanFoodPerson'] > meanIncidence  : return 1   # food consumption above the average of the food consumption of all countries.

# Add the new variable food_consumption to subData
sub1['food_consumption'] = sub1.apply (lambda row: food_consumption (row),axis=1)

# Create the conditions to a new variable named cholesterol_blood that will categorize the meanCholesterol answers
def cholesterol_blood (row):

   if row['meanCholesterol'] <= 5.2 : return 0         # (0) Desirable below 5.2 mmol/L
   if 5.2 < row['meanCholesterol'] <= 6.2 : return 1   # (1) Borderline high between 5.2 and 6.2 mmol/L
   if row['meanCholesterol'] > 6.2 : return 2          # (2) High above 6.2 mmol/L

# Add the new variable sugar_consumption to subData
sub1['cholesterol_blood'] = sub1.apply (lambda row: cholesterol_blood (row),axis=1)
```

The code to make the Logistic Regression model and the odds ratios

```python
# Logistic Regression analysis
lreg1 = smf.logit(formula = 'incidence_cancer ~ sugar_consumption + food_consumption + cholesterol_blood', data = sub1).fit()
print (lreg1.summary())

# odd ratios with 95% confidence intervals
params = lreg1.params
conf = lreg1.conf_int()
conf['OR'] = params
conf.columns = ['Lower CI', 'Upper CI', 'OR']
print (numpy.exp(conf))

```

```
                           Logit Regression Results                           
==============================================================================
Dep. Variable:       incidence_cancer   No. Observations:                  129
Model:                          Logit   Df Residuals:                      125
Method:                           MLE   Df Model:                            3
Date:                Sat, 24 Sep 2016   Pseudo R-squ.:                  0.5627
Time:                        20:26:10   Log-Likelihood:                -35.268
converged:                       True   LL-Null:                       -80.654
                                        LLR p-value:                 1.496e-19
==============================================================================
                        coef  std err        z    P>|z|    [95.0% Conf. Int.]
------------------------------------------------------------------------------
Intercept            -4.9331    1.049   -4.705    0.000      -6.988    -2.878
sugar_consumption     0.5915    0.317    1.864    0.062      -0.031     1.214
food_consumption      3.0577    0.827    3.696    0.000       1.436     4.679
cholesterol_blood     2.1235    0.650    3.267    0.001       0.849     3.398
==============================================================================

                   Lower CI  Upper CI    OR
Intercept              0.00      0.06  0.01
sugar_consumption      0.97      3.37  1.81
food_consumption       4.20    107.69 21.28
cholesterol_blood      2.34     29.90  8.36

```

After adding the variables food_consumption and cholesterol_blood, the variable sugar_consumption becomes a confounding variable beeing not significant for the comparison.

The odds of the greatest incidence of new breast cancer cases were higher for countries with a big food consumption (OR=21.28, 95% CI = 1.436-4.679, p>.0001). 
We can say that countries that have a bigger food consumption are 21.28 times more likely to have a great incidence of breast cancer.

For the cholesterol in the blood, the results were OR=8.36, 95% CI = 0.849-3.398, p=.0001. 
So, counties that have a borderline high cholesterol in the blood are 8.36 times more likely to have a big incidence of breast cancer than countries that the population has a desirable amount of cholesterol in the blood.

The hypothesis that the sugar consumption would increase the incidence of cancer become unacceptable because the sugar consumption becomes a confounding variable for this model. Therefore, we saw that either the food consumption and the cholesterol in the blood are significant variables for the work.


