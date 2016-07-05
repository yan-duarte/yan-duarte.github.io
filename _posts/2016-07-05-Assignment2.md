---
published: true
date: '2016-07-05 14:00:00 -0300'
Name:
  - Assignment: Running Your First Program
categories:
  - Data Management and Visualization
tags:
  - week2
title: 'Assignment 2: Running Your First Program'
---

## STEP 1: Run your first program. 

This program will be used throughout the remainder of the course and become the basis of your data analysis going forward.

You can download the python script [here](https://yan-duarte.github.io/archives/assignment2.py).

## STEP 2: Run frequency distributions for your chosen variables and select columns, and possibly rows.

The results of the first program that demonstrates the frequency distributions were:

#### Importing the packages and the [data set](https://yan-duarte.github.io/archives/separatedData.csv) 

```python
import pandas
import numpy

data = pandas.read_csv("separatedData.csv", low_memory = False)
```

#### Print data set dimension

```python
print(len(data))
print(len(data.columns))
```

```
129
6
```

#### Change data type among variables to numeric

```python
data["breastCancerAll"]   = data["breastCancerAll"].convert_objects(convert_numeric=True)
data["breastCancer100th"] = data["breastCancer100th"].convert_objects(convert_numeric=True)
data["meanSugarPerson"]   = data["meanSugarPerson"].convert_objects(convert_numeric=True)
data["meanFoodPerson"]    = data["meanFoodPerson"].convert_objects(convert_numeric=True)
data["meanCholesterol"]   = data["meanCholesterol"].convert_objects(convert_numeric=True)
```

#### Count of breastCancerAll - Number of new breast cancer cases in 2002

```python
print("Count of breastCancerAll - Number of new breast cancer cases in 2002")
c1 = data["breastCancerAll"].value_counts(sort=False)
print(c1)
```

```
2330      1
55689     1
1027      1
7429      1
82951     1
1032      1
2568      1
266       1
231       1
525       1
16        1
126227    1
20        1
21        1
5142      1
3609      1
36634     1
4635      1
28        1
543       1
2848      1
6945      1
34        1
5411      1
2598      1
3879      1
447       1
45        1
7273      1
47        1
         ..
1174      1
3514      1
3668      1
4117      1
194       1
196       1
1221      1
14358     1
3845      1
463       2
509       1
4309      1
687       1
12253     1
2388      1
40928     1
41957     1
230       1
4742      1
236       1
209995    1
15855     1
2288      1
243       1
32245     1
55        1
13051     1
1795      1
765       1
84        1
Name: breastCancerAll, dtype: int64
```
