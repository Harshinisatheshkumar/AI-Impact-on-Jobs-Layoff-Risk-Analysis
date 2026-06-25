
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Harshini\OneDrive\Documents\AI Impact on Jobs Project\dataset\ai-impact-jobs-layoff-risk-dataset.csv")

df.head()
df.tail()
df.shape
df.columns
df.info()

df.isnull().sum()
df.duplicated().sum()
df.describe()

risk_count = df['Layoff_Risk'].value_counts()
print(risk_count)

risk_count.plot(kind='bar')
plt.xlabel('Layoff Risk')
plt.ylabel('Number of Employees')
plt.title('Distribution of Layoff Risk')
plt.show()

industry_risk = pd.crosstab(df['Industry'], df['Layoff_Risk'])
print(industry_risk)
industry_risk.plot(kind='bar', figsize=(10,6))
plt.xlabel('Industry')
plt.ylabel('Count')
plt.title('Industry vs Layoff Risk')
plt.show()

company_risk = pd.crosstab(df['Company_Size'], df['Layoff_Risk'])
print(company_risk)
company_risk.plot(kind='bar')
plt.xlabel('Company Size')
plt.ylabel('Count')
plt.title('Company Size vs Layoff Risk')
plt.show()

ai_risk = pd.crosstab(df['AI_Adoption_Level'], df['Layoff_Risk'])
print(ai_risk)
ai_risk.plot(kind='bar')
plt.xlabel('AI Adoption Level')
plt.ylabel('Count')
plt.title('AI Adoption Level vs Layoff Risk')
plt.show()

job_risk = pd.crosstab(df['Job_Role'], df['Layoff_Risk'])
print(job_risk)
job_risk.plot(kind='bar', figsize=(12,6))
plt.xlabel('Job Role')
plt.ylabel('Count')
plt.title('Job Role vs Layoff Risk')
plt.show()

df.to_csv('AI_Impact_Cleaned.csv', index=False)