---
published: true
date: '2016-07-29 19:00:00 -0300'
Name:
  - Assignment: Running an analysis of variance
categories:
  - Data Analysis Tools
tags:
  - Data Analysis Tools
title: 'Assignment 1: Running an analysis of variance'
---
This is the first assignment for the data analysis tool course, second of a series of five courses from Data Analysis and Interpretation ministered from Wesleyan University.
The content of the first course you can see [here](https://yan-duarte.github.io/tags/#Data Management and Visualization).

For this assignment, we have to make the Analysis of Variance (ANOVA) in our data.
As I am already working with a quantitative response variable and a categorical explanatory variable, it is possible to use the ANOVA technique and, as the explanatory variable have five categories, it will be necessary to use the post hoc test for ANOVA.

The complete program for this assignment can be download [here](https://yan-duarte.github.io/archives/dat-assignment1.py) and the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv).


## **Analysis of Variance**

Below is the code to make the ANOVA technique:

First I have imported the libraries and management the data like in the other assignments presented until here.

```python
import pandas
import numpy
import statistics
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi

# Import the data set to memory
data = pandas.read_csv("separatedData.csv", low_memory = False)

# Change data type among variables to numeric
data["breastCancer100th"] = data["breastCancer100th"].convert_objects(convert_numeric=True)
data["meanSugarPerson"]   = data["meanSugarPerson"].convert_objects(convert_numeric=True)

# Create a subData with only the variables breastCancer100th, meanSugarPerson, meanFoodPerson, meanCholesterol
sub1=data[['breastCancer100th', 'meanSugarPerson']]

# Create the conditions to a new variable named sugar_consumption that will categorize the meanSugarPerson answers
def sugar_consumption (row):
   if 0 < row['meanSugarPerson'] <= 30 : return 0    # Desirable between 0 and 30 g.
   if 30 < row['meanSugarPerson'] <= 60 : return 1   # Raised between 30 and 60 g.
   if 60 < row['meanSugarPerson'] <= 90 : return 2   # Borderline high between 60 and 90 g.
   if 90 < row['meanSugarPerson'] <= 120 : return 3  # High between 90 and 120 g.
   if row['meanSugarPerson'] > 120 : return 4        # Very high under 120g.

# Add the new variable sugar_consumption to subData
sub1['sugar_consumption'] = sub1.apply (lambda row: sugar_consumption (row),axis=1)
```

Then I have created a new sub data and make the ANOVA method.

```python 
# creating a sub data with only the breast cancer cases and the sugar consumption mean
sub2 = sub1[['breastCancer100th', 'sugar_consumption']].dropna()

# using ols function for calculating the F-statistic and associated p value
model1 = smf.ols(formula='breastCancer100th ~ C(sugar_consumption)', data=sub2).fit()
print (model1.summary())
```

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:      breastCancer100th   R-squared:                       0.411
Model:                            OLS   Adj. R-squared:                  0.392
Method:                 Least Squares   F-statistic:                     21.59
Date:                Fri, 29 Jul 2016   Prob (F-statistic):           1.55e-13
Time:                        19:03:11   Log-Likelihood:                -560.14
No. Observations:                 129   AIC:                             1130.
Df Residuals:                     124   BIC:                             1145.
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
=============================================================================================
                                coef    std err          t      P>|t|      [95.0% Conf. Int.]
---------------------------------------------------------------------------------------------
Intercept                    20.6481      3.651      5.655      0.000        13.421    27.875
C(sugar_consumption)[T.1]     2.9940      5.682      0.527      0.599        -8.251    14.239
C(sugar_consumption)[T.2]    14.0744      4.995      2.818      0.006         4.189    23.960
C(sugar_consumption)[T.3]    25.3777      4.995      5.081      0.000        15.492    35.263
C(sugar_consumption)[T.4]    45.5661      5.520      8.254      0.000        34.640    56.493
==============================================================================
Omnibus:                        2.575   Durbin-Watson:                   1.688
Prob(Omnibus):                  0.276   Jarque-Bera (JB):                2.533
Skew:                           0.336   Prob(JB):                        0.282
Kurtosis:                       2.864   Cond. No.                         5.76
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```
