__author__ = 'YanDuarte'

import pandas
import numpy
import statistics
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi

# Import the data set to memory
data = pandas.read_csv("separatedData.csv", low_memory = False)

# Change data type among variables to numeric
data["breastCancer100th"] = data["breastCancer100th"].convert_objects(convert_numeric=True)
data["meanSugarPerson"]   = data["meanSugarPerson"].convert_objects(convert_numeric=True)

# Create a subData with only the variables breastCancer100th, meanSugarPerson, meanFoodPerson, meanCholesterol
sub1=data[['breastCancer100th', 'meanSugarPerson']]

# Create the conditions to a new variable named sugar_consumption that will categorize the meanSugarPerson answers
def sugar_consumption (row):
   if 0 < row['meanSugarPerson'] <= 30 : return 0    # Desirable between 0 and 30 g.
   if 30 < row['meanSugarPerson'] <= 60 : return 1   # Raised between 30 and 60 g.
   if 60 < row['meanSugarPerson'] <= 90 : return 2   # Borderline high between 60 and 90 g.
   if 90 < row['meanSugarPerson'] <= 120 : return 3  # High between 90 and 120 g.
   if row['meanSugarPerson'] > 120 : return 4        # Very high under 120g.

# Add the new variable sugar_consumption to subData
sub1['sugar_consumption'] = sub1.apply (lambda row: sugar_consumption (row),axis=1)

# creating a sub data with only the breast cancer cases and the sugar consumption mean
sub2 = sub1[['breastCancer100th', 'sugar_consumption']].dropna()

# using ols function for calculating the F-statistic and associated p value
model1 = smf.ols(formula='breastCancer100th ~ C(sugar_consumption)', data=sub2).fit()
print (model1.summary())

# means for breast cancer by sugar consumption
print ('means for breast cancer by sugar consumption')
m1= sub2.groupby('sugar_consumption').mean()
print (m1)

# standard deviations for breast cancer by sugar consumption
print ('standard deviations for breast cancer by sugar consumption')
sd1 = sub2.groupby('sugar_consumption').std()
print (sd1)

# Post hoc test for ANOVA (as the categorical variable have five categories)
mc1 = multi.MultiComparison(sub2['breastCancer100th'], sub2['sugar_consumption'])
res1 = mc1.tukeyhsd()
print(res1.summary())
