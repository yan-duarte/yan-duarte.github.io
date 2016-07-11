---
published: true
date: '2016-07-11 14:00:00 -0300'
Name:
  - Assignment: Making Data Management Decisions
categories:
  - Data Management and Visualization
tags:
  - week3
title: 'Assignment 3: Making Data Management Decisions'
---

## WHAT TO SUBMIT:

Once you have written a successful program that manages your data, create a blog entry where you post your program and the results/output that displays at least 3 of your data managed variables as frequency distributions. Write a few sentences describing these frequency distributions in terms of the values the variables take, how often they take them, the presence of missing data, etc.


```python
import pandas
import numpy
import statistics

# Import the data set to memory
data = pandas.read_csv("separatedData.csv", low_memory = False)

# Change data type among variables to numeric
data["breastCancer100th"] = data["breastCancer100th"].convert_objects(convert_numeric=True)
data["meanSugarPerson"]   = data["meanSugarPerson"].convert_objects(convert_numeric=True)
data["meanFoodPerson"]    = data["meanFoodPerson"].convert_objects(convert_numeric=True)
data["meanCholesterol"]   = data["meanCholesterol"].convert_objects(convert_numeric=True)

# Create a subData with only the variables breastCancer100th, meanSugarPerson, meanFoodPerson, meanCholesterol
sub1=data[['breastCancer100th','meanSugarPerson', 'meanFoodPerson', 'meanCholesterol']]
```


```python
# Create the conditions to a new variable named sugar_consumption that will categorize the meanSugarPerson answers
def sugar_consumption (row):
   if 0 < row['meanSugarPerson'] <= 30 : return 0    # Desirable between 0 and 30 g.
   if 30 < row['meanSugarPerson'] <= 60 : return 1   # Raised between 30 and 60 g.
   if 60 < row['meanSugarPerson'] <= 90 : return 2   # Borderline high between 60 and 90 g.
   if 90 < row['meanSugarPerson'] <= 120 : return 3  # High between 90 and 120 g.
   if row['meanSugarPerson'] > 120 : return 4        # Very high under 120g.

# Add the new variable sugar_consumption to subData
sub1['sugar_consumption'] = sub1.apply (lambda row: sugar_consumption (row),axis=1)

# Count of sugar_consumption
print("Count of sugar_consumption - Range of sugar consumption based on the mean of the quantity (grams per person and day) of sugar and sweeters between 1961 and 2002")
c1 = sub1["sugar_consumption"].value_counts(sort=False)
print(c1)

# Percentage of sugar_consumption
print("Percentage of sugar_consumption - Range of sugar consumption based on the mean of the quantity (grams per person and day) of sugar and sweeters between 1961 and 2002")
p1 = sub1["sugar_consumption"].value_counts(sort=False,normalize=True)
print(p1)
```

```
Count of sugar_consumption - Range of sugar consumption based on the mean of the quantity (grams per person and day) of sugar and sweeters between 1961 and 2002
0    27
1    19
2    31
3    31
4    21
Name: sugar_consumption, dtype: int64

Percentage of sugar_consumption - Range of sugar consumption based on the mean of the quantity (grams per person and day) of sugar and sweeters between 1961 and 2002
0    0.209302
1    0.147287
2    0.240310
3    0.240310
4    0.162791
Name: sugar_consumption, dtype: float64
```

```python

#Make the average of meanFoodPerson values.
food_mean = statistics.mean(data["meanFoodPerson"])

# Create the conditions to a new variable named food_consumption that will categorize the meanFoodPerson answers
def food_consumption (row):
   if row['meanFoodPerson'] <= food_mean : return 0  # Food consumption below the world average.
   if row['meanFoodPerson'] > food_mean : return 1   # Food consumption under the world average.

# Add the new variable sugar_consumption to subData
sub1['food_consumption'] = sub1.apply (lambda row: food_consumption (row),axis=1)

# Count of food_consumption
print("Count of food_consumption - Mean of the food consumption of countries based on the mean  of the total supply of food (kilocalories / person & day) between 1961 and 2002")
c2 = sub1["food_consumption"].value_counts(sort=False)
print(c2)

# Percentage of food_consumption
print("Percentage of food_consumption - Mean of the food consumption of countries based on the mean of the total supply of food (kilocalories / person & day) between 1961 and 2002")
p2 = sub1["food_consumption"].value_counts(sort=False, normalize=True)
print(p2)
```

```
Count of food_consumption - Mean of the food consumption of countries based on the mean  of the total supply of food (kilocalories / person & day) between 1961 and 2002
0    71
1    58
Name: food_consumption, dtype: int64

Percentage of food_consumption - Mean of the food consumption of countries based on the mean of the total supply of food (kilocalories / person & day) between 1961 and 2002
0    0.550388
1    0.449612
Name: food_consumption, dtype: float64
```

```python

# Create the conditions to a new variable named cholesterol_blood that will categorize the meanCholesterol answers
def cholesterol_blood (row):
   if row['meanCholesterol'] <= 5.2 : return 0         # Desirable below 5.2 mmol/L
   if 5.2 < row['meanCholesterol'] <= 6.2 : return 1   # Borerline high between 5.2 and 6.2 mmol/L
   if row['meanCholesterol'] > 6.2 : return 2          # High above 6.2 mmol/L

# Add the new variable cholesterol_blood to subData
sub1['cholesterol_blood'] = sub1.apply (lambda row: cholesterol_blood (row),axis=1)

# Count of cholesterol_blood
print("Count of cholesterol_blood - Range of the average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002")
c3 = sub1["cholesterol_blood"].value_counts(sort=False)
print(c3)

# Percentage of cholesterol_blood
print("Percentage of cholesterol_blood - Range of the average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002")
p3 = sub1["cholesterol_blood"].value_counts(sort=False,normalize=True)
print(p3)
```

```
Count of cholesterol_blood - Range of the average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002
0    94
1    35
Name: cholesterol_blood, dtype: int64
Percentage of cholesterol_blood - Range of the average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002
0    0.728682
1    0.271318
Name: cholesterol_blood, dtype: float64
```