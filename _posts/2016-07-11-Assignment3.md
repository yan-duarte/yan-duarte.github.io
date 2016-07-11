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

  - Download the program [here](https://yan-duarte.github.io/archives/assignment3.py) and the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv);

In the last [assignment](https://yan-duarte.github.io/2016/Assignment2/), I had already made the data management that I thought necessary, but I made it in the excel with formulas.

Now, I remade the data management directly in python, and the program output can be seen down in the post.

The results were still the same. The sample used was the incidence of new breast cancer cases in 129 differents countries. After running the program, It was possible to observe that the consumption of sugar is considered desirable only in 20.9% of the countries of the dataset. Taking into account that this metric is based on the average of the desirable sugar ingest in grams per day of the woman (25g) and the man (36g) [[1]][ref1] and [[2]][ref2].

To the food consumption data, I made the average of all countries consumption and compared each country consumption to this mean. 55% of the countries stay under the average.

At last, to range the total cholesterol in the blood of the countries I used as a base the metric of Mayo Clinic [[3]][ref3]. In the dataset, none of the values exceeded to a high level of total cholesterol and almost 73% of the countries presented to be in the desirable level.

### Reference

[[1]][ref1] Life by Daily Burn Are You Exceeding Your Daily Sugar Intake in Just One Meal INFOGRAPHIC. Visited 05 Jul 2016. URL: http://dailyburn.com/life/health/daily-sugar-intake-infographic/.

[[2]][ref2] MD-Health How Many Grams of Sugar Per Day. Visited 06/07/2016. URL: http://www.md-health.com/How-Many-Grams-Of-Sugar-Per-Day.html.

[[3]][ref3] Cholesterol Test - Procedure details. Visited 05 Jul 2016. URL: http://www.mayoclinic.org/tests-procedures/cholesterol-test/details/results/rsc-20169555.


## **Output of the program:**

#### **Importing the packages and the [data set (csv)](https://yan-duarte.github.io/archives/separatedData.csv)**
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

#### **Making the new variable sugar_consumption**
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

#### **Count and Percentage of the new variable sugar_consumption**
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

#### **Making the new variable food_consumption**
```python
#Make the average of meanFoodPerson values.
food_mean = statistics.mean(data["meanFoodPerson"])

# Create the conditions to a new variable named food_consumption that will categorize the meanFoodPerson answers
def food_consumption (row):
   if row['meanFoodPerson'] <= food_mean : return 0  # Food consumption below the world average.
   if row['meanFoodPerson'] > food_mean : return 1   # Food consumption under the world average.

# Add the new variable food_consumption to subData
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

#### **Count and Percentage of the new variable food_consumption**
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

#### **Making the new variable cholesterol_blood**
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

#### **Count and Percentage of the new variable cholesterol_blood**
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
<br>

## **Review criteria**
Your assessment will be based on the evidence you provide that you have completed all of the steps. When relevant, gradients in the scoring will be available to reward clarity (for example, you will get one point for submitting output that is not understandable, but two points if it is understandable). In all cases, consider that the peer assessing your work is likely not an expert in the field you are analyzing. You will be assessed equally on your description of your frequency distributions.

Specific rubric items, and their point values, are as follows:

  - Was the program output interpretable (i.e. organized and labeled)? (1 point)
  - Does the program output display three data managed variables as frequency tables? (1 point)
  - Did the summary describe the frequency distributions in terms of the values the variables take, how often they take them, the presence of missing data, etc.? (2 points)

  
[ref1]: http://dailyburn.com/life/health/daily-sugar-intake-infographic/

[ref2]: http://www.md-health.com/How-Many-Grams-Of-Sugar-Per-Day.html

[ref3]: http://www.mayoclinic.org/tests-procedures/cholesterol-test/details/results/rsc-20169555
