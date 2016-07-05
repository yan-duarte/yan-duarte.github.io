__author__ = 'yanDuarte'

import pandas
import numpy

# Import the data set to memory
data = pandas.read_csv("separatedData.csv", low_memory = False)

# Print data set dimension
print(len(data))
print(len(data.columns))

# Change data type among variables to numeric
data["breastCancerAll"]   = data["breastCancerAll"].convert_objects(convert_numeric=True)
data["breastCancer100th"] = data["breastCancer100th"].convert_objects(convert_numeric=True)
data["meanSugarPerson"]   = data["meanSugarPerson"].convert_objects(convert_numeric=True)
data["meanFoodPerson"]    = data["meanFoodPerson"].convert_objects(convert_numeric=True)
data["meanCholesterol"]   = data["meanCholesterol"].convert_objects(convert_numeric=True)

# Getting the count and percentage of variable breastCancerAll
print("Count of breastCancerAll - Number of new breast cancer cases in 2002")
c1 = data["breastCancerAll"].value_counts(sort=False)
print(c1)

print("Percentage of breastCancerAll - Number of new breast cancer cases in 2002")
p1 = data["breastCancerAll"].value_counts(sort=False,normalize=True)
print(p1)

# Getting the count and percentage of variable breastCancer100th
print("Count of breastCancer100th - Number of new breast cancer cases per 100,000 female in 2002")
c2 = data["breastCancer100th"].value_counts(sort=False)
print(c2)

print("Percentage of breastCancer100th - Number of new breast cancer cases in per 100,000 female 2002")
p2 = data["breastCancer100th"].value_counts(sort=False,normalize=True)
print(p2)

# Getting the count and percentage of variable meanSugarPerson
print("Count of meanSugarPerson - Mean of the food consumption quantity (grams per person and day) of sugar and sweeters between 1961 and 2002")
c3 = data["meanSugarPerson"].value_counts(sort=False)
print(c3)

print("Percentage of meanSugarPerson - Mean of the food consumption quantity (grams per person and day) of sugar and sweeters between 1961 and 2002")
p3 = data["meanSugarPerson"].value_counts(sort=False,normalize=True)
print(p3)

# Getting the count and percentage of variable meanFoodPerson
print("Count of meanFoodPerson - Mean of the total supply of food (kilocalories / person & day) between 1961 and 2002")
c4 = data["meanFoodPerson"].value_counts(sort=False)
print(c4)

print("Percentage of meanFoodPerson - Mean of the total supply of food (kilocalories / person & day) between 1961 and 2002")
p4 = data["meanFoodPerson"].value_counts(sort=False,normalize=True)
print(p4)

# Getting the count and percentage of variable meanCholesterol
print("Count of meanCholesterol - The average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002")
c5 = data["meanCholesterol"].value_counts(sort=False)
print(c5)

print("Percentage of meanCholesterol - The average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002")
p5 = data["meanCholesterol"].value_counts(sort=False)
print(p5)


