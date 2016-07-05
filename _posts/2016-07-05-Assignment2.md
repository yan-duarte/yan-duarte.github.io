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

## **WHAT TO SUBMIT:**

Following completion of your first program, create a blog entry where you post:

  1. _Your program:_ You can download it [here](https://yan-duarte.github.io/archives/assignment2.py);
  2. _The output that displays three of your variables as frequency tables:_ Present at the end of this post;
  3. _A few sentences describing your frequency distributions in terms of the values the variables take, how often they take them, the presence of missing data, etc._

After the first week assignment and the second week lessons, I realized that my code book could be improved.
All of my variables have a different response for each entry, so I decided to create response categories.
The new code book stayed in that way:

|   Variable Name    |      Description of Indicator   |  Main Source |
|:----:|:----------------------------------------:|:----:|
| breastCancerAll    | Total number of new female cases of breast cancer during the 2002 year. | IARC (International Agency for Research on Cancer) |
| breastCancer100th  | Number of new cases of breast cancer in 100,000 female residents during the 2002 year. | IARC (International Agency for Research on Cancer) |
| meanSugarPerson    | Mean of the food consumption quantity (grams per person and day) of sugar and sweeters between years 1961 and 2002 | FAO modified |
| sugarConsumption   | Consumption of sugar based in the meanSugarPerson <br> (0) Desirable between 0 and 30 g. <br> (1) Raised between 30 and 60 g. <br>(2) Borderline high between 60 and 90 g. <br>(3) High between 90 and 120 g. <br> (4) Very high under 120g. | FAO modified |
| meanFoodPerson     | Mean of the total supply of food (kilocalories / person & day) available in a country, divided by the population and 365 (the number of days in the year) between the years | FAO modified |
| foodCountryMean    | Consumption of food based in the meanFoodPerson <br> (0) food consumption below the world average. <br> (1) food consumption under the world average. | FAO modified |
| meanCholesterol    | The average of the mean TC (Total Cholesterol) of the female population, counted in mmol per L; (calculated as if each country has the same age composition as the world | MRC-HPA Centre for Environment and Health |
| cholesterolInBlood | Total Cholesterol in blood based in the meanCholesterol <br> (0) Desirable below 5.2 mmol/L <br> (1) Borerline high between 5.2 and 6.2 mmol/L <br> (2) High above 6.2 mmol/L| MRC-HPA Centre for Environment and Health |

The new attributes were:

  - sugarConsumption
  - foodCountryMean
  - cholesterolInBlood

Witch I will give more importance in the sugarComsumption and breastCancer100th to make this work and answer the question:

  - _Does the sugar consumption has some relation with the incidence of breast cancer?_

If I can, I will also try to answer the other two questions:

  - _Does the food consumption quantity has some relation with the incidence of breast cancer?_
  - _Does the Cholesterol in blood has some relation with the incidence of breast cancer?_




## **The results of the first program that demonstrates the frequency distributions were:**

#### **Importing the packages and the [data set](https://yan-duarte.github.io/archives/separatedData.csv)**

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

#### **Percentage of breastCancer100th - Number of new breast cancer cases per 100,000 female in 2002**

```python
print("Percentage of breastCancer100th - Number of new breast cancer cases in per 100,000 female 2002")
p2 = data["breastCancer100th"].value_counts(sort=False,normalize=True)
print(p2)
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

#### **Count of meanSugarPerson - Mean of the food consumption quantity (grams per person and day) of sugar and sweeters between 1961 and 2002**

```python
print("Count of meanSugarPerson - Mean of the food consumption quantity (grams per person and day) of sugar and sweeters between 1961 and 2002")
c3 = data["meanSugarPerson"].value_counts(sort=False)
print(c3)
```

```
Count of meanSugarPerson - Mean of the food consumption quantity (grams per person and day) of sugar and sweeters between 1961 and 2002
109.655238    1
135.032381    1
6.132381      1
7.828571      1
9.002857      1
11.416667     1
12.656190     1
13.504286     1
14.352381     1
15.004762     1
16.505238     1
17.875238     2
19.440952     1
20.223810     1
16.113810     1
122.050476    1
24.072857     1
25.834286     1
19.636667     1
89.822857     1
33.010476     1
88.322619     1
36.663571     1
38.096429     1
17.744762     1
42.402857     1
43.773571     1
44.231190     1
45.665476     1
48.730714     1
             ..
153.490476    1
129.161190    1
155.903333    1
156.358810    1
158.382857    1
16.179048     1
89.692381     1
102.479048    1
77.754286     1
114.026190    1
104.110000    1
48.859048     1
163.861429    1
100.456667    1
48.990238     1
78.732619     1
109.068095    1
12.199524     2
116.244286    1
81.996429     1
136.467857    1
24.007619     1
116.831429    1
137.967619    1
111.742857    1
120.419524    1
110.307619    1
55.773810     1
85.582381     1
56.360952     1
Name: meanSugarPerson, dtype: int64
```

#### **Percentage of meanSugarPerson - Mean of the food consumption quantity (grams per person and day) of sugar and sweeters between 1961 and 2002**

```python
print("Percentage of meanSugarPerson - Mean of the food consumption quantity (grams per person and day) of sugar and sweeters between 1961 and 2002")
p3 = data["meanSugarPerson"].value_counts(sort=False,normalize=True)
print(p3)
```

```
Percentage of meanSugarPerson - Mean of the food consumption quantity (grams per person and day) of sugar and sweeters between 1961 and 2002
109.655238    0.007752
135.032381    0.007752
6.132381      0.007752
7.828571      0.007752
9.002857      0.007752
11.416667     0.007752
12.656190     0.007752
13.504286     0.007752
14.352381     0.007752
15.004762     0.007752
16.505238     0.007752
17.875238     0.015504
19.440952     0.007752
20.223810     0.007752
16.113810     0.007752
122.050476    0.007752
24.072857     0.007752
25.834286     0.007752
19.636667     0.007752
89.822857     0.007752
33.010476     0.007752
88.322619     0.007752
36.663571     0.007752
38.096429     0.007752
17.744762     0.007752
42.402857     0.007752
43.773571     0.007752
44.231190     0.007752
45.665476     0.007752
48.730714     0.007752
                ...   
153.490476    0.007752
129.161190    0.007752
155.903333    0.007752
156.358810    0.007752
158.382857    0.007752
16.179048     0.007752
89.692381     0.007752
102.479048    0.007752
77.754286     0.007752
114.026190    0.007752
104.110000    0.007752
48.859048     0.007752
163.861429    0.007752
100.456667    0.007752
48.990238     0.007752
78.732619     0.007752
109.068095    0.007752
12.199524     0.015504
116.244286    0.007752
81.996429     0.007752
136.467857    0.007752
24.007619     0.007752
116.831429    0.007752
137.967619    0.007752
111.742857    0.007752
120.419524    0.007752
110.307619    0.007752
55.773810     0.007752
85.582381     0.007752
56.360952     0.007752
Name: meanSugarPerson, dtype: float64
```

#### **Count of meanFoodPerson - Mean of the total supply of food (kilocalories / person & day) between 1961 and 2002**

```python
print("Count of meanFoodPerson - Mean of the total supply of food (kilocalories / person & day) between 1961 and 2002")
c4 = data["meanFoodPerson"].value_counts(sort=False)
print(c4)
```

```
Count of meanFoodPerson - Mean of the total supply of food (kilocalories / person & day) between 1961 and 2002
2304.815000    1
2049.749762    1
2051.645714    1
1903.354524    1
2309.620238    1
2449.240238    1
2568.582857    1
3337.127143    1
2570.400714    1
3086.735238    1
2799.776667    1
2170.986905    1
2682.600000    1
2330.306905    1
3355.360000    1
2844.485714    1
2528.245000    1
2590.527143    1
3103.022857    1
3105.945000    1
3110.555238    1
3111.079762    1
2600.138810    1
1856.959762    1
2092.814048    1
2093.786667    1
2608.065000    1
2097.137143    1
2355.189762    1
2100.220000    1
              ..
3263.549524    1
2497.398095    1
3236.134524    1
3268.145714    1
3276.063810    1
2504.215476    1
2249.160238    1
2252.738095    1
2467.725952    1
3538.345000    1
2261.211667    1
3399.341429    1
2265.761429    1
2011.058095    1
2016.943810    1
1758.630952    1
2016.136667    1
2779.450238    1
2241.080238    1
3046.440952    1
2280.320476    1
2026.566905    1
3056.635714    1
3056.570476    1
2544.911190    1
2033.953333    1
2075.497857    1
3321.688333    1
2335.295238    1
2559.963333    1
Name: meanFoodPerson, dtype: int64
```

#### **Percentage of meanFoodPerson - Mean of the total supply of food (kilocalories / person & day) between 1961 and 2002**

```python
print("Percentage of meanFoodPerson - Mean of the total supply of food (kilocalories / person & day) between 1961 and 2002")
p4 = data["meanFoodPerson"].value_counts(sort=False,normalize=True)
print(p4)
```

```
Percentage of meanFoodPerson - Mean of the total supply of food (kilocalories / person & day) between 1961 and 2002
2304.815000    0.007752
2049.749762    0.007752
2051.645714    0.007752
1903.354524    0.007752
2309.620238    0.007752
2449.240238    0.007752
2568.582857    0.007752
3337.127143    0.007752
2570.400714    0.007752
3086.735238    0.007752
2799.776667    0.007752
2170.986905    0.007752
2682.600000    0.007752
2330.306905    0.007752
3355.360000    0.007752
2844.485714    0.007752
2528.245000    0.007752
2590.527143    0.007752
3103.022857    0.007752
3105.945000    0.007752
3110.555238    0.007752
3111.079762    0.007752
2600.138810    0.007752
1856.959762    0.007752
2092.814048    0.007752
2093.786667    0.007752
2608.065000    0.007752
2097.137143    0.007752
2355.189762    0.007752
2100.220000    0.007752
                 ...   
3263.549524    0.007752
2497.398095    0.007752
3236.134524    0.007752
3268.145714    0.007752
3276.063810    0.007752
2504.215476    0.007752
2249.160238    0.007752
2252.738095    0.007752
2467.725952    0.007752
3538.345000    0.007752
2261.211667    0.007752
3399.341429    0.007752
2265.761429    0.007752
2011.058095    0.007752
2016.943810    0.007752
1758.630952    0.007752
2016.136667    0.007752
2779.450238    0.007752
2241.080238    0.007752
3046.440952    0.007752
2280.320476    0.007752
2026.566905    0.007752
3056.635714    0.007752
3056.570476    0.007752
2544.911190    0.007752
2033.953333    0.007752
2075.497857    0.007752
3321.688333    0.007752
2335.295238    0.007752
2559.963333    0.007752
Name: meanFoodPerson, dtype: float64
```

#### **Count of meanCholesterol - The average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002**

```python
print("Count of meanCholesterol - The average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002")
c5 = data["meanCholesterol"].value_counts(sort=False)
print(c5)
```

```
Count of meanCholesterol - The average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002
4.963593    1
4.314205    1
4.460195    1
4.971775    1
5.269529    1
5.213246    1
5.518175    1
4.662961    1
4.572733    1
4.285046    1
5.940398    1
5.213605    1
4.576413    1
4.488439    1
4.998857    1
5.697471    1
4.781725    1
4.889021    1
4.479256    1
4.661546    1
5.276595    1
4.931813    1
4.504864    1
4.828869    1
4.388709    1
5.566977    1
5.485402    1
5.162131    1
4.846607    1
4.384400    1
           ..
5.376592    1
4.717971    1
4.296541    1
5.695061    1
4.645267    1
4.759214    1
4.582186    1
4.373992    1
5.760482    1
5.064298    1
4.865923    1
4.946654    1
4.914303    1
5.084593    1
5.813268    1
4.715270    1
4.315217    1
4.890947    1
5.252250    1
5.194020    1
4.768728    1
4.541453    1
4.876906    1
5.781620    1
4.414488    1
4.301795    1
4.383932    1
4.922564    1
5.264072    1
5.627696    1
Name: meanCholesterol, dtype: int64
```

#### **Percentage of meanCholesterol - The average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002**

```python
print("Percentage of meanCholesterol - The average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002")
p5 = data["meanCholesterol"].value_counts(sort=False)
print(p5)
```

```
Percentage of meanCholesterol - The average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002
4.963593    1
4.314205    1
4.460195    1
4.971775    1
5.269529    1
5.213246    1
5.518175    1
4.662961    1
4.572733    1
4.285046    1
5.940398    1
5.213605    1
4.576413    1
4.488439    1
4.998857    1
5.697471    1
4.781725    1
4.889021    1
4.479256    1
4.661546    1
5.276595    1
4.931813    1
4.504864    1
4.828869    1
4.388709    1
5.566977    1
5.485402    1
5.162131    1
4.846607    1
4.384400    1
           ..
5.376592    1
4.717971    1
4.296541    1
5.695061    1
4.645267    1
4.759214    1
4.582186    1
4.373992    1
5.760482    1
5.064298    1
4.865923    1
4.946654    1
4.914303    1
5.084593    1
5.813268    1
4.715270    1
4.315217    1
4.890947    1
5.252250    1
5.194020    1
4.768728    1
4.541453    1
4.876906    1
5.781620    1
4.414488    1
4.301795    1
4.383932    1
4.922564    1
5.264072    1
5.627696    1
Name: meanCholesterol, dtype: int64
```

## Review criteria

Your assessment will be based on the evidence you provide that you have completed all of the steps. When relevant, gradients in the scoring will be available to reward clarity (for example, you will get one point for submitting output that is not understandable, but two points if it is understandable). In all cases, consider that the peer assessing your work is likely not an expert in the field you are analyzing. You will be assessed equally on your description of your frequency distributions.

Specific rubric items, and their point values, are as follows:

  - Was the program output interpretable (i.e. organized and labeled)? (1 point)
  - Does the program output display three data managed variables as frequency tables? (1 point)
  - Did the summary describe the frequency distributions in terms of the values the variables take, how often they take them, the presence of missing data, etc.? (2 points)
