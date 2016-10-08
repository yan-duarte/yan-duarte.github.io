---
title: 'Assignment 1: Running a Classification Tree'
date: '2016-10-08 00:00:00 -0300'
categories:
  - Machine Learning for Data Analysis
tags:
  - Machine Learning for Data Analysis
published: true
---

This is the first assignment for the machine learning for data analysis course, fourth from a series of five courses from Data Analysis and Interpretation ministered from Wesleyan University.
The previous content you can see [here](https://yan-duarte.github.io/tags/).

In this assignment, we have to run a classification decision tree.

My response variable is the number of new cases of breast cancer in 100,000 female residents during the year 2002 (breastCancer100th).
My first explanatory variable is the mean of the total supply of food (kilocalories / person & day) available in a country, divided by the population and 365 between the years 1961 and 2002 (meanFoodPerson).
My second explanatory variable is the average of the mean TC (Total Cholesterol) of the female population, counted in mmol per L; (calculated as if each country has the same age composition as the world population) between the years 1980 and 2002 (meanCholesterol).

Note that all off my variables are quantitative. Thus, I management they transforming it to qualitative.

All of the images posted in the blog can be better view by clicking the right button of the mouse and opening the image in a new tab.

The complete program for this assignment can be download [here](https://yan-duarte.github.io/archives/mlda-assignment1.py) and the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv).

You also can run the code using jupyter notebook by clicking [here](https://github.com/yan-duarte/yan-duarte.github.io/blob/master/archives/mlda-ass1.ipynb){:target="_blank"}.

## **Contents of variables**

Variable breastCancer100th:

  - (0) The incidence of breast cancer is below the average of the incidence of all countries.
  - (1) The incidence of breast cancer is above the average of the incidence of all countries.
    
Variable meanFoodPerson:
  
  - (0) The food consumption below the average of the food consumption of all countries.
  - (1) The food consumption above the average of the food consumption of all countries.
  
Variable meanCholesterol:
  
  - (0) Desirable below 5.2 mmol/L
  - (1) Borderline high between 5.2 and 6.2 mmol/L
  - (2) High above 6.2 mmol/L __*__
  
__*__ There is no data in the dataset that has a cholesterol in blood above 6.2, so I only used the two first categories.

## **Running a Classification Tree**

The first thing to do is to import the libraries and prepare the data to be used.

```python
import pandas
import sklearn.metrics
import statistics
from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from io import StringIO
from IPython.display import Image
import pydotplus

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x)

#load the data
data = pandas.read_csv('separatedData.csv')

# convert to numeric format
data["breastCancer100th"] = pandas.to_numeric(data["breastCancer100th"], errors='coerce')
data["meanFoodPerson"]   = pandas.to_numeric(data["meanFoodPerson"], errors='coerce')
data["meanCholesterol"]   = pandas.to_numeric(data["meanCholesterol"], errors='coerce')

# listwise deletion of missing values
sub1 = data[['breastCancer100th', 'meanFoodPerson', 'meanCholesterol']].dropna()

# Create the conditions to a new variable named sugar_consumption that will categorize the meanSugarPerson answers
meanIncidence = statistics.mean(sub1['breastCancer100th'])

def incidence_cancer (row):
    if row['breastCancer100th'] <= meanIncidence : return 0   # Incidence of breast cancer is below the average of the incidence of all countries.
    if row['breastCancer100th'] > meanIncidence  : return 1   # incidence of breast cancer is above the average of the incidence of all countries.

# Add the new variable sugar_consumption to subData
sub1['incidence_cancer'] = sub1.apply (lambda row: incidence_cancer (row),axis=1)

# Create the conditions to a new variable named food_consumption that will categorize the meanFoodPerson answers
meanFood = statistics.mean(sub1['meanFoodPerson'])

def food_consumption (row):
    if row['meanFoodPerson'] <= meanFood : return 0   # food consumption below the average of the food consumption of all countries.
    if row['meanFoodPerson'] > meanFood  : return 1   # food consumption above the average of the food consumption of all countries.

# Add the new variable food_consumption to subData
sub1['food_consumption'] = sub1.apply (lambda row: food_consumption (row),axis=1)

# Create the conditions to a new variable named cholesterol_blood that will categorize the meanCholesterol answers
def cholesterol_blood (row):

   if row['meanCholesterol'] <= 5.2 : return 0         # (0) Desirable below 5.2 mmol/L
   if 5.2 < row['meanCholesterol'] <= 6.2 : return 1   # (1) Borderline high between 5.2 and 6.2 mmol/L
   if row['meanCholesterol'] > 6.2 : return 2          # (2) High above 6.2 mmol/L

# Add the new variable sugar_consumption to subData
sub1['cholesterol_blood'] = sub1.apply (lambda row: cholesterol_blood (row),axis=1)
```

The code to make the Logistic Regression model and the odds ratios

```python
"""
Modeling and Prediction
"""
#Split into training and testing sets
predictors = sub1[['food_consumption', 'cholesterol_blood']]
targets = sub1['incidence_cancer']

#Train = 60%, Test = 40%
pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size=.4)

#Build model on training data
classifier=DecisionTreeClassifier()
classifier=classifier.fit(pred_train,tar_train)

predictions=classifier.predict(pred_test)

cmatrix = sklearn.metrics.confusion_matrix(tar_test, predictions)
accuracy = sklearn.metrics.accuracy_score(tar_test, predictions)
print(cmatrix)
print(accuracy)

#Displaying the decision tree
out = StringIO()
tree.export_graphviz(classifier, out_file=out)
graph = pydotplus.graph_from_dot_data(out.getvalue())
Image(graph.create_png())
```

![Figure 1]({{site.baseurl}}/yan-duarte.github.io/images/mlda-assignments/mlda-ass1-fig1.png)

Decision tree analysis was performed to test nonlinear relationships among a series of explanatory variables and a binary, categorical response variable.

As mentioned above, the explanatory variables included as possible contributors to a classification tree model evaluating breast cancer new cases were:
  
  - The mean of food consumption (grams per day) between the years 1961 and 2002.
  - The average of the Total Cholesterol mean of the female population (mmol/L) between the years 1980 and 2002 (meanCholesterol).

There were 77 samples for train and 52 for the test.
The confusion matrix of the test was:
 
``` 
  [[39  1]
   [ 5  7]]
```
  
We can see that the accuracy is 88.46% and we have 1.92% of true negative and 9.62% of false positive.

Sensitivity
= TP / (TP + FN)
= 39 / (39 + 5)
≈ 88.63%

Specificity
= TN / (FP + TN)
= 7 / (1 + 7)
= 87.50%
 
The total number of samples for train the decision tree was 77.
A total of 48 (62.34%) countries in the samples have the incidence of new breast cancer cases below the mean, while 29 (37.66%) are above.

We have four leafs in the decision tree that can be interpreted in a followed way: 

  - The food consumption below the mean and cholesterol in blood below 5.2 mmol/L represents 50.65% (39 samples) which:
    - 94.87% (37 samples) have the incidence of breast cancer below the mean.
    - 05.13% (2 samples) have the incidence of breast cancer above the mean.

  - The food consumption below the mean and cholesterol in blood above 5.2 mmol/L represents 02.60% (2 samples) which:
    - 100% (2 samples) have the incidence of breast cancer below the mean.
    
  - The food consumption above the mean and cholesterol in blood below 5.2 mmol/L represents 15.58% (12 samples) which:
    - 58.33% (7 samples) have the incidence of breast cancer below the mean.
    - 41.66% (5 samples) have the incidence of breast cancer above the mean.

  - The food consumption above the mean and cholesterol in blood above 5.2 mmol/L represents 31.17% (24 samples) which:
    - 08.33% (2 samples) have the incidence of breast cancer below the mean.
    - 91.66% (22 samples) have the incidence of breast cancer above the mean.
    
We can conclude that if the country has the food consumption below the mean and the cholesterol in the blood under 5.2mmol/L it would have the incidence of breast cancer below the mean.

Now, if the country has the food consumption above the mean and the cholesterol in blood over 5.2mmol/L, then it would have the incidence of breast cancer above the mean.
