---
title: 'Assignment 1: Writing About Your Data'
date: '2016-09-01 16:30:00 -0300'
categories:
  - Regression Modeling Practice
tags:
  - Regression Modeling Practice
published: true
---
This is the first assignment for the regression modeling practice course, third from a series of five courses from Data Analysis and Interpretation ministered from Wesleyan University.
The previous content you can see [here](https://yan-duarte.github.io/tags/).

In this assignment, we have to describe the sample, the data collection procedure, and how do I manage my data.


## Sample

The sample is from GAPMINDER a non-profit venture promoting sustainable global development and achievement of the United Nations Millennium Development Goals by increased use and understanding of statistics and other information about social, economic and environmental development at local, national and global levels.

GAPMINDER uses data from others data providers, I choose to use the variable number of new cases of breast cancer in 100,000 female residents during the years provide by the International Agency for Research on Cancer (IARC).

The incidence of new breast cancer data was compiled by Gapminder using data from [IARC GLOBOCAN 2002 (estimates for 2002)](http://globocan.iarc.fr/) and [IARC CI5 (Cancer Incidence in 5 Continents - Vol. I to VIII)](http://ci5.iarc.fr/) .

It has the incidence of new breast cancer data since the year of 1953 to 2002 from 174 different countries where only the year of 2002 has the complete data of all countries.

Another variable used was the food consumption quantity (grams per person and day) of sugar and sweeters. GAPMINDER compiled the data from Food and Agriculture Organization of the United Nations ([FAO](http://faostat.fao.org/)). Food supply data is some of the most important data in FAOSTAT. In fact, this data is the basis for estimation of global and national undernourishment assessment, when it is combined with parameters and other data sets.
This data has been the foundation of food balance sheets ever since they were first constructed. The data is accessed by both business and governments for economic analysis and policy setting, as well as being used by the academic community. 

The provide data is from 1961 until 2004 of 156 different countries.





Since most of the cancer registries were not national level, we only picked several countries and territories for comparisons: Canada, Costa Rica, Czech Republic, Denmark, Estonia, Finland, Hong Kong, Iceland, New Zealand, Norway, Slovak Republic, Slovenia and Sweden. A direct combination has been done because IARC CI5 time series data stops in year 1997 and all 2002 data comes from IARC GLOBOCAN 2002 data.	






The sample is from the first wave of the National Epidemiologic Survey on Alcohol and
Related Conditions (NESARC), the largest nationwide longitudinal survey of alcohol and
drug use and associated psychiatric and medical comorbidities. Participants (N=43,093)
represented the civilian, non-institutionalized adult population of the United States, and
included persons living in households, military personnel living off base, and persons
residing in the following group quarters: boarding or rooming houses, non-transient hotels
and motels, shelters, facilities for housing workers, college quarters, and group homes. The
NESARC included over sampling of Blacks, Hispanics and young adults aged 18 to 24 years.
The data analytic sample for this study included participants 18-25 years old who reported
smoking at least 1 cigarette per day in the past 30 days (N=1,320).
Procedure
Data were collected by trained U.S. Census Bureau Field Representatives during 2001–
2002 through computer-assisted personal interviews (CAPI). One adult was selected for
interview in each household, and interviews were conducted in respondents’ homes
following informed consent procedures.
Measures
Lifetime major depression (i.e. those experienced in the past 12 months and prior to the
past 12 months) was assessed using the NIAAA, Alcohol Use Disorder and Associated
Disabilities Interview Schedule – DSM-IV (AUDADIS-IV) (Grant et al., 2003; Grant, Harford,
Dawson, & Chou, 1995). The tobacco module of the AUDADIS-IV contains detailed
questions on the frequency, quantity, and patterning of tobacco use as well as symptom
criteria for DSM-IV nicotine dependence. Current smoking was evaluated through both
smoking frequency (“About how often did you usually smoke in the past year?”) coded
dichotomously to represent presence or absence of daily smoking, and quantity (“On the
days that you smoked in the last year, about how many cigarettes did you usually smoke?”),
a quantitative variable that ranged from 1 cigarette per day to 98 cigarettes per day





we can choose to run an ANOVA, Chi-Square test or correlation coefficient that includes a moderator. I have chosen to run the correlation coefficient with the moderator. 
The data that I am using is adapted from gapminder and both of my variables (response and explanatory) are already quantitative. 
The response variable is the incidence of new breast cancer in 100,000 female residents during the 2002 year while the explanatory variable is the mean of the sugar consumption (grams per person and day) between 1961 and 2002. 
To the moderator, I am using the mean of the total supply of food (kilocalories / person & day) available in a country divided by the population and 365 (the number of days in the year) between the years 1961 and 2002. This variable is subdivided in three categories:
