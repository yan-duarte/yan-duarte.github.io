__author__ = 'YanDuarte'

import pandas
import numpy
import statistics
import seaborn
import matplotlib.pyplot as plt


# Import the data set to memory
data = pandas.read_csv("separatedData.csv", low_memory = False)

# Change data type among variables to numeric
data["breastCancer100th"] = data["breastCancer100th"].convert_objects(convert_numeric=True)
data["meanSugarPerson"]   = data["meanSugarPerson"].convert_objects(convert_numeric=True)
data["meanFoodPerson"]    = data["meanFoodPerson"].convert_objects(convert_numeric=True)
data["meanCholesterol"]   = data["meanCholesterol"].convert_objects(convert_numeric=True)

# Create a subData with only the variables breastCancer100th, meanSugarPerson, meanFoodPerson, meanCholesterol
sub1=data[['breastCancer100th','meanSugarPerson', 'meanFoodPerson', 'meanCholesterol']]

#Univariate histogram of the incidence of breast cancer in 100,000 female residents during the 2002 year.
seaborn.distplot(sub1["breastCancer100th"].dropna(), kde=False);
plt.xlabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
plt.ylabel('Number of counties.')
plt.title('Histogram of the Incidence of Breast Cancer.')
plt.show()

desc1 = sub1["breastCancer100th"].describe()
print(desc1)

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

#Univariate histogram of the Mean of the sugar consumption (grams per person and day) between 1961 and 2002.
seaborn.distplot(sub1["meanSugarPerson"].dropna(), kde=False);
plt.xlabel('Mean of the sugar consumption (grams per person and day) between 1961 and 2002.')
plt.ylabel('Number of counties.')
plt.title('Histogram of the Sugar Consumption.')
plt.show()

desc2 = sub1["meanSugarPerson"].describe()
print(desc2)

#Univariate bar graph of the Mean of the sugar consumption (grams per person and day) between 1961 and 2002.
seaborn.countplot(x="sugar_consumption", data=sub1)
plt.xlabel('Mean of the sugar consumption (grams per person and day) between 1961 and 2002.')
plt.ylabel('Number of counties.')
plt.title('Histogram of the Sugar Consumption.')
plt.show()

# Bivariate Scatterplot Q->Q -  Incidence of breast cancer versus sugar consumption
scat1 = seaborn.regplot(x="meanSugarPerson", y="breastCancer100th", fit_reg=True, data=sub1)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
plt.title('Scatterplot for the association between the incidence of breast cancer and the sugar consumption.')
plt.show()

# Bivariate bar graph C->Q -  Incidence of breast cancer versus sugar consumption
seaborn.factorplot(x='sugar_consumption', y='breastCancer100th', data=sub1, kind="bar", ci=None)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
plt.title('Bar graph for the Association between the incidence of breast cancer and the sugar consumption.')
plt.show()