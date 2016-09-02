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


## **Sample**

The sample is from GAPMINDER a non-profit venture promoting sustainable global development and achievement of the United Nations Millennium Development Goals by increased use and understanding of statistics and other information about social, economic and environmental development at local, national and global levels.

GAPMINDER uses data from others data providers, I choose to use the variable number of new cases of breast cancer in 100,000 female residents during the years provide by the International Agency for Research on Cancer (IARC).

The incidence of new breast cancer data was compiled by Gapminder using data from [IARC GLOBOCAN 2002 (estimates for 2002)](http://globocan.iarc.fr/) and [IARC CI5 (Cancer Incidence in 5 Continents - Vol. I to VIII)](http://ci5.iarc.fr/) .

It has the incidence of new breast cancer data since the year of 1953 to 2002 from N=174 different countries where only the year of 2002 has the complete data of all countries.

Another variable used was the food consumption quantity (grams per person and day) of sugar and sweeters. GAPMINDER compiled the data from Food and Agriculture Organization of the United Nations ([FAO](http://faostat.fao.org/)). Food supply data is some of the most important data in FAOSTAT. In fact, this data is the basis for estimation of global and national undernourishment assessment, when it is combined with parameters and other data sets.
This data has been the foundation of food balance sheets ever since they were first constructed. The data is accessed by both business and governments for economic analysis and policy setting, as well as being used by the academic community. 

The provided data is from 1961 until 2004 of N=156 different countries.


## **Procedure**

The incidence of new breast case data was collected with the amount of the information available for each country. In theory, there are as many methods as countries, and because of the variety and the complexity of these methods, an overall quality score for the incidence and mortality estimates combined is almost impossible to establish.
However, an alphanumeric scoring system which independently describes the availability of incidence and mortality data has been established at the country level. The combined score is presented together with the estimates for each country with an aim of providing a broad indication of the robustness of the estimation. 

Availability of incidence data:

  - A. High quality* national data or high quality regional (coverage greater than 50%).
  - B. High quality* regional (coverage between 10% and 50%).
  - C. High quality* regional (coverage lower than 10%).
  - D. National data (rates).
  - E. Regional data (rates).
  - F. Frequency data.
  - G. No data.

The period of this data collection was from 1953 until 2002. [(Reference)](http://globocan.iarc.fr/Pages/DataSource_and_methods.aspx).

For the sugar consumption per person and day, the FAO data is obtained through the total quantity of foodstuffs produced in a country added to the total quantity imported and adjusted to any change in stocks that may have occurred since the beginning of the reference period gives the supply available during that period. On the utilisation side, a distinction is made between the quantities exported, fed to livestock + used for seed, losses during storage and transportation, and food supplies available for human consumption. The per capita supply of each such food item available for human consumption is then obtained by dividing the respective quantity by the related data on the population actually partaking in it. The period of this data collection was from 1961 until 2004. [(Reference)](http://faostat.fao.org/site/354/default.aspx).

## **Measures**

Since most of the incidence of breast cancer registries before 2002 were missing, I opted to pick only the data from 2002 of GAPMINDER/IARC. To merge the information between this data and the sugar consumption, I only used data from N=129 countries. In this works, the incidence of breast cancer is a quantitative response variable that ranged from 3.9 to 101.10 new breast cancer cases per 100,000 female.

For the sugar consumption, I realized that would be better to make an average of the data from 1953 until 2002. The result was used as the explanatory variable and, during the course, I used it either as a quantitative variable as much as a qualitative variable. To the quantitative variable, it ranged from 6.13 to 163.86 sugar consumption per person and day. While to the qualitative variable, I separated the data into five categories:

  - Desirable: between 0 and 30 g per day.
  - Raised: between 30 and 60 g per day.
  - Borderline high: between 60 and 90 g per day.
  - High: between 90 and 120 g per day.
  - Very high: under 120g per day.
  

  





