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

#### **Importing the packages and the [data set](https://yan-duarte.github.io/archives/separatedData.csv) **

```python
import pandas
import numpy

data = pandas.read_csv("separatedData.csv", low_memory = False)
```

#### **Print data set dimension**

```python
print(len(data))
print(len(data.columns))
```

```
129
6
```

#### **Change data type among variables to numeric**

```python
data["breastCancerAll"]   = data["breastCancerAll"].convert_objects(convert_numeric=True)
data["breastCancer100th"] = data["breastCancer100th"].convert_objects(convert_numeric=True)
data["meanSugarPerson"]   = data["meanSugarPerson"].convert_objects(convert_numeric=True)
data["meanFoodPerson"]    = data["meanFoodPerson"].convert_objects(convert_numeric=True)
data["meanCholesterol"]   = data["meanCholesterol"].convert_objects(convert_numeric=True)
```

#### **Count of breastCancerAll - Number of new breast cancer cases in 2002**

```python
print("Count of breastCancerAll - Number of new breast cancer cases in 2002")
c1 = data["breastCancerAll"].value_counts(sort=False)
print(c1)
```

```
Count of breastCancerAll - Number of new breast cancer cases in 2002
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

#### **Percentage of breastCancerAll - Number of new breast cancer cases in 2002**

```python
print("Percentage of breastCancerAll - Number of new breast cancer cases in 2002")
p1 = data["breastCancerAll"].value_counts(sort=False,normalize=True)
print(p1)
```

```
Percentage of breastCancerAll - Number of new breast cancer cases in 2002
2330      0.007752
55689     0.007752
1027      0.007752
7429      0.007752
82951     0.007752
1032      0.007752
2568      0.007752
266       0.007752
231       0.007752
525       0.007752
16        0.007752
126227    0.007752
20        0.007752
21        0.007752
5142      0.007752
3609      0.007752
36634     0.007752
4635      0.007752
28        0.007752
543       0.007752
2848      0.007752
6945      0.007752
34        0.007752
5411      0.007752
2598      0.007752
3879      0.007752
447       0.007752
45        0.007752
7273      0.007752
47        0.007752
            ...   
1174      0.007752
3514      0.007752
3668      0.007752
4117      0.007752
194       0.007752
196       0.007752
1221      0.007752
14358     0.007752
3845      0.007752
463       0.015504
509       0.007752
4309      0.007752
687       0.007752
12253     0.007752
2388      0.007752
40928     0.007752
41957     0.007752
230       0.007752
4742      0.007752
236       0.007752
209995    0.007752
15855     0.007752
2288      0.007752
243       0.007752
32245     0.007752
55        0.007752
13051     0.007752
1795      0.007752
765       0.007752
84        0.007752
Name: breastCancerAll, dtype: float64
```

#### **Count of breastCancer100th - Number of new breast cancer cases per 100,000 female in 2002**

```python
print("Count of breastCancer100th - Number of new breast cancer cases per 100,000 female in 2002")
c2 = data["breastCancer100th"].value_counts(sort=False)
print(c2)
```

```
Count of breastCancer100th - Number of new breast cancer cases per 100,000 female in 2002
31.6    1
46.6    1
3.9     1
30.9    1
6.4     1
29.7    1
10.3    1
31.8    1
12.3    1
13.6    1
15.3    1
16.5    2
30.3    1
18.7    1
19.5    3
20.6    2
21.5    1
22.5    2
23.5    2
24.7    4
25.9    2
26.0    1
28.1    4
29.8    2
30.6    1
31.2    3
32.7    1
33.4    1
34.2    2
35.1    2
       ..
16.6    1
16.2    1
17.1    1
24.1    1
46.2    1
18.2    2
10.5    1
19.1    1
19.0    1
20.4    2
87.2    1
23.3    1
26.4    1
50.3    1
18.4    1
23.1    1
24.2    1
29.0    1
13.0    1
25.2    1
83.1    1
24.0    1
30.0    1
26.1    1
29.5    1
55.5    1
30.8    1
74.4    1
20.2    1
84.7    1
Name: breastCancer100th, dtype: int64
```