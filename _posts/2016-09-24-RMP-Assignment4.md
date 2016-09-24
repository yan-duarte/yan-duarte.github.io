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

Note that all off my variables are quantitative. Thus, I must management they transforming it to qualitative.

Variable breastCancer100th:

  -(0) The incidence of breast cancer is below the average of the incidence of all countries.
  -(1) The incidence of breast cancer is above the average of the incidence of all countries.
    
Variable meanSugarPerson:
  
  -(0) Desirable 0 and 30 g.
  -(1) Raised with 30 and 60 g.
  -(2) Borderline high 60 and 90 g.
  -(3) High between 90 and 120 g.
  -(4) Very high under 120g.

  
Variable meanFoodPerson:
  
  -(0) The food consumption below the average of the food consumption of all countries.
  -(1) The food consumption above the average of the food consumption of all countries.
  
Variable meanCholesterol:
  
  -
  -

All of the images posted in the blog can be better view by clicking the right button of the mouse and opening the image in a new tab.

The complete program for this assignment can be download [here](https://yan-duarte.github.io/archives/rmp-assignment4.py) and the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv).

## **Test a Multiple Regression Model**

The first thing to do is to import the libraries and prepare the data to be used.

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

The explanatory variables are centered and the first OLS Regression Test was made with only the meanSugarPerson variable.

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

The results for this test is the same as the [assignment 2](https://yan-duarte.github.io/2016/RMP-Assignment2/)

We can see in the OLS Regression Results that the p-value is considerably less than our alpha level of 0.05 wich tells us that we can reject the null hypothesis and concludes that the sugar consumption is significantly associated with the incidence of breast cancer cases.

The coefficient for sugar consumption is 0.3667 and the intercept is 37.9876. This means that the equation for the best line of this graph is:

breastCancer100th = 37.9876 + 0.3667 * meanSugarPerson
The column P>| t | give us the p-value for our explanatory variables, association with the response variable. This p-value is 0.000 wich means that it is really small confirming the significance associated with the variables.

Other information that OLS Regression Results give to us is the R-square. This value can be interpreted in the following way: If we know the sugar consumption grams per day of a woman we can predict 41% of the variability we will see in the incidence of breast cancer cases.

After make the linear regression test, we are going to do now the polynomial regression test. For this, we have to add the polynomial second order of the meanSugarPerson variable into the scatterplot and into the regression analysis.

```python
# first order (linear) scatterplot
scat1 = seaborn.regplot(x="meanSugarPerson", y="breastCancer100th", scatter=True, data=sub1)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')

# fit second order polynomial
# run the 2 scatterplots together to get both linear and second order fit lines
scat1 = seaborn.regplot(x="meanSugarPerson", y="breastCancer100th", scatter=True, order=2, data=sub1)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
```

![Figure 1]({{site.baseurl}}/yan-duarte.github.io/images/rmp-assignments/rmp-ass3-fig1.png)

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
===================================================================================
                              coef  std err        t    P>|t|    [95.0% Conf. Int.]
-----------------------------------------------------------------------------------
Intercept                  34.4829    2.339   14.742    0.000      29.854    39.112
meanSugarPerson_c           0.3680    0.039    9.556    0.000       0.292     0.444
I(meanSugarPerson_c ** 2)   0.0020    0.001    2.089    0.039       0.000     0.004
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

For the polynomial OLS Regression Results, we can see that the p-value still less than 0.05 assuming that we can reject the null hypothesis and concludes that the correlation between sugar consumption and incidence of breast cancer is significantly strong.

The coefficient for sugar consumption is 0.3680, for the polynomial sugar consumption we have a value of 0.0020 and for the intercept 34.4829. This means that the equation for the best line of this graph is:

breastCancer100th = 34.4829 + 0.3680 * meanSugarPerson + 0.0020 * meanSugarPerson²

The R-square in this scenario is slightly greater than the previous and can be interpreted as If we know the sugar consumption grams per day of a woman we can predict 43% of the variability we will see in the incidence of breast cancer cases.

After this analysis is time to add another explanatory variable, the amount of food consumption in kilocalories per day.

```python
# adding food consumption
reg3 = smf.ols('breastCancer100th  ~ meanSugarPerson_c + I(meanSugarPerson_c**2) + meanFoodPerson_c',
               data=sub1).fit()
print (reg3.summary())
```

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:      breastCancer100th   R-squared:                       0.653
Model:                            OLS   Adj. R-squared:                  0.645
Method:                 Least Squares   F-statistic:                     78.54
Date:                Mon, 12 Sep 2016   Prob (F-statistic):           1.27e-28
Time:                        23:21:27   Log-Likelihood:                -525.90
No. Observations:                 129   AIC:                             1060.
Df Residuals:                     125   BIC:                             1071.
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
===================================================================================
                              coef  std err        t    P>|t|    [95.0% Conf. Int.]
-----------------------------------------------------------------------------------
Intercept                  33.5975    1.834   18.320    0.000      29.968    37.227
meanSugarPerson_c           0.1377    0.040    3.476    0.001       0.059     0.216
I(meanSugarPerson_c ** 2)   0.0025    0.001    3.333    0.001       0.001     0.004
meanFoodPerson_c            0.0316    0.004    8.975    0.000       0.025     0.039
==============================================================================
Omnibus:                        0.058   Durbin-Watson:                   1.720
Prob(Omnibus):                  0.971   Jarque-Bera (JB):                0.062
Skew:                           0.042   Prob(JB):                        0.970
Kurtosis:                       2.935   Cond. No.                     3.59e+03
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.59e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

The OLS Regression Results demonstrates the p-value and the P>| t | for all variables lower than 0.05.
We can conclude that both meanSugarPerson and meanFoodPerson are significantly associated with the incidence of new breast cancer cases.

The R-square increased considerably from 43% to 65.3%.

Thereafter, as the meanFoodPerson improved the study, let's try to add the cholesterol in blood variable.

```python
# adding mean cholesterol
reg4 = smf.ols('breastCancer100th  ~ meanSugarPerson_c + I(meanSugarPerson_c**2) + meanCholesterol_c',
               data=sub1).fit()
print (reg4.summary())
```

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:      breastCancer100th   R-squared:                       0.728
Model:                            OLS   Adj. R-squared:                  0.722
Method:                 Least Squares   F-statistic:                     111.6
Date:                Mon, 12 Sep 2016   Prob (F-statistic):           3.40e-35
Time:                        23:21:31   Log-Likelihood:                -510.23
No. Observations:                 129   AIC:                             1028.
Df Residuals:                     125   BIC:                             1040.
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
===================================================================================
                              coef  std err        t    P>|t|    [95.0% Conf. Int.]
-----------------------------------------------------------------------------------
Intercept                  32.7510    1.629   20.111    0.000      29.528    35.974
meanSugarPerson_c           0.0165    0.040    0.410    0.683      -0.063     0.096
I(meanSugarPerson_c ** 2)   0.0029    0.001    4.465    0.000       0.002     0.004
meanCholesterol_c          45.7660    3.909   11.709    0.000      38.030    53.502
==============================================================================
Omnibus:                        5.132   Durbin-Watson:                   1.947
Prob(Omnibus):                  0.077   Jarque-Bera (JB):                5.067
Skew:                          -0.316   Prob(JB):                       0.0794
Kurtosis:                       3.736   Cond. No.                     8.65e+03
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.65e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

When we add the meanCholesterol variable to the multiple regression tests, we can see that this variable made the meanSugarPerson p-value get increased over than 0.5, assuming that the meanCholesterol is a confounding variable for this work.

## **Q-Q Plot**

```python
#Q-Q plot for normality
fig4 = sm.qqplot(reg3.resid, line='r')
plt.show(fig4)
```
![Figure 2]({{site.baseurl}}/yan-duarte.github.io/images/rmp-assignments/rmp-ass3-fig2.png)

The qqplot for our regression model shows that the residuals generally follow a straight line, but deviate at the lower and higher quantiles. This indicates that our residuals did not follow perfect normal distribution meaning that the curvilinear association that we observed in our scatter plot may not be fully estimated by the quadratic sugar consumption.

## **Standardized residuals for all observations**

```python
# simple plot of residuals
stdres = pandas.DataFrame(reg3.resid_pearson)
plt.plot(stdres, 'o', ls='None')
l = plt.axhline(y=0, color='r')
plt.ylabel('Standardized Residual')
plt.xlabel('Observation Number')
```
![Figure 3]({{site.baseurl}}/yan-duarte.github.io/images/rmp-assignments/rmp-ass3-fig3.png)

*"The standardized residuals are simply the residual values transformed to have a mean of zero and a standard deviation of one. This transformation is called normalizing or standardizing the values so that they fit a standard normal distribution. In a standard normal distribution 68% of the observations are expected to fall within one standard deviation of the mean. So between -1 and 1 standard deviations. And 95% of the observations are expected to fall within 2 standard deviations of the mean.*

*With the standard normal distribution, we would expect 95% of the values of the residuals to fall between two standard deviations of the mean. Residual values that are more than two standard deviations from the mean in either direction, are a warning sign that we may have some outliers. However, there are no observations that have three or more standard deviations from the mean. So we do not appear to have any extreme outliers.*

*In terms of evaluating the overall fit of the model, there's some other rules of thumb that you can use to determine how well your model fits the data based on the distribution of the residuals. If more than 1% of our observations has standardized residuals with an absolute value greater than 2.5, or more than 5% have an absolute value of greater than or equal to 2, then there is evidence that the level of error within our model is unacceptable. That is the model is a fairly poor fit to the observed data."*

In this work, only 1 point is exceeded an absolute value of 2.5 representing less than 1% and there are 6 points (4.65%) that are greater than or equal to an absolute value of 2.0. This suggests that the model is good.


```python
# additional regression diagnostic plots
fig2 = plt.figure(figsize=(12,8))
fig2 = sm.graphics.plot_regress_exog(reg3,  "meanFoodPerson_c", fig=fig2)
plt.show(fig2)
```

![Figure 4]({{site.baseurl}}/yan-duarte.github.io/images/rmp-assignments/rmp-ass3-fig4.png)

The plot in the upper right hand corner shows the residuals for each observation at different values of Internet use rate. There's not a clearly pattern on it, as there is points all over the graph, we can assume that model predict food consumption kilocalories as well for countries that have either high or low incidence of breast cancer new cases.

To take a look at the contribution of each individual explanatory variable to model fit we analysis the partial regression residual plot (the third plot). It attempts to show the effect of adding meanFoodPerson as an additional explanatory variable to the model. Given that one or more explanatory variables are already in the model. This plot demonstrates the relationship between the response variable and specific explanatory variable, after controlling for the other explanatory variables. We can see that the meanFoodPerson has a linear pattern meaning that it meets the linearity assumption in the multiple regression.



## **Leverage Plot**

```python
# leverage plot
fig3=sm.graphics.influence_plot(reg3, size=8)
plt.show(fig3)
```

![Figure 5]({{site.baseurl}}/yan-duarte.github.io/images/rmp-assignments/rmp-ass3-fig5.png)

*"Finally, we can examine a leverage plot to identify observations that have an unusually large influence on the estimation of the predicted value of the response variable, mean of sugar consumption grams per day, or that are outliers, or both.*

*The leverage of an observation can be thought of in terms of how much the predicted scores for the other observations would differ if the observations in question were not included in the analysis. The leverage always takes on values between zero and one. A point with zero leverage has no effect on the regression model. And outliers are observations with residuals greater than 2 or less than -2."*


One of the first things we see in the leverage plot is that we have a few outliers, contents that have residuals greater than 2 or less than -2. We've already identified some of these outliers in some of the other plots we've looked at, but this plot also tells us that these outliers have small or close to zero leverage values, meaning that although they are outlying observations, they do not have an undue influence on the estimation of the regression model. On the other hand, we see that there are a few cases with higher than average leverage. But one in particular is more obvious in terms of having an influence on the estimation of the predicted value of sugar consumption per day. This observation has a high leverage but is not an outlier. We don't have any observations that are both high leverage and outliers.
