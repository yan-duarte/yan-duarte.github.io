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







#### **Univariate Analysis**
For this work, the variables that will be used are:
  
  - Tuberculosis treatment success rate (% of new cases).
  - Health expenditure per capita, PPP (constant 2011 international dollar)
  - Water and Sanitation: Access to Drinking Water and Access to Sanitation
  - Air Quality: Household Air Quality, Air Pollution - Average Exposure to PM2.5 and Air Pollution
  - Smoking prevalence, females (% of adults)
  - Smoking prevalence, males (% of adults)
  - Business impact of tuberculosis
  - Tuberculosis case detection rate (%, all forms)
  - Incidence of tuberculosis (per 100,000 people)
  - GDP (PPP) (share of world total) (%)

All variables are quantitative and will be used without any management.




## **References**

[[1] QOG Standard Dataset 2016][ref_01]

[[2] Environmental Performance Data][ref_02]

[[3] International Monetary Fund][ref_03]

[[4] Worldbank - World Development Indicators][ref_04]

[[5] World Economic Forum][ref_05]


[ref_01]: http://qog.pol.gu.se/data/datadownloads/qogstandarddata
[ref_02]: http://epi.yale.edu/downloads
[ref_03]: http://www.imf.org/external/pubs/ft/weo/2014/01/weodata/weoselgr.aspx
[ref_04]: http://data.worldbank.org/data-catalog/world-development-indicators
[ref_05]: http://www.weforum.org/issues/competitiveness-0/gci2012-data-platform
