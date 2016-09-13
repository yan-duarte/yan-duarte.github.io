__author__ = 'Yan'

import numpy
import pandas
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x)

#load the data
data = pandas.read_csv('separatedData.csv')

# convert to numeric format
data["breastCancer100th"] = pandas.to_numeric(data["breastCancer100th"], errors='coerce')
data["meanSugarPerson"]   = pandas.to_numeric(data["meanSugarPerson"], errors='coerce')
data["meanFoodPerson"]   = pandas.to_numeric(data["meanFoodPerson"], errors='coerce')
data["meanCholesterol"]   = pandas.to_numeric(data["meanCholesterol"], errors='coerce')

# listwise deletion of missing values
sub1 = data[['breastCancer100th', 'meanSugarPerson', 'meanFoodPerson', 'meanCholesterol']].dropna()

####################################################################################
# POLYNOMIAL REGRESSION
####################################################################################

# first order (linear) scatterplot
scat1 = seaborn.regplot(x="meanSugarPerson", y="breastCancer100th", scatter=True, data=sub1)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')

# fit second order polynomial
# run the 2 scatterplots together to get both linear and second order fit lines
scat1 = seaborn.regplot(x="meanSugarPerson", y="breastCancer100th", scatter=True, order=2, data=sub1)
plt.xlabel('Mean of the sugar consumption between 1961 and 2002.')
plt.ylabel('Incidence of breast cancer in 100,000 female residents during the 2002 year.')

# center quantitative IVs for regression analysis
sub1['meanSugarPerson_c'] = (sub1['meanSugarPerson'] - sub1['meanSugarPerson'].mean())
sub1['meanFoodPerson_c']  = (sub1['meanFoodPerson'] - sub1['meanFoodPerson'].mean())
sub1['meanCholesterol_c']   = (sub1['meanCholesterol'] - sub1['meanCholesterol'].mean())
sub1[["meanSugarPerson_c", "meanFoodPerson_c", 'meanCholesterol_c']].describe()

# linear regression analysis
reg1 = smf.ols('breastCancer100th ~ meanSugarPerson_c', data=sub1).fit()
print (reg1.summary())

# quadratic (polynomial) regression analysis
reg2 = smf.ols('breastCancer100th ~ meanSugarPerson_c + I(meanSugarPerson_c**2)', data=sub1).fit()
print (reg2.summary())

####################################################################################
# EVALUATING MODEL FIT
####################################################################################

# adding food consumption
reg3 = smf.ols('breastCancer100th  ~ meanSugarPerson_c + I(meanSugarPerson_c**2) + meanFoodPerson_c',
               data=sub1).fit()
print (reg3.summary())

#Q-Q plot for normality
fig4 = sm.qqplot(reg3.resid, line='r')
plt.show(fig4)

# simple plot of residuals
stdres = pandas.DataFrame(reg3.resid_pearson)
plt.plot(stdres, 'o', ls='None')
l = plt.axhline(y=0, color='r')
plt.ylabel('Standardized Residual')
plt.xlabel('Observation Number')


# additional regression diagnostic plots
fig2 = plt.figure(figsize=(12,8))
fig2 = sm.graphics.plot_regress_exog(reg3,  "meanFoodPerson_c", fig=fig2)
plt.show(fig2)

# leverage plot
fig3=sm.graphics.influence_plot(reg3, size=8)
plt.show(fig3)

# adding mean cholesterol
reg4 = smf.ols('breastCancer100th  ~ meanSugarPerson_c + I(meanSugarPerson_c**2) + meanCholesterol_c',
               data=sub1).fit()
print (reg4.summary())