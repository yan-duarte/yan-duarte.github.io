---
title: 'Assignment 2: Running a Random Forest'
date: '2016-10-10 15:00:00 -0300'
categories:
  - Machine Learning for Data Analysis
tags:
  - Machine Learning for Data Analysis
published: true
---

This is the second assignment for the machine learning for data analysis course, fourth from a series of five courses from Data Analysis and Interpretation ministered from Wesleyan University.
The previous content you can see [here](https://yan-duarte.github.io/tags/).

In this assignment, we have to run a Random Forest Classification.

My response variable is the number of new cases of breast cancer in 100,000 female residents during the year 2002 (breastCancer100th).
My first explanatory variable is the mean of sugar consumption quantity (grams per person and day) between the years 1961 and 2002.
My second explanatory variable is the mean of the total supply of food (kilocalories / person & day) available in a country, divided by the population and 365 between the years 1961 and 2002.
My third explanatory variable is the average of the mean TC (Total Cholesterol) of the female population, counted in mmol per L; (calculated as if each country has the same age composition as the world population) between the years 1980 and 2002.

Note that my response variable is quantitative. Thus, I management it transforming to qualitative.

All of the images posted in the blog can be better view by clicking the right button of the mouse and opening the image in a new tab.

The complete program for this assignment can be download [here](https://yan-duarte.github.io/archives/mlda-assignment2.py) and the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv).

You also can run the code using jupyter notebook by clicking [here](https://github.com/yan-duarte/yan-duarte.github.io/blob/master/archives/mlda-ass2.ipynb){:target="_blank"}.

## **Contents of variables**

Variable incidence_cancer:

  - (0) The incidence of breast cancer is below the average of the incidence of all countries.
  - (1) The incidence of breast cancer is above the average of the incidence of all countries.
   

## **Running a Classification Tree**

The first thing to do is to import the libraries and prepare the data to be used.

```python
%matplotlib inline

import pandas
import sklearn.metrics
import statistics
import numpy as np
import matplotlib.pylab as plt
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x)

#load the data
data = pandas.read_csv('separatedData.csv')

# convert to numeric format
data["breastCancer100th"] = pandas.to_numeric(data["breastCancer100th"], errors='coerce')
data["meanSugarPerson"]   = pandas.to_numeric(data["meanSugarPerson"], errors='coerce')
data["meanFoodPerson"]   = pandas.to_numeric(data["meanFoodPerson"], errors='coerce')
data["meanCholesterol"]   = pandas.to_numeric(data["meanCholesterol"], errors='coerce')

# listwise deletion of missing values
sub1 = data[['breastCancer100th', 'meanFoodPerson', 'meanCholesterol', 'meanSugarPerson']].dropna()

# Create the conditions to a new variable named incidence_cancer that will categorize the meanSugarPerson answers
meanIncidence = statistics.mean(sub1['breastCancer100th'])

def incidence_cancer (row):
    if row['breastCancer100th'] <= meanIncidence : return 0   # Incidence of breast cancer is below the 
                                                              # average of the incidence of all countries.
    if row['breastCancer100th'] > meanIncidence  : return 1   # Incidence of breast cancer is above the average 
                                                              # of the incidence of all countries.

# Add the new variable sugar_consumption to subData
sub1['incidence_cancer'] = sub1.apply (lambda row: incidence_cancer (row),axis=1)
```

The code to make the Random Forest classification

```python
#Split into training and testing sets
predictors = sub1[[ 'meanSugarPerson', 'meanFoodPerson', 'meanCholesterol']]
targets = sub1['incidence_cancer']

#Train = 60%, Test = 40%
pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size=.4)

#Build model on training data
classifier=RandomForestClassifier(n_estimators=25)
classifier=classifier.fit(pred_train,tar_train)

predictions=classifier.predict(pred_test)

confusion_matrix = sklearn.metrics.confusion_matrix(tar_test,predictions)
accuracy_score = sklearn.metrics.accuracy_score(tar_test, predictions)

print (confusion_matrix)
print (accuracy_score)

# fit an Extra Trees model to the data
model = ExtraTreesClassifier()
model.fit(pred_train,tar_train)
# display the relative importance of each attribute
print(model.feature_importances_)
```

```
#Confusion_matrix:
[[31  3]
 [ 2 16]]
 
#accuracy_score
0.903846153846

#relative importance of each attribute
[ 0.21311057  0.38723056  0.39965887]
```

```python
"""
Running a different number of trees and see the effect
 of that on the accuracy of the prediction
"""

trees=range(25)
accuracy=np.zeros(25)

for idx in range(len(trees)):
    classifier=RandomForestClassifier(n_estimators=idx + 1)
    classifier=classifier.fit(pred_train,tar_train)
    predictions=classifier.predict(pred_test)
    accuracy[idx]=sklearn.metrics.accuracy_score(tar_test, predictions)
    
plt.cla()
plt.plot(trees, accuracy)

print(accuracy)
print(statistics.mean(accuracy))
```

![Figure 1]({{site.baseurl}}/yan-duarte.github.io/images/mlda-assignments/mlda-ass2-fig1.png)

```
#Accuracy from 25 trees
[ 0.84615385  0.80769231  0.80769231  0.86538462  0.88461538  0.84615385
  0.90384615  0.88461538  0.88461538  0.90384615  0.88461538  0.86538462
  0.86538462  0.88461538  0.88461538  0.88461538  0.88461538  0.88461538
  0.86538462  0.84615385  0.86538462  0.84615385  0.88461538  0.88461538
  0.86538462]
  
#Mean of the accuracy from 25 trees
0.86923076923076925
```

Random forest analysis was performed to evaluate the importance of a series of explanatory variables in predicting a binary, categorical response variable. As mentioned above, the explanatory variables included as possible contributors to random forest evaluatingbreast cancer new cases were:

  - The mean of sugar consumption quantity (grams per person and day) between the years 1961 and 2002.
  - The mean of food consumption (grams per day) between the years 1961 and 2002.
  - The average of the Total Cholesterol mean of the female population (mmol/L) between the years 1980 and 2002 (meanCholesterol).

The explanatory variables with the highest relative importance scores were the average of the Total Cholesterol mean in blood (39.96%). The accuracy of the random forest was 90.38%. The subsequent growing of multiple trees rather than a single tree does not added much to the overall accuracy of the model. This suggest that the interpretation of a single decision tree may be appropriate.


