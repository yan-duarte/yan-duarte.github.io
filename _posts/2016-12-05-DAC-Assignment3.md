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
Table 1 shows descriptive statistics for the quantitative data analytic variables.


| Analysis Variable |   N   |   Mean   |   Std Dev   |   Minimun   |   Maximum   |
|:----:|--------:|--------:|--------:|--------:|--------:|
| Air Quality                   |  109  |    78.97 |   18.73 | 14.30 |  100.00 |
| Water and Sanitation access   |  109  |    55.56 |   33.05 |  2.88 |  100.00 |
| GDP PPP share of world total  |  109  |     0.81 |    2.44 |  0.00 |   19.57 |
| Health expenditure per capita |  109  |  1424.78 | 1626.97 | 34.81 | 8845.18 |
| Smoking prevalence females    |  109  |    11.57 |   10.22 |  0.40 |   39.80 |
| Smoking prevalence males      |  109  |    34.44 |   12.83 |  8.90 |   71.80 |
| TB case detection rate        |  109  |    75.28 |   17.89 | 16.00 |  120.00 |
| Incidence of TB               |  109  |   128.83 |  195.29 |  1.60 | 1042.00 |
| TB treatment success rate     |  109  |    78.29 |   15.64 |  0.00 |  100.00 |
| Business impact of TB         |  109  |     5.24 |    1.05 |  2.27 |    6.84 |





The average manufacturing lead time was 21.45 hours (sd=3.86), with a minimum lead time of 9.40 hours and a maximum of 33.37 hours. In addition, equipment failure occurred in manufacturing for nearly half of the batches (48%; N=329) and trainees were involved in the production of 51% (N=351) of the batches.




To make this research, the QOG Standard Dataset 2016 [[1]][ref_01] was used. This dataset consists of approximately 2500 variables from more than 100 data sources.
The used variables was extracted from four differents database:
  
  - Environmental Performance Data (EPI) [[2]][ref_02];
  - International Monetary Fund (IMF) [[3]][ref_03];
  - Worldbank - World Development Indicators (WDI) [[4]][ref_04];
  - World Economic Forum (WEF) [[5]][ref_05].

In the QoG Standard CS dataset, data from 2012 is prioritized, however, if no data are available for a country for 2012, data for 2013 is included. If no data
for 2013 exists, data for 2011 is included, and so on up to a maximum of +/- 3 years.

In the [codebook](http://yan-duarte.github.io/archives/QOG_codebook.pdf) you can find a detailed description of all data sources and variables sorted by original data sources.

Every single variable has a different sample number. The variables with the most samples are _Incidence of tuberculosis (per 100,000 people)_, _Air Quality_ and _Water and Sanitation_ with N=191. The variable with the lowest samples are _Smoking prevalence, females_ and _Smoking prevalence, males_ with N = 127.

After dropping the countries with miss information, a total of N = 109 was selected to make the research.

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

#### **Bivariate Analysis**
The distributions for the predictors and the tuberculosis treatment success rate response variable were evaluated by examining the mean, standard deviation and minimum and maximum values.

Scatter plots were also examined. For test bivariate associations between individual predictors and the tuberculosis treatment success rate response variable, pearson correlation were used.

Lasso regression with the least angle regression selection algorithm was used to identify the subset of variables that best predicted the tuberculosis treatment success rate. 
The lasso regression model was estimated on a training data set consisting of a random sample of 60% of the batches (N=65). A test data set included the other 40% of the batches (N=44). All predictor variables were standardized to have a mean=0 and standard deviation=1 prior to conducting the lasso regression analysis. Cross validation was performed using k-fold cross validation specifying 10 cross validation folds. The change in the cross validation mean squared error rate at each step was used to identify the best subset of predictor variables. Predictive accuracy was assessed by determining the mean squared error rate of the training data prediction algorithm when applied to observations in the test data set.


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
