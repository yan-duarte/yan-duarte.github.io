---
published: true
date: '2016-07-29 19:00:00 -0300'
Name:
  - Assignment: Running a Chi-Square Test of Independence
categories:
  - Data Analysis Tools
tags:
  - Data Analysis Tools
title: 'Assignment 2: Running a Chi-Square Test of Independence'
---
This is the second assignment for the data analysis tool course, second of a series of five courses from Data Analysis and Interpretation ministered from Wesleyan University.
The content of the first course you can see [here](https://yan-duarte.github.io/tags/#Data Management and Visualization).
The first assignment of this course you can see [here](https://yan-duarte.github.io/2016/DAT-Assignment1/)

For this assignment, we have to run a chi-square test of independence in our data.
The data that I am using is adapted from gapminder and the response variable (the incidence of new breast cancer in 100,000 female residents during the 2002 year) is quantitative while the explanatory variable (mean of the sugar consumption (grams per person and day) between 1961 and 2002) is qualitative with five categories.
 
To run the chi-square test, both variables must be qualitative. 
Thereby, I transformed the response variable into a qualitative variable with two categories:

  - (0) The incidence of breast cancer is below the average of the incidence of all countries.
  - (1) The incidence of breast cancer is above the average of the incidence of all countries.

Therefore the hypothesis that is being approached is that the higher quantity of sugar consumption in countries increases the incidence of new breast cancer cases.

The complete program for this assignment can be download [here](https://yan-duarte.github.io/archives/dat-assignment2.py) and the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv).


## **Chi-Square Test of Independence**

Below is the code to make the Chi-Square Test of Independence technique:

First I have imported the libraries and management the data like in the other assignments presented until here. Another thing done was to make the response variable qualitative.

```python
import pandas
import numpy
import scipy.stats
import seaborn
import matplotlib.pyplot as plt
import statistics

# Import the data set to memory
data = pandas.read_csv("separatedData.csv", low_memory = False)

# Change data type among variables to numeric
data["breastCancer100th"] = data["breastCancer100th"].convert_objects(convert_numeric=True)
data["meanSugarPerson"]   = data["meanSugarPerson"].convert_objects(convert_numeric=True)

# Create a subData with only the variables breastCancer100th, meanSugarPerson, meanFoodPerson, meanCholesterol
sub1=data[['breastCancer100th', 'meanSugarPerson']]

# Create the conditions to a new variable named sugar_consumption that will categorize the meanSugarPerson answers
meanIncidence = statistics.mean(sub1['breastCancer100th'])

def incidence_cancer (row):
    if row['breastCancer100th'] <= meanIncidence : return 0   # Incidence of breast cancer is below the average of the incidence of all countries.
    if row['breastCancer100th'] > meanIncidence  : return 1   # incidence of breast cancer is above the average of the incidence of all countries.
    
# Add the new variable sugar_consumption to subData
sub1['incidence_cancer'] = sub1.apply (lambda row: incidence_cancer (row),axis=1)

# Create the conditions to a new variable named sugar_consumption that will categorize the meanSugarPerson answers
def sugar_consumption (row):
   if 0 < row['meanSugarPerson'] <= 30 : return 0    # Desirable between 0 and 30 g.
   if 30 < row['meanSugarPerson'] <= 60 : return 1   # Raised between 30 and 60 g.
   if 60 < row['meanSugarPerson'] <= 90 : return 2   # Borderline high between 60 and 90 g.
   if 90 < row['meanSugarPerson'] <= 120 : return 3  # High between 90 and 120 g.
   if row['meanSugarPerson'] > 120 : return 4        # Very high under 120g.

# Add the new variable sugar_consumption to subData
sub1['sugar_consumption'] = sub1.apply (lambda row: sugar_consumption (row),axis=1)

# creating a sub data with only the breast cancer cases and the sugar consumption mean
sub2 = sub1[['incidence_cancer', 'sugar_consumption']].dropna()
```

After that, the chi-square test was run

```python 
# contingency table of observed counts
ct1=pandas.crosstab(sub2['incidence_cancer'], sub2['sugar_consumption'])
print (ct1)

# column percentages
colsum=ct1.sum(axis=0)
colpct=ct1/colsum
print(colpct)

# chi-square
print ('chi-square value, p value, expected counts')
cs1= scipy.stats.chi2_contingency(ct1)
print (cs1)

# set variable types
sub2["sugar_consumption"] = sub2["sugar_consumption"].astype('category')
# new code for setting variables to numeric:
sub2['incidence_cancer'] = pandas.to_numeric(sub2['incidence_cancer'], errors='coerce')

# graph percent with incidence of breast cancer within each sugar consumption group
seaborn.factorplot(x="sugar_consumption", y="incidence_cancer", data=sub2, kind="bar", ci=None)
plt.xlabel('Days smoked per month')
plt.ylabel('Proportion Nicotine Dependent')
plt.show()
```

```
sugar_consumption   0   1   2   3   4
incidence_cancer                     
0                  27  18  20  18   5
1                   0   1  11  13  16

sugar_consumption    0         1         2         3         4
incidence_cancer                                              
0                  1.0  0.947368  0.645161  0.580645  0.238095
1                  0.0  0.052632  0.354839  0.419355  0.761905

chi-square value, p value, expected counts
(39.512867893214903, 5.4581126727845847e-08, 4, array([[ 18.41860465,  12.96124031,  21.14728682,  21.14728682,  14.3255814 ],
       [  8.58139535,   6.03875969,   9.85271318,   9.85271318,   6.6744186 ]]))
```

![Figure 1]({{site.baseurl}}/yan-duarte.github.io/images/dat-assignment2/dat-ass2-fig1.png)

We can see that the p-value is lower than 0.05 indicating that the null hypothesis is false.
The graph indicates us that the hypothesis is correct, however, as we have five categories in the explanatory variable, we must get the newly allowed p-value and after that, make a Post hoc test in order to avoid the type 1 error.

## **Post hoc test**

Before make the post hoc test, we need to found the new p-value dividing the actual p-value (0.05) with the number of total comparations (10) resulting in 0.005.

With this in mind, now is time to make the post hoc test by comparing each pair of the categories.
In order to not increase the content in this page, I will not show the code of this part here. You can download the full code in this [link](https://yan-duarte.github.io/archives/dat-assignment2.py).

To make it simple, I will put the results in a table to demonstrates what p-value was obtained for each pair compared.



|     |  0  |  1  |  2  |  3  |  4  |
|:---:|:---:|:---:|:---:|:---:|:---:|
|  0  |        \*           |                     |                    |                   |                   |
|  1  |  0.858286501232     |         \*          |                    |                   |                   |
|  2  |  0.00191759274614   |  0.0368386728613    |        \*          |                   |                   |
|  3  |  0.000457422007878  |  0.0131816834514    |  0.794297293406    |         \*        |                   |
|  4  |  1.55172436526e-07  |  2.53962662117e-05  |  0.00932500384294  |  0.0310969514839  |           \*




```
=========================================================================================
          0                   1                  2                 3                 4
-----------------------------------------------------------------------------------------
0         *
1   0.858286501232            *
2   0.00191759274614   0.0368386728613           *
3   0.000457422007878  0.0131816834514    0.794297293406           *
4   1.55172436526e-07  2.53962662117e-05  0.00932500384294  0.0310969514839          *      
-----------------------------------------------------------------------------------------
```

The indexes of the groups are: 

  - (0) Desirable 0 and 30 g.
  - (1) Raised with 30 and 60 g.
  - (2) Borderline high 60 and 90 g.
  - (3) High between 90 and 120 g.
  - (4) Very high under 120g.

This means that the amount of new breast cancer cases among the population that intakes sugar in the proportions of this groups doesn't have a significant difference. However, to the other seven comparisons, the post hoc test presents that the null hypothesis is false, demonstrating that the high consumption of sugar has a relation with a greater incidence of breast cancer case.
