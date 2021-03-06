---
title: 'Assignment 3: Preliminary Results'
date: '2016-12-05 20:00:00 -0300'
categories:
  - Data Analysis Capstone
tags:
  - Data Analysis Capstone
published: true
---

This is the third assignment for the Data Analysis Capstone from Data Analysis and Interpretation course ministered by Wesleyan University.
You can see all the previous content [here](https://yan-duarte.github.io/tags/).

In this assignment, we have to talk about the results obtained in the research.

### **Results**

#### **Descriptive Statistics**
[Table 1](#table1) shows descriptive statistics for the quantitative data analytic variables.
The average of the response variable, tuberculosis treatment success rate, was 78.29%, with a minimum success rate of 0% and a maximum of 100%.

<center><a name="table1">Table 1.</a> Descriptive Statistic for Data Analytic Variables.</center>

| Analysis Variable             |   N   |   Mean   |   Std Dev   |   Minimun   |   Maximum   |
|:------------------------------|------:|---------:|------------:|------------:|------------:|
| Air Quality                   |  109  |    78.97 |       18.73 |       14.30 |      100.00 |
| Water and Sanitation access   |  109  |    55.56 |       33.05 |        2.88 |      100.00 |
| GDP PPP share of world total  |  109  |     0.81 |        2.44 |        0.00 |       19.57 |
| Health expenditure per capita |  109  |  1424.78 |     1626.97 |       34.81 |     8845.18 |
| Smoking prevalence females    |  109  |    11.57 |       10.22 |        0.40 |       39.80 |
| Smoking prevalence males      |  109  |    34.44 |       12.83 |        8.90 |       71.80 |
| TB case detection rate        |  109  |    75.28 |       17.89 |       16.00 |      120.00 |
| Incidence of TB               |  109  |   128.83 |      195.29 |        1.60 |     1042.00 |
| TB treatment success rate     |  109  |    78.29 |       15.64 |        0.00 |      100.00 |
| Business impact of TB         |  109  |     5.24 |        1.05 |        2.27 |        6.84 |

<br>

#### **Bivariate Analysis**

Scatter plots for the association between the tuberculosis success rate response variable and quantitative predictors ([Figure 1](#figure1)) revealed that only the variables _GDP PPP share of the world total_, _Smoking prevalence males_ and _Incidence of Tuberculosis_ increased when the tuberculosis treatment had a greater success rate. However, the other variables decreased when the success treatment rate had a great value.

<center><a name="figure1">Figure 1.</a> Association between predictors and tuberculosis success rate.</center>
![Figure 1]({{site.baseurl}}/yan-duarte.github.io/images/dac-assignments/bivariate_analysis.png)

[Table 2](#table2) shows all the Pearson values of the variables. The variables _GDP PPP share of world total_, _Smoking prevalence males_ and _Incidence of tuberculosis_ were not significantly associated with the response variable tuberculosis treatment success rate.

<center><a name="table2">Table 2.</a> Pearson values of the association between predictors and tuberculosis success rate.</center>

| Analysis Variable             |   Pearson   |   p-value  |
|:------------------------------|------------:|-----------:|
| Air Quality                   |   -0.26776  |     0.0049 |
| Water and Sanitation access   |   -0.38838  | 3.0049e-05 |
| GDP PPP share of world total  |    0.04870  |     0.6150 |
| Health expenditure per capita |   -0.37709  | 5.3036e-05 |
| Smoking prevalence females    |   -0.41092  | 9.0657e-06 |
| Smoking prevalence males      |    0.07624  |    0.43071 |
| TB case detection rate        |   -0.30539  |    0.00124 |
| Incidence of TB               |    0.16489  |    0.08664 |
| Business impact of TB         |   -0.33497  |    0.00037 |

<br>

#### **Multivariable Analysis**

[Figure 2](#figure2) shows that only four variables were retained in the model selected by the lasso regression analysis. The other five predictors were excluded. The _Smoking prevalence females (%)_ and the _Helath expenditure per capita_ were most strongly associated with tuberculosis success treatment rate, followed by _Air quality_ and at last _Water and sanitation access_ ([Table 3](#table3)).


<center><a name="figure2">Figure 2.</a> Regression Coefficients Progression for Lasso Paths.</center>
![Figure 2]({{site.baseurl}}/yan-duarte.github.io/images/dac-assignments/multivariate_analysis1.png)

<center><a name="table3">Table 3.</a> Lasso Regression Coefficients.</center>

| Analysis Variable             |     Coef    |
|:------------------------------|------------:|
| Air Quality                   |   -0.95440  |
| Water and Sanitation access   |   -0.94431  |
| Health expenditure per capita |   -1.41151  |
| Smoking prevalence females    |   -3.17685  |

<br>

As the data set have low samples, the data were not splited into training and a test sets. The least angle regression algorithm with k=10 fold cross-validation was used to estimate the lasso regression model in the data set. The change in the cross-validation average (mean) squared error at each step was used to identify the best subset of predictor variables.

[Figure 3](#figure3) shows that there is variability across the individual cross-validation folds in the training data set, but the change in the mean square error as variables are added to the model follows the same pattern for each fold.

<center><a name="figure3">Figure 3.</a> Mean squared error on each fold.</center>
![Figure 3]({{site.baseurl}}/yan-duarte.github.io/images/dac-assignments/multivariate_analysis2.png)

The mean squared error for the data was MSE = 193.10 and the R-square value was 0.2034, indicating that the selected model explained 20.34% of the variance in tuberculosis success treatment rate for the dataset.