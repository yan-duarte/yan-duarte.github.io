---
title: 'Assignment 2: Test a Basic Linear Regression Model'
date: '2016-09-10 18:40:00 -0300'
categories:
  - Regression Modeling Practice
tags:
  - Regression Modeling Practice
published: true
---
This is the second assignment for the regression modeling practice course, third from a series of five courses from Data Analysis and Interpretation ministered from Wesleyan University.
The previous content you can see [here](https://yan-duarte.github.io/tags/).

In this assignment, we have to Test a Basic Linear Regression Model with our data.

To do that, one management with the data must be done. As both explanatory and response variable are quantitative the only modification to do is to center in the mean the explanatory variable by subtracting the mean from the data values, then the value 0 will be the mean.


## **Test a Basic Linear Regression Model**


```python
import pandas
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn
import matplotlib.pyplot as plt
import statistics

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x)

# Import the data set to memory
data = pandas.read_csv("separatedData.csv", low_memory = False)

# Change data type among variables to numeric
data["breastCancer100th"] = data["breastCancer100th"].convert_objects(convert_numeric=True)
data["meanSugarPerson"]   = data["meanSugarPerson"].convert_objects(convert_numeric=True)

# Create a subData with only the variables breastCancer100th, meanSugarPerson, meanFoodPerson, meanCholesterol
sub1 = data[['breastCancer100th','meanSugarPerson']]

#If you have a quantitative explanatory variable, center it so that the mean = 0 (or really close to 0) by subtracting the mean, and then calculate the mean to check your centering.
mean = statistics.mean(sub1['meanSugarPerson'])
sub1['meanSugarPerson'] = sub1['meanSugarPerson'] - mean

# BASIC LINEAR REGRESSION
scat1 = seaborn.regplot(x="meanSugarPerson", y="breastCancer100th", scatter=True, data=data)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
plt.title('Scatterplot for the association between the incidence of breast cancer and the sugar consumption.')
plt.show()

print(scat1)

print ("OLS regression model for the association between incidence of breast cancer and the sugar consumption")
reg1 = smf.ols('breastCancer100th ~ meanSugarPerson', data=data).fit()
print (reg1.summary())
```

```
OLS regression model for the association between incidence of breast cancer and the sugar consumption
                            OLS Regression Results                            
==============================================================================
Dep. Variable:      breastCancer100th   R-squared:                       0.410
Model:                            OLS   Adj. R-squared:                  0.406
Method:                 Least Squares   F-statistic:                     88.34
Date:                Sat, 10 Sep 2016   Prob (F-statistic):           2.99e-16
Time:                        19:16:04   Log-Likelihood:                -560.18
No. Observations:                 129   AIC:                             1124.
Df Residuals:                     127   BIC:                             1130.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
===================================================================================
                      coef    std err          t      P>|t|      [95.0% Conf. Int.]
-----------------------------------------------------------------------------------
Intercept          10.0325      3.402      2.949      0.004         3.301    16.764
meanSugarPerson     0.3667      0.039      9.399      0.000         0.289     0.444
==============================================================================
Omnibus:                        3.414   Durbin-Watson:                   1.778
Prob(Omnibus):                  0.181   Jarque-Bera (JB):                3.052
Skew:                           0.291   Prob(JB):                        0.217
Kurtosis:                       2.522   Cond. No.                         180.
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```