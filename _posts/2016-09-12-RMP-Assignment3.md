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

Note that all my explanatories variables are quantitative, thus I must center the variables by subtracting the mean from the data values, then the value 0 will be very close to the mean. 

The complete program for this assignment can be download [here](https://yan-duarte.github.io/archives/rmp-assignment3.py) and the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv).

## **Test a Multiple Regression Model**





Summarize what you found. Discuss the results for the associations between all of your explanatory variables and your response variable. Make sure to include statistical results (Beta coefficients and p-values) in your summary.


Report whether or not your results supported your hypothesis for the association between your primary explanatory response variable.


Discuss whether or not there was evidence of confounding for the association between your primary explanatory and response variable.


Generate regression diagnostic plots and write a few sentences describing what these plots tell you about your regression model in terms of the distribution of the residuals, model fit, influential observations, and outliers.


Include your multiple regression output in your blog.
