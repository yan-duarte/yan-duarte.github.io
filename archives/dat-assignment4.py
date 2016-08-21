__author__ = 'YanDuarte'

import pandas
import numpy
import statistics
import seaborn
import matplotlib.pyplot as plt
import scipy

# Import the data set to memory
data = pandas.read_csv("separatedData.csv", low_memory = False)

# Change data type among variables to numeric
data["breastCancer100th"] = data["breastCancer100th"].convert_objects(convert_numeric=True)
data["meanSugarPerson"]   = data["meanSugarPerson"].convert_objects(convert_numeric=True)
data["meanFoodPerson"]   = data["meanFoodPerson"].convert_objects(convert_numeric=True)

#making the categories of the moderator variable
def foodPerson (row):
   if row['meanFoodPerson'] <= 2150:
      return 0
   elif row['meanFoodPerson'] <= 2600 :
      return 1
   elif row['meanFoodPerson'] > 2600:
      return 2

data['foodPerson'] = data.apply (lambda row: foodPerson (row),axis=1)

#show how much occurrences for each category
chk1 = data['foodPerson'].value_counts(sort=False, dropna=False)
print(chk1)


# Create a subData with only the variables breastCancer100th, meanSugarPerson for each foodperson categories
data_clean = data[['breastCancer100th','meanSugarPerson','foodPerson']]

sub1=data_clean[(data_clean['foodPerson']== 0)]
sub2=data_clean[(data_clean['foodPerson']== 1)]
sub3=data_clean[(data_clean['foodPerson']== 2)]

print ('association between meanSugarPerson and breastCancer100th for LOW food consumption')
print (scipy.stats.pearsonr(sub1['meanSugarPerson'], sub1['breastCancer100th']))
print ('       ')
print ('association between meanSugarPerson and breastCancer100th for MIDDLE food consumption')
print (scipy.stats.pearsonr(sub2['meanSugarPerson'], sub2['breastCancer100th']))
print ('       ')
print ('association between meanSugarPerson and breastCancer100th for HIGH food consumption')
print (scipy.stats.pearsonr(sub3['meanSugarPerson'], sub3['breastCancer100th']))
#%%
# Bivariate Scatterplot Q->Q - Sugar consumption versus incidence of breast cancer for LOW food consumption
scat1 = seaborn.regplot(x="meanSugarPerson", y="breastCancer100th", fit_reg=True, data=sub1)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
plt.title('Scatterplot for the association between the sugar consumption and the incidence of breast cancer for LOW food consumption.')
plt.show()
#%%
# Bivariate Scatterplot Q->Q - Sugar consumption versus incidence of breast cancer for MIDDLE food consumption
scat1 = seaborn.regplot(x="meanSugarPerson", y="breastCancer100th", fit_reg=True, data=sub2)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
plt.title('Scatterplot for the association between the sugar consumption and the incidence of breast cancer for MIDDLE food consumption.')
plt.show()
#%%
# Bivariate Scatterplot Q->Q - Sugar consumption versus incidence of breast cancer for HIGH food consumption
scat1 = seaborn.regplot(x="meanSugarPerson", y="breastCancer100th", fit_reg=True, data=sub3)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
plt.title('Scatterplot for the association between the sugar consumption and the incidence of breast cancer for HIGH food consumption.')
plt.show()


