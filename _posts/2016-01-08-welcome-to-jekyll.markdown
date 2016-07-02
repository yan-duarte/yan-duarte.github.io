---
title: 'Assignment 1: Getting Your Research Project Started'
date: '2016-07-01 22:05:00 -0300'
categories:
  - Data Management and Visualization
tags:
  - week1
published: true
---
## STEP 1: Choose a data set that you would like to work with.
After I have analyzed the data set from the suggested codebooks, I decided to use the [Gapminder][link_gapminder]. I have chosen this dataset because it has subjects that is related to my areas of interests.

## STEP 2: Identify a specific topic of interest.
There is a lot of different subjects in Gapminder but the one that most drew me attention was the _"Breast cancer, new cases per 100,000 women"_ because this disease was my subject of study in my master degree.

## STEP 3: Prepare a codebook of your own.
The codebook was created based on Gapminder codebook. It contains all the variables details for both my topics.

|   Variable Name   |      Description of Indicator   |  Main Source |
|:----:|:----------------------------------------:|:----:|
| breastCancerAll   | Total number of new female cases of breast cancer during the 2002 year. | IARC (International Agency for Research on Cancer) |
| breastCancer100th | Number of new cases of breast cancer in 100,000 female residents during the 2002 year. | IARC (International Agency for Research on Cancer) |
| meanSugarPerson   | Mean of the food consumption quantity (grams per person and day) of sugar and sweeters between years 1961 and 2002 | FAO modified |
| meanFoodPerson    | Mean of the total supply of food (kilocalories / person & day) available in a country, divided by the population and 365 (the number of days in the year) between the years | FAO modified |
| meanCholesterol   | The average of the mean TC (Total Cholesterol) of the female population, counted in mmol per L; (calculated as if each country has the same age composition as the world | MRC-HPA Centre for Environment and Health |

## STEP 4: Identify a second topic that you would like to explore in terms of its association with your original topic.
When I looked again in Gapminder, there were three topics that I thought that could have some link with the incidence of new breast cancer cases:

  1. [Sugar per person (g per day)][link_gmsugar];
  2. [Food supply (kilocalories / person & day)][link_gmfood];
  3. [Cholesterol (fat) in blood, woomen, (mmol/L)][link_gmcholesterol].

The arrangement of each data set was informed in a relation with country and year. For data set 1 (Sugar per person) the year range is between 1961 and 2004. The second data set (Food supply) is between 1961 and 2007, and the last one (Cholesterol) is between 1980 and 2008.
Therefore, I realized that it would be interesting to make the years values average of each country from the start of data set until 2002, as the breast cancer new cases data set is of 2002.
With that information, and, as the three topics has a relation with alimentation, I would be able to explore if there is a relation between alimentation and the incidence of breast cancer.

So in my research, I can make until three question that has some link:

  1. _Does the sugar consumption has some relation with the incidence of breast cancer?_
  2. _Does the food consumption quantity has some relation with the incidence of breast cancer?_
  3. _Does the Cholesterol in blood has some relation with the incidence of breast cancer?_

At first, I will focus on the first question, trying to answer all of them during the course.

## STEP 5: Add questions/items/variables documenting this second topic to your personal codebook.
Done.

## STEP 6: Perform a literature review to see what research has been previously done on this topic.

The breast cancer is the second disease that most cause obits among women in all the world.

The study [[1]][study_1] investigate the incidence and mortality of cancer with known risk factors and dietary practices. To do that, it collects information from differents data sets like height, weight, food consumption, etc. The information gathered is an average value from several countries.
The results from the study realized that the height and weight is both highly correlated with total fat consumption and, the total fat consumption is the variable most highly correlated with the mortality rates.

In the study [[2]][study_2] were calculated multivariate odds ratios and population attributable risks for breast cancer with dietary b-carotene and vitamin E intake, alcohol consumption, physical activity, and, for postmenopausal women, body mass index.
The data was from a case control study conducted in Italy from June 1991 through April 1994.
The study presented that the risks associated with alcohol and b-carotene intake were larger among premenopausal women, and the risk related to physical activity were larger among postmenopausal women.
In the end, the study indicates that about 1/3 of the breast cancer cases in this Italian population could be avoided. It would be possible by the intervention on a few selected and modifiable risk factors: reducing alcohol intake, having a diet richer in fruit, vegetables, and vegetable oil, and a higher level of physical activity.

[[1]][study_1] Gray G. E., Pike M. C., Henderson B. E. (1979). Breast-cancer incidence and mortality rates in different countries in relation to known risk factors and dietary practices. Jan;39(1):1-7.

[[2]][study_2] Mezzetti M., La Vecchia C., Decarli A., Boyle P., Talamini R., Franceschi S. (1998). Population attributable risk for breast cancer: diet, nutrition, and physical exercise. Mar 4;90(5):389-94.


[link_gapminder]:      http://www.gapminder.org

[link_gmsugar]: https://www.gapminder.org/world/#$majorMode=chart$is;shi=t;ly=2003;lb=f;il=t;fs=11;al=30;stl=t;st=t;nsl=t;se=t$wst;tts=C$ts;sp=5.59290322580644;ti=2010$zpv;v=0$inc_x;mmid=XCOORDS;iid=phAwcNAVuyj1jiMAkmq1iMg;by=ind$inc_y;mmid=YCOORDS;iid=phAwcNAVuyj2sdmdhX9zuKg;by=ind$inc_s;uniValue=8.21;iid=phAwcNAVuyj0XOoBL_n5tAQ;by=ind$inc_c;uniValue=255;gid=CATID0;by=grp$map_x;scale=log;dataMin=194;dataMax=96846$map_y;scale=lin;sma=49;smi=2.65$cd;bd=0$inds=

[link_gmfood]: https://www.gapminder.org/world/#$majorMode=chart$is;shi=t;ly=2003;lb=f;il=t;fs=11;al=30;stl=t;st=t;nsl=t;se=t$wst;tts=C$ts;sp=5.59290322580644;ti=2010$zpv;v=0$inc_x;mmid=XCOORDS;iid=phAwcNAVuyj1jiMAkmq1iMg;by=ind$inc_y;mmid=YCOORDS;iid=0ArfEDsV3bBwCdGlYVVpXX20tbU13STZyVG0yNkRrZnc;by=ind$inc_s;uniValue=8.21;iid=phAwcNAVuyj0XOoBL_n5tAQ;by=ind$inc_c;uniValue=255;gid=CATID0;by=grp$map_x;scale=log;dataMin=194;dataMax=96846$map_y;scale=lin;sma=49;smi=2.65$cd;bd=0$inds=

[link_gmcholesterol]:  https://www.gapminder.org/world/#$majorMode=chart$is;shi=t;ly=2003;lb=f;il=t;fs=11;al=30;stl=t;st=t;nsl=t;se=t$wst;tts=C$ts;sp=5.59290322580644;ti=2008$zpv;v=0$inc_x;mmid=XCOORDS;iid=phAwcNAVuyj1jiMAkmq1iMg;by=ind$inc_y;mmid=YCOORDS;iid=0ArfEDsV3bBwCdGJHcHZkSUdBcU56aS1OT3lLeU4tRHc;by=ind$inc_s;uniValue=8.21;iid=phAwcNAVuyj0XOoBL_n5tAQ;by=ind$inc_c;uniValue=255;gid=CATID0;by=grp$map_x;scale=log;dataMin=194;dataMax=96846$map_y;scale=lin;dataMin=3.974;dataMax=6.2$map_s;sma=50;smi=2$cd;bd=0$inds=

[study_1]: http://www.ncbi.nlm.nih.gov/pubmed/758926

[study_2]: http://www.ncbi.nlm.nih.gov/pubmed/9498489
