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

## WHAT TO SUBMIT:

Following completion of your first program, create a blog entry where you post:

  1. _Your program:_ Download the program [here](https://yan-duarte.github.io/archives/assignment2.py) and the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv);
  2. _The output that displays three of your variables as frequency tables:_ Present at the end of this post;
  3. _A few sentences describing your frequency distributions in terms of the values the variables take, how often they take them, the presence of missing data, etc._

After the first week assignment and the second week lessons, I realized that my codebook could be improved.
All of my variables have a different response for each entry, so I decided to create response categories. You can download the new full codebook and dataset in this [xlsx file](https://yan-duarte.github.io/archives/codebook.xlsx). The attributes of codebook that I will use in this work stayed in that way:

|   Variable Name    |      Description of Indicator   |  Main Source |
|:----:|:----------------------------------------:|:----:|
| breastCancer100th  | Number of new cases of breast cancer in 100,000 female residents during the 2002 year. | IARC (International Agency for Research on Cancer) |
| sugarConsumption   | Consumption of sugar based in the meanSugarPerson <br> (0) Desirable between 0 and 30 g. <br> (1) Raised between 30 and 60 g. <br>(2) Borderline high between 60 and 90 g. <br>(3) High between 90 and 120 g. <br> (4) Very high under 120g. | FAO modified |
| foodCountryMean    | Consumption of food based in the meanFoodPerson <br> (0) food consumption below the world average. <br> (1) food consumption under the world average. | FAO modified |
| cholesterolInBlood | Total Cholesterol in blood based in the meanCholesterol <br> (0) Desirable below 5.2 mmol/L <br> (1) Borerline high between 5.2 and 6.2 mmol/L <br> (2) High above 6.2 mmol/L| MRC-HPA Centre for Environment and Health |

<br>
The new attributes were made based on the old ones presented in the [assignment 1](https://yan-duarte.github.io/2016/Assignment1/).
I will give more importance in the sugarComsumption and breastCancer100th attributes to make this work and answer the question:

  - _Does the sugar consumption has some relation with the incidence of breast cancer?_

If I can, I will also try to answer the other two questions:

  - _Does the food consumption quantity has some relation with the incidence of breast cancer?_
  - _Does the Cholesterol in blood has some relation with the incidence of breast cancer?_

After running the program, It was possible to observe that the consumption of sugar is considered desirable only in 20.9% of the countries of the dataset. Taking into account that this metric is based on the average of the desirable sugar ingest in grams per day of the woman (25g) and the man (36g) [[1]][ref1] and [[2]][ref2].

To the food consumption data, I made the average of all countries consumption and compared each country consumption to this mean. 55% of the countries stay under the average.

At last, to range the total cholesterol in the blood of the countries I used as a base the metric of Mayo Clinic [[3]][ref3]. In the dataset, none of the values exceeded to a high level of total cholesterol and almost 73% of the countries presented to be in the desirable level.

### Reference

[[1]][ref1] Life by Daily Burn Are You Exceeding Your Daily Sugar Intake in Just One Meal INFOGRAPHIC. Visited 05 Jul 2016. URL: http://dailyburn.com/life/health/daily-sugar-intake-infographic/.

[[2]][ref2] MD-Health How Many Grams of Sugar Per Day. Visited 06/07/2016. URL: http://www.md-health.com/How-Many-Grams-Of-Sugar-Per-Day.html.

[[3]][ref3] Cholesterol Test - Procedure details. Visited 05 Jul 2016. URL: http://www.mayoclinic.org/tests-procedures/cholesterol-test/details/results/rsc-20169555.



## **The results of the first program that demonstrates the frequency distributions were:**

#### **Importing the packages and the [data set (csv)](https://yan-duarte.github.io/archives/separatedData.csv)**

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
9
```

#### **Change data type among variables to numeric**

```python
data["breastCancer100th"] = data["breastCancer100th"].convert_objects(convert_numeric=True)
data["sugarConsumption"]   = data["sugarConsumption"].convert_objects(convert_numeric=True)
data["foodCountryMean"]    = data["foodCountryMean"].convert_objects(convert_numeric=True)
data["cholesterolInBlood"]   = data["cholesterolInBlood"].convert_objects(convert_numeric=True)
```

#### **Count of breastCancerAll - Number of new breast cancer cases in 2002**

```python
print("Count of breastCancer100th - Number of new breast cancer cases per 100,000 female in 2002")
c1 = data["breastCancer100th"].value_counts(sort=False)
print(c1)
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

#### **Percentage of breastCancer100th - Number of new breast cancer cases in per 100,000 female 2002**

```python
print("Percentage of breastCancer100th - Number of new breast cancer cases in per 100,000 female 2002")
p1 = data["breastCancer100th"].value_counts(sort=False,normalize=True)
print(p1)
```

```
Percentage of breastCancer100th - Number of new breast cancer cases in per 100,000 female 2002
31.6    0.007752
46.6    0.007752
3.9     0.007752
30.9    0.007752
6.4     0.007752
29.7    0.007752
10.3    0.007752
31.8    0.007752
12.3    0.007752
13.6    0.007752
15.3    0.007752
16.5    0.015504
30.3    0.007752
18.7    0.007752
19.5    0.023256
20.6    0.015504
21.5    0.007752
22.5    0.015504
23.5    0.015504
24.7    0.031008
25.9    0.015504
26.0    0.007752
28.1    0.031008
29.8    0.015504
30.6    0.007752
31.2    0.023256
32.7    0.007752
33.4    0.007752
34.2    0.015504
35.1    0.015504
          ...   
16.6    0.007752
16.2    0.007752
17.1    0.007752
24.1    0.007752
46.2    0.007752
18.2    0.015504
10.5    0.007752
19.1    0.007752
19.0    0.007752
20.4    0.015504
87.2    0.007752
23.3    0.007752
26.4    0.007752
50.3    0.007752
18.4    0.007752
23.1    0.007752
24.2    0.007752
29.0    0.007752
13.0    0.007752
25.2    0.007752
83.1    0.007752
24.0    0.007752
30.0    0.007752
26.1    0.007752
29.5    0.007752
55.5    0.007752
30.8    0.007752
74.4    0.007752
20.2    0.007752
84.7    0.007752
Name: breastCancer100th, dtype: float64
```

#### **Count of sugarConsumption - Range of sugar consumption based on the mean of the quantity (grams per person and day) of sugar and sweeters between 1961 and 2002**

```python
print("Count of sugarConsumption - Range of sugar consumption based on the mean of the quantity (grams per person and day) of sugar and sweeters between 1961 and 2002")
c2 = data["sugarConsumption"].value_counts(sort=False)
print(c2)
```

```
Count of sugarConsumption - Range of sugar consumption based on the mean of the quantity (grams per person and day) of sugar and sweeters between 1961 and 2002
0    27
1    19
2    31
3    31
4    21
Name: sugarConsumption, dtype: int64
```

#### **Percentage of sugarConsumption - Range of sugar consumption based on the mean of the quantity (grams per person and day) of sugar and sweeters between 1961 and 2002**

```python
print("Percentage of sugarConsumption - Range of sugar consumption based on the mean of the quantity (grams per person and day) of sugar and sweeters between 1961 and 2002")
p2 = data["sugarConsumption"].value_counts(sort=False,normalize=True)
print(p2)
```

```
Percentage of sugarConsumption - Range of sugar consumption based on the mean of the quantity (grams per person and day) of sugar and sweeters between 1961 and 2002
0    0.209302
1    0.147287
2    0.240310
3    0.240310
4    0.162791
Name: sugarConsumption, dtype: float64
```

#### **Count of foodCountryMean - Mean of the food consumption of countries based on the mean  of the total supply of food (kilocalories / person & day) between 1961 and 2002**

```python
print("Count of foodCountryMean - Mean of the food consumption of countries based on the mean  of the total supply of food (kilocalories / person & day) between 1961 and 2002")
c3 = data["foodCountryMean"].value_counts(sort=False)
print(c3)
```

```
Count of foodCountryMean - Mean of the food consumption of countries based on the mean  of the total supply of food (kilocalories / person & day) between 1961 and 2002
0    71
1    58
Name: foodCountryMean, dtype: int64
```

#### **Percentage of foodCountryMean - Mean of the food consumption of countries based on the mean  of the total supply of food (kilocalories / person & day) between 1961 and 2002**

```python
print("Percentage of foodCountryMean - Mean of the food consumption of countries based on the mean of the total supply of food (kilocalories / person & day) between 1961 and 2002")
p3 = data["foodCountryMean"].value_counts(sort=False, normalize=True)
print(p3)
```

```
Percentage of foodCountryMean - Mean of the food consumption of countries based on the mean of the total supply of food (kilocalories / person & day) between 1961 and 2002
0    0.550388
1    0.449612
Name: foodCountryMean, dtype: float64
```

#### **Count of cholesterolInBlood - Range of the average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002**

```python
print("Count of cholesterolInBlood - Range of the average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002")
c4 = data["cholesterolInBlood"].value_counts(sort=False)
print(c4)
```

```
Count of cholesterolInBlood - Range of the average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002
0    94
1    35
Name: cholesterolInBlood, dtype: int64
```

#### **Percentage of cholesterolInBlood - Range of the average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002**

```python
print("Percentage of cholesterolInBlood - Range of the average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002")
p4 = data["cholesterolInBlood"].value_counts(sort=False,normalize=True)
print(p4)
```

```
Percentage of cholesterolInBlood - Range of the average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002
0    0.728682
1    0.271318
Name: cholesterolInBlood, dtype: float64
```


## Review criteria

Your assessment will be based on the evidence you provide that you have completed all of the steps. When relevant, gradients in the scoring will be available to reward clarity (for example, you will get one point for submitting output that is not understandable, but two points if it is understandable). In all cases, consider that the peer assessing your work is likely not an expert in the field you are analyzing. You will be assessed equally on your description of your frequency distributions.

Specific rubric items, and their point values, are as follows:

  - Was the program output interpretable (i.e. organized and labeled)? (1 point)
  - Does the program output display three data managed variables as frequency tables? (1 point)
  - Did the summary describe the frequency distributions in terms of the values the variables take, how often they take them, the presence of missing data, etc.? (2 points)
  
[ref1]: http://dailyburn.com/life/health/daily-sugar-intake-infographic/

[ref2]: http://www.md-health.com/How-Many-Grams-Of-Sugar-Per-Day.html

[ref3]: http://www.mayoclinic.org/tests-procedures/cholesterol-test/details/results/rsc-20169555

