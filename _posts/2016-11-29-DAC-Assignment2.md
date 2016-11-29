---
title: 'Assignment 2: Methods'
date: '2016-11-29 18:00:00 -0300'
categories:
  - Data Analysis Capstone
tags:
  - Data Analysis Capstone
published: true
---

This is the first assignment for the Data Analysis Capstone from Data Analysis and Interpretation course ministered by Wesleyan University.
You can see all the previous content [here](https://yan-duarte.github.io/tags/).

In this assignment, we have to make a title and an introduction to the Research Question.

#### **Title**

The relation between the importance that individuals, governments, and companies give to health and the success rate in the treatment of tuberculosis.

#### **Research question**

How does the relation of the importance give to health of individuals, governments and companies influence the success rate in the treatment of tuberculosis?

#### **Hypothesis**

If a country expends more with health, has a good air quality and an easy access to water and sanitation, then the success rate in tuberculosis treatment will be higher and the incidence of new cases of this disease will be lower.

In contrast, not only the country needs to care about health. If the country has a high number of smokers, the rate in tuberculosis treatment will be lower and the incidence of new cases of this disease will be higher.

#### **Motivation/Rationale**

Tuberculosis (TB) remains a major global health problem. 
In 2012, 1.3 million people were believed to have died because of tuberculosis with an estimated 8.6 million new cases of TB worldwide [[1]][ref_01].The number of TB deaths is unacceptably large given that most are preventable [[2]][ref_02].
The purpose of this project is to enforce and determine what measures of healthcare are related to the tuberculosis treatment.

#### **Potential Implications**

As it is a dangerous disease that has a good chance of prevention, it would be interesting to have some measures that countries could take to decrease it.

#### **Dataset and variables**

To make this research, I decide to use the QOG Standard Dataset 2016 [[3]][ref_03]. This dataset consists of approximately 2500 variables from more than 100 data sources.
At first, I am thinking to use variables from four differents database:
  
  - Environmental Performance Data (EPI) [[4]][ref_04];
  - International Monetary Fund (IMF) [[5]][ref_05];
  - Worldbank - World Development Indicators (WDI) [[6]][ref_06];
  - World Economic Forum (WEF) [[7]][ref_07].
  
The response variable is the Tuberculosis treatment success rate (% of new cases).
  
There are a series of explanatory that can be used, at first I included these ones:

  - Health expenditure per capita, PPP (constant 2011 international dollar)
  - Water and Sanitation: Access to Drinking Water and Access to Sanitation
  - Air Quality: Household Air Quality, Air Pollution - Average Exposure to PM2.5 and Air Pollution
  - Smoking prevalence, females (% of adults)
  - Smoking prevalence, males (% of adults)
  - Business impact of tuberculosis
  - Tuberculosis case detection rate (%, all forms)
  - Incidence of tuberculosis (per 100,000 people)
  - GDP (PPP) (share of world total) (%)


## **References**

[[1] Tuberculosis: Causes, Symptoms and Treatments][ref_01]

[[2] Global Tuberculosis Report 2013][ref_02]

[[3] QOG Standard Dataset 2016][ref_03]

[[4] Environmental Performance Data][ref_04]

[[5] International Monetary Fund][ref_05]

[[6] Worldbank - World Development Indicators][ref_06]

[[7] World Economic Forum][ref_07]


[ref_01]: http://www.medicalnewstoday.com/articles/8856.php
[ref_02]: http://apps.who.int/iris/bitstream/10665/91355/1/9789241564656_eng.pdf
[ref_03]: http://qog.pol.gu.se/data/datadownloads/qogstandarddata
[ref_04]: http://epi.yale.edu/downloads
[ref_05]: http://www.imf.org/external/pubs/ft/weo/2014/01/weodata/weoselgr.aspx
[ref_06]: http://data.worldbank.org/data-catalog/world-development-indicators
[ref_07]: http://www.weforum.org/issues/competitiveness-0/gci2012-data-platform
