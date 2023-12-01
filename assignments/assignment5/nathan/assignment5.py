import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from scipy.stats import f_oneway

# Import the dataset
url = './forest+fires/forestfires.csv' 
df = pd.read_csv(url) 

# Exploratory Data Analysis (EDA)
# Explore the dataset's structure and summary statistics

print(df.info())  # Display information about the dataset, including data types and missing values
print(df.describe())  # Display summary statistics

# Visualize key features using plots
# Scatter plot: Temperature vs. Burned Area
plt.figure(figsize=(10, 6)) 
sns.scatterplot(x='temp', y='area', data=df)
plt.title('Scatter Plot: Temperature vs. Burned Area')
plt.xlabel('Temperature')
plt.ylabel('Burned Area')
plt.show()

# Bar plot: Burned Area for Each Month
plt.figure(figsize=(10, 6)) 
sns.barplot(x='month', y='area', data=df)
plt.title('Burned Area for Each Month')
plt.xlabel('Month')
plt.ylabel('Burned Area') 
plt.show()

# Hypothesis Formulation
# Formulate at least two hypotheses related to the dataset
# Hypothesis 1: Burned area is positively correlated with temperature.
# Hypothesis 2: The month influences the amount of burned area.

# Hypothesis Testing
# Test the formulated hypotheses using statistical tests or visualizations

# Hypothesis 1 test 
correlation = df['temp'].corr(df['area'])
print(f"Correlation between temperature and burned area: {correlation}")

# Hypothesis 2 test 
month_groups = [df['area'][df['month'] == month] for month in df['month'].unique()]
# Perform ANOVA
f_statistic, p_value = f_oneway(*month_groups)

# Print the results
print(f'ANOVA F-statistic: {f_statistic}')
print(f'P-value: {p_value}')

# Interpret the results
alpha = 0.05  # Set significance level
if p_value < alpha:
    print("Reject the null hypothesis. There are significant differences in burned area among months.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in burned area among months.")


# Documentation and Reporting
# Document the entire analysis process, including code and explanations
'''
First, I opened the dataset and looked for key features to display in graph format. 
I decided to create a scatter plot showing the relationship between temperature and burned area. 
I also decided to create a bar plot showing the average amount of burned area for each month.

I chose to create these hypothesis: 
Hypothesis 1: Burned area is positively correlated with temperature.
Hypothesis 2: The month influences the amount of burned area.

To analyze hypothesis 1, I used the pandas DataFrame corr() method to find a correlation between the temperature 
and burned area.
To analyze hypothesis 2, I imported f_oneway from scipy.stats in order to perform an ANOVA (Analysis of Variance) test.
First I created a list of subgroups where each subgroup contains the 'area' values for each month. I then got the
p value and f statistic from the list using f_oneway. I then compared the p value to the 0.05 alpha value to determine
if I reject the null hypothesis (there is no significant differences in burned area among moths).
'''
# Summarize key findings in a clear and concise report
''' 
For hypothesis 1, I found that the correlation value between the temperature and burned area is .098. This means there is a weak positive correlation 
as -1 would be a perfect negative correlation and 1 wwould be a perfect positive correlation. In other words, there is not really any
significant relationship between the temperature and the burned area. 

For hypothesis 2, I found that p value is .993. Since this is not less than the 0.05 alpha value, I failed to reject the null hypothesis, meaning that there
is indeed no significant differences in burned area among months. In other words, there is no significant relationship between the month and amount of burned 
area. The small f-statistic of 0.253 means that the means of burned area for each month are relatively similar. This further supports that there is no significant 
relationship between the month and amount of burned area.
'''