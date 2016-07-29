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

We can see that the F-test is 21.59 and the p-value is lower than 0.05 indicating that the null hypothesis is false.

For the mean and the standard deviation we have:

```python 
# means for breast cancer by sugar consumption
print ('means for breast cancer by sugar consumption')
m1= sub2.groupby('sugar_consumption').mean()
print (m1)

# standard deviations for breast cancer by sugar consumption
print ('standard deviations for breast cancer by sugar consumption')
sd1 = sub2.groupby('sugar_consumption').std()
print (sd1)
```
```
means for breast cancer by sugar consumption
                   
sugar_consumption  breastCancer100th                 
0                          20.648148
1                          23.642105
2                          34.722581
3                          46.025806
4                          66.214286

standard deviations for breast cancer by sugar consumption
                   
sugar_consumption  breastCancer100th                 
0                           6.607535
1                          10.970228
2                          16.280432
3                          26.222649
4                          25.255302
```

We can see that the mean for each category is different but there are some categories that have a close value. However, as we have five categories in the explanatory variable, we need to make a Post hoc test in order to avoid the type 1 error.

## **Post hoc test**

```python
# Post hoc test for ANOVA (as the categorical variable have five categories)
mc1 = multi.MultiComparison(sub2['breastCancer100th'], sub2['sugar_consumption'])
res1 = mc1.tukeyhsd()
print(res1.summary())
```

```
Multiple Comparison of Means - Tukey HSD,FWER=0.05
==============================================
group1 group2 meandiff  lower    upper  reject
----------------------------------------------
  0      1     2.994   -12.7348 18.7227 False 
  0      2    14.0744   0.2475  27.9013  True 
  0      3    25.3777  11.5508  39.2045  True 
  0      4    45.5661  30.2834  60.8489  True 
  1      2    11.0805  -4.2234  26.3843 False 
  1      3    22.3837   7.0799  37.6875  True 
  1      4    42.5722  25.9412  59.2031  True 
  2      3    11.3032  -2.0384  24.6448 False 
  2      4    31.4917  16.6466  46.3368  True 
  3      4    20.1885   5.3433  35.0336  True 
----------------------------------------------
```

The Post hoc test presented us that only three comparison groups have the null hypothesis confirmed. The groups are: 

  - (0) Desirable with (1) Raised
  - (1) Raised with (2) Borderline high
  - (2) Borderline high with (3) High

This means that the amount of new breast cancer cases among the population that intakes sugar in the proportions of this groups doesn't have a significant difference. However, to the other seven comparisons, the post hoc test presents that the null hypothesis is false, demonstrating that the high consumption of sugar has a relation with a greater incidence of breast cancer case.

Maybe if 