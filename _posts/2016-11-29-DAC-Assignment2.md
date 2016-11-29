---
title: 'Assignment 2: Methods'
date: '2016-11-29 18:00:00 -0300'
categories:
  - Data Analysis Capstone
tags:
  - Data Analysis Capstone
published: true
---

This is the second assignment for the Data Analysis Capstone from Data Analysis and Interpretation course ministered by Wesleyan University.
You can see all the previous content [here](https://yan-duarte.github.io/tags/).

In this assignment, we have to talk about the methods used in the research.

### **Methods**

#### **Sample**
To make this research, the QOG Standard Dataset 2016 [[1]][ref_01] was used. This dataset consists of approximately 2500 variables from more than 100 data sources.
The used variables was extracted from four differents database:
  
  - Environmental Performance Data (EPI) [[2]][ref_02];
  - International Monetary Fund (IMF) [[3]][ref_03];
  - Worldbank - World Development Indicators (WDI) [[4]][ref_04];
  - World Economic Forum (WEF) [[5]][ref_05].

All the variables used are:

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

In the QoG Standard TS dataset, data from 1946 to 2015 is included and the unit of analysis is country-year (e.g. Sweden-1946, Sweden-1947 and so on).

In the [codebook](http://yan-duarte.github.io/archives/QOG_codebook.pdf) you can find a detailed description of all data sources and variables sorted by original data sources.

Every single variable has a different sample number. The variables with the most samples are _Incidence of tuberculosis (per 100,000 people)_, _Air Quality_ and _Water and Sanitation_ with N=191. The variable with the lowest samples are _Smoking prevalence, females_ and _Smoking prevalence, males_ with N = 127.

After dropping the countries with miss information, a total of N = 109 was selected to make the research.

#### **Measures**
The manufacturing lead time response variable was measured for each drug batch by calculating the number of hours between release of the batch manufacturing order and completion of product packaging.
Predictors included 1) an average of the number of units of each drug ingredient on the bill of materials that was in stock at the time of release of the batch manufacturing order, 2) any equipment failure during production (yes/no) based on Engineering reports, and 3) the number of production steps that were required to complete the manufacturing process.
Employee records were used to determine 4) whether or not trainees were involved during the production process, with trainees defined as production operators who had been working less than 6 months in their current job at the time of manufacturing. Operator fatigue was assessed by 5) the average number of hours of sleep the night before batch production that each production operator reported, and 6) the average of the number of shift hours production operators had already worked prior to beginning batch production.

#### **Analysis**
The distributions for the predictors and the manufacturing lead time response variable were evaluated by examining frequency tables for categorical variables and calculating the mean, standard deviation and minimum and maximum values for quantitative variables.
Scatter plots and box plots were also examined, and Pearson correlation and Analysis of Variance (ANOVA) were used to test bivariate associations between individual predictors and the manufacturing lead time response variable.
Lasso regression with the least angle regression selection algorithm was used to identify the subset of variables that best predicted manufacturing lead time. The lasso regression model was estimated on a training data set consisting of a random sample of 60% of the batches (N=411). A test data set included the other 40% of the batches (N=273). All predictor variables were standardized to have a mean=0 and standard deviation=1 prior to conducting the lasso regression analysis. Cross validation was performed using k-fold cross validation specifying 10 cross validation folds. The change in the cross validation mean squared error rate at each step was used to identify the best subset of predictor variables. Predictive accuracy was assessed by determining the mean squared error rate of the training data prediction algorithm when applied to observations in the test data set.


## **References**

[[1] QOG Standard Dataset 2016][ref_03]

[[2] Environmental Performance Data][ref_04]

[[3] International Monetary Fund][ref_05]

[[4] Worldbank - World Development Indicators][ref_06]

[[5] World Economic Forum][ref_07]


[ref_01]: http://qog.pol.gu.se/data/datadownloads/qogstandarddata
[ref_02]: http://epi.yale.edu/downloads
[ref_03]: http://www.imf.org/external/pubs/ft/weo/2014/01/weodata/weoselgr.aspx
[ref_04]: http://data.worldbank.org/data-catalog/world-development-indicators
[ref_05]: http://www.weforum.org/issues/competitiveness-0/gci2012-data-platform
