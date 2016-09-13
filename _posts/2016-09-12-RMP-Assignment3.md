---
title: 'Assignment 3: Test a Multiple Regression Model'
date: '2016-09-12 19:20:00 -0300'
categories:
  - Regression Modeling Practice
tags:
  - Regression Modeling Practice
published: true
---
This is the third assignment for the regression modeling practice course, third from a series of five courses from Data Analysis and Interpretation ministered from Wesleyan University.
The previous content you can see [here](https://yan-duarte.github.io/tags/).

In this assignment, we have to Test a Basic Multiple Regression Model with our data.

For my response variable is the number of new cases of breast cancer in 100,000 female residents during the year 2002.
My explanatory variable is the mean of sugar consumption quantity (grams per person and day) between the years 1961 and 2002.

To make the assignment of this week I have add two other explanatory variables:
  
  - Mean of the total supply of food (kilocalories / person & day) available in a country, divided by the population and 365 (the number of days in the year) between the years 1961 and 2002.
  - The average of the mean TC (Total Cholesterol) of the female population, counted in mmol per L; (calculated as if each country has the same age composition as the world population) between the years 1980 and 2002.

Note that all my explanatories variables are quantitative. Thus, I must center the variables by subtracting the mean from the data values, then the value 0 will be very close to the mean. 

The complete program for this assignment can be download [here](https://yan-duarte.github.io/archives/rmp-assignment3.py) and the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv).

## **Test a Multiple Regression Model**

```python
import numpy
import pandas
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn

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
```

```python
# first order (linear) scatterplot
scat1 = seaborn.regplot(x="meanSugarPerson", y="breastCancer100th", scatter=True, data=sub1)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
```

```python
# fit second order polynomial
# run the 2 scatterplots together to get both linear and second order fit lines
scat1 = seaborn.regplot(x="meanSugarPerson", y="breastCancer100th", scatter=True, order=2, data=sub1)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
```

```python
# center quantitative IVs for regression analysis
sub1['meanSugarPerson_c'] = (sub1['meanSugarPerson'] - sub1['meanSugarPerson'].mean())
sub1['meanFoodPerson_c']  = (sub1['meanFoodPerson'] - sub1['meanFoodPerson'].mean())
sub1['meanCholesterol_c']   = (sub1['meanCholesterol'] - sub1['meanCholesterol'].mean())
sub1[["meanSugarPerson_c", "meanFoodPerson_c", 'meanCholesterol_c']].describe()

# linear regression analysis
reg1 = smf.ols('breastCancer100th ~ meanSugarPerson_c', data=sub1).fit()
print (reg1.summary())
```

```
OLS Regression Results                            
==============================================================================
Dep. Variable:      breastCancer100th   R-squared:                       0.410
Model:                            OLS   Adj. R-squared:                  0.406
Method:                 Least Squares   F-statistic:                     88.34
Date:                Mon, 12 Sep 2016   Prob (F-statistic):           2.99e-16
Time:                        23:15:22   Log-Likelihood:                -560.18
No. Observations:                 129   AIC:                             1124.
Df Residuals:                     127   BIC:                             1130.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
=====================================================================================
                        coef    std err          t      P>|t|      [95.0% Conf. Int.]
-------------------------------------------------------------------------------------
Intercept            37.9876      1.651     23.007      0.000        34.720    41.255
meanSugarPerson_c     0.3667      0.039      9.399      0.000         0.289     0.444
==============================================================================
Omnibus:                        3.414   Durbin-Watson:                   1.778
Prob(Omnibus):                  0.181   Jarque-Bera (JB):                3.052
Skew:                           0.291   Prob(JB):                        0.217
Kurtosis:                       2.522   Cond. No.                         42.3
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

```

```python
# quadratic (polynomial) regression analysis
reg2 = smf.ols('breastCancer100th ~ meanSugarPerson_c + I(meanSugarPerson_c**2)', data=sub1).fit()
print (reg2.summary())
```

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:      breastCancer100th   R-squared:                       0.430
Model:                            OLS   Adj. R-squared:                  0.421
Method:                 Least Squares   F-statistic:                     47.52
Date:                Mon, 12 Sep 2016   Prob (F-statistic):           4.18e-16
Time:                        23:15:22   Log-Likelihood:                -557.98
No. Observations:                 129   AIC:                             1122.
Df Residuals:                     126   BIC:                             1131.
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
=============================================================================================
                                coef    std err          t      P>|t|      [95.0% Conf. Int.]
---------------------------------------------------------------------------------------------
Intercept                    34.4829      2.339     14.742      0.000        29.854    39.112
meanSugarPerson_c             0.3680      0.039      9.556      0.000         0.292     0.444
I(meanSugarPerson_c ** 2)     0.0020      0.001      2.089      0.039         0.000     0.004
==============================================================================
Omnibus:                        1.821   Durbin-Watson:                   1.808
Prob(Omnibus):                  0.402   Jarque-Bera (JB):                1.520
Skew:                           0.263   Prob(JB):                        0.468
Kurtosis:                       3.075   Cond. No.                     3.58e+03
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.58e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```


Summarize what you found. Discuss the results for the associations between all of your explanatory variables and your response variable. Make sure to include statistical results (Beta coefficients and p-values) in your summary.


Report whether or not your results supported your hypothesis for the association between your primary explanatory response variable.


Discuss whether or not there was evidence of confounding for the association between your primary explanatory and response variable.


Generate regression diagnostic plots and write a few sentences describing what these plots tell you about your regression model in terms of the distribution of the residuals, model fit, influential observations, and outliers.


Include your multiple regression output in your blog.
