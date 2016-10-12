---
title: 'Assignment 3: Running a Lasso Regression Analysis'
date: '2016-10-17 14:00:00 -0300'
categories:
  - Machine Learning for Data Analysis
tags:
  - Machine Learning for Data Analysis
published: true
---

This is the third assignment for the machine learning for data analysis course, fourth from a series of five courses from Data Analysis and Interpretation ministered by Wesleyan University.
The previous content you can see [here](https://yan-duarte.github.io/tags/).

In this assignment, we have to run a Lasso Regression Analysis.

My response variable is the number of new cases of breast cancer in 100,000 female residents during the year 2002 (breastCancer100th).
My first explanatory variable is the mean of sugar consumption quantity (grams per person and day) between the years 1961 and 2002.
My second explanatory variable is the mean of the total supply of food (kilocalories / person & day) available in a country, divided by the population and 365 between the years 1961 and 2002.
My third explanatory variable is the average of the mean TC (Total Cholesterol) of the female population, counted in mmol per L; (calculated as if each country has the same age composition as the world population) between the years 1980 and 2002.

Note that my response variable is quantitative. Thus, I management it transforming to qualitative.

All of the images posted in the blog can be better view by clicking the right button of the mouse and opening the image in a new tab.

The complete program for this assignment can be download [here](https://yan-duarte.github.io/archives/mlda-assignment3.py) and the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv).

You also can run the code using jupyter notebook by clicking [here](https://github.com/yan-duarte/yan-duarte.github.io/blob/master/archives/mlda-ass3.ipynb){:target="_blank"}.

## **Contents of variables**

Variable incidence_cancer:

  - (0) The incidence of breast cancer is below the average of the incidence of all countries.
  - (1) The incidence of breast cancer is above the average of the incidence of all countries.
   

## **Running a Lasso Regression Analysis**

The first thing to do is to import the libraries and prepare the data to be used.

```python
import pandas
import statistics
import numpy as np
import matplotlib.pylab as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LassoLarsCV
from sklearn import preprocessing

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

#Split into training and testing sets
predvar = sub1[[ 'meanSugarPerson', 'meanFoodPerson', 'meanCholesterol']]
targets = sub1['incidence_cancer']
```

To run the Lasso Regression Analysis we must standardize the predictors to have mean = 0 and standard deviation = 1.

```python
# standardize predictors to have mean=0 and sd=1
predictors = predvar.copy()
predictors['meanSugarPerson']=
			preprocessing.scale(predictors['meanSugarPerson'].astype('float64'))
predictors['meanFoodPerson']=
			preprocessing.scale(predictors['meanFoodPerson'].astype('float64'))
predictors['meanCholesterol']=
			preprocessing.scale(predictors['meanCholesterol'].astype('float64'))

# split data into train and test sets - Train = 70%, Test = 30%
pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets,
                                                              test_size=.3, random_state=123)
```

```python
# specify the lasso regression model
model=LassoLarsCV(cv=10, precompute=False).fit(pred_train,tar_train)

# print variable names and regression coefficients
dict(zip(predictors.columns, model.coef_))
```

```
{'meanCholesterol': 0.22564201762237368,
 'meanFoodPerson': 0.15430005397580904,
 'meanSugarPerson': 0.0002943836394151331}
```

```python
# plot coefficient progression
m_log_alphas = -np.log10(model.alphas_)
ax = plt.gca()
plt.plot(m_log_alphas, model.coef_path_.T)
plt.axvline(-np.log10(model.alpha_), linestyle='--', color='k',
            label='alpha CV')
plt.ylabel('Regression Coefficients')
plt.xlabel('-log(alpha)')
plt.title('Regression Coefficients Progression for Lasso Paths')
```

![Figure 1]({{site.baseurl}}/yan-duarte.github.io/images/mlda-assignments/mlda-ass3-fig1.png)

```python
# plot mean square error for each fold
m_log_alphascv = -np.log10(model.cv_alphas_)
plt.figure()
plt.plot(m_log_alphascv, model.cv_mse_path_, ':')
plt.plot(m_log_alphascv, model.cv_mse_path_.mean(axis=-1), 'k',
         label='Average across the folds', linewidth=2)
plt.axvline(-np.log10(model.alpha_), linestyle='--', color='k',
            label='alpha CV')
plt.legend()
plt.xlabel('-log(alpha)')
plt.ylabel('Mean squared error')
plt.title('Mean squared error on each fold')
```

![Figure 1]({{site.baseurl}}/yan-duarte.github.io/images/mlda-assignments/mlda-ass3-fig2.png)

```python
# MSE from training and test data
from sklearn.metrics import mean_squared_error
train_error = mean_squared_error(tar_train, model.predict(pred_train))
test_error = mean_squared_error(tar_test, model.predict(pred_test))
print ('training data MSE')
print(train_error)
print ('test data MSE')
print(test_error)
```

```
training data MSE
0.0790314442922
test data MSE
0.12526564828
```

```python
# R-square from training and test data
rsquared_train=model.score(pred_train,tar_train)
rsquared_test=model.score(pred_test,tar_test)
print ('training data R-square')
print(rsquared_train)
print ('test data R-square')
print(rsquared_test)
```

```
training data R-square
0.638126230205
test data R-square
0.411947373351
```




Random forest analysis was performed to evaluate the importance of a series of explanatory variables in predicting a binary, categorical response variable. As mentioned above, the explanatory variables included as possible contributors to random forest evaluating breast cancer new cases were:

  - The mean of sugar consumption quantity (grams per person and day) between the years 1961 and 2002.
  - The mean of food consumption (grams per day) between the years 1961 and 2002.
  - The average of the Total Cholesterol mean of the female population (mmol/L) between the years 1980 and 2002 (meanCholesterol).

The explanatory variables with the highest relative importance scores were the average of the Total Cholesterol mean in the blood (39.96%). The accuracy of the random forest was 90.38%. The subsequent growing of multiple trees rather than a single tree does not benefit to the overall accuracy of the model. This suggests that the interpretation of a single decision tree may be appropriate.
