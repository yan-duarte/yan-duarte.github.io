__author__ = 'YanDuarte'

import pandas
import numpy

# Import the data set to memory
data = pandas.read_csv("separatedData.csv", low_memory = False)

# Print data set dimension
print(len(data))
print(len(data.columns))

# Change data type among variables to numeric
data["breastCancer100th"] = data["breastCancer100th"].convert_objects(convert_numeric=True)
data["sugarConsumption"]   = data["sugarConsumption"].convert_objects(convert_numeric=True)
data["foodCountryMean"]    = data["foodCountryMean"].convert_objects(convert_numeric=True)
data["cholesterolInBlood"]   = data["cholesterolInBlood"].convert_objects(convert_numeric=True)

# Getting the count and percentage of variable breastCancer100th
print("Count of breastCancer100th - Number of new breast cancer cases per 100,000 female in 2002")
c1 = data["breastCancer100th"].value_counts(sort=False)
print(c1)

print("Percentage of breastCancer100th - Number of new breast cancer cases in per 100,000 female 2002")
p1 = data["breastCancer100th"].value_counts(sort=False,normalize=True)
print(p1)

# Getting the count and percentage of variable sugarConsumption
print("Count of sugarConsumption - Range of sugar consumption based on the mean of the quantity (grams per person and day) of sugar and sweeters between 1961 and 2002")
c2 = data["sugarConsumption"].value_counts(sort=False)
print(c2)

print("Percentage of sugarConsumption - Range of sugar consumption based on the mean of the quantity (grams per person and day) of sugar and sweeters between 1961 and 2002")
p2 = data["sugarConsumption"].value_counts(sort=False,normalize=True)
print(p2)

# Getting the count and percentage of variable foodCountryMean
print("Count of foodCountryMean - Mean of the food consumption of countries based on the mean  of the total supply of food (kilocalories / person & day) between 1961 and 2002")
c3 = data["foodCountryMean"].value_counts(sort=False)
print(c3)

print("Percentage of foodCountryMean - Mean of the food consumption of countries based on the mean of the total supply of food (kilocalories / person & day) between 1961 and 2002")
p3 = data["foodCountryMean"].value_counts(sort=False, normalize=True)
print(p3)

# Getting the count and percentage of variable cholesterolInBlood
print("Count of cholesterolInBlood - Range of the average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002")
c4 = data["cholesterolInBlood"].value_counts(sort=False)
print(c4)

print("Percentage of cholesterolInBlood - Range of the average of the mean TC (Total Cholesterol) of the female population counted in mmol per L between 1980 and 2002")
p4 = data["cholesterolInBlood"].value_counts(sort=False,normalize=True)
print(p4)

