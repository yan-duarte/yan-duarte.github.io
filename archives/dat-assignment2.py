__author__ = 'YanDuarte'


import pandas
import numpy
import scipy.stats
import seaborn
import matplotlib.pyplot as plt
import statistics

# Import the data set to memory
data = pandas.read_csv("separatedData.csv", low_memory = False)

# Change data type among variables to numeric
data["breastCancer100th"] = data["breastCancer100th"].convert_objects(convert_numeric=True)
data["meanSugarPerson"]   = data["meanSugarPerson"].convert_objects(convert_numeric=True)

# Create a subData with only the variables breastCancer100th, meanSugarPerson, meanFoodPerson, meanCholesterol
sub1=data[['breastCancer100th', 'meanSugarPerson']]

# Create the conditions to a new variable named sugar_consumption that will categorize the meanSugarPerson answers
meanIncidence = statistics.mean(sub1['breastCancer100th'])

def incidence_cancer (row):
    if row['breastCancer100th'] <= meanIncidence : return 0   # Incidence of breast cancer is below the average of the incidence of all countries.
    if row['breastCancer100th'] > meanIncidence  : return 1   # incidence of breast cancer is above the average of the incidence of all countries.

# Add the new variable sugar_consumption to subData
sub1['incidence_cancer'] = sub1.apply (lambda row: incidence_cancer (row),axis=1)

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
sub2 = sub1[['incidence_cancer', 'sugar_consumption']].dropna()


#
#***********************************************************************************
#  Starts the chi-square test
#***********************************************************************************
#

# contingency table of observed counts
ct1=pandas.crosstab(sub2['incidence_cancer'], sub2['sugar_consumption'])
print (ct1)

# column percentages
colsum=ct1.sum(axis=0)
colpct=ct1/colsum
print(colpct)

# chi-square
print ('chi-square value, p value, expected counts')
cs1= scipy.stats.chi2_contingency(ct1)
print (cs1)

# set variable types
sub2["sugar_consumption"] = sub2["sugar_consumption"].astype('category')
# new code for setting variables to numeric:
sub2['incidence_cancer'] = pandas.to_numeric(sub2['incidence_cancer'], errors='coerce')

# graph percent with incidence of breast cancer within each sugar consumption group
seaborn.factorplot(x="sugar_consumption", y="incidence_cancer", data=sub2, kind="bar", ci=None)
plt.xlabel('Sugar consumption')
plt.ylabel('Incidence of breast cancer')
plt.show()

#
#***********************************************************************************
#  Starts the post hoc test
#***********************************************************************************
#


listPValue = []

for x in range(0, 4):
    for y in range(x+1, 5):
        print("\n\n\n")

        #Group x vs group y
        recode = {x: x, y: y}
        sub2['COMP'+str(x)+'v'+str(y)]= sub2['sugar_consumption'].map(recode)

        # contingency table of observed counts
        ct=pandas.crosstab(sub2['incidence_cancer'], sub2['COMP'+str(x)+'v'+str(y)])
        print (ct)

        # column percentages
        colsum=ct.sum(axis=0)
        colpct=ct/colsum
        print(colpct)

        print ('chi-square value, p value, expected counts')
        cs= scipy.stats.chi2_contingency(ct)
        print (cs)

        # store the p-values
        listPValue.append(str(cs[1]))


print("\n\n")

print()
print(listPValue[0])
print(listPValue[1] + '     '  + listPValue[4])
print(listPValue[2] + '    '  + listPValue[5] + '      '  + listPValue[7])
print(listPValue[3] + '    '  + listPValue[6] + '    '  + listPValue[8] + '    '  + listPValue[9])







