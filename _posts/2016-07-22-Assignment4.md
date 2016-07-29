---
published: true
date: '2016-07-22 21:00:00 -0300'
Name:
  - Assignment: Creating Graphs for Your Data
categories:
  - Data Management and Visualization
tags:
  - Data Management and Visualization
title: 'Assignment 4: Creating Graphs for Your Data'
---
## PREVIOUS CONTENT

  - [Assignment 1](https://yan-duarte.github.io/2016/Assignment1/).
  - [Assignment 2](https://yan-duarte.github.io/2016/Assignment2/).
  - [Assignment 3](https://yan-duarte.github.io/2016/Assignment3/).
  - Link to download the dataset [here](https://yan-duarte.github.io/archives/separatedData.csv).
  - Link to download the codebook [here](https://yan-duarte.github.io/archives/codebook.xlsx).

## WHAT TO SUBMIT:

Once you have written a successful program that creates univariate and bivariate graphs, create a blog entry where you post your program and the graphs that you have created. Write a few sentences describing what your graphs reveal in terms of your individual variables and the relationship between them.

  - Download the graph program [here](https://yan-duarte.github.io/archives/assignment4.py).

In the last [assignment (3)](https://yan-duarte.github.io/2016/Assignment3/), I had made the data management that I thought necessary. Now is time to create the graphics that represent this data.

I did that in two ways, in the first one I made the Quantitative->Quantitave method generating a scatterplot and the second one was a Qualitative->Quantitative method that creates a bar graph.
Before I present the result of the relationship between the two variable in graph, let's see the histogram and the metrics extracted in each attribute separated.

## **Univariate graphs**

### **Incidence of breast cancer**

The first attribute was the incidence of breast cancer in 100,000 female residents during the 2002 year. As it is a quantitative attribute, was generated the histogram of the data.

```python
#Univariate histogram of the incidence of breast cancer in 100,000 female residents during the 2002 year.
seaborn.distplot(sub1["breastCancer100th"].dropna(), kde=False);
plt.xlabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
plt.ylabel('Number of counties.')
plt.title('Histogram of the Incidence of Breast Cancer.')
plt.show()
```

![Figure 1]({{site.baseurl}}/yan-duarte.github.io/images/assignment4/graph1.png)

We can observe in the histogram that most of the countries have an incidence of cancer around 30 and 40 cases per 100,000 female. The extracted metrics of this attribute were:

```python
desc1 = sub1["breastCancer100th"].describe()
print(desc1)

```

```
count    129.000000
mean      37.987597
std       24.323873
min        3.900000
25%       20.600000
50%       29.700000
75%       50.300000
max      101.100000
Name: breastCancer100th, dtype: float64
```

With this, we can see that 75% of the countries have an incidence of breast cancer under 50.30 per 100,000 female.

### **Sugar consumption**

The second attribute is the sugar consumption. For this attribute, I have made two graphs: one that shows the histogram of the original data and the other one that shows the bar graph of this attribute relocated into categories.

#### **Histogram**

```python
#Univariate histogram of the Mean of the sugar consumption (grams per person and day) between 1961 and 2002.
seaborn.distplot(sub1["meanSugarPerson"].dropna(), kde=False);
plt.xlabel('Mean of the sugar consumption (grams per person and day) between 1961 and 2002.')
plt.ylabel('Number of counties.')
plt.title('Histogram of the Sugar Consumption.')
plt.show()
```

![Figure 2]({{site.baseurl}}/yan-duarte.github.io/images/assignment4/graph2.png)

This histogram is almost evenly distributed, we can see that the countries that have the most sugar consumption are in the 20 and the 110 grams per person.

```python
desc2 = sub1["meanSugarPerson"].describe()
print(desc2)

```

```
count    129.000000
mean      76.238394
std       42.488004
min        6.132381
25%       42.206429
50%       79.714524
75%      110.307619
max      163.861429
Name: meanSugarPerson, dtype: float64
```

The mean of sugar consumption is 76.24 and we can see that 75% of the countries have an consumption of sugar under 110.31 grams per day.

#### **Bar graph**

```python
#Univariate bar graph of the Mean of the sugar consumption (grams per person and day) between 1961 and 2002.
seaborn.countplot(x="sugar_consumption", data=sub1)
plt.xlabel('Mean of the sugar consumption (grams per person and day) between 1961 and 2002.')
plt.ylabel('Number of counties.')
plt.title('Histogram of the Sugar Consumption.')
plt.show()
```

![Figure 3]({{site.baseurl}}/yan-duarte.github.io/images/assignment4/graph3.png)

Where the consumption is:

  - (0) Desirable between 0 and 30 g.
  - (1) Raised between 30 and 60 g.
  - (2) Borderline high between 60 and 90 g.
  - (3) High between 90 and 120 g.
  - (4) Very high under 120g.

The bar graph behaved very similarly as the histogram.

## **Bivariate graphs**

The two bivariate graphics are presented below:

```python
#Bivariate Scatterplot Q->Q -  Incidence of breast cancer versus sugar consumption
scat1 = seaborn.regplot(x="meanSugarPerson", y="breastCancer100th", fit_reg=True, data=sub1)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
plt.title('Scatterplot for the association between the incidence of breast cancer and the sugar consumption.')
plt.show()

#Bivariate bar graph C->Q -  Incidence of breast cancer versus sugar consumption
seaborn.factorplot(x='sugar_consumption', y='breastCancer100th', data=sub1, kind="bar", ci=None)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
plt.title('Bar graph for the Association between the incidence of breast cancer and the sugar consumption.')
plt.show()
```

![Figure 4]({{site.baseurl}}/yan-duarte.github.io/images/assignment4/graph4.png)

![Figure 5]({{site.baseurl}}/yan-duarte.github.io/images/assignment4/graph5.png)

In both graphics, we can see that there is a relation with the incidence of breast cancer and the consumption of sugar. At the same time that the sugar consumption is increased the incidence of new breast cancer cases is increased too.

## **Review criteria**

Your assessment will be based on the evidence you provide that you have completed all of the steps. When relevant, gradients in the scoring will be available to reward clarity (for example, you will get one point for submitting graphs that do not accurately represent your data, but two points if the data is accurately represented). In all cases, consider that the peer assessing your work is likely not an expert in the field you are analyzing. You will be assessed equally on your description of your frequency distributions.

Specific rubric items, and their point values, are as follows:

  - Was a univariate graph created for each of the selected variables? (2 points)
  - Was a bivariate graph created for the selected variables? (2 points)
  - Did the summary describe what the graphs revealed in terms of the individual variables and the relationship between them? (2 points)
