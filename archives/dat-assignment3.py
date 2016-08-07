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

# Create a subData with only the variables breastCancer100th, meanSugarPerson, meanFoodPerson, meanCholesterol
sub1 = data[['breastCancer100th','meanSugarPerson']]

# Bivariate Scatterplot Q->Q -  Incidence of breast cancer versus sugar consumption
scat1 = seaborn.regplot(x="meanSugarPerson", y="breastCancer100th", fit_reg=True, data=sub1)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')
plt.title('Scatterplot for the association between the incidence of breast cancer and the sugar consumption.')
plt.show()


print ('association between meanSugarPerson and breastCancer100th')
print (scipy.stats.pearsonr(sub1['meanSugarPerson'], sub1['breastCancer100th']))

print('\n r²=')
print(scipy.stats.pearsonr(sub1['meanSugarPerson'], sub1['breastCancer100th'])[0]*scipy.stats.pearsonr(sub1['meanSugarPerson'], sub1['breastCancer100th'])[0])
